import json
from html import escape
from html_utils import render_md, inline, fence_start, fence_end


def _answer_html(points):
    # Accept complete fenced points and legacy decks with one entry per line.
    lines = []
    active_fence = None
    for point in points:
        if active_fence is not None:
            lines.append(point)
            if fence_end(point, active_fence):
                active_fence = None
                lines.append('')
        elif (fence := fence_start(point.split('\n', 1)[0])):
            lines.extend(['', point])
            if '\n' not in point:
                active_fence = fence[1]
            else:
                lines.append('')
        else:
            lines.append('- ' + point)
    return render_md('\n'.join(lines))


def _front_html(front):
    if any(fence_start(line) for line in front.splitlines()):
        heading, _, body = front.partition('\n')
        return '<h2>' + inline(heading) + '</h2>' + render_md(body)
    return '<h2>' + inline(front) + '</h2>'


def build_flashcard_page(source, target, subject, topic, topicpage, write, link):
    deck = json.loads(source.read_text(encoding='utf-8'))
    cards = deck['cards']
    card_html = []
    for index, card in enumerate(cards):
        card_html.append(
            f'<article class="flashcard-item" data-card-index="{index}" '
            f'data-card-category="{escape(card["category"], quote=True)}" tabindex="0" '
            f'role="button" aria-expanded="false" aria-label="Reveal answer: {escape(card["front"], quote=True)}">'
            f'<div class="flashcard-front"><span class="flashcard-side-label">Question</span>'
            f'<span class="flashcard-category">{escape(card["category"])}</span>'
            f'{_front_html(card["front"])}'
            f'<p class="flashcard-prompt">Select the card or press Space to reveal the answer.</p></div>'
            f'<div class="flashcard-back"><span class="flashcard-side-label">Answer</span>'
            f'<div class="flashcard-answer">{_answer_html(card["back"])}</div></div></article>'
        )
    content = (
        f'<div class="reader-tools"><a href="{link(target, topicpage)}">← Back to topic</a>'
        f'<button type="button" onclick="window.print()">Print cards</button></div>'
        f'<section class="flashcard-app" data-flashcard-deck>'
        f'<div class="flashcard-heading"><h1>{escape(deck["title"])}</h1></div>'
        f'<div class="flashcard-status" aria-live="polite"><strong><span data-flashcard-current>1</span> of '
        f'<span data-flashcard-total>{len(cards)}</span></strong></div>'
        f'<div class="flashcard-stage">{"".join(card_html)}</div>'
        f'<div class="flashcard-controls" aria-label="Flash card controls">'
        f'<button type="button" data-flashcard-action="previous">← Previous</button>'
        f'<button type="button" data-flashcard-action="next">Next →</button></div>'
        f'<div class="flashcard-order-controls">'
        f'<button type="button" data-flashcard-action="shuffle">Shuffle cards</button>'
        f'<button type="button" data-flashcard-action="reset">Reset order</button></div>'
        f'<p class="flashcard-keyboard-help">Keyboard: Space or Enter reveals the answer; ← and → move between cards.</p>'
        f'</section><script defer src="{link(target, target.parent.parent / "flashcards.js")}"></script>'
    )
    write(
        target,
        deck['title'],
        content,
        [(subject.split(' - ')[0], topicpage.parents[1] / 'index.html'), (topic, topicpage)],
        subject,
    )
    return target, f'{len(cards)} flash cards'
