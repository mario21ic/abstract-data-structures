#include <iostream>
#include <array>

class Node {
  public:
    int value;
    int *prev;
    int *next;
};

int main ()
{
    std::array<Node,4> nodos;
    int array_len = nodos.size();
    std::cout << "size of nodos: " << array_len << std::endl;
    std::cout << "sizeof(nodos): " << sizeof(nodos) << std::endl;

    std::cout << "## Assing values " << std::endl;
    for (int i=0; i<array_len; i++) {
        nodos[i].value = 3+i;
        std::cout << "nodo.value: " << nodos[i].value << std::endl;
    }

    std::cout << "## Assing next " << std::endl;
    for (int i=0; i<=(array_len-1); i++) {
        std::cout << "nodo.value: " << nodos[i].value << std::endl;
        if (i == array_len-1) {
            nodos[i].next = &nodos[0].value;
        } else {
            nodos[i].next = &nodos[i+1].value;
        }
        std::cout << "nodo.next: " << *nodos[i].next << std::endl;
    }

    std::cout << "## Assing prev " << std::endl;
    for (int i=0 ; i<array_len; i++) {
        std::cout << "nodo.value: " << nodos[i].value << std::endl;
        if (i == 0) {
            nodos[i].prev = &nodos[array_len-1].value;
        } else {
            nodos[i].prev = &nodos[i-1].value;
        }
        std::cout << "nodo.prev: " << *nodos[i].prev << std::endl;
    }

    return 0;
}

