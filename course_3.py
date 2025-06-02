
'''
    1-5 最大间隙问题
    问题描述: 最大间隙: 给定n个实数x1、x2、...、xn, 求这n个数在实轴上相邻两个数之间的最大差值。假设对任何实数的下取整函数耗时 O(1),
    设计解最大间隙问题的线性时间算法
    算法设计: 对于给定的n个实数 x1、x2、...、xn, 计算它们的最大间隙。(最好使用上鸽舍原理)
'''

# 为了解决上述的问题，可以设计一个线性时间算法。该算法基于鸽舍原理(抽屉原理)，通过分桶策略将问题转化为相邻非空桶之间
# 的最大间隙计算，从而实现O(n)的时间复杂度

# TODO: 代码解释
# 1、初始化检查: 如果数组元素少于2个，最大间隙为0；若所有元素相等，最大间隙也为0
# 2、桶初始化: 创建n+1个桶，每个桶初始化为无穷大(最大值)和负无穷大(最大值)
# 3、元素分配:
#       遍历每个元素，若元素等于最大值，则放入最后一个桶(索引n)
#       否则，计算元素应放入的桶索引: index = floor((x - min_val) / width)
#       更新桶内最小值和最大值
# 4、计算最大间隙
#       初始化prev_max为第一个桶的最大值
#       遍历后续桶，若桶非空，计算当前桶最小值与prev_max的差值，更新最大间隙
#       更新prev_max为当前桶的最大值
# 返回结果: 遍历完成后返回最大间隙值

import math  # 导入数学模块，用于处理浮点数计算


def maximum_gap(nums):
    # 如果数组长度小于2，无法计算间隙，直接返回0
    n = len(nums)
    if n < 2:
        return 0

    # 计算数组的最小值和最大值
    min_val = min(nums)
    max_val = max(nums)

    # 如果所有元素都相等，最大间隙为0
    if min_val == max_val:
        return 0

    # 初始化桶结构：
    # 创建n+1个桶（利用鸽舍原理，确保至少有一个空桶）
    # bucket_min 存储每个桶的最小值，初始化为正无穷
    # bucket_max 存储每个桶的最大值，初始化为负无穷
    bucket_min = [float('inf')] * (n + 1)
    bucket_max = [float('-inf')] * (n + 1)

    # 计算桶的宽度（每个桶覆盖的数值范围）
    width = (max_val - min_val) / n

    # 将每个元素分配到对应的桶中
    for x in nums:
        # 处理最大值特殊情况：直接放入最后一个桶
        if math.isclose(x, max_val, rel_tol=1e-12, abs_tol=1e-12):
            index = n
        else:
            # 计算元素应该放入的桶索引
            index = int(math.floor((x - min_val) / width))

        # 更新桶的最小值
        if x < bucket_min[index]:
            bucket_min[index] = x
        # 更新桶的最大值
        if x > bucket_max[index]:
            bucket_max[index] = x

    # 初始化最大间隙和上一个非空桶的最大值
    max_gap = 0
    prev_max = bucket_max[0]  # 第一个桶的最大值

    # 遍历所有桶（从第1个桶到第n个桶）
    for i in range(1, n + 1):
        # 如果当前桶非空（即有元素落入）
        if bucket_min[i] != float('inf'):
            # 计算当前桶最小值与前一个非空桶最大值的间隙
            gap = bucket_min[i] - prev_max
            # 更新最大间隙
            if gap > max_gap:
                max_gap = gap
            # 更新上一个非空桶的最大值为当前桶的最大值
            prev_max = bucket_max[i]

    # 返回计算得到的最大间隙
    return max_gap
