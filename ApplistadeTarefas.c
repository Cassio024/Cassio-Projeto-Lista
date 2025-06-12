#include <stdio.h>
#include <stdlib.h> // Para system("cls") ou system("clear") no Windows/Linux
#include <string.h> // Para strcpy

// Definição da estrutura da tarefa
typedef struct {
    char descricao[100];
    int concluida; // 0 para não concluída, 1 para concluída
} Tarefa;

// Constante para o número máximo de tarefas
#define MAX_TAREFAS 100

// Array para armazenar as tarefas
Tarefa listaDeTarefas[MAX_TAREFAS];
int numTarefas = 0; // Contador de tarefas atuais

// --- Funções ---

// Função para limpar a tela do console
void limparTela() {
#ifdef _WIN32
    system("cls"); // Para Windows
#else
    system("clear"); // Para Linux/macOS
#endif
}

// Função para adicionar uma nova tarefa
void adicionarTarefa() {
    if (numTarefas < MAX_TAREFAS) {
        printf("\n--- Adicionar Nova Tarefa ---\n");
        printf("Digite a descrição da tarefa: ");
        // Limpar o buffer do teclado antes de ler a string
        getchar();
        fgets(listaDeTarefas[numTarefas].descricao, sizeof(listaDeTarefas[numTarefas].descricao), stdin);
        // Remover o '\n' lido pelo fgets
        listaDeTarefas[numTarefas].descricao[strcspn(listaDeTarefas[numTarefas].descricao, "\n")] = 0;

        listaDeTarefas[numTarefas].concluida = 0; // Inicialmente não concluída
        numTarefas++;
        printf("Tarefa adicionada com sucesso!\n");
    } else {
        printf("A lista de tarefas está cheia. Não é possível adicionar mais tarefas.\n");
    }
    printf("Pressione Enter para continuar...");
    getchar(); // Espera o Enter
}

// Função para listar todas as tarefas
void listarTarefas() {
    printf("\n--- Lista de Tarefas ---\n");
    if (numTarefas == 0) {
        printf("Nenhuma tarefa na lista.\n");
    } else {
        for (int i = 0; i < numTarefas; i++) {
            printf("%d. [%c] %s\n", i + 1,
                   listaDeTarefas[i].concluida ? 'X' : ' ',
                   listaDeTarefas[i].descricao);
        }
    }
    printf("Pressione Enter para continuar...");
    getchar(); // Espera o Enter
}

// Função para marcar uma tarefa como concluída
void marcarTarefaConcluida() {
    printf("\n--- Marcar Tarefa como Concluída ---\n");
    if (numTarefas == 0) {
        printf("Nenhuma tarefa para marcar como concluída.\n");
        printf("Pressione Enter para continuar...");
        getchar(); // Espera o Enter
        return;
    }

    listarTarefas();
    int indiceTarefa;
    printf("Digite o número da tarefa a ser marcada como concluída: ");
    scanf("%d", &indiceTarefa);

    if (indiceTarefa >= 1 && indiceTarefa <= numTarefas) {
        listaDeTarefas[indiceTarefa - 1].concluida = 1;
        printf("Tarefa '%s' marcada como concluída!\n", listaDeTarefas[indiceTarefa - 1].descricao);
    } else {
        printf("Número de tarefa inválido.\n");
    }
    printf("Pressione Enter para continuar...");
    getchar(); // Limpar o buffer do teclado
    getchar(); // Espera o Enter
}

// --- Função Principal (main) ---
int main() {
    int opcao;

    do {
        limparTela();
        printf("--- Gerenciador de Tarefas ---\n");
        printf("1. Adicionar Tarefa\n");
        printf("2. Listar Tarefas\n");
        printf("3. Marcar Tarefa como Concluída\n");
        printf("0. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        // Limpar o buffer do teclado
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                adicionarTarefa();
                break;
            case 2:
                listarTarefas();
                break;
            case 3:
                marcarTarefaConcluida();
                break;
            case 0:
                printf("Saindo do Gerenciador de Tarefas. Até mais!\n");
                break;
            default:
                printf("Opção inválida. Tente novamente.\n");
                printf("Pressione Enter para continuar...");
                getchar(); // Espera o Enter
        }
    } while (opcao != 0);

    return 0;
}