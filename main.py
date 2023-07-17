import subprocess

import matplotlib.pyplot as plt


def compilar_e_rodar(arquivo_c, algoritmo, tamanho, qtdExecucoes, qtdThreads):
    # Compila
    comandoCompilacao = ['gcc', arquivo_c, '-o', 'executavel']
    processoCompilacao = subprocess.run(
        comandoCompilacao, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Verif erros de compilação
    if processoCompilacao.returncode != 0:
        print('Erro de compilação:')
        print(processoCompilacao.stderr.decode('utf-8'))
        return

    if algoritmo == "1":
        algoritmo = "-s"
    elif algoritmo == "2":
        algoritmo = "-p"

    mediaTempoExecucao = 0.0
    temposExec = []
    for i in range(qtdExecucoes):
        comandoExecucao = ['./executavel', algoritmo, tamanho, qtdThreads]
        # Executa o programa
        processoExecucao = subprocess.run(
            comandoExecucao, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # obtem retorno
        retorno = processoExecucao.stdout.decode('utf-8')
        mediaTempoExecucao += float(retorno)
        temposExec.append(float(retorno))

    mediaTempoExecucao /= qtdExecucoes
    print("Media do tempo de execução: ", mediaTempoExecucao, "s")

    return mediaTempoExecucao

    # # Dados para o eixo x e y
    # x = [1, 2, 3, 4, 5]
    # y = [2, 4, 6, 8, 10]

    # # Plotando o gráfico
    # plt.plot(x, y, 'ro')  # 'ro' representa pontos vermelhos (red circles)
    # plt.xlabel('Eixo X')
    # plt.ylabel('Eixo Y')
    # plt.title('Gráfico de exemplo')
    # plt.show()


# arquivo C
arquivo = 'principal.c'

qtdThreads = input("Digite a quantidade de threads do seu computador: ")
choice = input(
    "Deseja (1) ver o grafico de speedup ou (2) rodar individualmente um algoritmo?\n")
if choice == "1":
    threads = [1, 2, 4, 8]

    tempoParalelo1000=[]
    tempoSequencial1000 = compilar_e_rodar(arquivo, "1", "TAM_1", 1, "1")
    
    tempoParalelo1000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "1"))
    tempoParalelo1000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "2"))
    tempoParalelo1000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "4"))
    tempoParalelo1000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "8"))

    speedup1000= [tempoSequencial1000/tempoParalelo1000[i] for i in range(len(threads))]

    print(speedup1000)


    tempoParalelo2000=[]

    tempoSequencial2000 = compilar_e_rodar(arquivo, "1", "TAM_1", 1, "1")
    
    tempoParalelo2000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "1"))
    tempoParalelo2000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "2"))
    tempoParalelo2000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "4"))
    tempoParalelo2000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "8"))

    speedup2000= [tempoSequencial2000/tempoParalelo2000[i] for i in range(len(threads))]

    print(speedup2000)

    tempoParalelo4000=[]

    tempoSequencial4000 = compilar_e_rodar(arquivo, "1", "TAM_1", 1, "1")
    
    tempoParalelo4000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "1"))
    tempoParalelo4000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "2"))
    tempoParalelo4000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "4"))
    tempoParalelo4000.append(compilar_e_rodar(arquivo, "2", "TAM_1", 1, "8"))

    speedup4000= [tempoSequencial4000/tempoParalelo4000[i] for i in range(len(threads))]

    print(speedup4000)



    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)





    linear = [i for i in threads]

    # cores: 
    # chata->vermelho
    # molina->amarelo
    # badas->rosa
    ax1.plot(threads, speedup1000, c='red', label="SpeedUp Paralelo PC-1")


    ax2.plot(threads, speedup2000, c='red', label="SpeedUp Paralelo PC-1")


    ax3.plot(threads, speedup4000, c='red', label="SpeedUp Paralelo PC-1")



    ax1.plot(threads, linear, c='green', label="Crescimento Linear")
    ax1.grid(True)

    ax2.plot(threads, linear, c='green', label="Crescimento Linear")
    ax2.grid(True)

    ax3.plot(threads, linear, c='green', label="Crescimento Linear")
    ax3.grid(True)


    #ax1.set_xlabel("Threads")
    #ax1.set_ylabel("SpeedUp")
    ax1.set_title("Matrix: 1000x1000")
    # plt.suptitle("Tamanho da matrix: 1000x1000")

    #ax2.set_xlabel("Threads")
    ax2.set_ylabel("SpeedUp")
    ax2.set_title("Matrix: 2000x2000")


    ax3.set_xlabel("Threads")
    #ax3.set_ylabel("SpeedUp")
    ax3.set_title("Matrix: 4000x4000")
    fig.tight_layout()


    # plt.xticks([i+1 for i in range(12)])
    # plt.yticks([i+1 for i in range(12)])

    # plt.legend()
    plt.show()

elif choice == "2":
    algoritmo = input(
        "Escolha o algortimo para ser utilizado:\n(1) para Sequencial\n(2) para Paralelo\n")
    tamanho = input(
        "Qual tamanho da matriz?\n(1) Tamanho = 1000\n(2) Tamanho  = 2000\n(3) Tamanho = 4000\n")
    qtdExecucoes = input("Deseja rodar o codigo quantas vezes?\n")
    qtdExecucoes = int(qtdExecucoes)
    # chama a função para compilar e executar o código C
    compilar_e_rodar(arquivo, algoritmo, "TAM_" +
                     tamanho, qtdExecucoes, qtdThreads)
