# Author - Nitin Patle
# B.Tech 

def activation_function_and_xor(yin):
    if yin>1:
        return 1
    return 0

# and 
weight_vector_and = [1, 1]

def mcculloch_and_neuron(inp):
    yin = 0
    for i in range(len(inp)):
        yin = yin + inp[i]*weight_vector_and[i]
    yout = activation_function_and_xor(yin)
    return yout

weight_vector_xor_first_layer = [
    [2, -1],
    [-1, 2]
]
weight_vector_xor_second_layer = [[2, 2]]


def sigma_yin(inp, weight):
    yin = 0
    for i in range(len(inp)):
        yin = yin + inp[i]*weight[i]
    return yin

def mcculloch_xor_neuron(inp):
    yin = 0
    z1_z2 = [0, 0]
    for i in range(len(weight_vector_xor_first_layer)):
        z1_z2[i] = sigma_yin(inp, weight_vector_xor_first_layer[i])
        z1_z2[i] = activation_function_and_xor(z1_z2[i])
    for i in range(len(weight_vector_xor_second_layer)):
        yin = yin + sigma_yin(z1_z2, weight_vector_xor_second_layer[i])
    return activation_function_and_xor(yin)

def main():
    inp = [0, 0]
    print(mcculloch_and_neuron(inp))
    inp = [1, 0]
    print(mcculloch_xor_neuron(inp))

if __name__ == "__main__":
    main()



