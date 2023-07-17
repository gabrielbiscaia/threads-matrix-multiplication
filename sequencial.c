#include <stdio.h>
#include <stdlib.h>


extern float ** matriz1;
extern float ** matriz2;
extern float ** matrizResultante;
extern int tamanho;
extern clock_t inicio, fim;

void multiplicaSequencial(void){

    // Marca o tempo inicial
    inicio = clock();

    for(int i=0; i<tamanho; i++){
        for(int j=0; j<tamanho; j++){
            for(int x=0; x<tamanho; x++){
                matrizResultante[i][j]+=matriz1[i][x]*matriz2[x][j];
            }
        }
    }

    // Marca o tempo final
    fim = clock();

}