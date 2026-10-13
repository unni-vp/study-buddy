"""Reference-aligned additions to the maintained Macbeth maps."""
from biology_course_maps import p, m


def enrich_maps(maps):
    overview, characters, power, deception, writing = maps
    overview['panels'][1]['lines'][1] = 'The witches are **catalysts**; Macbeth chooses. “Vaulting ambition” (1.7) is a riding **metaphor** of overreaching.'
    overview['panels'][1]['lines'][2] = 'Regicide: killing Duncan. Usurpation: seizing the crown. New crimes try to protect the first; violence escalates.'
    overview['panels'][3]['lines'][2] = 'Malcolm, Duncan’s named heir, offers legitimate succession and responsible leadership.'
    overview['panels'][5]['lines'][1] = 'Essay: select theme connections that answer the question. Trace beginning, middle and end with evidence and methods.'

    characters['panels'][0]['lines'][2] = '**Hubris:** overconfidence in prophecy. **Hamartia:** ambition overriding judgement. Pity for wasted potential can coexist with condemnation.'
    characters['panels'][1]['lines'][0] = '“Unsex me here” (1.5): an **imperative** asking to suppress compassion. Manhood challenges pressure Macbeth into murder.'
    characters['panels'][3]['lines'][0] = 'Banquo is a **foil**: tempted but more restrained. “Instruments of darkness” (1.3) uses evil **imagery** to question prophecy. Fleance escapes.'
    characters['panels'][3]['lines'][1] = 'Macduff resists tyranny and grieves. “I must also feel it as a man” (4.3): the inclusive **adverb** joins feeling to courage.'
    characters['panels'][4]['lines'][0] = 'Duncan rewards service but misjudges loyalty. His welcome creates **dramatic irony**: the audience knows the danger he cannot see.'
    characters['panels'][4]['lines'][1] = 'Malcolm is the named heir. He tests loyalty; “king-becoming graces” (4.3) uses **ethical vocabulary** to define responsible rule.'
    characters['panels'][5]['lines'][0] = 'Witches are deceptive **catalysts**, offering tempting predictions and double meanings. They never tell Macbeth to kill Duncan.'

    power['panels'][0]['lines'][0] = 'Macbeth knows duties as relative, subject and host. His **soliloquy** reveals conscience. “Vaulting ambition” (1.7) is a riding **metaphor** of excess.'
    power['panels'][4]['lines'][0] = 'Duncan nurtures loyalty. Macbeth commits **regicide** and **usurps** the crown. “Fruitless crown” (3.1): an infertility **metaphor** of insecurity.'
    power['panels'][4]['lines'][1] = 'Scotland suffers. Malcolm’s recognised claim and moral concerns offer restoration, contrasting with Macbeth’s self-protection.'
    power['panels'][4]['lines'].append('**Divine right:** belief in God-given royal authority. Macduff’s “anointed temple” (2.3) is a sacred **metaphor** for Duncan’s body.')

    deception['panels'][0]['lines'][0] = '“Fair is foul” (1.1): **paradox** confuses good and evil. Lady Macbeth’s “innocent flower” and “serpent” (1.5) use contrasting **images**.'
    deception['panels'][2]['lines'][2] = '**Hubris:** Macbeth treats partial truth as complete protection. Equivocation encourages false certainty.'
    deception['panels'][3]['lines'][0] = 'Witches act as **catalysts**; Macbeth still plans and chooses. Banquo hears prophecy too, but exercises greater restraint.'
    deception['panels'][4]['lines'][0] = 'Lady Macbeth makes murder proof of manhood: a **conditional challenge**. Macbeth initially gives courage moral limits.'
    deception['panels'][5]['lines'][1] = 'Patriarchal expectations help explain the pressure to prove manhood. Royal and witchcraft beliefs can deepen specific interpretations.'

    writing['panels'][4]['lines'][0] = 'About 40 minutes. 20 literary marks + 5 for writing accuracy. Select relevant themes and three/four developing moments.'
    writing['panels'][4]['lines'][2] = 'Claim → evidence → method → meaning/effect → question. Develop connected paragraphs, rather than listing every theme.'
    writing['panels'][5]['lines'][0] = '“Vaulting ambition”: riding **metaphor**. “Fruitless crown”: infertility **metaphor**. “Little water” to “damned spot”: **structural reversal**.'
    writing['panels'][5]['lines'][1] = '“also feel it as a man” (4.3): inclusive **adverb**. “Walking shadow”: insubstantial-life **metaphor**.'

    maps.append(m('05-connected-themes-and-essay-planning', 'Connected themes & essay planning',
                  ['Choose a focus', 'Connect evidence', 'Develop the meaning'], [
        p('V + A: violence and ambition',
          '**Violence:** service to Scotland becomes murder for personal power, then attacks on innocents.',
          '**Ambition:** “vaulting ambition” (1.7), a riding **metaphor**, shows Macbeth knows the danger.',
          'Connect cause and consequence: desire for power changes the purpose of violence.'),
        p('G + G: guilt and gender',
          '**Guilt:** “Out, damned spot” (5.1), a failed **imperative** in fragmented prose, exposes lost control.',
          '**Gender:** “then you were a man” (1.7) makes identity conditional on murder.',
          'Macduff’s “also” (4.3) joins grief to courage. Feeling does not cancel manhood.'),
        p('A + S: concealment and prophecy',
          '**Appearance and reality:** “Stars, hide your fires” (1.4), an **imperative** with light-dark imagery, hides desire.',
          '**Supernatural:** “none of woman born” (4.1) uses **equivocation**, not a reliable guarantee.',
          'Witches are catalysts; Macbeth’s choices remain visible.'),
        p('Kingship remains important',
          '**Regicide:** killing a king. **Usurpation:** taking power without a legitimate right.',
          'Duncan names Malcolm heir. Responsible rule serves Scotland; tyranny serves Macbeth.',
          '**Divine right:** belief in God-given authority. The sacred “anointed temple” **metaphor** (2.3) makes murder sacrilegious.'),
        p('Build a whole-play argument',
          '**VAGGAS:** a memory aid, not a required checklist. Choose connections that fit the question.',
          '**Inner conflict:** conscience against ambition; pressure about manhood; guilt becoming renewed violence.',
          'For each idea: accurate evidence, a method, meaning and effect. Explain change across the play.'),
        p('Choose the right evidence',
          '**15-mark extract:** analyse the printed passage throughout. Avoid switching to a whole-play essay.',
          '**25-mark essay:** select developing moments from across the play. Three strong ideas can work; no fixed paragraph count.',
          'Qualify claims: influence is not compulsion; courage does not excuse cruelty. Context supports close analysis.')
    ]))
    return maps
