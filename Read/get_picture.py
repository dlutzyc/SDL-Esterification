#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: get_picture.py
Author: Zinc Zou
Email: zincou@163.com
Date: 2024/9/27
Copyright: 慕乐网络科技(大连）有限公司
        www.mools.net
        moolsnet@126.com
Description: 
"""


def draw(txt_name):
    import matplotlib.pyplot as plt
    import numpy as np
    import time

    # 初始化图和轴
    fig, ax = plt.subplots()
    ax.set_xlabel('time[min]')
    ax.set_ylabel('voltage[mV]')

    # 打开文件
    with open(txt_name, 'r') as file:
        # 跳过标题行
        next(file)

        # 初始化列表来存储数据
        times = []
        signals = []

        # 逐行读取数据
        for line in file:

            print(line)
            try:
                time_str, signal_str = line.split('\t')  # 假设数据由制表符分隔
            except:
                break
            time_float = float(time_str.strip())
            signal_float = float(signal_str.strip())

            # 将数据添加到列表中
            times.append(time_float)
            signals.append(signal_float)
            if len(times)%10 == 0 :
                # 绘制点
                ax.plot(times, signals, 'r-', markersize=2)  # 'ro-' 表示红色圆圈和线
                # time.sleep(1)
                # 暂停一下以便看到效果
                plt.pause(0.001)

    # 完成后，显示图表
    plt.show()


if __name__ == '__main__':
    name = r'data/阿司匹林待测05.txt'
    draw(name)
