"""Readable equation and conversion lines for science mind-map panels."""
import re

_CHAINS = (
    (r'P\s*=\s*E/t\s*=\s*W/t', 'P = E/t; P = W/t; W: work done (J)'),
    (r'P\s*=\s*VI\s*=\s*I²R', 'P = VI; P = I²R'),
    (r'E\s*=\s*Pt\s*=\s*QV', 'E = Pt; E = QV'),
    (r'F\s*=\s*Δp/Δt\s*=\s*m\(v\s*[−-]\s*u\)/Δt', 'F = Δp/Δt; F = m(v − u)/Δt'),
    (r'1 m\s*=\s*100 cm\s*=\s*1000 mm', '1 m = 100 cm; 1 m = 1000 mm'),
)
_QUANTITY = r'(?:\*\*)?(?:[A-Za-zρλθΔ][A-Za-zρλθΔ₀-₉²³ₖₚₛ]*\s*(?:=|\bin\b)|[A-Za-zρλθΔ][₀-₉²³ₖₚₛ]*\s*:|\d+(?:\.\d+)?\s*(?:cm[²³]?|mm[²³]?|dm³|[µμn]m|kg|mg|g|m)\s*=)'

def equation_lines(value):
    """Split independent relationships, retaining emphasis and calculation chains.

    A numerical equality such as 24 + 2 × 17 = 58 is a single worked stage.
    C=C bonds, subscripts and decimal points must remain intact.
    """
    original=value
    for pattern,replacement in _CHAINS:value=re.sub(pattern,replacement,value)
    value=re.sub(r'\.(\*\*)? (?='+_QUANTITY+r')', r'.\1; ', value)
    value=re.sub(r',\s*(?='+_QUANTITY+r')', '; ', value)
    value=value.replace('m = Δy/Δx, c at x=0', 'm = Δy/Δx; c at x=0')
    value=value.replace('m=Δy/Δx. c at x=0', 'm=Δy/Δx; c at x=0')
    value=value.replace('Ethene CH₂=CH₂, propene CH₂=CHCH₃', 'Ethene: CH₂=CH₂; Propene: CH₂=CHCH₃')
    if '=' in value:
        value=re.sub(r'(?<!e\.g)(?<!i\.e)(?<!s\.f)\.(\*\*)?(?= (?:\*\*)?[A-Z0-9])', r'.\1;', value)
    if value==original and ';' not in value:return [value]
    parts=[];current='';strong=False;i=0
    while i<len(value):
        if value[i:i+2]=='**':
            strong=not strong;current+='**';i+=2;continue
        if value[i]==';':
            part=(current+('**' if strong else '')).strip()
            if part.replace('**','').strip():parts.append(part)
            current='**' if strong else '';i+=1
            while i<len(value) and value[i]==' ':i+=1
            continue
        current+=value[i];i+=1
    if current.replace('**','').strip():parts.append(current.strip())
    assert all(p.count('**')%2==0 for p in parts),(original,parts)
    return parts

def format_markdown(text):
    """Use the same independent math lines in the complete text counterpart."""
    result=[]
    for line in text.splitlines():
        if not line.strip():
            result.append('');continue
        if line.startswith(('#','|')):
            result.append(line);continue
        bullet=line.startswith('- ')
        parts=equation_lines(line[2:] if bullet else line)
        if bullet:result.extend('- '+part for part in parts)
        else:result.extend('\n\n'.join(parts).splitlines())
    return '\n'.join(result).rstrip()+'\n'
