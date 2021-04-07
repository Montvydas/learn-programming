import numpy as np

class NeuralNetwork:
    def __init__(self, input_count):
        np.random.seed(1)
        # +1 for the bias input
        self.weights = 2 * np.random.random((input_count + 1, 1)) - 1
        # print('weights:\n', self.weights)
        '''
        weights:
        [[w0],
         [w1],
         ...
         [wn]]
        '''
        
    def relu(self, x):
        return x * (x > 0)

    def relu_deriv(self, x):
        return (x > 0) * 1
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_deriv(self, x):
        return x * (1 - x)
    
    def _add_bias(self, arr):
        return np.c_[np.ones(arr.shape[0]), arr]

    def get_weights(self):
        return self.weights
        
    def train_sigmoid(self, training_inputs, training_outputs, iterations):
        biased_inputs = self._add_bias(training_inputs)
        for _ in range(iterations):
            # print('inputs:\n', training_inputs)
            '''
            inputs:
            [[x00, x10, x20], 
            [x01, x11, x21],
                  ...
            [x0n, x1n, x2n]]
            '''
            guessed_outputs = self.sigmoid(np.dot(biased_inputs, self.weights))
            # print('outputs:\n', guessed_outputs)
            '''
            outputs:
            [[y0],
             [y1],
             ...
             [yn]]
            '''
            error = training_outputs - guessed_outputs
            # print('error:\n', error)
            '''
            error:
            [[e0],
             [e1],
             ...
             [en]]
            '''
            adjust = error * self.sigmoid_deriv(guessed_outputs)
            # print('adjust:\n', adjust)
            
            self.weights += np.dot(biased_inputs.T, adjust)
            # print(self.weights)

        print(self.weights)
        # exit()
    
    def guess_sigmoid(self, test_inputs):
        return self.sigmoid(np.dot(self._add_bias(test_inputs), self.weights))

    def train_relu(self, training_inputs, training_outputs, iterations):
        biased_inputs = self._add_bias(training_inputs)
        for _ in range(iterations):
            guessed_outputs = self.relu(np.dot(biased_inputs, self.weights))
            error = training_outputs - guessed_outputs
            adjust = error * self.relu_deriv(guessed_outputs)
            self.weights += np.dot(biased_inputs.T, adjust)

        print(self.weights)

    def guess_relu(self, test_inputs):
        return self.relu(np.dot(self._add_bias(test_inputs), self.weights))
    
if __name__ == '__main__':
    architecture = """
    Architecture:
    We have 4 inputs (well, 3, but then 1 for bias) and one hidden layer consisting of 1 neuron 
    plus that neuron activation function:
    
    in   synapses   neuron               out
    
    1 ------wb---\\
                  \\
    x0 -----w0-----\\
                    \\
    x1 -----w1------ O-activation ------ y
                    / 
    x2 -----w2-----/
    
    * Normalised functions used is ReLU (Sigmoid was used before, but showed problems
    in certain scenarios, however ReLU showed better results overall).
    
    Procedure: 
    1) Initialise weights with random values between -1 and 1 with mean of 0: 
        weights = [[w0], 
                   [w1], 
                   [w2]] 
    2) Create different training data: 
        training_inputs = [[x00, x10, x20], 
                           [x01, x11, x21],
                                 ...
                           [x0n, x1n, x2n]]
    3) Define outputs for the training data:
        training_outputs = [[y0], 
                            [y1], 
                            ...
                            [yn]]
    4) Perform training... For a large number of iterations e.g. 10_000, perform
    the same operations:
        a) calculate the expected output aka guess using _weights_ and _inputs_ (dot product)
        b) compare the _guessed output_ with the _expected output_ to calculate error for 
            each of training sets
        c) adjust the error by multiplying it by the slope, since the furthest away form 
            the expected value, the more adjustment is needed (gradient descent?)
        d) adjust the _weights_ by adding the calculated _error_
    5) Test the input to see how the network behaves by passing in some user values:
        normalise(dot(weights, [[x0, x1, x2]])) -> [[y]]
    """
    np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
    
    input_count = 3
    or_neural_net = NeuralNetwork(input_count=input_count)
    nor_neural_net = NeuralNetwork(input_count=input_count)
    and_neural_net = NeuralNetwork(input_count=input_count)
    nand_neural_net = NeuralNetwork(input_count=input_count)
    xor_neural_net = NeuralNetwork(input_count=input_count) # XOR requires 2 layers for 2 inputs :/

    if input_count == 2:
        some_gate_in = np.array([[0, 0],
                                [0, 1],
                                [1, 0],
                                [1, 1]])

        or_gate_out = np.array([[0, 1, 1, 1]]).T
        nor_gate_out = np.array([[1, 0, 0, 0]]).T
        and_gate_out = np.array([[0, 0, 0, 1]]).T
        nand_gate_out = np.array([[1, 1, 1, 0]]).T
        xor_gate_out = np.array([[0, 1, 1, 0]]).T
        
    if input_count == 3:
        some_gate_in = np.array([[0, 0, 0],
                                [0, 0, 1],
                                [0, 1, 0],
                                [0, 1, 1],
                                [1, 0, 0],
                                [1, 0, 1],
                                [1, 1, 0],                        
                                [1, 1, 1]])
        
        or_gate_out = np.array([[0, 1, 1, 1, 1, 1, 1, 1]]).T
        nor_gate_out = np.array([[1, 0, 0, 0, 0, 0, 0, 0]]).T
        and_gate_out = np.array([[0, 0, 0, 0, 0, 0, 0, 1]]).T
        nand_gate_out = np.array([[1, 1, 1, 1, 1, 1, 1, 0]]).T
        xor_gate_out = np.array([[0, 1, 1, 1, 1, 1, 1, 0]]).T

    
    # xor_neural_net.train_relu(some_gate_in, xor_gate_out, 10_000)
    or_neural_net.train_sigmoid(some_gate_in, or_gate_out, 10_000)
    nor_neural_net.train_sigmoid(some_gate_in, nor_gate_out, 10_000)
    and_neural_net.train_sigmoid(some_gate_in, and_gate_out, 10_000)
    nand_neural_net.train_sigmoid(some_gate_in, nand_gate_out, 10_000)
    xor_neural_net.train_sigmoid(some_gate_in, xor_gate_out, 10_000)

    print('Enter either 0 or 1 for the following (e.g. [0, 1, 0] or [1, 0, 1]):')
    test_inputs = [int(input(f'x{i}: ')) for i in range(input_count)]

    print('OR:', or_neural_net.guess_sigmoid(np.array([test_inputs]))[0])
    print('NOR:', nor_neural_net.guess_sigmoid(np.array([test_inputs]))[0])
    print('AND:', and_neural_net.guess_sigmoid(np.array([test_inputs]))[0])
    print('NAND:', nand_neural_net.guess_sigmoid(np.array([test_inputs]))[0])
    print('XOR:', xor_neural_net.guess_sigmoid(np.array([test_inputs]))[0])