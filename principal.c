//importação das bilbiotecas necessárias
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <time.h>
//importação dos outros arquivos
#include "util.c"
#include "sequencial.c"
#include "paralelo.c"
//Quantidade de threads de cada aluno
#define THREADS_ARTHUR 2
#define THREADS_GABRIEL 8
#define THREADS_PEDRO 4
//Tamanho das matrizes
#define TAM_1 1000
#define TAM_2 2000
#define TAM_3 4000
//Declaração Matrizes
float ** matriz1;
float ** matriz2;
float ** matrizResultante;
int tamanho;
int qtdThreads;
//variaveis para calcular tempo
time_t fim, inicio;
double tempoFinal;

pthread_mutex_t mutex;

double main(int argc, char* argv[]){
    
    
    tempoFinal=0.0;
    if(argc==4){
        if(strcmp(argv[3],"8")){
            qtdThreads=THREADS_GABRIEL;
        }
        else if(strcmp(argv[3],"4")){
            qtdThreads=THREADS_PEDRO;
        }
        else if(strcmp(argv[3],"2")){
            qtdThreads=THREADS_ARTHUR;
        }
        else if(strcmp(argv[3],"1")){
            qtdThreads=1;
        }
                    
        if (strcmp(argv[2], "TAM_1") == 0) {
            tamanho = TAM_1;
        } else if (strcmp(argv[2], "TAM_2") == 0) {
            tamanho = TAM_2;
        } else if (strcmp(argv[2], "TAM_3") == 0) {
            tamanho = TAM_3;
        } else {
            tamanho = 0;
        }


        
        //Inicia a semente do gerador de numeros aleatórios com o tempo atual.
        srand(time(0));

        matriz1 = geraMatriz();
        povoarMatriz(matriz1);
        matriz2 = geraMatriz();
        povoarMatriz(matriz2);
        matrizResultante = geraMatriz();

        if(strcmp(argv[1], "-s")== 0){
            //Marca o tempo inicial
            inicio = time(NULL);

            multiplicaSequencial(); 

            // Marca o tempo final
            fim = time(NULL);  
        }
        else if(strcmp(argv[1], "-p")== 0){
            //Marca o tempo inicial
            inicio = time(NULL);

            pthread_t threads[qtdThreads];
            int idsThreads[qtdThreads];

            pthread_mutex_init(&mutex, NULL);

            for(int i=0; i<qtdThreads; i++){
                idsThreads[i]=i;
                pthread_create(&threads[i], NULL, multiplicaParalelo, &idsThreads[i]);
            }

            for(int i=0; i<qtdThreads; i++){
                pthread_join(threads[i],NULL);
            }
  

            pthread_mutex_destroy(&mutex);
            //imprimirMatriz(tamanho, tamanho);
            // Marca o tempo final
            fim = time(NULL);
        }
        
        // Calcula o tempo de CPU utilizado em segundos
 
        liberarMemoria();
        tempoFinal = fim-inicio;
    }

    return tempoFinal;

}
