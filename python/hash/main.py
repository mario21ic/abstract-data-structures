#!/usr/bin/env python

#lista_size = 10
lista_size = 13
hash_table = [None] * lista_size


"""
# old
def get_hash(input_str):
    hash = 0
    for c in input_str:
        hash += ord(c)
    return hash
"""

def get_hash(input_str):
    hash = 0
    x = 1
    for c in input_str:
        hash += ord(c) * x
        #print("x",x)
        x+=1
    return hash

def get_index(input_hash):
    return input_hash % lista_size

def insert_lista(index, valor):
    print("Index to insert %s" % index)
    if hash_table[index] != None:
        raise Exception("Collision: Index already exists")
        # 1: next to
        # 2: linked list
        # 3: refact hash function
    hash_table[index] = valor

dato1 = ("marcos", 74489223)
dato1_hash = get_hash(dato1[0])
print(dato1_hash)
dato1_index = get_index(dato1_hash)
print(dato1_index)
insert_lista(dato1_index, dato1[1])
print(hash_table)


dato2 = ("mena", 74482221)
dato2_hash = get_hash(dato2[0])
print(dato2_hash)
dato2_index = get_index(dato2_hash)
print(dato2_index)
insert_lista(dato2_index, dato2[1])
print(hash_table)

dato3 = ("socram", 12345678)
dato3_hash = get_hash(dato3[0])
print(dato3_hash)
dato3_index = get_index(dato3_hash)
print(dato3_index)
insert_lista(dato3_index, dato3[1])
print(hash_table)

