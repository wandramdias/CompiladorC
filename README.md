#  Analisador Léxico para Linguagem C desenvolvido em Python 

Este é um **analisador léxico** desenvolvido em Python para processar arquivos `.c` e identificar os tokens válidos da linguagem C. Ele simula a etapa de análise léxica de um compilador.

---

##  Como funciona

1. **Entrada**: Arquivos `.c` na pasta `testes/`.
2. **Tokenização**: O script `main.py` usa expressões regulares definidas em `Tokens.py` para identificar os tokens.
3. **Saída**: Tokens são salvos como listas de tuplas na pasta `outputs_lexico/`, com o nome do arquivo seguido de `_tokens.txt`.

---

##  Executando o analisador

```bash
python3 main.py
```

Cada arquivo `.c` processado gerará uma saída correspondente na pasta `outputs_lexico/`.

---

##  Tokens reconhecidos

###  Diretivas de Pré-processador
- Ex: `#include`, `#define`
- Regex: `#\s*\w+.*`

###  Comentários
- Linha única: `// comentário`
- Múltiplas linhas: `/* comentário */`

###  Literais
- Strings: `"Texto"`
- Caracteres: `'a'`, `'\n'`
- Números: `123`, `3.14`

###  Palavras-chave (keywords)
- `int`, `float`, `return`, `if`, `else`, `while`, `for`, `struct`, etc.

###  Identificadores
- Funções: `main()`
- Variáveis: `idade`, `contador`

###  Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`, `%`
- **Lógicos**: `&&`, `||`, `!`
- **Relacionais**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Atribuição composta**: `+=`, `-=`, `*=`, `/=`, `%=`
- **Bitwise**: `&`, `|`

###  Delimitadores
- Parênteses: `(` `)`
- Chaves: `{` `}`
- Colchetes: `[` `]`
- Vírgula: `,`
- Ponto e vírgula: `;`

###  Espaços e linhas
- Espaços, tabulações e quebras de linha são ignorados ou usados para rastreamento de posição.

###  Caracteres não reconhecidos
- Disparam um erro:

```python
SyntaxError: Caractere inesperado '.' na linha X
```

---

##  Exemplo de saída

```python
[
    ('KW_INT', 'int'),
    ('ID_VAR', 'main'),
    ('DELIM_LPAREN', '('),
    ('DELIM_RPAREN', ')'),
    ('DELIM_LBRACE', '{'),
    ('KW_RETURN', 'return'),
    ('INT_LITERAL', '0'),
    ('DELIM_SEMICOLON', ';'),
    ('DELIM_RBRACE', '}'),
]
```

---

##  Observações finais

- Ignora comentários e diretivas do pré-processador na saída dos tokens final.
- Distingue entre identificadores de função e variáveis.
- Interrompe a análise caso encontre caracteres inválidos.

---

Desenvolvido como parte de um projeto de compilador em Python. 💻

