#Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as cn
import random
import numpy as np
import time


# Conecta-se ao servidor do jogo
s = cn.connect(2037)

# Define as constantes para o algoritmo Q-learning
ALPHA = 0.5
GAMMA = 0.9
EPSILON = 0.1
NUM_EPISODES = 1000

# Define as ações possíveis
actions = ['left', 'right', 'jump']

# Inicializa a Q-table com zeros
q_table = np.zeros((96, 3))


# Inicia o loop de episódios
for i in range(NUM_EPISODES):
    # Reseta o ambiente e obtém o estado inicial
    action = 'jump'
    state, reward = cn.get_state_reward(s, action)

    # Inicia o loop para cada passo do episódio
    while reward != -1:
        # Escolhe a ação a ser tomada usando a política epsilon-greedy
        if random.uniform(0, 0.1) < EPSILON:
            action = random.choice(actions)
        #else:
            ###??? Pegar o máximo valor da tabela q_table

        # Executa a ação e recebe o novo estado e a recompensa
        new_state, reward = cn.get_state_reward(s, action)

        # Atualiza a Q-table usando a equação de Q-learning
        #???q_table[state, action] += ALPHA * (reward + GAMMA * np.max(q_table[new_state]) - q_table[state, action])

        # Define o novo estado como o estado atual
        state = new_state

        # Espera um tempo antes de executar o próximo passo do episódio
        # time.sleep(0.01)

    # Exibe a recompensa obtida no final do episódio
    print(f"Episódio {i}: Recompensa = {reward}")

