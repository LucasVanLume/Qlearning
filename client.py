#Aqui vocês irão colocar seu algoritmo de aprendizado
import connection as cn

state = cn.connect()

estado, recompensa = cn.get_state_reward(state, "jump")

