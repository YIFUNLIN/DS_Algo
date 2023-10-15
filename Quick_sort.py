def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        # left 會往右走，直到找到>=pivot的值才會停下來
        while left <= right and arr[left] <= pivot:
            left += 1  # 沒有就繼續往右走
        # right 會往左走，直到找到<=pivot的值才會停下來
        while left <= right and arr[right] >= pivot:
            right -= 1
        if(left > right):  # 當左右交錯後，left來到right的左邊，代表找到可以結束了
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]  # 此交換操作會直接修改 arr 陣列在記憶體中的內容
    return right  # 第一次QuickSort切割完，都由right來決定位置


def QuickSort(arr, low, high):  # 負責recrusive用
    if low < high:
        pivot_index = partition(arr, low, high)
        QuickSort(arr, low, pivot_index - 1)
        QuickSort(arr, pivot_index+1, high)


if __name__ == '__main__':  # 寫這個的用意是避免日後此程式被其他程式import時，__main__這一段裡面被定義的東西被執行到
    arr = [6, 8, 3, 5, 7, 9, 7, 0, -5]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)  # 印出此修改完的array內容
else:  # 當想要給其他程式import 時使用，才寫在else這邊  (他們才會看到，才可以用)
    print("歡迎光臨，只有外來的才看的到歐")

print('hello')
