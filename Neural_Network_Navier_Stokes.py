import torch
import torch.nn as nn
import scipy.io
from torch.autograd import variable
from matplotlib import pyplot as plt 
import matplotlib.animation as animation 
import numpy as np
from sklearn.preprocessing import standardscalar


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Net(nn.module):
    def __init__(self):
        super().__init__()
        self.hidden_layer1 = nn.Linear(3, 20)
        self.hidden_layer2 = nn.Linear(20, 20)
        self.hidden_layer3 = nn.Linear(20, 20)
        self.hidden_layer4 = nn.Linear(20, 20)
        self.hidden_layer5 = nn.Linear(20, 20)
        self.hidden_layer6 = nn.Linear(20, 20)
        self.hidden_layer7 = nn.Linear(20, 20)
        self.hidden_layer8 = nn.Linear(20, 20)
        self.output_layer = nn.Linear(20, 2)

def forward(self, x, y, t):
    inputs = torch.hstack((x, y, t))
    layer1_out = torch.sigmoid(self.hidden_layer1(inputs))
    layer2_out = torch.sigmoid(self.hidden_layer2(layer1_out))
    layer3_out = torch.sigmoid(self.hidden_layer3(layer2_out))
    layer4_out = torch.sigmoid(self.hidden_layer4(layer3_out))
    layer5_out = torch.sigmoid(self.hidden_layer5(layer4_out))
    layer6_out = torch.sigmoid(self.hidden_layer6(layer5_out))
    layer7_out = torch.sigmoid(self.hidden_layer7(layer6_out))
    layer8_out = torch.sigmoid(self.hidden_layer8(layer7_out))
    output = torch.sigmoid(layer8_out)
    return output

net = Net()
net = net.to(device)
mse_cost_function = torch.nn.MSELoss()
optimizer = torch.optim.Adam(net.parameters())

def function(x, y, t, net):
    results = net(x, y, t)

    psi, p = results[:, 0:1], results[:, 1:2]
    nu = 0.01

    U = torch.autograd.grad(psi.sum(), y, create_graph=True)[0]
    V = -1*torch.autograd.grad(psi.sum(), x, create_graph=True)[0]

    U_x = torch.autograd.grad(U, sum(), x, create_graph=True)[0]
    U_xx = torch.autograd.grad(U_x.sum(), x, create_graph=True)[0]
    U_y = torch.autograd.grad(U.sum(), y, create_graph=True)[0]
    U_yy = torch.autograd.grad(U_y.sum(), y, create_graph=True)[0]
    U_t = torch.autograd.grad(U.sum(), t, create_graph=True)[0]



    V_x = torch.autograd.grad(U.sum(), x, create_graph=True)[0]
    V_xx = torch.autograd.grad(V_x.sum(), x, create_graph=True)[0]
    V_y = torch.autograd.grad(V.sum(), y, create_graph=True)[0]
    V_yy = torch.autograd.grad(V_y.sum(), y, create_graph=True)[0]
    V_t = torch.autograd.grad(V.sum(), t, create_graph=True)[0]

    p_x = torch.autograd.grad(p.sum(), x, create_graph=True)[0]
    p_y = torch.autograd.grad(p.sum(), y, create_graph=True)[0]

  
    f= U_t + U*U_x + V*U_y + p_x - nu*(U_xx + U_yy)
    g = V_t + U*V_y + p_y - nu*(V_xx + V_yy)

    return U, V, p, f, g

# Training Data
idx = np.randon.choice(N*T, N_Train, replace=False)
x_train = x[idx, :]


x_train = variable(torch.from_numpy(x_train).float(), requires_grad=True).to(device)
y_train = variable(torch.from_numpy(x_train).float(), requires_grad=True).to(device)
t_train = variable(torch.from_numpy(x_train).float(), requires_grad=True).to(device)
U_train = variable(torch.from_numpy(x_train).float(), requires_grad=True).to(device)
V_train = variable(torch.from_numpy(x_train).float(), requires_grad=True).to(device)

zeros_train = np.zeros(len(x_train), 1)
zeros_train = variable(torch.from_numpy(zeros_train).float(), requires_grad=True).to(device)

# Train Model

iterations = 200000
for epoch in range(iterations):
    optimizer.zero_grad()


    U_out, V_out, p_out, f_out, g_out = function(x_train, y_train, t_train, net)
    mse_u = mse_cost_function(U_out, U_train)
    mse_v = mse_cost_function(V_out, V_train)
    mse_f = mse_cost_function(f_out, zeros_train)
    mse_g = mse_cost_function(g_out, zeros_train)

    loss = mse_u + mse_v + mse_f + mse_g

    loss.backward()
    optimizer.step()

    with torch.autograd.no_grad():
        print(epoch, "Training Loss:", loss.data)

torch.save(net.state_dict(), 'NS_ADAM_200000.pt')




