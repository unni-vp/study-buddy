"""Verify literal code, source indentation and Computer Science flash-card recovery."""
from html.parser import HTMLParser
from pathlib import Path
import ast
import json
import re
import unittest

from html_utils import render_md, inline
from flashcards_from_qa import parse_cards
from flashcard_navigation import _answer_html

ROOT = Path(__file__).resolve().parents[1]


class CodeBlocks(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.blocks = []
        self.in_pre = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.in_pre = True
            self.blocks.append('')

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.in_pre = False

    def handle_data(self, text):
        if self.in_pre:
            self.blocks[-1] += text


class CodeRenderingTests(unittest.TestCase):
    def test_code_is_literal_with_blank_lines_and_indentation(self):
        code = '# A comment\nif left < right:\n    print("**literal** [x](url) & >")\n\n    total += 1\n'
        rendered = render_md('Before\n```python\n'+code+'```\nAfter')
        self.assertEqual(CodeBlocks(rendered).blocks, [code])
        self.assertIn('class="language-python"', rendered)
        self.assertNotIn('<strong>', rendered)
        self.assertNotIn('<a ', rendered)
        self.assertIn('<p>Before</p>', rendered)
        self.assertIn('<p>After</p>', rendered)

    def test_longer_fence_can_contain_shorter_fence(self):
        self.assertEqual(CodeBlocks(render_md('````text\n```\nvalue ← 2\n````')).blocks,
                         ['```\nvalue ← 2\n'])

    def test_inline_code_does_not_interpret_markdown(self):
        self.assertEqual(inline('Use `**x** < y & [link](url)`.'),
                         'Use <code>**x** &lt; y &amp; [link](url)</code>.')

    def test_flashcard_conversion_preserves_code_and_comments(self):
        code = 'for count in range(5):\n    # Keep this indentation\n\n    total += count\n'
        source = '# Practice\n\n## 4 marks\n\n**1.** Write a loop.\n\n**Answer:**\n\n```python\n'+code+'```\n\nExplain the total.\n'
        cards = parse_cards(source)
        self.assertEqual(len(cards), 1)
        self.assertEqual(CodeBlocks(_answer_html(cards[0]['back'])).blocks, [code])
        self.assertIn('<li>Explain the total.</li>', _answer_html(cards[0]['back']))

    def test_legacy_flashcard_lines_remain_a_code_block(self):
        points = ['```python', 'for n in range(2):', '    print(n)', '```', 'Two outputs.']
        self.assertEqual(CodeBlocks(_answer_html(points)).blocks, ['for n in range(2):\n    print(n)\n'])

    def test_existing_source_code_and_decks(self):
        count = 0
        for source in (ROOT/'Computer Science - AQA').rglob('*.md'):
            if source.parent.name not in ['Revision Notes','Questions and Answers']:
                continue
            raw = source.read_text(encoding='utf-8')
            matches = re.findall(r'^```([^\n]*)\n(.*?)^```[ \t]*$', raw, re.M|re.S)
            self.assertEqual(CodeBlocks(render_md(raw)).blocks, [body for _,body in matches], str(source))
            for language, body in matches:
                if language.strip() == 'python':
                    ast.parse(body)
                count += 1
        self.assertGreaterEqual(count, 21)
        for topic in (ROOT/'Computer Science - AQA').glob('[0-9][0-9] - *'):
            decks = list((topic/'Flash Cards').glob('*.json'))
            if not decks:
                continue
            deck = json.loads(decks[0].read_text(encoding='utf-8'))
            source = next((topic/'Questions and Answers').glob('*.md'))
            regenerated = parse_cards(source.read_text(encoding='utf-8'))
            self.assertEqual(deck['cards'], regenerated, topic.name)
            for card in deck['cards']:
                for point in card['back']:
                    if point.startswith('```'):
                        self.assertIn(point.split('\n',1)[1].rsplit('\n',1)[0],
                                      CodeBlocks(_answer_html(card['back'])).blocks[0])


if __name__ == '__main__':
    unittest.main()
