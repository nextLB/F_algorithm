'''
    1-3 最多约数问题
    问题描述: 正整数x的约数是能整除x的正整数。正整数x的约数个数记为div(x)。例如，1、2、5、10都是正整数10的约数，且div(10)=4。
    设a和b是2个正整数，a<=b，找出a和b之间约数个数最多的数x。
    算法设计：对于给定的2个正整数a<=b,计算a和b之间约数个数最多的数
'''
import numpy as np

MAXP = 50

# primes()函数用于产生质数
def primes():
    GET = np.full(MAXP+1, True, dtype=bool)
    for i in range(2, MAXP+1):
        if GET[i]:
            j = i + 1
            while j <= MAXP:
                GET[j] = False
                j += i
    print(GET)


# search()函数用于搜索最多约数



if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    primes()



