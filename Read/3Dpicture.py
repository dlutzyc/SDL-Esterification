#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: 3Dpicture.py
Author: Zinc Zou
Email: zincou@163.com
Date: 2024/9/27
Copyright: 慕乐网络科技(大连）有限公司
        www.mools.net
        moolsnet@126.com
Description: 
"""


def print_hi(name):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    # 数据
    time = np.array([1, 2, 3, 4, 5])  # 时间
    yield_1x = np.array([26.52, 33.52, 36.70, 41.45, 43.79]) / 100  # 1倍质量催化剂产率，转换为小数
    yield_2x = np.array([32.68, 40.44, 39.62, 46.83, 50.15]) / 100  # 2倍质量催化剂产率，转换为小数
    yield_3x = np.array([36.96, 44.98, 49.23, 51.40, 51.37]) / 100  # 3倍质量催化剂产率，转换为小数

    # 创建图形和轴
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制三条曲线
    ax.scatter(time, yield_1x, np.zeros_like(time), label='1-fold quality catalyst yield')
    ax.scatter(time, yield_2x, np.ones_like(time), label='2-fold quality catalyst yield')
    ax.scatter(time, yield_3x, np.ones_like(time)*2, label='3-fold quality catalyst yield')

    # 设置标签
    ax.set_xlabel('time (h)')
    ax.set_ylabel('productivity (%)')
    ax.set_zlabel('Catalyst_Quality')

    # 设置z轴的刻度
    ax.set_zticks([0, 1, 2])
    ax.set_zticklabels(['1_times', '2_times', '3_times'])

    # 添加图例
    ax.legend(loc='upper right')  # 将图例放在左上角

    # 显示图形
    plt.show()


def print_picture():
    import matplotlib.pyplot as plt
    import numpy as np

    # 数据
    time = np.array([1, 2, 3, 4, 5])
    yields_1x = np.array([26.52, 33.52, 36.70, 41.45, 43.79])
    yields_2x = np.array([32.68, 40.44, 39.62, 46.83, 50.15])
    yields_3x = np.array([36.96, 44.98, 49.23, 51.40, 51.37])

    # 催化剂质量倍数
    catalyst_multipliers = [1, 2, 3]

    # 创建一个图形
    fig, ax = plt.subplots()

    size_scale = 3  # 缩放因子，可以根据需要调整
    max_size = 1000  # 最大点大小

    # 绘制散点图，使用点的大小来表示产率
    for multiplier, yields in zip(catalyst_multipliers, [yields_1x, yields_2x, yields_3x]):
        for t, y in zip(time, yields):
            size = (y / np.max(yields) * max_size) * size_scale
            ax.scatter(t, multiplier, s=size, c='y', alpha=0.7)
            # 在每个点中心添加文本，显示其产率值
            # 由于散点的大小可能会影响文本的可见性，我们可能需要稍微调整文本的位置
            # 这里我们使用va='center'和ha='center'来确保文本在点的中心
            ax.text(t, multiplier, f'{y:.2f}', ha='center', va='center', color='red')

        # 设置x轴和y轴的范围
    ax.set_xlim(0.5, 5.5)  # 设置x轴的范围从0到6
    ax.set_ylim(0.5, 3.5)  # 设置y轴的范围从0到4
    # 设置标签和刻度
    ax.set_xlabel('time (h)')
    ax.set_ylabel('Catalyst_Quality')
    ax.set_yticks(catalyst_multipliers)
    ax.set_yticklabels([f'{m}_times' for m in catalyst_multipliers])

    # 添加颜色条
    # cbar = fig.colorbar(ax.collections[0], ax=ax, label='Yield (%)')
    fig.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
    # 显示图例
    # ax.legend(title='Catalyst_Quality')

    # 显示图形
    plt.show()


def picture():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import time

    # 数据
    time = np.array([1, 2, 3, 4, 5])
    yields_1x = np.array([26.52, 33.52, 36.70, 41.45, 43.79])
    yields_2x = np.array([32.68, 40.44, 39.62, 46.83, 50.15])
    yields_3x = np.array([36.96, 44.98, 49.23, 51.40, 51.37])

    # 催化剂质量倍数
    catalyst_multipliers = [1, 2, 3]

    # 创建一个图形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 为每个催化剂倍数绘制散点图
    colors = ['r', 'g', 'b']  # 不同的颜色表示不同的催化剂倍数
    for multiplier, yields, color in zip(catalyst_multipliers, [yields_1x, yields_2x, yields_3x], colors):
        ax.scatter(time, yields, np.full_like(time, multiplier), c=color, label=f'{multiplier}-fold catalyst')

        # 添加图例
    # ax.legend()

    # 设置轴标签
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Yield (%)')
    ax.set_zlabel('Catalyst Multiplier')

    # 显示图形
    plt.show()


def three_d_picture():
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    from mpl_toolkits.mplot3d import Axes3D

    # 数据
    time_list = np.array([1, 2, 3, 4, 5, 6])
    yields_1x = np.array([26.52 , 33.52 , 36.70 , 41.45 , 43.79 , 46.13])
    yields_3x = np.array([30.06 , 42.09 , 43.63 , 50.90 , 52.87 , 56.33])
    yields_4x = np.array([32.84 , 44.06 , 50.13 , 55.11 , 56.49 , 58.75])
    yields_5x = np.array([38.79 , 50.87 , 56.46 , 60.70 , 62.55 , 64.28])

    # 催化剂质量倍数
    catalyst_multipliers = np.array([0.58,1.74,0.58*4,2.9])

    # 为了插值，我们需要一个更密集的催化剂倍数网格
    # 这里我们简单地在线性空间中生成更多的点
    num_points_between = 10  # 每个催化剂倍数之间插入的点数（不包括端点）
    catalyst_grid = np.linspace(catalyst_multipliers[0], catalyst_multipliers[-1],
                                len(catalyst_multipliers) * (num_points_between + 1) - num_points_between)

    # 初始化一个数组来存储插值后的产率（时间 x 催化剂倍数网格）
    time_grid, catalyst_grid = np.meshgrid(time_list, catalyst_grid, indexing='ij')
    yields_grid = np.zeros_like(time_grid)

    # 对每个时间点进行插值
    # 注意：这里我们使用了简单的线性插值，但这可能不是最准确的方法
    # 更复杂的数据可能需要使用如 scipy.interpolate.interp1d 的插值方法，并可能需要更多的数据点
    for t_idx, t in enumerate(time_list):
        # print(t_idx, t)
        f = np.interp(catalyst_grid, catalyst_multipliers, [yields_1x[t_idx], yields_3x[t_idx], yields_4x[t_idx], yields_5x[t_idx]],
                      left=np.nan, right=np.nan)
        # 注意：np.interp 不直接支持多维插值，所以我们需要对每个时间点单独插值
        # 并且这里我们假设在催化剂倍数范围之外的值是 NaN（或可以设置为其他合理的外推值）
        # 但在这个例子中，我们不需要外推，因为 catalyst_grid 已经根据 catalyst_multipliers 设定了
        print(f)
        yields_grid[t_idx, :] = f[t_idx]

        # 绘制三维曲面图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(time_grid, catalyst_grid, yields_grid, cmap='viridis', edgecolor='none')

    # 添加颜色条
    # fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    # 设置轴标签
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Catalyst (g)')
    ax.set_zlabel('Yield (%)')

    plt.savefig(f'Output/{time.time()}.jpg')

    # 显示图形
    plt.show()


if __name__ == '__main__':
    # print_hi('3Dpicture')
    # picture()
    # print_picture()
    three_d_picture()