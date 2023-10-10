import numpy as np


bounds = [[0,1],[0,1],[0,1],[0,1],[0,1]]
dim = 5
fmax = 100
fmin = 0
vmax = 0
y_opt = 10

def f(theta):
      T = 5
      m = 5
      n = 4
      R1 = np.array([[1.0000, 0.8209, 0.4744, 0.1791],
                     [1.0000, 0.6892, 0.6806, 0.1563],
                     [1.0000, 1.0000, 0.7841, 0.0000],
                     [0.7067, 1.0000, 1.0000, 0.0000],
                     [0.7013, 1.0000, 1.0000, 0.0000]
                     ])
      R2 = np.array([[0.7215, 0.5224, 0.2436, 0.4179],
                     [0.7403, 0.4459, 0.5000, 0.3906],
                     [0.7531, 0.7273, 0.4205, 0.2500],
                     [0.4400, 0.7606, 0.7639, 0.2405],
                     [0.4416, 0.7258, 0.7848, 0.2319]
                     ])
      R3 = np.array([[0.3415, 0.2687, 0.0000, 0.6716],
                     [0.4675, 0.2297, 0.2500, 0.6719],
                     [0.4568, 0.4545, 0.2273, 0.5000],
                     [0.2533, 0.4930, 0.5278, 0.4810],
                     [0.2078, 0.5323, 0.5696, 0.4638]
                     ])
      R4 = np.array([[0.2532, 0.0000, 0.7051, 1.0000],
                     [0.4935, 0.0000, 0.0000, 1.0000],
                     [0.2346, 0.2338, 0.0000, 0.7125],
                     [0.0000, 0.2394, 0.2361, 0.6456],
                     [0.0000, 0.2419, 0.2658, 0.8116]
                     ])
      R5 = np.array([[0.0000, 1.0000, 1.0000, 0.0000],
                     [0.0000, 1.0000, 1.0000, 0.0000],
                     [0.0000, 0.0000, 1.0000, 1.0000],
                     [1.0000, 0.0000, 0.0000, 1.0000],
                     [1.0000, 0.0000, 0.0000, 1.0000]
                     ])
      lambda1 = 0.4
      lambda2 = 0.1
      lambda3 = 0.2
      lambda4 = 0.1
      lambda5 = 0.2

      RC = np.array(0.4 * R1 + 0.1 * R2 + 0.2 * R3 + 0.1 * R4 + 0.2 * R5)

      R1_ = theta[0] * R1 + (1 - theta[0]) * RC
      R2_ = theta[1] * R2 + (1 - theta[1]) * RC
      R3_ = theta[2] * R3 + (1 - theta[2]) * RC
      R4_ = theta[3] * R4 + (1 - theta[3]) * RC
      R5_ = theta[4] * R5 + (1 - theta[4]) * RC


      lambda1_ = (lambda1 + (1 - theta[0]) / sum(1 - theta)) / 2
      lambda2_ = (lambda2 + (1 - theta[1]) / sum(1 - theta)) / 2

      lambda3_ = (lambda3 + (1 - theta[2]) / sum(1 - theta)) / 2
      lambda4_ = (lambda4 + (1 - theta[3]) / sum(1 - theta)) / 2
      lambda5_ = (lambda5 + (1 - theta[4]) / sum(1 - theta)) / 2

      RC_ = lambda1_ * R1_ + lambda2_ * R2_ + lambda3_ * R3_ + lambda4_ * R4_ + lambda5_ * R5_
      D1 = abs(R1_ - RC_)
      D2 = abs(R2_ - RC_)
      D3 = abs(R3_ - RC_)
      D4 = abs(R4_ - RC_)
      D5 = abs(R5_ - RC_)
      y = np.sum(D1 + D2 + D3 + D4 + D5) / (T*m*n)
      return y, 0

if __name__ == "__main__":
      print(f(np.array([0.1,0.2,0.3,0.4,0.5])))
