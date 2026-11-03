#pesquisa_satisfaçao
total_excelente = 0
total_ruim = 0
for contador in range (50):
    nome = input("nome do cliente")
    idade = int(input('idade do cliente'))
    opiniao = int(input("digite sua opniao (1-excelente, 2-bom, 3-ruim):  "))
             #Se a opnião do cliente foi 1 (Excelente)
    if  opiniao == 1:
            total_excelente = total_excelente + 1 
             #Se não, se a opnião do cliente foi 3 
    elif opiniao == 3:
            total_ruim = total_ruim + 1 
            #Resultado final dos votos
print("o resultado final de votos excelentes foi:", total_excelente)
print("o resultado final de votos ruins foi:", total_ruim)
    


 