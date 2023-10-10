import cv2
import numpy as np

# 加载图片
img = cv2.imread('img.png')

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 高斯滤波
gray = cv2.GaussianBlur(gray, (3,3), 0)

# 边缘检测
edges = cv2.Canny(gray, 50, 150)

# 霍夫变换检测直线
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

# 绘制直线
if lines is not None:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# 参数化椭圆
if lines is not None:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        # 计算椭圆的参数
        x = int((x1 + x2) / 2)
        y = int((y1 + y2) / 2)
        a = int((x2 - x1) / (2 * np.sin(theta)))
        b = int((y2 - y1) / (2 * np.sin(theta)))
        # 绘制椭圆
        cv2.circle(img,(x,y),(a,b),(0,0,255),2)

# 显示结果
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()