import numpy as np
import math
from scipy.integrate import ode

def sign(value):
    if value > 1.0e-3:
        return 1
    elif value < -1.0e-3:
        return -1
    else:
        return 0
    pass

class Car(object):
    """Model expressing a simulated car"""
    def __init__(self, initialCondition=np.zeros(4), initialInput=np.zeros(2)):
        super(Car, self).__init__()

        # 初期状態の設定
        t0 = 0.0         # 初期時間 0[sec]
        self.dt = 1.0 / 100  # シミュレーションの時間幅   0.001[sec]

        # 状態変数の設定
        self.x = initialCondition #[x, y, v, theta] 特に指定が無ければ初期状態は全て0
        # 入力の設定
        self.i = initialInput     #[a, phi]         特に指定が無ければ初期入力は共に0

        # 微分解法の設定
        self.solver = ode(self.dynamics).set_integrator('dopri5') # 解法の指定
        self.solver.set_initial_value(self.x,t0)  # 初期条件の指定
        self.solver.set_f_params(self.i)          #

    def run(self, input):
        self.i = input
        solver = self.solver
        solver.set_f_params(input)
        solver.integrate(solver.t+self.dt)
        self.x = solver.y
        # print(input)
        return solver.t, solver.y

    def dynamics(self, input):
        return np.array([self.velX(), self.velY(), self.acc(input), self.yawRate(input)])

    def posX(self):
        return self.x[0]

    def posY(self):
        return self.x[1]

    def vel(self):
        return self.x[2]

    def course(self):
        return self.x[3]

    def velX(self):
        return self.vel() * math.cos(self.x[3])

    def velY(self):
        return self.vel() * math.sin(self.x[3])

    def acc(self, input):
        # print(input)
        if input[0] >= 0:
            return input[0]
        else:
            return sign(self.vel()) * input[0]

    def yawRate(self, input):
        l=1.0
        # print(input)
        return self.vel() * math.tan(input[1]) / l
