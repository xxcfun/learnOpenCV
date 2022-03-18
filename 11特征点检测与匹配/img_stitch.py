"""
图像拼接
1 读取文件，将图片设置成一样大小，默认640*480
2 找特征点，描述子，计算单应性矩阵
3 根据单应性矩阵对图像进行变换，然后平移
4 拼接并输出最终结果
"""
import cv2
import numpy as np


# 获取单应性矩阵的函数
def get_homo(img1, img2):
    # 1 创建特征转换对象
    # 2 通过特征转换对象获得特征点和描述子
    # 3 创建特征匹配器
    # 4 进行特征匹配
    # 5 过滤特征点，找出有效的特征匹配点
    # 6 最后得到单应性矩阵

    # 创建对象
    sift = cv2.SIFT_create()

    # 通过特征转换对象获得特征点和描述子
    k1, d1 = sift.detectAndCompute(img1, None)
    k2, d2 = sift.detectAndCompute(img2, None)

    # 创建特征匹配器
    bf = cv2.BFMatcher()

    # 进行特征匹配
    maches = bf.knnMatch(d1, d2, k=2)

    # 过滤特征点，找出有效的特征匹配点
    verify_matchs = []
    # 经验可得这里用0.8 用0.7来测试
    verify_ratio = 0.7
    for m1, m2 in maches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matchs.append(m1)

    min_matches = 8
    if len(verify_matchs) > min_matches:
        img1_pts = []
        img2_pts = []

        for m in verify_matchs:
            img1_pts.append(k1[m.queryIdx].pt)
            img2_pts.append(k2[m.trainIdx].pt)

        # [(x1, y1), (x2, y2), ...]
        # [[x1, y1], [x2, y2], ...]

        # 调整参数格式
        img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)

        # 寻找单应性矩阵
        H, mask = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 5.0)

        return H
    else:
        print("err: not enough matches ! ! !")
        exit()


# 进行图像拼接的函数
def stitch_image(img1, img2, H):
    # 1 获得每张图片的四个角点
    # 2 对图片进行变换（单应性矩阵使图进行旋转，平移）
    # 3 创建一张大图，将两张图拼接在一起
    # 4 将结果输出

    # 获得原始图高、宽
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)

    # 图像做变换
    img1_transform = cv2.perspectiveTransform(img1_dims, H)

    # 横向拼接
    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)

    # 获取最大和最小值 ravel的作用是二维变一维
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel()-0.5)
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel()+0.5)

    # 平移的距离
    transform_dist = [-x_min, -y_min]

    # 构建一个齐次坐标
    # [1, 0, dx]
    # [0, 1, dy]
    # [0, 0, 1 ]
    transform_array = np.array([
        [1, 0, transform_dist[0]],
        [0, 1, transform_dist[1]],
        [0, 0, 1]
    ])

    # 投影变换
    result = cv2.warpPerspective(img1, transform_array.dot(H), (x_max-x_min, y_max-y_min))
    # result = cv2.warpPerspective(img1, H, (x_max-x_min, y_max-y_min))

    # 拼接
    result[transform_dist[1]:transform_dist[1]+h2, transform_dist[0]:transform_dist[0]+w2] = img2
    return result


# 读取两张图片
img1 = cv2.imread('bin1.png')
img2 = cv2.imread('bin2.png')

# 将两张图片设置成一样大小
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

input = np.hstack((img1, img2))

# 获得单应性矩阵
H = get_homo(img1, img2)

# 进行图像拼接
result_image = stitch_image(img1, img2, H)

cv2.imshow('result_image', result_image)
cv2.waitKey(0)
