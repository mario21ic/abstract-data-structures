#include <stdio.h>

struct node
{
    int value;
    int *next;
};

int main()
{
    struct node nodo1, nodo2, nodo3, nodo4;
    nodo1.value = 2;
    nodo2.value = 5;
    nodo3.value = 7;
    nodo4.value = 9;

    printf("nodo1.value: %d\n", nodo1.value);
    printf("nodo2.value: %d\n", nodo2.value);
    printf("nodo3.value: %d\n", nodo3.value);
    printf("nodo4.value: %d\n", nodo4.value);

    nodo1.next = &nodo2.value;
    printf("nodo1 ptr: %p\n", &nodo1);
    printf("nodo1.next ptr: %p\n", &nodo1.next);
    printf("nodo1.next.value: %d\n", *nodo1.next);

    nodo2.next = &nodo3.value;
    printf("nodo2 ptr: %p\n", &nodo2);
    printf("nodo2.next ptr: %p\n", &nodo2.next);
    printf("nodo2.next.value: %d\n", *nodo2.next);

    nodo3.next = &nodo4.value;
    printf("nodo3 ptr: %p\n", &nodo3);
    printf("nodo3.next ptr: %p\n", &nodo3.next);
    printf("nodo3.next.value: %d\n", *nodo3.next);

    return 0;
}
