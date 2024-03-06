from array import *

def fibonacci(chave):
    atual = 1
    anterior = 0
    while( atual < chave):
        aux = anterior
        anterior = atual
        atual = anterior + aux
        
    return atual

valor = int(input())
atual = fibonacci(valor)

if atual == valor:
    print("o numero ",valor," existe na sequencia")
else:
    print("não esta na fila")