//Teste C completo
#include <stdio.h>
#define PI 3.14159

// Função principal
int main() {
    // Declarações
    int inteiro = 10;
    float decimal = 2.5;
    char letra = 'Z';
    char* mensagem = "Olá, mundo com acento: café!\n";

    // Operadores
    inteiro += 5;
    decimal = inteiro * PI;
    if (inteiro > 10 && decimal <= 100.0) {
        printf("%s", mensagem);
    } else {
        // Comentário com acento: elétrico
        printf("Nada a fazer.\n");
    }

    // Loop
    for (int i = 0; i < 5; i++) {
        printf("Valor de i: %d\n", i);
    }

    // Struct e ponteiro
    struct Pessoa {
        char nome[100];
        int idade;
    };
    struct Pessoa p1;
    struct Pessoa* p_ptr = &p1;

    // // Atribuições
    // p1.idade = 30;
    // p_ptr->idade = 31;

    return 0;
}
