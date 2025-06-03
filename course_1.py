'''
    1-3 最多约数问题
    问题描述: 正整数x的约数是能整除x的正整数。正整数x的约数个数记为div(x)。例如，1、2、5、10都是正整数10的约数，且div(10)=4。
    设a和b是2个正整数，a<=b，找出a和b之间约数个数最多的数x。
    算法设计：对于给定的2个正整数a<=b,计算a和b之间约数个数最多的数
'''

# TODO: 代码解释
# 初始化: 定义前15个质数列表primes
# 主函数 find_number_with_most_divisors
#   处理输入区间[a, b]
#   调用DFS函数生成候选数，并更新约数个数最多的数
#   若未找到候选数(best_num==0):
#       若区间长度 <= 10000,暴力扫描每个数的约数个数
#       否则，返回区间最小数a
# DFS函数
#   参数: 当前数current_value, 当前约数个数current_divisors, 上一个指数last_exponent, 当前质数索引index
#   剪纸: 当前数超过b, 或当前约数个数无法超过最大记录
#   递归生成数: 尝试跳过当前质数， 或使用当前质数的指数 (1到last_exponent)
#   更新: 若生成数在[a, b]内且约数个数更多(或相同但数更小)，则更新结果
# 辅助函数count_divisors: 计算一个数的约数个数(通过遍历到平方根)

import math  # 导入数学模块（实际代码中未使用）

# 预定义的前15个质数列表，用于高效生成约数最多的候选数
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def find_number_with_most_divisors(a, b):
    if a > b:  # 处理无效输入：如果a大于b，直接返回a
        return a

    # 初始化最佳结果：best_num存储约数最多的数，max_divisors存储最大约数个数
    best_num = 0
    max_divisors = 0

    # 深度优先搜索(DFS)函数 - 核心算法
    def dfs(current_value, current_divisors, last_exponent, index):
        nonlocal best_num, max_divisors  # 引用外层变量

        # 边界检查1：当前值超过上限b，停止搜索
        if current_value > b:
            return

        # 检查当前值是否在[a, b]区间内
        if current_value >= a:
            # 更新最佳结果：约数更多，或约数相同但数值更小
            if current_divisors > max_divisors or (current_divisors == max_divisors and current_value < best_num):
                best_num = current_value
                max_divisors = current_divisors

        # 边界检查2：所有质数已用完
        if index >= len(primes):
            return

        # 边界检查3：指数已降至0以下
        if last_exponent < 1:
            return

        # 剪枝优化1：当前约数乘积不可能超过最大值
        if current_divisors * (last_exponent + 1) < max_divisors:
            return

        p = primes[index]  # 获取当前质数

        # 剪枝优化2：继续乘质数会超过b
        if current_value > b // (p ** last_exponent):
            return

        # 选项1：不使用当前质数，直接处理下一个质数
        dfs(current_value, current_divisors, last_exponent, index + 1)

        temp = current_value  # 保存当前值
        # 尝试当前质数的不同指数(1到last_exponent)
        for e in range(1, last_exponent + 1):
            temp *= p  # 乘以当前质数
            if temp > b:  # 超过上限则停止
                break

            # 计算新的约数个数：根据约数定理公式
            new_divisors = current_divisors * (e + 1)

            # 剪枝优化3：新约数个数不够大
            if new_divisors < max_divisors:
                continue

            # 选项2：使用当前质数^e，继续处理下一个质数
            # 指数递减保证：下一个质数的指数不超过当前指数(e)
            dfs(temp, new_divisors, e, index + 1)

    # 启动DFS：初始值为1，约数1个，初始指数60，从第一个质数开始
    dfs(1, 1, 60, 0)

    # 处理未找到候选数的情况
    if best_num == 0:
        # 小范围区间：暴力计算每个数的约数个数
        if b - a + 1 <= 10000:
            best_candidate = a
            max_count = 0
            # 遍历区间内所有数
            for x in range(a, b + 1):
                count = count_divisors(x)  # 计算约数个数
                # 更新最佳候选数
                if count > max_count or (count == max_count and x < best_candidate):
                    best_candidate = x
                    max_count = count
            return best_candidate
        else:
            # 大范围区间：返回区间左端点（后备方案）
            return a

    return best_num  # 返回找到的最佳结果


# 计算一个数的约数个数的辅助函数
def count_divisors(n):
    if n == 1:  # 1的约数只有自身
        return 1

    count = 0  # 约数计数器
    i = 1  # 起始因子

    # 只需遍历到sqrt(n)
    while i * i <= n:
        if n % i == 0:  # 发现约数
            if i * i == n:  # 平方根情况
                count += 1
            else:  # 非平方根情况（一对约数）
                count += 2
        i += 1

    return count  # 返回总约数个数


if __name__ == '__main__':
    # a, b = map(int, input().split(' '))
    # 测试用例：在[3, 40]区间内寻找约数最多的数
    a = 3
    b = 40
    resultNumber = find_number_with_most_divisors(a, b)
    print(resultNumber)  # 预期输出：36（有9个约数）


