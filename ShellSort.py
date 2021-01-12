def  shellSort(numList):
    n = len(numList)
    if n == 0 or n == 1:
        return numList # 陣列只有0個或1個數值所以不用排序，直接return
    gap = n // 2  # 將數字總個數除以2
    while gap >= 1:
        for i in range(gap,n):
            # 把前gap個空出来，以便進行各组之間的插入排序(插入排序也是把第一個元素空出来，當成已經排好序的序列)
            tempindex = i
            while tempindex >= gap and numList[tempindex - gap] > numList[tempindex]:
                numList[i - gap], numList[tempindex] = numList[tempindex],numList[tempindex - gap]
                tempindex -= gap
                # 先把一個子序列中的元素排好序，某個子序列中的元素下標之間的個隔為gap
        gap = gap // 2 # 將數字總個數除以2
    return numList #
numlist = [4,5,7,8,6,1,2,3,4]
print(shellSort(numlist))