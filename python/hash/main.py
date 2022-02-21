#!/usr/bin/env python

lista_size = 10
lista = [None] * lista_size


def get_hash(input_str):
    hash = 0
    for c in input_str:
        hash += ord(c)
    return hash

def get_index(input_hash):
    return input_hash % lista_size

def insert_lista(index, valor):
    print("Index to insert %s" % index)
    if lista[index] != None:
        raise Exception("Index already exists")
    lista[index] = valor

dato1 = ("marcos", 74489223)
dato1_hash = get_hash(dato1[0])
print(dato1_hash)
dato1_index = get_index(dato1_hash)
print(dato1_index)
insert_lista(dato1_index, dato1[1])
print(lista)


dato2 = ("mena", 74482221)
dato2_hash = get_hash(dato2[0])
print(dato2_hash)
dato2_index = get_index(dato2_hash)
print(dato2_index)
insert_lista(dato2_index, dato2[1])
print(lista)

dato3 = ("socram", 12345678)
dato3_hash = get_hash(dato3[0])
print(dato3_hash)
dato3_index = get_index(dato3_hash)
print(dato3_index)
insert_lista(dato3_index, dato3[1])
print(lista)

