#include <stdio.h>
#include <stdlib.h>

extern float ** matriz1;
extern float ** matriz2;
extern float ** matrizResultante;
extern int tamanho;
extern int qtdThreads;
extern pthread_mutex_t mutex;

void *multiplicaParalelo(void *arg){

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
    pthread_exit(NULL);
}