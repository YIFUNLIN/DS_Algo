def countingSort(array):
    """ 初始化"""
    size = len(array)
    output = [0] * size  # Output大小是[1...n]
    count = [0] * 10  # 預設鍵值範圍為[0..9]

    """ 利用Count來累積次數和作為日後紀錄各元素end位置的索引"""
    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):  # 將count 拿來改作為紀錄之後output array 的end 位置
        count[i] += count[i-1]  # 利用前一人結束的位置+自己當前的count數 = 得出自己end位置

    """ 利用end位置 index，將資料放入到Output Array中"""
    i = size - 1  # 因為count 現在是用結束位置來紀錄資料，為了求有stable特定，資料要從最後一筆由右往左填入
    while i >= 0:  # 開始從原始陣列的末端遍歷每個元素
        # 將資料由右往左依序放入count中找出end位置，再依(該索引位置 - 1)填入output中，因為array是從0開始數，需要減去 1 來將這個值轉換成正確的array索引
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1  # 放完要扣1，將來有相同資料再放到他的前一格
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


data = [2, 5, 3, 0, 2, 3, 0, 3]
print("原始資料:", data)
countingSort(data)
print("排序後結果:", data)
