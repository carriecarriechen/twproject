#coding=utf-8

#import numpy 可以用这库重构一下！！！
#num_list = numpy.zeros((2,5))


#行 Row 列 Col
#活1 死0

#打印二维数组
def print2d(list2d):
    for i in range(len(list2d)):  #行数
        for j in range(len(list2d[0])):  #列数
            print(str(list2d[i][j])+"   ",end='')
        print('')
    print('')

#让用户创建二维数组,初始化棋盘
def putin2d():
    m=int(input('请输入棋盘长度：'))
    n=int(input('请输入棋盘宽度：'))
    list2d = [([0] * n) for i in range(m)]
    print2d(list2d)
    print('现在棋盘上所有细胞均死亡，请复活一些细胞吧~~~输入坐标即可，用空格隔开,用回车结束。')
    print('比如1-2 2-3 代表复活1行2列和2行3列的细胞')
    print('注：左上角第一个细胞为0-0，输入坐标值不能超过数组的最大下标')
    str=input('请输入要复活的细胞坐标：')   #这里可以考虑一些用户输入不合法的情况！！！
    list1=str.split()
    for i in list1:
        row,col=int(i.split('-')[0]),int(i.split('-')[1])
        list2d[row][col]=1
    print2d(list2d)
    return list2d


#计算棋盘每一代的情况
def next_status(list2d):
    for i in range(len(list2d)):  #行数
        for j in range(len(list2d[0])):  #列数
            # 周围有几个活细胞（这里其实已经加上了自己）
            count=0
            for m in range(max(0,i-1),min(i+2,len(list2d))):  #防止越界
                for n in range(max(0,j-1),min(j+2,len(list2d[0]))):
                    if list2d[m][n]==1:
                        count=count+1
            result=count-list2d[i][j]
            if result==3:
                list2d[i][j]=1
            elif result==2 and list2d[i][j]==1:
                list2d[i][j]=1
            else:
                list2d[i][j]=0
            #print2d(list2d)
    print('下一代：')
    print2d(list2d)
    return list2d

#迭代N代
def iteration(list2d,n):
    i = 1
    while n > 0:
        print('第 %d 代' % (i))
        newlist = next_status(list2d)
        n -= 1
        i += 1



if __name__ == '__main__':
    list2d = putin2d()
    n=int(input("请输入迭代到第几代："))
    iteration(list2d,n)
