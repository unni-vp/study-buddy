"""Run the published long answers against normal, boundary and failure cases."""
from pathlib import Path
import contextlib,io,re,unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
RAW=(ROOT/'Computer Science - AQA/02 - Programming/Questions and Answers/Programming - Questions and Answers.md').read_text(encoding='utf-8')

def answer_code(number):
    prompts={29:'A bookshop awards loyalty credits',30:'The following list stores school club names',31:'Write a Python function called `read_score`',32:'Write a Python authentication program',33:'Write a Python program that accepts exactly',34:'Write a Python program for a five-question addition quiz'}
    prefix=prompts[number] if isinstance(number,int) else number
    section=next(text for text in re.split(r'^\*\*\d+\.\*\* ',RAW,flags=re.M) if text.startswith(prefix))
    answer=section.split('**Answer:**',1)[1]
    return re.search(r'^```python\n(.*?)^```',answer,re.M|re.S)[1]

def run(number,inputs,call=None,random_numbers=None):
    capture=io.StringIO();namespace={}
    with contextlib.ExitStack() as stack:
        reader=stack.enter_context(patch('builtins.input',side_effect=[str(x) for x in inputs]))
        if random_numbers is not None:rand=stack.enter_context(patch('random.randint',side_effect=random_numbers))
        stack.enter_context(contextlib.redirect_stdout(capture))
        exec(compile(answer_code(number),f'published-answer-{number}','exec'),namespace)
        result=call(namespace) if call else None
    return capture.getvalue().splitlines(),reader.call_count,result,rand.call_args_list if random_numbers is not None else []

class ProgrammingAnswers(unittest.TestCase):
    def test_identifier_strings_and_year_suffix(self):
        for name,year,expected in [('Thompson',2009,'Tho09'),('Lee',2000,'Lee00'),('Li',2027,'Invalid'),('',2099,'Invalid'),('smith',2099,'smi99')]:
            _,_,result,_=run('Write a Python function `make_code',[],call=lambda ns:ns['make_code'](name,year))
            self.assertEqual(result,expected)

    def test_nested_seating_count(self):
        lines,_,_,_=run('In this seating plan',[]);self.assertEqual(lines,['7'])

    def test_corrected_mean_includes_first_and_fraction(self):
        for values,expected in [([2,5],3.5),([4,4],4.0),([0,1],0.5),([-3],-3.0)]:
            _,_,result,_=run('This function should return the mean',[],call=lambda ns:ns['mean_score'](values))
            self.assertEqual(result,expected)

    def test_count_all_duplicates_and_reset_local_counter(self):
        for target,expected in [('red',3),('blue',1),('Red',0),('',0)]:
            lines,calls,_,_=run('Write a Python function `count_matches', [target]);self.assertEqual(lines,[str(expected)]);self.assertEqual(calls,1)
        _,_,result,_=run('Write a Python function `count_matches',['red'],call=lambda ns:ns['count_matches']([], 'red'))
        self.assertEqual(result,0)

    def test_character_codes_and_alphabet_wrap(self):
        for text,expected in [('AZ','BA'),('ZZ','AA'),('ABC','BCD'),('','')]:
            _,_,result,_=run('Write a Python function `next_letters',[],call=lambda ns:ns['next_letters'](text))
            self.assertEqual(result,expected)

    def test_loyalty_rates_and_boundaries(self):
        for years in [0,3,4,5]:
            for books in [0,1,11,12,13,30]:
                expected=books*3 if years>=4 else books if books>=12 else 0
                lines,calls,_,_=run(29,[books,years])
                self.assertEqual(lines,[str(expected)])
                self.assertEqual(calls,2)

    def test_search_first_middle_last_absent_and_case(self):
        for word,expected in [('chess',True),('coding',True),('tennis',True),('dance',False),('',False),('Tennis',False)]:
            lines,calls,_,_=run(30,[word]);self.assertEqual(lines,[str(expected)]);self.assertEqual(calls,1)

    def test_validation_rejects_both_sides_and_returns_endpoints(self):
        for inputs,lo,hi,expected in [([-1,101,0],0,100,0),([101,-1,100],0,100,100),([45],0,100,45),([0,11,1],1,10,1),([-5,-3],-3,-3,-3)]:
            lines,calls,result,_=run(31,inputs,call=lambda ns:ns['read_score'](lo,hi))
            self.assertEqual(result,expected);self.assertEqual(calls,len(inputs));self.assertEqual(lines,[])

    def test_authentication_success_requires_both_and_stops(self):
        cases=[(['learner','Code27'],'Access granted',2),(['wrong','Code27','learner','wrong','learner','Code27'],'Access granted',6),(['learner','bad']*3,'Access denied',6),(['wrong','Code27']*3,'Access denied',6),(['','']*3,'Access denied',6),(['Learner','code27']*3,'Access denied',6)]
        for inputs,out,calls in cases:
            lines,used,_,_=run(32,inputs);self.assertEqual(lines,[out]);self.assertEqual(used,calls)

    def test_scores_validation_pass_boundary_and_mean(self):
        for inputs,mean,passes in [([-1,0,100,101,49,50,75],54.8,3),([0]*5,0.0,0),([100]*5,100.0,5),([50]*5,50.0,5)]:
            lines,calls,_,_=run(33,inputs);self.assertEqual(lines,[f'Mean: {mean}',f'Passes: {passes}']);self.assertEqual(calls,len(inputs))

    def test_quiz_random_endpoints_feedback_and_percentage(self):
        numbers=[1,12,12,1,1,1,12,12,6,6];sums=[13,13,2,24,12]
        for answers,score in [(sums,5),([0]*5,0),([13,0,2,0,12],3)]:
            lines,calls,_,random_calls=run(34,answers,random_numbers=numbers)
            self.assertEqual(calls,5);self.assertEqual(len(random_calls),10)
            self.assertTrue(all(c.args==(1,12) for c in random_calls))
            for i,(actual,expected) in enumerate(zip(answers,sums)):
                self.assertEqual(lines[2*i],f'{numbers[2*i]} + {numbers[2*i+1]}')
                self.assertEqual(lines[2*i+1],'Correct' if actual==expected else 'Incorrect')
            self.assertEqual(lines[-2:],[f'Score: {score}',f'Percentage: {score/5*100}'])

if __name__=='__main__':unittest.main()
