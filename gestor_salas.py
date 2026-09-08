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
#etapa3 -leitura de dados operacionais
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print("cabealho:", cabecalho)
print("linha1:", linha1)
print("linha2:", linha2)
print("linha3:", linha3)
print("linha4:", linha4)

#etapa4 - painel consolidado da empresa
empresa = startups["nome"]
print(f"{empresa} é a atual ocupante da sala A1.")

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()[1:]
    custo_total = 0.0

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        _, valor = linha.split(",", 1)
        custo_total += float(valor.strip())

print("\n=== painel consolidado da empresa ===")
print(f"nome da empresa: {empresa}")
print("sala ocupada: sala A1")
print(f"valor total investido/gasto: R$ {custo_total:.2f}")
