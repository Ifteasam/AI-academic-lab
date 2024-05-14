# AND Gate Using Perceptron

# a b y
# 0 0 0 
# 0 1 0
# 1 0 0
# 1 1 1

def activation(out,threshold):
    if out>=threshold:
        return 1
    else:
        return 0

def perceptron(and_input):
    a = [0,0,1,1]
    b = [0,1,0,1]
    y = [0,0,0,1] # Actual Output
    w = [1.4,1.5]
    threshold = 1
    learning_rate = 0.1
    i=0
    print("Perceptron Training : ")
    print("#####################")
    print("-----------------")
    while i<4:
        summation = a[i]*w[0] + b[i]*w[1]
        o = activation(summation,threshold)
        print("Input : " + str(a[i]) +" , "+ str(b[i]))
        print("Weights : " + str(w[0]) +" , "+ str(w[1]))
        print("summation : "+str(summation) + " threshold : "+str(threshold) )
        print("Actual Output : "+str(y[i])+" Predicated Output : "+str(o))
        if(o!=y[i]):
            # w = w + learning_rate(actual_output - predicated_output)*input
            print("_______\nUpdating Weights")
            w[0]=w[0]+learning_rate*(y[i]-o)*a[i]
            w[1]=w[1]+learning_rate*(y[i]-o)*b[i]
            print("Updated Weights : " + str(w[0]) +" , "+ str(w[1]))
            i = -1
            print("\nWeights Updated Training Again : ")
            print("###################################")
        i=i+1
        print("------------------")
    # Prediction Part
    summation = and_input[0]*w[0] + and_input[1]*w[1]
    return activation(summation,threshold)


and_input = [1,1]
print("AND GAte Output For "+str(and_input) + " : " + str(perceptron(and_input)))
