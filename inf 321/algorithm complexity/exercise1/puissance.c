#include <stdio.h>
#include <stdlib.h>

float puissance_iterative(float x, int n){
    if(n ==0){
        return 1;
    }

    float result = 1;

    for(int i=1;i<n;i++){
        result = result*x; //operation barometre
    }
    return result;
    /*
    complexite: dans le pire des cas:O(n);
                dans le meilleur des cas:O(1)
    */
}

float puissance_recursive(float x, int n){
    if(n == 0){
        return 1;
    }
    return puissance_recursive(x,n-1)*x;//operation barometre
    /*
    complexite: dans le pire des cas:O(n);
                dans le meilleur des cas:O(1)
    */
}

    /*
        Sur cette base, on conclut que les deux ont la meme complexite.
        Donc ils sont tous deux aussi performants l'un que l'autre.
    */

int main(){
    float x = 21;
    int n = 100;

    printf("%f puissance %d est egal a %f",x,n,puissance_iterative(x,n));
    //printf("%f puissance %d est egal a %f",x,n,puissance_recursive(x,n));

    return 0;
}