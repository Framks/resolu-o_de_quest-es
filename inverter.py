def inverter(palavra):
    invertida = ""
    for i in range(len(palavra)-1,-1,-1):
        invertida = invertida+palavra[i]
    return invertida


frase = input()
frase_invertida = inverter(frase)
print(frase_invertida)
