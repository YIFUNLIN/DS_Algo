# radixSort會根據最大值的位數，依次對輸入數組 arr 的每個位數從低到高進行排序(個位、十位、百位...)
# 在每個數位上，都會調用 countingSort 函數來進行實際的排序操作

def radixSort(arr):
    max1 = max(arr)  # 挑選資料中的最大值

    # 初始化一個變量 exp = 1 ，用於識別要排序的當前位數
    # 例如，當 exp 為1時，代表在個位數；exp 為10時，在十位數
    exp = 1

    # while 迴圈將持續執行，直到 exp 超過 max1 的最大數位。這樣確保了對數組的每個位數都進行了排序
    while max1 / exp >= 1:  # 確保不會超出自身所在的位數    如 936 / 1000 = 0.936 則不會執行
        countingSort(arr, exp)  # 對 arr 中的特定位數依序進行排序。 exp 代表當前排序的位數是多少
        exp *= 10  # 每次乘10，可在每次迴圈中移動到下一個位數。eg.從個位數->十位數->百位數->....等等


def countingSort(arr, exp1):  # 根據特定的位數來對array進行排序
    n = len(arr)

    # initialize
    output = [0] * (n)  # 長度為 n 的輸出array，全初始化為0，將用來存儲排序後的資料
    # 作為 buckets，建一個長度為10 (十進制0~9) 且初始化後的array，用來記錄（0-9)的bucket對應值的出現次數
    count = [0] * (10)

    # 初期count: 只記錄了每個數字在當前處理的位數上出現的次數
    # eg. [0,1,2,1,2,2]，初始 count = [1,2,3,0,0,0,0,0,0,0] 0出現1次、1出現2次、2出現3次
    for i in range(0, n):  # 遍歷每筆資料
        index = arr[i] // exp1  # 使用 exp1 來確定每個元素當前數位的值
        count[index % 10] += 1  # %10 確保值或落在對應的(0~9)buckets，表示各個bucket中0~9的出現次數

    # 以下為更新後的count:要得到累積後次數的效果，每個元素儲存的是小於或等於當前值的元素出現數量 (後面要找值該放在哪會很快)
    # 更新後的 count 數組會變成 count = [1,3,6,6,6,6,6,6,6,6]。這樣，我們就能知道小於或等於每個數字的元素有多少
    # count中的 3 代表 <= 2 的值有3個
    for i in range(1, 10):
        # 配合array index 從0~9，實現累加的樣子  0的值給1、1的值給2、以此類推~~
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1       # 因為array從0~(n-1)而已
    while i >= 0:   # while 迴圈是從輸入數組的末尾開始，用 count 數組來確定每個數字在輸出數組的位置
        index = arr[i] // exp1  # 計算當前位數的值  可能在個位or十位or百位....

        # 利用先前更新過的累加count，來找出資料要正確插入的位置
        # 例如 count[7] = 5代表 <= 7的數字在此位數上總共出現了5次，所以我們就會把該值插入到index 4的位置 （array 從0開始數）
        # (index % 10) 是為了能落在buckets範圍內(0~9)，而 -1是因為 array從0開始
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1  # 更新 count array累加值，因為該位置已被佔用
        # eg. count 數組為 [0, 2, 2, 2, 2, 2, 2, 4, 4, 4]，這裡 count[7] = 4 意味著有四個元素的個位數小於或等於7
        # 如果要放置一個元素，其個位數是7，我們會把它放在 output 數組的第四個位置（索引3，因為索引是從0開始的）。然後，我們需要減少 count[7] 的值，因為該位置已經被佔用了
        # 所以執行 count[7] -= 1 之後，count 數組變為 [0, 2, 2, 2, 2, 2, 2, 3, 4, 4]。這樣，下一個個位數是7的元素會被放在 output 數組的第三個位置（索引2）
        # 但它後面其他值保持不變。這是因為我們只使用了一個位數值剛好（或更小）的“位置

        i -= 1  # 向前移動到輸入數組的下一個元素

    # 將排好的array複製回原array
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
