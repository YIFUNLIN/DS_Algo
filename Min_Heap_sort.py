# Heap Sort - using min-Heap
def adjust(arr, i, n):  # 負責確保Heap都滿足Min-Heap性質
    child = 2 * i
    item = arr[i-1]  # 因為array從0開始算，所以要-1

    while child <= n:
        if child < n and arr[child-1] > arr[child]:  # 左右子點比大小。若右子點<左子點
            child += 1  # 改用右子點作為代表
        if item <= arr[child-1]:  # 若父點仍小於(左右子點之中的最小值)
            break  # 跳出迴圈

        # 若該子點的值比父點小，將該子點與父點交換
        arr[(child // 2) - 1] = arr[child-1]
        child *= 2  # 繼續往下一層走，直到沒有子點>父點
    arr[(child // 2) - 1] = item  # 離開while loop後，將原先父點的值插到該交換完的子點上
    print("調整過程:", arr)


def heapify(arr, n):  # 實現buttom-up定義
    for i in range((n // 2), 0, -1):  # 從最後一個父點，往回依序調整
        adjust(arr, i, len(arr))  # 調用adjust()使其符合Max-Heap定義


def heapSort(arr, n):
    heapify(arr, len(arr))  # 調用heapify()，將未排序好的arr轉成Max-heap

    for i in range(n, 1, -1):  # 再執行(n-1)回合的Delete-max
        arr[i-1], arr[0] = arr[0], arr[i-1]  # 每次都拿最後一個節點跟root交換，最大值被移到末端
        print("交換", arr)
        # 再調用adjust()確保滿足Max-heap，而利用i-1 確保只調整為排序的資料，跳過了剛剛拉到最後一個位置的max
        adjust(arr, 1, i-1)  # 再利用adjsut()，可產生由小到大排序結果

    return arr


arr = [5, 10, 2, 7, 1]
heapSort(arr, len(arr))
print("排序後", arr)
