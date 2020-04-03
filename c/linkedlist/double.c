#include <stdio.h>

struct node
{
    int value;
    int *prev;
    int *next;
};

int main()
{
    struct node nodos[4];
    //struct node nodos[4] = {2, 3, 4, 5};
    int array_len = sizeof(nodos)/sizeof(nodos[0]);
    printf("Size of array: %d\n", array_len);

    printf("## Assing values\n");
    for(int i = 0; i < array_len; ++i) {
        nodos[i].value = 3+i;
        printf("nodo.value: %d\n", nodos[i].value);
    }

    printf("## Assing next\n");
    for(int i = 0; i < array_len-1; ++i) {
        nodos[i].next = &nodos[i+1].value;
        printf("nodo.value: %d\n", nodos[i].value);
        //printf("nodo.next prt: %p\n", &nodos[i].next);
        printf("nodo.next value: %d\n", *nodos[i].next);
    }

    printf("## Assing prev\n");
    for(int i = 1; i < array_len; ++i) {
        nodos[i].prev = &nodos[i-1].value;
        printf("nodo.value: %d\n", nodos[i].value);
        //printf("nodo.prev prt: %p\n", &nodos[i].prev);
        printf("nodo.prev value: %d\n", *nodos[i].prev);
    }

    return 0;
}
