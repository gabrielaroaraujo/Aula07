notas=[0.0]*5
soma=0
cont=0
for n in range(len(notas)):
    notas[n]=float(input("digite a nota {n+1}:"))
for s in range(len(notas)):
    soma+=notas[s]
media=soma/len(notas)
for c in range(len(notas)):
    if notas[c]>media:
        cont+=1
print (f"encontramos {cont} alunos acima da media {media}")