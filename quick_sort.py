def quick(data,size,left,right):
    #第一个中间值就是data[left]
    if left < right:
        left_next = left + 1    #从中间值的下一个开始往右查找大于中间值的键值
        while data[left_next] < data[left]:
            if left_next + 1 >= size:
                break
            left_next += 1      #逐个往右边查找出大的那个
        right_pre = right       #右边从right开始查找小于的
        while data[right_pre] > data[left]:
            right_pre -= 1      #逐个往右边查找出小的那个
        #这时候找到了第一个大于和小于中间值的元素，比较两个索引的大小
        #之所以用while，是因为交换完了要接着比较
        while left_next < right_pre:
            #索引小于就交换
            data[left_next],data[right_pre] = data[right_pre],data[left_next]
            #将left_next+1接着查找
            left_next += 1
            while data[left_next] < data[left]:
                left += 1
            #将right_pre-1接着查找
            right_pre -= 1
            while data[right_pre] > data[left]:
                right_pre -= 1
        #如果while left_next < right_pre:满足，就接着查找
        #如果不满足，就和中间值换，然后分割左右两个进行继续排序
        data[left],data[right_pre] = data[right_pre],data[left]
        for i in range(size):
            print(data[i],'',end='')
        print()
        #以right_pre为基准点，进行分割左右两个
        #使用递归调用
        quick(data,size,left,right_pre-1)   #以right_pre为分割点分成左右两边，将左边的进行递归调用
        quick(data,size,right_pre+1,right)  #以right_pre为分割点分成左右两边,将右边的进行递归调用

"""
主程序编写
"""
def main():
    data = [26,3,18,1,67,8,55]
    print("您输入的原始数据是：")
    for i in range(len(data)):
        print(data[i],'',end='')
    print('\n')
    print("排序过程如下：")
    quick(data,len(data),0,len(data)-1)
    print("排序结果是：")
    for i in range(len(data)):
        print(data[i],'',end='')

if __name__ == '__main__':
    main()