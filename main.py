import subprocess

import matplotlib.pyplot as plt



def compilar_e_rodar(arquivo_c, algoritmo, tamanho, qtdExecucoes, qtdThreads):
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
    temposExec = []
    for i in range(qtdExecucoes):
            comandoExecucao=['./executavel', algoritmo, tamanho, qtdThreads]
            #Executa o programa
            processoExecucao = subprocess.run(comandoExecucao, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            #obtem retorno
            retorno = processoExecucao.stdout.decode('utf-8')
            mediaTempoExecucao += float(retorno)
            temposExec.append(float(retorno))
            
    mediaTempoExecucao /= qtdExecucoes
    print("Media do tempo de execução: "+mediaTempoExecucao+"s")

    return temposExec

    # # Dados para o eixo x e y
    # x = [1, 2, 3, 4, 5]
    # y = [2, 4, 6, 8, 10]

    # # Plotando o gráfico
    # plt.plot(x, y, 'ro')  # 'ro' representa pontos vermelhos (red circles)
    # plt.xlabel('Eixo X')
    # plt.ylabel('Eixo Y')
    # plt.title('Gráfico de exemplo')
    # plt.show()

#arquivo C
arquivo = 'principal.c'

qtdThreads = input("Digite a quantidade de threads do seu computador: ")
choice= input("Deseja (1) ver o grafico de speedup ou (2) rodar individualmente um algoritmo?")
if choice == 1:
    threads = [1,2,4,8]

    sequencialTam1=compilar_e_rodar(arquivo, "1", "TAM_1", 3, 1)

    pareleloTam1=compilar_e_rodar(arquivo, "2", "TAM_1", 3, 2)

    pareleloTam2=compilar_e_rodar(arquivo, "2", "TAM_1", 3, 4)

    pareleloTam3=compilar_e_rodar(arquivo, "2", "TAM_1", 3, 8)

    speedup = [sequencialTam1[0] / pareleloTam1[i] for i in range(len(pareleloTam1))]

    # Plotando o gráfico
    plt.plot(threads, speedup, 'bo-')  # 'bo-' representa pontos azuis interconectados (blue circles)
    plt.xlabel('Número de Threads')
    plt.ylabel('Speedup')
    plt.title('Gráfico de Speedup')
    plt.grid(True)
    plt.show()


    sequencialTam1=compilar_e_rodar(arquivo, "1", "TAM_2", 3, 1)

    pareleloTam1=compilar_e_rodar(arquivo, "2", "TAM_2", 3, 2)

    pareleloTam2=compilar_e_rodar(arquivo, "2", "TAM_2", 3, 4)
    
    pareleloTam3=compilar_e_rodar(arquivo, "2", "TAM_2", 3, 8)




    sequencialTam1=compilar_e_rodar(arquivo, "1", "TAM_3", 3, 1)

    pareleloTam1=compilar_e_rodar(arquivo, "2", "TAM_3", 3, 2)

    pareleloTam2=compilar_e_rodar(arquivo, "2", "TAM_3", 3, 4)
    
    pareleloTam3=compilar_e_rodar(arquivo, "2", "TAM_3", 3, 8)
    


elif choice == 2:
    algoritmo = input("Escolha o algortimo para ser utilizado:\n(1) para Sequencial\n(2) para Paralelo\n")
    tamanho= input("Qual tamanho da matriz?\n(1) Tamanho = 1000\n(2) Tamanho  = 2000\n(3) Tamanho = 4000\n")
    qtdExecucoes = input("Deseja rodar o codigo quantas vezes?\n")
    qtdExecucoes= int(qtdExecucoes)
     #chama a função para compilar e executar o código C
    compilar_e_rodar(arquivo, algoritmo, "TAM_"+tamanho,qtdExecucoes, qtdThreads)   


