"""Check revision-note supplements survive regeneration without losing Q&A code."""
import json
from pathlib import Path
import tempfile
import unittest
from flashcards_from_qa import build_cards

class Supplements(unittest.TestCase):
    def test_updates_and_code_additions_survive_regeneration(self):
        with tempfile.TemporaryDirectory() as folder:
            topic = Path(folder)
            (topic/'Questions and Answers').mkdir()
            source = topic/'Questions and Answers'/'qa.md'
            source.write_text('## 1 mark\n\n**1.** What is cache?\n\n**Answer:** Fast memory.\n', encoding='utf-8')
            code = '```python\nif ready:\n    print("Go")\n```'
            supplement = {'updates': [{'front': 'What is cache?', 'back': ['Fast memory close to the CPU.']}],
                          'additions': [{'category': 'Apply', 'front': 'Trace this code.', 'back': [code]}]}
            path = topic/'revision-flashcards.json'
            path.write_text(json.dumps(supplement), encoding='utf-8')
            cards = build_cards(source)
            self.assertEqual(cards[0]['back'], ['Fast memory close to the CPU.'])
            self.assertEqual(cards[1]['back'], [code])
            self.assertEqual(cards, build_cards(source))
            supplement['updates'][0]['front'] = 'A removed question'
            path.write_text(json.dumps(supplement), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Unknown flashcard update'):
                build_cards(source)
            supplement['updates'] = []
            supplement['additions'][0]['front'] = 'WHAT IS CACHE?'
            path.write_text(json.dumps(supplement), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Duplicate flashcard prompts'):
                build_cards(source)
            supplement['additions'][0]['front'] = 'Valid prompt'
            supplement['additions'][0]['back'] = []
            path.write_text(json.dumps(supplement), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Missing flashcard answer'):
                build_cards(source)

if __name__ == '__main__':
    unittest.main()
