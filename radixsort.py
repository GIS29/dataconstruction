import random


def radix(data,size):
    n = 1   #首先从各位开始
    while n <= 100:
        tmp = [[0] * 100 for row in range(10)]  #建立一个二维数组存储数据
        #存储临时数据
        for i in range(size):   #逐个查看数据
            m = (data[i] // n) % 10  #m为n位数的值，如36取十位数（36/10）%10=3
            tmp[m][i] = data[i]
        k = 0
        #取出临时数据
        for i in range(10):
            for j in range(size):
                if tmp[i][j] != 0:  #把不为零的数据取出来放到data中
                    data[k] = tmp[i][j]
                    k += 1
        print('经过%3d位数排序后：'%n,end='')
        showdata(data,size)
        n *= 10

def showdata(data,size):
    for i in range(size):
        print('%5d'%data[i],end='')
    print()

def inputarr(data,size):
    for i in range(size):
        data[i] = random.randint(0,999)

def main():
    data = [0] * 100
    size = int(input('请输入数组大小（100以下）：'))
    print('您输入的原始数据：')
    inputarr(data,size)
    showdata(data,size)
    radix(data,size)

if __name__ == '__main__':
    main()