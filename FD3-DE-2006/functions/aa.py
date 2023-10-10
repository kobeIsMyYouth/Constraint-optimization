import numpy as np
# R_1 = [
#     [0.333,0.000,0.000,0.000],
#     [0.000,1.000,0.500,0.333],
#     [1.000,0.500,0.250,1.000],
#     [0.667,0.000,1.000,0.778]
# ]
# R_2 = [
#     [0.500,1.000,0.000,0.500],
#     [0.250,0.000,1.000,0.750],
#     [1.000,1.000,0.500,0.000],
#     [0.000,0.500,1.000,1.000]
# ]
# R_3 = [
#     [0.500,0.667,0.000,0.000],
#     [0.500,0.333,1.000,0.714],
#     [1.000,1.000,0.667,1.000],
#     [0.000,0.000,0.333,0.714]
# ]
# lamb= np.array([0.3,0.3,0.4])
# R_A = 0.3 * R_1 + 0.3 * R_2 + 0.4 * R_3
# print(R_A.round(3))

bounds = [(0,1),(0,1),(0,1)]
# thelta = [θ_1,θ_2,θ_3]
dim = 3
fmax = 10
fmin = 0
vmax = 1
y_opt = 10

# def f(thelta):
#     R_1 = np.array([
#         [0.333, 0.000, 0.000, 0.000],
#         [0.000, 1.000, 0.500, 0.333],
#         [1.000, 0.500, 0.250, 1.000],
#         [0.667, 0.000, 1.000, 0.778]
#     ])
#     R_2 = np.array([
#         [0.500, 1.000, 0.000, 0.500],
#         [0.250, 0.000, 1.000, 0.750],
#         [1.000, 1.000, 0.500, 0.000],
#         [0.000, 0.500, 1.000, 1.000]
#     ])
#     R_3 = np.array([
#         [0.500, 0.667, 0.000, 0.000],
#         [0.500, 0.333, 1.000, 0.714],
#         [1.000, 1.000, 0.667, 1.000],
#         [0.000, 0.000, 0.333, 0.714]
#     ])
#     R_A = 0.3 * R_1 + 0.3 * R_2 + 0.4 * R_3
#     y = (sum(map(sum,abs(0.7 * R_1 * thelta[0] + 0.7 * R_A * (1 - thelta[0]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.4 * R_3 * thelta[
#         2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
#         0.7 * R_2 * thelta[1] + 0.7 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[0] - 0.3 * R_A * (1 - thelta[0]) - 0.4 * R_3 * thelta[
#             2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
#         0.6 * R_3 * thelta[2] + 0.6 * R_A * (1 - thelta[2]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[
#             0] - 0.3 * R_A * (1 - thelta[0]))))) / 48 - 1
#     return y

def f(thelta):
    R_1 = np.array([
                [0.333, 0.000, 0.000, 0.000],
                [0.000, 1.000, 0.500, 0.333],
                [1.000, 0.500, 0.250, 1.000],
                [0.667, 0.000, 1.000, 0.778]
            ])
    R_2 = np.array([
                [0.500, 1.000, 0.000, 0.500],
                [0.250, 0.000, 1.000, 0.750],
                [1.000, 1.000, 0.500, 0.000],
                [0.000, 0.500, 1.000, 1.000]
            ])
    R_3 = np.array([
                [0.500, 0.667, 0.000, 0.000],
                [0.500, 0.333, 1.000, 0.714],
                [1.000, 1.000, 0.667, 1.000],
                [0.000, 0.000, 0.333, 0.714]
            ])
    R_A = 0.3 * R_1 + 0.3 * R_2 + 0.4 * R_3
    z = (sum(map(sum,abs(R_1 - 0.3 * R_1 * thelta[0] - 0.3 * R_A * (1 - thelta[0]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.4 * R_3 *
             thelta[2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
        R_2 - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[0] - 0.3 * R_A * (1 - thelta[0]) - 0.4 * R_3 * thelta[
            2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
        R_3 - 0.4 * R_3 * thelta[2] - 0.4 * R_A * (1 - thelta[2]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[
            0] - 0.3 * R_A * (1 - thelta[0]))))) / 48
    w1 = (sum(map(sum,abs(0.7 * R_1 * thelta[0] + 0.7 * R_A * (1 - thelta[0]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.4 * R_3 * thelta[
        2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
        0.7 * R_2 * thelta[1] + 0.7 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[0] - 0.3 * R_A * (1 - thelta[0]) - 0.4 * R_3 * thelta[
            2] - 0.4 * R_A * (1 - thelta[2])))) + sum(map(sum,abs(
        0.6 * R_3 * thelta[2] + 0.6 * R_A * (1 - thelta[2]) - 0.3 * R_2 * thelta[1] - 0.3 * R_A * (1 - thelta[1]) - 0.3 * R_1 * thelta[
            0] - 0.3 * R_A * (1 - thelta[0]))))) / 48 - 0.15
    w1 = max(w1,0)
    return z, w1