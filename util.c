#include <stdio.h>
#include <stdlib.h>
#include <time.h>

extern int tamanho;
extern float **matriz1;
extern float **matriz2;
extern float **matrizResultante;

void imprimirMatriz(int linhas, int colunas) {
    printf("\n\n\nMATRIZ1\n");
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("%.3f ", matriz1[i][j]);
        }
        printf("\n");
    }
    printf("\n\n\nMATRIZ2\n");
        for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("%.3f ", matriz2[i][j]);
        }
        printf("\n");
    }

    printf("\n\n\nMATRIZRESULTANTE\n");
        for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < colunas; j++) {
            printf("%.3f ", matrizResultante[i][j]);
        }
        printf("\n");
    }
}

float geraFloatAleatorio(void){
    float numeroAleatorio = 0;

    //Gera um número aleatório do tipo float entre 1.0 a 99.9
    numeroAleatorio = ((float)rand() / RAND_MAX) * 98.9 + 1.0;

    return numeroAleatorio;
}

void povoarMatriz(float** matriz){
        //povando matriz
    for(int linha =0; linha<tamanho; linha++){
        for(int coluna=0; coluna<tamanho; coluna++){
            matriz[linha][coluna]=geraFloatAleatorio();
        }
    }
}

float ** geraMatriz(){
    
    float **matriz, linha, coluna;

    //aloca tamanho de ponteiros float na memoria
    matriz = (float**) malloc(tamanho*sizeof(float*));
    for(int linha = 0; linha<tamanho; linha++){
        //para cada ponteiro representando linha, aloca-se memoria para colunas
        matriz[linha]= (float *)malloc(tamanho*sizeof(float));
    }

    return matriz;
}

void liberarMemoria() {
    if (matriz1 == NULL || matriz2 == NULL || matrizResultante == NULL ) {
        return; // Retorna se a matriz for nula
    }

    for (int i = 0; i < tamanho; i++) {
        free(matriz1[i]); // Libera cada linha da matriz
        free(matriz2[i]); // Libera cada linha da matriz
        free(matrizResultante[i]); // Libera cada linha da matriz

    }

    free(matriz1); // Libera o ponteiro para a matriz
    free(matriz2); // Libera o ponteiro para a matriz
    free(matrizResultante); // Libera o ponteiro para a matriz
}