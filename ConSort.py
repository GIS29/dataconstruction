"""
合并排序：两个已经有顺序的数组进行合并排序
"""
list1 = [21,6,4,3,999]
list2 = [71,2,3,2,999]
list3=[]
"""
选择排序，先将数组进行排序
"""
def select_sort(data,size):
    #第一次遍历，从第一个元素开始，逐个向后比较
    for base in range(len(data)):
        small = base
        #和第一层循环的元素逐个比较
        for next in range(base,size):
            if data[small] > data[next]:
                small = next
        data[base],data[small] = data[small],data[base]

"""
合并排序，将排序好的数组进行合并排序
"""
def Merge(data,size1,size2):
    global list1
    global list2
    global list3

    index1 = 0
    index2 = 0
    for index3 in range(len(list1)+len(list2)-2):
        #逐个比较两个元组中的数据大小，将小的存放在新的数组中
        if list1[index1] < list2[index2]:
            data.append(list1[index1])
            #将index+1，下次循环比较下一个元素
            index1+=1
            print("此数字{}取自第一个数列".format(data[index3]))
        else:
            data.append(list2[index2])
            #将index2+=1，下次循环比较下一个元素
            index2+=1
            print("此数字{}取自第二个数列".format(list3[index3]))
        print("目前的合并排序结果是：")
        for i in range(index3 + 1):
            print(list3[i],'',end='')
        print('\n')

"""
程序入口
"""
def merge_sort():
    global list1
    global list2
    global list3

    #先对数组进行排序
    select_sort(list1,len(list1)-1)
    select_sort(list2,len(list2)-1)

    print("第一个数组的排序结果：")
    for i in range(len(list1)-1):
        print(list1[i],'',end='')
    print('')
    print("第二个数组的排序结果：")
    for i in range(len(list2)-1):
        print(list2[i],'',end='')
    print('')

    print("===========================================")

    #两个数组合并排序
    Merge(list3,len(list1)-1,len(list2)-1)

    print("===========================================")

    print("\n合并排序的结果：")
    for i in range(len(list1)+len(list2)-2):
        print(list3[i],'',end='')
    print('\n')

if __name__ == '__main__':
    merge_sort()