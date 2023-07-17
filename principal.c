#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include "util.c"
#include "sequencial.c"
#include "paralelo.c"

#define THREADS_GABRIEL 8
#define THREADS_PEDRO 4

#define TAM_1 2000
#define TAM_2 4000
#define TAM_3 8000

float ** matriz1;
float ** matriz2;
float ** matrizResultante;
int tamanho;
int qtdThreads;

//variaveis para calcular tempo
clock_t inicio, fim;
double tempoFinal;

pthread_mutex_t mutex;

int main(int argc, char* argv[]){
    qtdThreads=THREADS_GABRIEL;
    
    if(argc==3){
        if (strcmp(argv[2], "TAM_1") == 0) {
            tamanho = TAM_1;
        } else if (strcmp(argv[2], "TAM_2") == 0) {
            tamanho = TAM_2;
        } else if (strcmp(argv[2], "TAM_3") == 0) {
            tamanho = TAM_3;
        } else {
            tamanho = 0;
        }

        printf("TAMANHO = %d", tamanho);
        //Inicia a semente do gerador de numeros aleatórios com o tempo atual.
        srand(time(0));

        matriz1 = geraMatriz();
        povoarMatriz(matriz1);
        matriz2 = geraMatriz();
        povoarMatriz(matriz2);
        matrizResultante = geraMatriz();


        if(strcmp(argv[1], "-s")== 0){
            //sequencial
            multiplicaSequencial();      
        }
        else if(strcmp(argv[1], "-p")== 0){
            //paralelo

            pthread_t threads[THREADS_GABRIEL];
            int idsThreads[THREADS_GABRIEL];

            pthread_mutex_init(&mutex, NULL);

            for(int i=0; i<THREADS_GABRIEL; i++){
                idsThreads[i]=i;
                pthread_create(&threads[i], NULL, multiplicaParalelo, &idsThreads[i]);
            }

            for(int i=0; i<THREADS_GABRIEL; i++){
                pthread_join(threads[i],NULL);
            }

            pthread_mutex_destroy(&mutex);
            //imprimirMatriz(tamanho, tamanho);
        }

        liberarMemoria();
    }

    // Calcula o tempo de CPU utilizado em segundos
    tempoFinal = ((double) (fim - inicio)) / CLOCKS_PER_SEC;


    printf("\nTempo inicial: %ld\nTempo final: %ld", inicio, fim);
    printf("\nO tempo de execução do programa foi de: %f\n", tempoFinal);

    return 0;
}