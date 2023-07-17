#include <stdio.h>
#include <stdlib.h>

extern float ** matriz1;
extern float ** matriz2;
extern float ** matrizResultante;
extern int tamanho;
extern int qtdThreads;
extern pthread_mutex_t mutex;
extern clock_t inicio, fim;


void *multiplicaParalelo(void *arg){

    // Marca o tempo inicial
    inicio = clock();

    int idThread = *((int*)arg);
    int inicio= (idThread * tamanho)/ qtdThreads;
    int fim= ((idThread+ 1)* tamanho)/ qtdThreads;

    for(int i=inicio; i<fim; i++){
        for(int j=0; j<tamanho; j++){
            float somatoria=0;
            for(int x=0; x<tamanho; x++){
                somatoria+=matriz1[i][x]*matriz2[x][j];
            }

            pthread_mutex_lock(&mutex);
            matrizResultante[i][j] = somatoria;
            // Desbloqueia o mutex após escrever na matriz resultante
            pthread_mutex_unlock(&mutex);
        }
    }

    // Marca o tempo final
    fim = clock();

    pthread_exit(NULL);
}