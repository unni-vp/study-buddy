"""Render the uploaded timetable as an offline, accessible month calendar."""
import calendar
from datetime import date
from html import escape
import json
import re


def render_timetable(root, page, link):
    data_path = root / 'timetable' / 'exams-2027.json'
    data = json.loads(data_path.read_text(encoding='utf-8'))
    year = data['year']
    events = {}
    for exam in data['exams']:
        day = date.fromisoformat(exam['date'])
        assert day.year == year
        assert exam['session'] in ('Morning', 'Afternoon')
        events.setdefault(day, []).append(exam)
    contingency = date.fromisoformat(data['contingency_date'])
    months = range(date.fromisoformat(data['exam_period']['start']).month, contingency.month + 1)
    sections = []
    for month in months:
        name = calendar.month_name[month]
        weeks = []
        for week in calendar.Calendar(firstweekday=0).monthdatescalendar(year, month):
            cells = []
            for day in week:
                if day.month != month:
                    cells.append('<div class="calendar-empty" aria-hidden="true"></div>')
                    continue
                items = []
                for exam in sorted(events.get(day, []), key=lambda e: e['session'] != 'Morning'):
                    subject = re.sub(r'[^a-z]+', '-', exam['subject'].lower()).strip('-')
                    items.append(
                        f'<div class="calendar-event event-{subject}" data-exam-date="{day.isoformat()}">'
                        f'<span class="event-session">{escape(exam["session"])}</span>'
                        f'<strong>{escape(exam["subject"])}</strong>'
                        f'<span class="event-component">{escape(exam["component"])}</span></div>'
                    )
                if day == contingency:
                    items.append('<div class="calendar-event event-contingency"><span class="event-session">Keep available</span><strong>Contingency day</strong></div>')
                classes = ['calendar-day']
                if items:
                    classes.append('has-event')
                if day.weekday() >= 5:
                    classes.append('calendar-weekend')
                cells.append(
                    f'<section class="{" ".join(classes)}" aria-label="{day.strftime("%A %d %B %Y")}">'
                    f'<time class="calendar-date" datetime="{day.isoformat()}"><span class="mobile-weekday">{day.strftime("%A")} </span>{day.day}<span class="mobile-month"> {name}</span></time>'
                    + ''.join(items) + '</section>'
                )
            quiet = not any(d.month == month and (events.get(d) or d == contingency) for d in week)
            week_class = 'calendar-week calendar-quiet-week' if quiet else 'calendar-week'
            weeks.append(f'<div class="{week_class}">' + ''.join(cells) + '</div>')
        weekdays = '<div class="calendar-weekdays" aria-hidden="true">' + ''.join(f'<span>{d}</span>' for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']) + '</div>'
        sections.append(f'<section class="calendar-month" data-calendar-month="{month}" aria-labelledby="month-{month}"><h2 id="month-{month}">{name} {year}</h2>{weekdays}<div class="calendar-weeks">{"".join(weeks)}</div></section>')
    buttons = ''.join(f'<button type="button" data-select-month="{m}" aria-pressed="false">{calendar.month_name[m]}</button>' for m in months)
    pending = ''.join(f'<li><strong>{escape(item["subject"])}: {escape(item["component"])}</strong><span>{escape(item["note"])}</span></li>' for item in data['dates_to_confirm'])
    pdf = link(page, root / 'timetable' / data['source'])
    css = link(page, root / 'library' / 'timetable.css')
    js = link(page, root / 'library' / 'timetable.js')
    return f'''
<link rel="stylesheet" href="{css}">
<div class="timetable-page">
  <div class="timetable-heading"><h1>Exam timetable</h1><div class="timetable-actions"><a href="{pdf}">View source PDF</a><button type="button" data-print-timetable hidden>Print</button></div></div>
  <div class="calendar-toolbar" data-calendar-controls hidden><div class="calendar-month-picker" role="group" aria-label="Choose month">{buttons}</div><div class="calendar-step"><button type="button" data-previous-month aria-label="Previous month">←</button><span data-active-month aria-live="polite"></span><button type="button" data-next-month aria-label="Next month">→</button></div></div>
  <div class="exam-calendar">{''.join(sections)}</div>
  <div class="timetable-information"><section class="timetable-info speaking-info"><h2>French speaking</h2><p><strong>19 April – 28 May {year}</strong></p><p>{escape(data['speaking_window']['note'])}</p></section><section class="timetable-info contingency-info"><h2>Contingency day</h2><p><strong>Wednesday 23 June {year}</strong></p><p>Keep this day available.</p></section><section class="timetable-info pending-info"><h2>Dates to confirm</h2><ul>{pending}</ul></section></div>
</div>
<script defer src="{js}"></script>
'''
