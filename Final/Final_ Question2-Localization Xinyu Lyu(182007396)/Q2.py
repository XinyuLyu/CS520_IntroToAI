
def value_iteration(): 
    global optimal_policy
    tran_prob = [0.1 * i for i in range(10)]# transition probabilities of each states
    tran_prob[0] = 1
    Unchange_prob = [1 - i for i in tran_prob]# probs of staying in current state
    Replace_prob = [1 for i in range(10)]    # probs of replacing
    Replace_prob[0] = 0
    Reward = [100 - i * 10 for i in range(10)]# rewards of transfer to next state
    Reward[-1] = 0
    Replace_cost = 250
    Beta = 0.9
    Gama = 0.00001
    U = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 states from new to dead
    Action = ['USE', 'REPLACE']
    flag =True
    while (flag):
        U1 = []
        Act = []
        D = 0
        for i in range(9):
            v = [(Unchange_prob[i] * (Reward[i] + Beta * U[i]) + tran_prob[i] * (Reward[i] + Beta * U[i + 1])),
                 Replace_prob[i] * (-Replace_cost + Beta * U[0])]
            u_update = max(v)
            Act.append(v.index(u_update))
            U1.append(u_update)
            if abs(u_update - U[i]) > D:
                D = abs(u_update - U[i])
        u_update = -Replace_cost + Beta * U[0]
        U1.append(u_update)
        Act.append(1)
        if abs(u_update - U[-1]) > D:
            D = abs(u_update - U[-1])
        U = U1
        optimal_policy = Act
        if D < Gama * (1 - Beta) / Beta:
            flag= False
    return optimal_policy,Action,U



if __name__=="__main__":
    optimal_policy, Action,utility=value_iteration()
    optimal_policy = [Action[i] for i in optimal_policy]
    result = zip(optimal_policy,utility)
    for i in result:
        print(i)