import test_data
import train_data

class hebb_model:
    
    # n = no of inputs
    # m = no of outputs
    # n represented by i
    # m represented by j

    def train(self, train_data):
        
        self.n = len(train_data.s)
        self.m = len(train_data.t)

        self.w = [[0 for i in range(self.n)] for j in range(self.m)]
        self.b = [0 for j in range(self.m)]

        flag = True
        while(True):
            # for every s -> t pair

            #for s in train_data.s:
                




            if flag:
                break


    # sigma yin if feeded with input and weight vectors, bias 
    def sigma_yin(self, x, w, b):
        yin = 0
        # total n inputs represented by i iterator 
        for i in range(len(x)):
            yin += x[i]*w[i]
        return yin

    # simple hebb rule activation function
    # 0 will be boundary 
    def activation_f_hebb(self, yin):
        if yin>=0:
            return 1
        return -1

    def test(self, test_data):


        return []
    

    