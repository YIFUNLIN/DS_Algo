def merge_sort(arr):
    if len(arr) > 1:
        # 做切割
        left_arr = arr[:len(arr) // 2]  # 切割完的左半部
        right_arr = arr[len(arr) // 2:]  # 切割完的右半部

        # 一直 recrusion 去做分割
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left_arr index
        j = 0  # right_arr index
        k = 0  # merged array index

        while i < len(left_arr) and j < len(right_arr):  # 當i,j都還在index範圍內時
            if left_arr[i] < right_arr[j]:  # 進行i,j索引位置的值比大小，小的人就加入到新的要用來排序的arr[]中
                arr[k] = left_arr[i]
                i += 1  # i再往前走一格
            else:  # 若是j比較小
                arr[k] = right_arr[j]
                j += 1  # j往前一格
            k += 1  # 不管怎樣，k都會往前一格

        # 當離開上面這個while時，代表已經有一邊的array走完
        # 設定兩個case: 只會執行一個 當一邊走完 則將剩下一邊的剩餘資料全加入新的array中

        # 以下兩個情況，只會執行其中一者
        while i < len(left_arr):  # Case 1: while loop結束，但i仍小於left_array
            arr[k] = left_arr[i]       # 將i這邊剩下的都複製到新的arr中
            i += 1
            k += 1

        while j < len(right_arr):  # Case 2: 若是j仍小於right_array
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 6, 8, 7, 9, 0, -3, -6]
merge_sort(arr_test)
print(arr_test)
