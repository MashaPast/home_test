import re


def modify_string(s: str) -> str:
    new_s = s.replace(',', '').replace('.', '')
    new_s = re.sub(r'[\(\[].*?[\)\]]', '', new_s)
    return new_s
