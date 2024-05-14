input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
output_data = [1, 0, 0, 0]
weight = [1, -1]
learning_rate = 0.5
threshold = -1


def learn(n):
    sum1 = 0
    for a in range(len(weight)):
        sum1 = sum1 + weight[a] * input_data[n][a]
    print("sum(w{}*x{}) = {}".format(n + 1, n + 1, sum1), end=" ")
    if sum1 < threshold:
        return 0
    else:
        return 1


def update_weight(er, n):
    for a in range(len(weight)):
        weight[a] = weight[a] + learning_rate * er * input_data[n][a]
        print("    w{} = w{}+{}*{}*{} = {}".format(a + 1, a + 1, learning_rate, er, input_data[n][a], weight[a]))


i = 0
while i <= 3:
    p_output = learn(i)
    print("{}  true value = {}".format(p_output, output_data[i]))
    if p_output != output_data[i]:
        error = output_data[i] - p_output
        update_weight(error, i)
        i = 0
    else:
        i= i+1
