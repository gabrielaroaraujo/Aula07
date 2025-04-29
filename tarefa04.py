nomes= ["joão","carlos","luisa","josé","clara"]
pesquisa=input("digite um nome para pesquisar")
for x in range(len(nomes)):
    if pesquisa==nomes[x]:
        print(f"achei{pesquisa} na posição{x}")
