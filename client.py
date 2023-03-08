#Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as cn
import random

state = cn.connect(2037)

# Define as constantes para o algoritmo Q-learning
ALPHA = 0.7
GAMMA = 0.9
EPSILON = 0.1
NUM_EPISODES = 20

# Define as ações possíveis
actions = ['left', 'jump', 'right']

for i in range(NUM_EPISODES):
    # variavel da proxima ação
    acao = random.choice(actions)
    estado, recompensa = cn.get_state_reward(state, acao)

    while recompensa != 300:
        # calculo da linha do arquivo resultado.txt a ser modificada
        posicao = int(estado[2:7], 2)*4 + int(estado[7:], 2) 

        # abrindo documento
        f = open('resultado.txt', 'r')  

        # Armazenando as linhas do arquivo em uma array
        resultados = f.readlines()

        # armazenando linha selecionada e recebendo valores separadamente
        linha = resultados[posicao]
        numeros_string = linha.split(" ")
        numeros = []

        for x in numeros_string:
            numeros.append(float(x))

        # Escolhe a ação a ser tomada usando a política epsilon-greedy
        if random.uniform(0, 1) < EPSILON:
            acao = random.choice(actions)
        else:
            # Pegar o máximo valor da tabela q_table
            valor = numeros.index(max(numeros[0], numeros[1], numeros[2]))
            acao = actions[valor]
        
        # Executa a ação e recebe o novo estado e a recompensa
        new_state, recompensa = cn.get_state_reward(state, acao)

        # calculo da nova linha do arquivo resultado.txt
        nova_posicao = int(new_state[2:7], 2)*4 + int(new_state[7:], 2)

        # armazenando nova linha selecionada e recebendo valores separadamente
        nova_linha = resultados[nova_posicao]
        novo_numeros_string = nova_linha.split(" ")
        novo_numeros = []

        for x in novo_numeros_string:
            novo_numeros.append(float(x)) 

        #OBS.: A ordem das colunas na Q-Table[left, jump, right]
        # substituindo o valor de acordo com a ação correspodente
        if acao == "left":
            novo_valor = ALPHA * (recompensa + GAMMA * max(float(novo_numeros_string[0]), float(novo_numeros_string[1]), float(novo_numeros_string[2])) - float(numeros_string[0]))
            atual = str(float(novo_valor) + float(numeros_string[0])) + " " + numeros_string[1] + " " + numeros_string[2]
        elif acao == "jump":
            novo_valor = ALPHA * (recompensa + GAMMA * max(float(novo_numeros_string[0]), float(novo_numeros_string[1]), float(novo_numeros_string[2])) - float(numeros_string[1]))
            atual = numeros_string[0] + " " + str(float(novo_valor) + float(numeros_string[1])) + " " + numeros_string[2]
        elif acao == "right":
            novo_valor = ALPHA * (recompensa + GAMMA * max(float(novo_numeros_string[0]), float(novo_numeros_string[1]), float(novo_numeros_string[2])) - float(numeros_string[2]))
            atual = numeros_string[0]+ " " + numeros_string[1] + " " + str(float(novo_valor) + float(numeros_string[2])) + "\n"
            atual = atual.replace(r"\n", "\n")

        # reescrevendo a linha selecionada
        resultados[posicao] = atual
        print(recompensa, " while")

        # reescrevendo documento com a array modificada
        f = open('resultado.txt', 'w')
        f.writelines(resultados)

        estado = new_state

# fechando documento 
f.close()