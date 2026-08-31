#Etapa1 -Cadastro das Empresas e seus projetos
startups = {
    "nome": "flare solution",
    "etapa": "aceleração",
    "inicio": "abril de 2026"
}
projetos_ativos =["app mobile", "signal found"]

print("STARTUP:",startups["nome"],"fase:",startups["etapa"])
print("projeto em andamento:",projetos_ativos[0],"inicio:",startups["inicio"])

#etapa2 -mapeamento de salas
#sala ocupada = 1 e sala livre =0
salas = [
    [1,0],
    [0,1]
]
print("status da sala A1", salas[0][0])
print("status da sala A2", salas[0][1])
print("status da sala B1", salas[1][0])
print ("status da sala B2", salas[1][1])
print("classificação de status: 1= ocupado e 0 = livre")