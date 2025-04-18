from AnalisadorLexico.AnalisadorLexico import tokenize


# Abrir e ler o arquivo 'programa1.c' localizado na pasta 'testes'
file_path = "testes/programa1.c"
with open(file_path, "r") as file:
    code = file.read()

# Gerar os tokens a partir do conteúdo do arquivo
tokens = tokenize(code)

# Salvar os tokens no formato de lista de tuplas
output_path = "AnalisadorLexico/tokens_output.txt"
with open(output_path, "w") as f:
    f.write("[\n")
    for token in tokens:
        f.write(f"    ('{token.type}', '{token.value}'),\n")
    f.write("]")

print("Tokens salvos em 'AnalisadorLexico/tokens_output.txt' no formato desejado")
