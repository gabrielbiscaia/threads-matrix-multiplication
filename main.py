import subprocess

def compilar_e_rodar(arquivo_c, algoritmo, tamanho, qtdExecucoes):
    #Compila
    comandoCompilacao = ['gcc', arquivo_c, '-o', 'executavel']
    processoCompilacao = subprocess.run(comandoCompilacao, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    #Verif erros de compilação
    if processoCompilacao.returncode != 0:
        print('Erro de compilação:')
        print(processoCompilacao.stderr.decode('utf-8'))
        return
    
    if algoritmo == "1":
        algoritmo="-s"
    elif algoritmo =="2":
        algoritmo ="-p"

    mediaTempoExecucao=0.0

    for i in range(qtdExecucoes):
            comandoExecucao=['./executavel', algoritmo, tamanho]
            #Executa o programa
            processoExecucao = subprocess.run(comandoExecucao, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            #obtem retorno
            retorno = processoExecucao.stdout.decode('utf-8')
            mediaTempoExecucao += float(retorno)
            
    mediaTempoExecucao /= qtdExecucoes
    print("Media do tempo de execução: "+mediaTempoExecucao+"s")

#arquivo C
arquivo = 'principal.c'

algoritmo = input("Escolha o algortimo para ser utilizado:\n(1) para Sequencial\n(2) para Paralelo\n")
tamanho= input("Qual tamanho da matriz?\n(1) Tamanho = 1000\n(2) Tamanho  = 2000\n(3) Tamanho = 4000\n")
qtdExecucoes = input("Deseja rodar o codigo quantas vezes?\n")
qtdExecucoes= int(qtdExecucoes)

#chama a função para compilar e executar o código C
compilar_e_rodar(arquivo, algoritmo, "TAM_"+tamanho,qtdExecucoes)
