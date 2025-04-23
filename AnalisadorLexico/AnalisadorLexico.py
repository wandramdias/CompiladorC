import re
from collections import namedtuple
from .Tokens import token_specification

Token = namedtuple("Token", ["type", "value"])

# Compilar os padrões de regex
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
get_token = re.compile(tok_regex).match

def tokenize(code):
    tokens = []
    line_num = 1
    pos = 0
    mo = get_token(code)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group()
        if kind == "NEWLINE":
            line_num += 1
        elif kind == "SKIP" or kind.startswith("COMMENT"):
            pass
        elif kind == "SKIP" or kind.startswith("PREPROCESSOR"):
            pass
        elif kind == "MISMATCH":
            raise SyntaxError(f"Caractere inesperado {value!r} na linha {line_num}")
        else:
            tokens.append(Token(kind, value))
        pos = mo.end()
        mo = get_token(code, pos)
    return tokens
