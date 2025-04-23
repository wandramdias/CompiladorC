token_specification = [
    ("PREPROCESSOR", r"#\s*\w+.*"),

    # Comentários e literais
    ("COMMENT_MULTI",  r"/\*[\s\S]*?\*/"),
    ("COMMENT_SINGLE", r"//.*"),
    ("STRING_LITERAL",         r'"(\\.|[^"\\])*"'),
    ("CHAR_LITERAL",           r"'(\\.|[^'\\])'"),

    # Palavras-chave (em ordem alfabética)
    ("KW_BREAK",       r"\bbreak\b"),
    ("KW_CASE",        r"\bcase\b"),
    ("KW_CHAR",        r"\bchar\b"),
    ("KW_CONST",       r"\bconst\b"),
    ("KW_CONTINUE",    r"\bcontinue\b"),
    ("KW_DEFAULT",     r"\bdefault\b"),
    ("KW_DO",          r"\bdo\b"),
    ("KW_DOUBLE",      r"\bdouble\b"),
    ("KW_ELSE",        r"\belse\b"),
    ("KW_ENUM",        r"\benum\b"),
    ("KW_EXTERN",      r"\bextern\b"),
    ("KW_FLOAT",       r"\bfloat\b"),
    ("KW_FOR",         r"\bfor\b"),
    ("KW_GOTO",        r"\bgoto\b"),
    ("KW_IF",          r"\bif\b"),
    ("KW_INT",         r"\bint\b"),
    ("KW_LONG",        r"\blong\b"),
    ("KW_REGISTER",    r"\bregister\b"),
    ("KW_RETURN",      r"\breturn\b"),
    ("KW_SHORT",       r"\bshort\b"),
    ("KW_SIGNED",      r"\bsigned\b"),
    ("KW_SIZEOF",      r"\bsizeof\b"),
    ("KW_STATIC",      r"\bstatic\b"),
    ("KW_STRUCT",      r"\bstruct\b"),
    ("KW_SWITCH",      r"\bswitch\b"),
    ("KW_TYPEDEF",     r"\btypedef\b"),
    ("KW_UNION",       r"\bunion\b"),
    ("KW_UNSIGNED",    r"\bunsigned\b"),
    ("KW_VOID",        r"\bvoid\b"),
    ("KW_VOLATILE",    r"\bvolatile\b"),
    ("KW_WHILE",       r"\bwhile\b"),

    # Identificadores (funções e variáveis)
    ("ID_FUNC",        r"\b[_a-zA-Z][_a-zA-Z0-9]*\b(?=\s*\()"),
    ("ID_VAR",         r"\b[_a-zA-Z][_a-zA-Z0-9]*\b"),

    # Números
    ("FLOAT_LITERAL",          r"\b\d+\.\d+\b"),
    ("INT_LITERAL",            r"\b\d+\b"),

    # Operadores compostos
    ("OP_PLUS_EQ",     r"\+="),
    ("OP_MINUS_EQ",    r"-="),
    ("OP_MUL_EQ",      r"\*="),
    ("OP_DIV_EQ",      r"/="),
    ("OP_MOD_EQ",      r"%="),
    ("OP_EQ",          r"=="),
    ("OP_NEQ",         r"!="),
    ("OP_LT_EQ",       r"<="),
    ("OP_GT_EQ",       r">="),
    ("OP_AND",         r"&&"),
    ("OP_OR",          r"\|\|"),

    # Operadores simples
    ("OP_PLUS",        r"\+"),
    ("OP_MINUS",       r"-"),
    ("OP_MUL",         r"\*"),
    ("OP_DIV",         r"/"),
    ("OP_MOD",         r"%"),
    ("OP_ASSIGN",      r"="),
    ("OP_LT",          r"<"),
    ("OP_GT",          r">"),
    ("OP_NOT",         r"!"),
    ("OP_BIT_AND",     r"&"),
    ("OP_BIT_OR",      r"\|"),

    # Delimitadores
    ("DELIM_LPAREN",    r"\("),
    ("DELIM_RPAREN",    r"\)"),
    ("DELIM_LBRACE",    r"\{"),
    ("DELIM_RBRACE",    r"\}"),
    ("DELIM_LBRACKET",  r"\["),
    ("DELIM_RBRACKET",  r"\]"),
    ("DELIM_COMMA",     r","),
    ("DELIM_SEMICOLON", r";"),

    # Espaço e outros
    ("NEWLINE",         r"\n"),
    ("SKIP",            r"[ \t\r]+"),
    ("MISMATCH",        r"."),

]