import os
from AnalisadorLexico.AnalisadorLexico import tokenize

# Diretórios de entrada e saída
input_dir = "testes"
output_dir = "outputs_lexico"

# Criar diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Iterar por todos os arquivos da pasta 'testes'
for filename in os.listdir(input_dir):
    if filename.endswith(".c"):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, "r") as file:
            code = file.read()

        # Tokenizar o conteúdo do arquivo
        tokens = tokenize(code)

        # Criar caminho de saída com mesmo nome do arquivo de entrada
        output_path = os.path.join(output_dir, f"{filename}_tokens.txt")
        with open(output_path, "w") as f:
            f.write("[\n")
            for token in tokens:
                f.write(f"    ('{token.type}', '{token.value}'),\n")
            f.write("]\n")

        print(f"Tokens de '{filename}' salvos em '{output_path}'")
