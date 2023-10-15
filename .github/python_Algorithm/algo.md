# Data Structure + Algo code
## Factorial N!
![](https://i.imgur.com/PFJjRr9.png)


- iterative(Non-recrusive) 
```
def Fac(i):
    if i == 0:
        return 1
    else:  
        s = 1                    #將遞迴公式一直往前推導，
                                 #發現需要設一個變數來儲存之前的值，推到最前面發現要設1
        for j in range(1,i+1):
            s = s * j      
        return s
```
- recrusive
寫遞迴時，要先去想他數學規則的定義
```
def Fac(i):
    if i == 0:
        return 1
    else:
        return i * Fac(i-1)
```
遞迴執行次數= N+1次

# **Fibonacci Number**
![](https://i.imgur.com/YNkcKCg.png)


- recrusive  => O( ((1+√5)/2)**n ) 
```
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
```
- iterative
```
#include<iostream>
using namespace std;
int Fib(int n){
    if (n == 0)
       return 0;
    else if (n == 1)
         return 1;
    else{
         int a = 0, b = 1,c;
         for(int i = 2; i <= n; i++){
                 c = a + b;
                 a = b;
                 b = c;
             }
             return c;     
         }
}
int main(){
    int num = 10;
    int result = Fib(num);
    cout<<result;
    system("pause");
    return 0;
}

```

### Fibonacci遞迴function calls 為: **Fib(n-1) + Fib(n-2) + 1次**

Ex.台大資工考題:
```
#include<iostream>
using namespace std;
#define MAX_N 5     //先定義想配置的數量 = 5 ，使程式碼更好維護 參數只要改一次就可 

int calls[MAX_N + 1] = {0};  //設全域變數，多配一個空間 因為要從0~5 會多1 

int Fib(int n)
{
	if(n <= MAX_N)   //只要在範圍內被呼叫到 
		calls[n]++;   //function call 就先+1 
		
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return Fib(n-1) + Fib(n-2);
	}
int main(){
	int total = 0;
	cout << "Fib(" << MAX_N << ") ="  << Fib(MAX_N) << endl;   //印出值 
	
	for(int i = 0; i <= MAX_N; i++){
		cout << "Fib(" << i << ") was called " << calls[i] << "times." << endl;   //印出每次呼叫的次數F(1)、F(2)、... 
		total += calls[i];
	}
	cout << "Total F(" << MAX_N << ") function calls = " << total << endl;    //印出所有呼叫次數總和 
	system("pause");	
	}
```
![](https://i.imgur.com/jVlCL10.png)

## Dynamic Programming
 =  Divide and  Conquer + Memorization組成
 
 是一種解決問題的策略，會將問題切分，並且依序解答，每次得到一小部分的答案就儲存起來，省去重複計算成本。
 
 [特點]

1. 通常使用數據結構（如array、list或dict）來儲存中間計算的結果，避免重複計算。

2. 通常是由小到大來解。從最小的子問題開始，逐步構建直到達到最終問題。 
然而，也可以使用自頂向下的方法，這通常稱為"記憶化搜索"或"記憶化遞迴"。
 
- Fibonacci Numbers using Dynamic Programming
```
#include<iostream>
using namespace std;
int DynamicFib(int n){
	int fib[n+2];
	fib[0] = 0;
	fib[1] = 1;
	for(int i = 2; i <= n; i++){
		fib[n] = fib[n-1] + fib[n-2];
		}
	return fib[n];
	}
int main(){
	int n;
	cout << "Enter number of terms: ";
	cin >> n;
	cout << n << "th Fibonacci terms: " << DynamicFib(n) << endl;
	system("pause");
	} 

```
Time Complexity = O(n)


# **Binomial Coefficient 二項式係數 **
Def: 
![](https://i.imgur.com/3tGuvLc.png)


- Recrusive
```
#include<iostream>
using namespace std;
int Bin(int n,int m){
    if(m == 0 || m == n)
         return 1;
    else
        return Bin(n - 1, m) + Bin(n - 1, m - 1); 
}
int main(){
    int n = 5, m = 3;
    int result = Bin(n,m);
    cout<<result;
    system("pause");
    return 0;
}
```

- Dynamic Programming for C(n,k)

Time complexity = O(n*k)


Auxiliary space = O(n*k)          #輔助空間

![](https://i.imgur.com/1fN0PNH.png)


(pyhton)版本
```
def bin(n,k):     #列、行
    C = [[0 for x in range(k+1)] for x in range(n+1)]    #設定儲存空間，k定義了行(元素的數量)，n定義了 列 

    for i in range(n+1):             #row
        for j in range(min(i,k)+1):  #column，用i目前所在位置與k的長度去比，不可能會大於i，看誰比較小就可以先停止此輪的迴圈
            if j == 0 or j == i:     
                C[i][j] =  1
            else:
                C[i][j] =  C[i-1][j-1] + C[i-1][j]
    return C[n][k]
```
    
(C++)
```
#include<iostream>
using namespace std;
int binomialCoeff(int n,int m){    //列、行 
    int C[n+1][m+1];               //定義一個額外空間
    for(int i = 0;i <= n;i++){     //探索每個"列"
		for(int j = 0; j <= min(i,m); j++){    //探索每個"行"
			if(j == 0 || j == i)          //行=0或跟列相等 則為1
				C[i][j] = 1;
			else
				C[i][j] = C[i-1][j] + C[i-1][j-1];
		}
	}
	return C[n][m];       //回傳結果
}
int main(){
    int n = 5, m = 4;
    cout<<binomialCoeff(n,m);
    system("pause");
    return 0;
}

```



# GCD(A,B) 最大公因數(Greatest Common Divisor)


<定義>

![](https://i.imgur.com/W2rqwep.png)


          
```
#include<iostream>
using namespace std;
int GCD(int a,int b){
	if(a % b == 0)
		return b;
	else
		return GCD(b,a%b);
	}

int main(){
    int a = 18, b = 32;
    cout<<GCD(a,b);
    system("pause");
    return 0;
}
```

# Ackerman Function : A(m,n)

![](https://i.imgur.com/JE0pcSt.png)
```
def A(m,n):
    if m == 0:   
        return n+1
    elif n == 0:
        return A(m-1,1)
    else:
        return A(m-1,A(m,n-1)) 
```
# - Exponential 指數
```
#include<iostream>
using namespace std;
int Exp(int x, int n){
	int f;
	if((n%2) == 0)  f = 1;
	else	f = x;
	if(n < 2)	return f;
	return f * Exp(x * x, n / 2);
	}

int main(){
    int a = 6, b = 3;
    cout<<Exp(a,b);
    system("pause");
    return 0;
}
```
# - Tower of Hanoi 河內塔
```
#include<iostream>
using namespace std;

void towerOfHanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        cout << "\n Move disk 1 from rod " << from << " to rod " << to;
        return;
    }
    towerOfHanoi(n-1, from, aux, to);
    cout << "\n Move disk " << n << " from rod "<< from << " to rod " << to;    //n代表盤子大小 1,2,3  從柱子? 到柱子? 
    towerOfHanoi(n-1, aux, to, from);
}

int main() {
    int a = 3;
    char b = 'A', c = 'C', d = 'B';
    towerOfHanoi(a, b, c, d);
    system("pause");
    return 0;
}

```
# - Permutations 排列組合
```
#include <iostream>
using namespace std;

void swap(char& a, char& b) {
    char temp = a;
    a = b;
    b = temp;
}
void perm(char *list, int i, int n) {
    if (i == n) {
        for (int j = 1; j <= n; j++)
            cout << list[j];
        cout << endl;
    } else {
        for (int j = i; j <= n; j++) {
            swap(list[i], list[j]);
            perm(list, i + 1, n);
            swap(list[i], list[j]);
        }
    }
}
int main() {
    int n = 3;
    char list[] = {' ', 'a', 'b', 'c'}; //前面放置一個空字串，因為j從1開始，list index 是從0開始，為了確保值都能印出來，放' '去佔第0位置好讓後面的值可以從位置1開始輸出
    perm(list, 1, n);
    system("pause");
    return 0;
}
```
# - Reverse 反轉
[法一]
```
#include <iostream>
using namespace std;
void reverse(char *str)
{
	if(*str)
	{
		reverse(str+1);
		cout<<*str;
	} 
}
int main() {
    char str[] = {'a', 'b', 'c','d','e','f','\0'};    //記得最後要添加空字符('\0')，才能正確判斷字串結束的位置 
    reverse(str);
    system("pause");
    return 0;
}
```
[法二]
```
#include <iostream>
using namespace std;
void swap(char& a, char& b)
{
	char temp = a;
	a = b;
	b = temp;
}
void reverse(char *A,int i,int j)
{
	if(i < j) {
		swap(A[i],A[j]);
		reverse(A,i+1, j-1);
	}
}
int main() {
	int i = 0,j = 4;
    char A[] = {' ','a', 'b', 'c','d','\0'};    //記得最後要添加空字符('\0')，才能正確判斷字串結束的位置 
    reverse(A,i,j);
    cout<<A<<endl;
    system("pause");
    return 0;
}
```
[法三] reverse 使用 recursive            

時間複雜度:O(n)
```
#include<iostream>
using namespace std;
void reverse(char *str)
{
	if(*str)     //str會從array[0] 開始走 
	{
		reverse(str + 1);  //str每次都會指向下一個字符 直到碰到'\0' 就會離開recrusive
		cout << *str; //在recrusive結束後 system才會開始回朔 去追之前有被recrusive呼叫到 但下面尚未被執行的程式碼片段 => 形成reverse
		}
}
int main(){
	char a[] = "hello";
	reverse(a);  
	system("pause");
	return 0;
	}
```
# Stack 製作 using array
```
#include <iostream>
using namespace std;
#define MAX 1000

class Stack {
private:
    int a[MAX];  // Maximum size of Stack
    int top;     //用來追蹤stack頂部位置 

public:
    Stack() { top = -1; }    //建構子  當一個 Stack 對象被創建時，這個建構子會被調用，並設置 top 為 -1。這意味著堆疊是空的

    bool push(int x) {   //將一個元素添加到堆疊頂部。
        if (top >= (MAX - 1)) {  //若stack已滿 （因是是從0開始數 所以  top 等於 MAX - 1 時 就代表滿了) 
            cout << "Stack Overflow";  //顯示 "Stack Overflow" 並返回 false 
            return false;
        }
        else {
            a[++top] = x;   //否則，將元素添加到堆疊頂部，並增加 top 的值。  先移動top到下一格 
            cout << x << " pushed into stack\n";
            return true;
        }
    }

    int pop() {
        if (top < 0) {
            cout << "Stack Underflow";
            return 0;
        }
        else {
            int x = a[top--];  //先取出該值 再移到上一格 
            return x;
        }
    }

    int peek() {  //返回堆疊頂部的元素
        if (top < 0) {
            cout << "Stack is Empty";
            return 0;
        }
        else {
            return a[top];
        }
    }

    bool isEmpty() {
        return (top < 0);
    }
};
int main() {
    Stack s;

    s.push(3);
    s.push(4);
    s.push(5);
    s.push(6);

    cout << "Top element is: " << s.peek() << endl;  // 預期輸出：6

    cout << "Elements popped from stack: ";
    while (!s.isEmpty()) {
        cout << s.pop() << " ";
    }
    cout << endl;  // 預期輸出：6 5 4 3
	system("pause");
    return 0;
}
```
# Check for balanced brackets(parentheses) 括號檢查    
(成大資管109)
![](https://hackmd.io/_uploads/SJ2ny0tah.png)

[法一] 難
```
#include<iostream>
#include<string>

using namespace std;

struct sNode {
    char data;
    struct sNode* next;
};

void push(struct sNode** top_ref, int new_data);
char pop(struct sNode** top_ref);

bool areBracketsBalanced(char exp[]);
bool isMatchingPair(char character1, char character2);

int main() {
    char exp[100];
    cout << "Enter an expression: ";
    cin >> exp;
    if (areBracketsBalanced(exp))
        cout << "Balanced \n";
    else
        cout << "Not Balanced \n";
    system("pause");
    return 0;
}

void push(struct sNode** top_ref, int new_data) {
    struct sNode* new_node = new sNode();

    if (new_node == NULL) {
        cout << "Stack overflow \n";
        exit(0);
    }

    new_node->data = new_data;
    new_node->next = (*top_ref);
    (*top_ref) = new_node;
}

char pop(struct sNode** top_ref) {
    char res;
    struct sNode* top;

    if (*top_ref == NULL) {
        cout << "Stack underflow \n";
        exit(0);
    } else {
        top = *top_ref;
        res = top->data;
        *top_ref = top->next;
        delete top;
        return res;
    }
}

bool areBracketsBalanced(char exp[]) {
    int i = 0;
    struct sNode* stack = NULL;
    while (exp[i]) {
        if (exp[i] == '{' || exp[i] == '(' || exp[i] == '[')
            push(&stack, exp[i]);
        if (exp[i] == '}' || exp[i] == ')' || exp[i] == ']') {
            if (stack == NULL) return false;
            else if (!isMatchingPair(pop(&stack), exp[i])) return false;
        }
        i++;
    }
    if (stack == NULL) return true; 
    else return false; 
}

bool isMatchingPair(char character1, char character2) {
    if (character1 == '(' && character2 == ')') return true;
    else if (character1 == '{' && character2 == '}') return true;
    else if (character1 == '[' && character2 == ']') return true;
    else return false;
}
```

[法二] 較好懂
```
#include<iostream>
#include<stack>   //裡面就包含了一些函數 push()、pop()、top()、empty()、size() 
using namespace std;
bool areParanthesisBalanced(string expr) {          //用來判斷括號是否達到平衡 
    stack<char> s;   //宣告用stack結構:s，來儲存char類型 
    char x;          //用於之後儲存要stack中最上面的符號 
    for (int i = 0; i < expr.length(); i++) {  //length 會從1開始算 而str 的index是從0 所以是會比length長度少 1 
        if (expr[i] == '(' || expr[i] == '[' || expr[i] == '{') {
            s.push(expr[i]);
            continue;    //直接跳到下一個for執行 
        }
        
        if(expr[i] == ')' || expr[i] == ']' || expr[i] =='}')
		{
        	if(s.empty())
        		return false;
		}

        switch (expr[i]) {
            case ')':
                x = s.top();
                s.pop();
                if (x != '(') return false;  //此時stack上方若非對應的左括弧 則有error 
                break;
            case '}':
                x = s.top();
                s.pop();
                if (x != '{') return false;
                break;
            case ']':
                x = s.top();
                s.pop();
                if (x != '[') return false;
                break;
        }
    }
    return (s.empty());
}

int main() {
    string expr;
    cout << "Enter the expression: ";
    cin >> expr;
    if (areParanthesisBalanced(expr))
        cout << "The expression is balanced." << endl;
    else
        cout << "The expression is not balanced." << endl;
	system("pause");
    return 0;
}



```
---
# 初等排序
|                | Best Case | Worst Case | Average Case | 空間複雜度 | 是否Stable |  特點   |
| -------------- | --------- | ---------- | ------------ | ---------- | ---------- | --- |
| Insertion Sort | O(n)      | O(n^2)     | O(n^2)       | O(1)       | 是         |資料量少就用它     |
| Selection Sort | O(n^2)    | O(n^2)     | O(n^2)       | O(1)       | 否         | 適合用於大型紀錄(有很多欄位構成的資料)的排序，因為每一回合頂多swap一次(因為swap成本很高)    |
| Bubble Sort    | O(n)      | O(n^2)     | O(n^2)       | O(1)       | 是         |     |
| Shell Sort (少考)    | O(n^3/2)  | O(n^2)     | O(n^2)       | O(1)       | 否       |     |





 ## Insertion Sort (插入排序)
 => 將第i筆資料插入到前(i-1)筆已排序好的串列中，則擁有i筆已排序完成的串列
```
#include<iostream>
using namespace std;

void insertionSort(int arr[],int n)
{
	int i,key,j;   //i:用來往後走、key:用來當作要被置換時的一個暫存空間、j:負責處理要排序的資料 
	for(i = 1;i < n; i++){  //array索引起始位置是從0，但故意從1開始  因為把第一筆也就是索引0視為已排好的第一筆 
		key = arr[i];   //暫時儲存i走到位置的值，為了之後可能要騰出空間用 
		j = i - 1;      //j每次都會退回去檢查已排序好最後一筆資料，當日後有位置挪動時，可達到檢查效果 
		
		while( j >= 0 && arr[j] > key)   //當已排序好的資料中的最後一筆仍比為排序中的一筆資料大時 
		{
			arr[j+1] = arr[j]; //將已排好的最後一筆放到未排序但比他小的位置 
			j = j - 1;       // j再後退，繼續檢查是否已排序好的資料中有無小於的 
		}                   // 持續再已排序好的資料中搜尋，直到沒有再跳出while loop 
		arr[j+1] = key;     //離開while迴圈條件是，在已排序好的資料中已無比她小的了，此時就將key插到第j+1的位置中 
	}
}
	
void printArray(int arr[],int n){
	for(int i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
	} 


int main(){
	int arr[] = {12,11,13,5,6};
	int N = sizeof(arr) / sizeof(arr[0]);
	
	insertionSort(arr,N);
	printArray(arr,N);
	
	system("pause");
	return 0;
	
	}

```

## Selection Sort (選擇排序)
=>從第i筆到第n筆，找出最小值，在與第i筆做swap，共(n-1)回合
```
#include<iostream>
using namespace std;

void selection_sort(int arr[],int n)
{
	for(int i = 0; i < (n-1); i++)  //最多從0~(n-2)回合，共(n-1)回合 
	{
		int min_idx = i;    //初值(最小值)先設在第 i 格 
		for(int j = i + 1; j < n; j++)  //從min的下一格開始找 直到(n-1)格 
		{
			if(arr[j] < arr[min_idx])   //若有人比min小 
				min_idx = j;    //將此值的索引給予min 
		}
		if(i!= min_idx)      //當跳出此內層loop後(代表已找到這回合的最小值) 
		{                            //做swap，將此min與i所在的值做交換 
			int temp = arr[min_idx];    
			arr[min_idx] = arr[i];
			arr[i] = temp;		
		} 
	}
}
int main(){
	int array[] = {18,8,6,2,5};
	int N = sizeof(array) / sizeof(array[0]);
	cout << "排序前: ";
	
	for(int i = 0;i < N; i++)
		cout << array[i] << " ";
	cout << endl; 
	selection_sort(array, N);
	cout << "排序後: ";
	
	for(int i = 0; i < N; i++)
		cout << array[i] << " ";
	cout << endl;
	system("pause");
	return 0;
		} 

```

## Bubble Sort (氣泡排序)
=>由左而右，兩兩紀錄依序互相比較，若前者>後者，則做swap。

[效果]:每一回合完，當時的最大值將會升到最高位置，最多作(n-1)回合即可完成sort

[結束條件]在某一回合中皆無swap發生，即可exit (代表sorting完成)
```
#include<iostream>
using namespace std;

void bubbleSort(int array[],int n)
{
	int i,j,flag;
	for(i = 0; i < n-1; i++)   //共作(n-1)回合 
	{
		flag = 0;    //若有一個回合皆無swap，代表已排序完成，可直接跳出迴圈 
		for(j = 0; j < n-i-1; j++)  // j 負責在內部跑的，分別做(n-2)、(n-3)、...回合，抓出規律後會小於(n-i-1) 
		{
			if(array[j] > array[j+1])   //若j走到的前者>後者 
			{                            //做swap 
				int temp = array[j];
				array[j] = array[j+1];
				array[j+1] = temp;		
				flag = 1;               //有swap，就把flag設為1 
			}
		}
		if(flag == 0)	                //都無swap時，才可跳出loop 
			break; 
	}
}

int main(){
	int array[] = {3,0,7,2,1};
	int n = sizeof(array) / sizeof(array[0]);
	cout << "原始陣列: "; 
	for(int i=0; i < n; i++)
		cout << array[i] << " ";
	cout << endl;
	
	cout << "Bubble sort排序後陣列: ";
	
	bubbleSort(array,n);
	
	for(int i = 0; i < n; i++)
		cout << array[i] << " ";
	cout << endl;
	system("pause");
	return 0;
		} 

```
# 高等排序 (我用Python寫)
|            | Best Case | Worst Case | Average Case | Space Complexity | 是否stable | 特點 |
| ---------- | --------- | ---------- | ------------ | ---------------- | ---------- | ---- |
| Quick Sort | O(n logn) | O(n^2)     | O(n logn)    | O(logn)~O(n)     | 否         |      |
| Merge Sort | O(n logn) | O(n logn)  | O(n logn)    | O(n)  |    是         |  Not Sorting in place(需額外空間儲存)   |

## Quick Sort(快速排序)
```
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


if __name__ == '__main__':
    arr = [6, 8, 3, 5, 7, 9, 7, 0, -5]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)  # 印出此修改完的array內容

```

## Merge Sort
```
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

        while i < len(left_arr) and j < len(right_arr):  #當i,j都還在index範圍內時
            if left_arr[i] < right_arr[j]:    #進行i,j索引位置的值比大小，小的人就加入到新的要用來排序的arr[]中
                arr[k] = left_arr[i]          
                i += 1                        #i再往前走一格
            else:                             #若是j比較小
                arr[k] = right_arr[j]        
                j += 1                        #j往前一格
            k += 1                            #不管怎樣，k都會往前一格

        # 當離開上面這個while時，代表已經有一邊的array走完
        # 設定兩個case: 只會執行一個 當一邊走完 則將剩下一邊的剩餘資料全加入新的array中

        #以下兩個情況，只會執行其中一者
        while i < len(left_arr):       #Case 1: while loop結束，但i仍小於left_array
            arr[k] = left_arr[i]       # 將i這邊剩下的都複製到新的arr中
            i += 1               
            k += 1

        while j < len(right_arr):      #Case 2: 若是j仍小於right_array
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 6, 8, 7, 9, 0, -3, -6]
merge_sort(arr_test)
print(arr_test)

```




