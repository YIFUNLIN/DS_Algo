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
|            | Best Case | Worst Case | Average Case | Space Complexity | 是否stable | 特點                                 |
| ---------- | --------- | ---------- | ------------ | ---------------- | ---------- | ------------------------------------ |
| Quick Sort | O(n logn) | O(n^2)     | O(n logn)    | O(logn)~O(n)     | 否         |                                      |
| Merge Sort | O(n logn) | O(n logn)  | O(n logn)    | O(n)             | 是         | Not Sorting in place(需額外空間儲存) |
| Heap Sort     |   O(n logn)  | O(n logn) | O(n logn)| O(1)   |否   |                                      |

## Quick Sort(快速排序)
![](https://hackmd.io/_uploads/Sk1uiXFbT.png)
![](https://hackmd.io/_uploads/HJk5j7tZp.png)
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
![](https://hackmd.io/_uploads/rkpss7t-T.png)

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

## Heap Sort
![](https://hackmd.io/_uploads/S1VOww9WT.png)

![](https://hackmd.io/_uploads/SkMqPPq-a.png)

![](https://hackmd.io/_uploads/S11k_P9-a.png)

## Max-Heap
```
# Heap Sort - using Max-Heap
def adjust(arr, i, n):  # 負責確保Heap都滿足Max-Heap性質
    child = 2 * i
    item = arr[i-1]

    while child <= n:
        if child < n and arr[child-1] < arr[child]:  # 左右子點比大小。若右子點>左子點
            child += 1  # 改用右子點作為代表
        if item >= arr[child-1]:  # 若父點仍大於(左右子點之中的最大值)
            break  # 跳出迴圈

        # 若該子點的值比父點大，將該子點與父點交換
        arr[(child // 2) - 1] = arr[child-1]
        child *= 2  # 繼續往下一層走，直到沒有子點<父點
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

```
## Min-Heap
```
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

```

# Linear-time Sorting method
若排序技巧不是採用Comparison-based技巧時，則有機會突破omega(n logn)之限制，來到O(n)
| Algo          | Best Case    | Worst Case | Average Case | Space Complexity | 是否stable | 特點                             |
| ------------- | --------- | ---------- | ------------ | ---------------- | ---------- | -------------------------------- |
| Radix Sort  | O(d*(n+r))         |    O(d*(n+r))        |  O(d*(n+r))            |   O(r*n)               |    是      |                                  |
| Counting Sort | O(n+k)    | O(n+k)     | O(n+k)       | O(n+k)           | 是         | 常拿來作為LSD Radix Sort的副程式 |

## LSD Radix Sort 基數排序 (又稱Bin Sort 或 Bucket Sort)
![](https://hackmd.io/_uploads/B1TqsdoWa.png)

### EX.
![](https://hackmd.io/_uploads/HJHhiuoZa.png)
![](https://hackmd.io/_uploads/BJshiOjW6.png)

---
#### Time-Complexity
每回合都要分配n筆資料，每回合還要合併r個buckets，共d個回合

=> O(d*(n+r))
![](https://hackmd.io/_uploads/SJ2d3Oj-p.png)

![](https://hackmd.io/_uploads/rJQt2djWp.png)
每個buckets都要配到與資料量一樣多的空間，避免當全部資料都落在同一個buckets空間不夠的最糟情況

配置O(n*r)

![](https://hackmd.io/_uploads/B1FYn_iZp.png)
![](https://hackmd.io/_uploads/Syy9huiWp.png =60%x)

因為遵守FIFO，所以是stable

![](https://hackmd.io/_uploads/rk6bCdi-T.png)
```
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
        count[index % 10] -= 1  # 更新 count 數組，因為該位置已被佔用
        # eg. count 數組為 [0, 2, 2, 2, 2, 2, 2, 4, 4, 4]，這裡 count[7] = 4 意味著有四個元素的個位數小於或等於7
        # 如果要放置一個元素，其個位數是7，我們會把它放在 output 數組的第四個位置（索引3，因為索引是從0開始的）。然後，我們需要減少 count[7] 的值，因為該位置已經被佔用了
        # 所以執行 count[7] -= 1 之後，count 數組變為 [0, 2, 2, 2, 2, 2, 2, 3, 4, 4]。這樣，下一個個位數是7的元素會被放在 output 數組的第三個位置（索引2）
        
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

```
## Counting Sort 計數排序
- [Data Structure版本]
![](https://hackmd.io/_uploads/SJOZf7ffa.png)

- [Algorithm版本]
![](https://hackmd.io/_uploads/rk8XMQfzp.png)


```
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
```


| Best Case | Worst Case | Average Case | Space Complexity | 是否stable | 特點    |
| --------- | ---------- | ------------ | ---------------- | ---------- | --- |
| O(n+k)    | O(n+k)     | O(n+k)       | O(n+k)           | 是         | 常拿來作為LSD Radix Sort的副程式 |

---
## Selection Problem
Q: 如何在n個 unsorted array中找出最小的資料?
A: 

[法一]: 

先在n個資料中花(n-1)次比較找出最小值，
再花(n-2)次比較找出第二小值，花(n-3)次找出第三小值...

比較次數 = (n-1) + (n-2) + (n-3) + .... +(n-i) 
        = O(n^2)
```
for k to i do
    在n-k+1 個data中找出minimum
```

[法二]:
先將資料排序(eg. Quick Sort、Heap Sort)，return[i]，即代表第[i]小 
花O(n logn)

[法三]:
利用Quick Sort的Partition 來實施，利用PK位置去判斷在第幾小
1. 目標i在PK左邊: 代表皆<PK，去左邊找第i小
2. 目標i在PK右邊: 代表皆>PK，去右邊找第(i-k)小


| Best Case | Average Case | Worst Case |
| -------- | -------- | -------- |
| O(n)   | O(n)  |O(n^2)   |



## Hashing
# 還沒讀!! 
---
# Graph 介紹:
https://hackmd.io/@Linnn/BJ7XI9yGa
# Graph Traversal
![](https://hackmd.io/_uploads/HJ52awzz6.png =90%x)
## DFS (Depth First Search,深度先搜尋)
![](https://hackmd.io/_uploads/SkXC3vGGp.png =90%x)

![](https://hackmd.io/_uploads/H1e9rPzGT.png =50%x)
>程式碼走訪完結果 = A B D E F C 
#### Stack實作DFS
```
def dfs(start_vertex, graph_dict):
    visited = set()   # 使用集合來保存已訪問的節點
    stack = [start_vertex]  # python的list可做為stack

    while stack:  # 當堆疊不為空時
        vertex = stack.pop()   # pop()掉最上面的node
        if vertex is not visited:  # 如果這個節點還未訪問
            print(vertex, end=" ")  # 印出來
            visited.add(vertex)     # 並標記加入到訪問過的set中
            stack.extend(graph_dict[vertex])  # 先對該node的鄰居全都丟入stack，後續會再處理
            # 利用list.extend()用於將一個list（或任何可迭代對象）的所有元素添加到另一個list的末端
            # 因為是while loop 再回去前面一一pop 檢視是否visited過了


# 測試 dfs_stack 函數
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs('A', graph_dict)
```
---
#### Recrusive 版 DFS
```
visited = set()  # 建立一個初始化集合
graph_dict = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs(vertex):  # vertex為目標走訪值
    global visited, graph_dict  # 當一個區域變數要修改全域變數的值時，要宣告為Global variable才能真正修改
    if vertex in visited:  # 如果當前節點已經被訪問過（即它已經在 visited 集合中）
        return visited    # 則回傳 visited 集合
    visited.add(vertex)   # 若當前節點尚未被訪問，則將其添加到 visited 集合中
    print(vertex, end=" ")   # 印出該點

    # 要去拜訪vertex的鄰居們，利用vertex去比對dict的key，當有找到時就回傳該列表
    for neighbor in graph_dict[vertex]:
        # neighbor會走訪該列表內的node
        if neighbor not in visited:  # 若該點未被拜訪過，則代表它不在visited集合內
            dfs(neighbor)            # 對它做 dfs 去拜訪他
    return visited


# 測試 dfs 函數
dfs('A')
```


## BFS (Breadth First Search, 廣度先搜尋)
![](https://hackmd.io/_uploads/r1ulpDfGT.png =90%x)

```
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


def BFS(start_vertex):
    visited = set()
    queue = [start_vertex]  # 利用list可實現Queue
    while queue:
        vertex = queue.pop(0)  # FIFO 利用pop(0)取出最前端元素
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(
                neighbor for neighbor in adjacency_list[vertex] if neighbor not in visited)

BFS('A')
```

## Spanning Tree (展開樹)
為連結Graph中所有node且不產生任何cycle的tree
![](https://hackmd.io/_uploads/SkYzUdfz6.png =70%x)

一. Def: 給予一個Connected 無向圖，G=(V:頂點數,E),令S=(V:頂點數,T:tree edge)為G的一個Spanning Tree，且S的頂點集合數要與Graph相同，則S滿足:
1. E = T  + B，T為Tree edge(拜訪時經過的邊)，B為Back edge(拜訪時沒經過的邊)
2. 若從B中任取一邊加入到S:Spanning Tree中，必定會形成unique cycle 
3. 在S中，任何頂點對之間，只存在一條unique simple path (除了起點與終點可能相同，其餘中間經過的點皆不同)

### [Note]:
1. G為connected <=> G必含Spanning Tree
2. 若G 是unconnected，則必無Spanning Tree
3. 連通的無向圖，Spanning Tree的數量 >= 1 (因為DFS、BFS的走訪不唯一，有多種走法)
4. 若Graph有 V個node，則Spanning Tree必有(V-1)條edges   (Tree的邊數會比node少1)
![](https://hackmd.io/_uploads/H1HXtOMGp.png =20%x)
6. G:連通無向圖的任一兩個Spanning Tree 不一定有共同邊
![](https://hackmd.io/_uploads/HyRyc_zzp.png)


## Min Spanning Tree (MST,最小成本展開樹)
一. Def: 給一個connected 無向圖，G=(V,E),邊上有cost值，則在G的所有Spanning Tree中，具有最小的邊成本總和者稱之。

![](https://hackmd.io/_uploads/rJ9OrOGG6.png =90%x)

### [Note]:
1. 若G有多個相同cost的邊，則MST可能>=1棵
2. 若G的各邊cost皆不同，則MST才唯一
- 實際應用: 
1. 電路布局成本最小化
2. 連結n個城市最小的交通建設成本
3. Router在進行Packet傳輸時所使用 eg. Spanning Tree Protocol (STP)

### [Algo]:
1. Kruskal's algo (以邊為主)
3. Prim's algo   (以點為主)
4. Sollin's algo (以樹邊為主)

以上皆採用 Greedy Strategy

---

#### Kruskal's algo
```
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):  # 定義Graph 該class的屬性
        self.V = vertices          # 有頂點
        self.graph = []            # 一個空列表，用於存儲圖形的所有邊和相對應的權重。

    def add_edge(self, u, v, w):   # u:起始頂點、v:結束頂點、w:權重
        # 將每條邊的資訊，插入到二維的Graph list中，Graph將會包含多個子列表
        self.graph.append([u, v, w])
        # eg. [[0, 1, 4], [1, 2, 2], [2, 3, 5]] 代表有3條邊，第一條是從頂點 0 到頂點 1，權重為 4 以此類推。

    # Search function
    def find(self, parent, i):  # 找出父點用，為了要實現Disjoint Set的前置作業，要判斷兩個node是否位於相同set
        if parent[i] == i:   # 若父點等於自己，就回傳自己
            return i
        return self.find(parent, parent[i])  # 父點不是自己，就recrusive 找出父點

    def apply_union(self, parent, rank, x, y):  # 會在兩個node確定是不同set後才被呼叫，做union
        # parent:是一個list，紀錄每個node的父node    rank: 該list表示每個頂點集合的深度或等級。  x 和 y: 這是我們要合併的兩個頂點
        xroot = self.find(parent, x)  # 找出兩個頂點 x 和 y 所屬set的root
        yroot = self.find(parent, y)

        # 比較兩個根的等級(高度)
        if rank[xroot] < rank[yroot]:  # 將level較小的set加到level較大的set上，以保持樹的高度盡可能小
            # 如果 x 的root 等級小於 y 的root 等級，就將 x 的root的父親設為 y 的root
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:   # 如果兩個集合的等級相同，任意一個作為新的root。
            parent[yroot] = xroot
            rank[xroot] += 1   # 相同高度tree相加，高度會多1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []  # 用來存MST的結果
        i, e = 0, 0  # 　i:索引、e:要添加到MST list的edge數量

        # Kruskal算法需要先考慮最小權重的邊，所以先依權重對所有邊進行排序。
        """
        1. self.graph: 這個屬性代表著一個二維列表，每個元素都是一個列表，代表一條邊。每條邊由三個元素組成: 起點(u), 終點(v), 和權重(w)。所以一個邊可以表示為 [u, v, w]。
        2. sorted() 函數: 這是Python的內建函數，用於對可迭代物件進行排序。
        3. key=lambda item: item[2]: 這部分指定了排序的條件。在這裡，我們需要根據每條邊的權重(w)進行排序，而權重是每條邊的第三個元素，所以我們使用索引2（因為Python的索引是從0開始的）。
        lambda是Python中的一個關鍵字，它允許我們定義一個小型無名的函數。在這裡，這個lambda函數將每條邊作為輸入（稱為item），並返回其權重作為輸出。"""
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # 用來實現判斷是否為Disjoint set 與 實現Union
        parent = []  # 紀錄每個node的父點
        rank = []    # 紀錄每個 set的等級

        for node in range(self.V):  # 遍歷圖中的每個頂點
            parent.append(node)     # 先將父點初始化，將每個node的父點視為其自己的集合
            rank.append(0)          # 儲存每個set的高度，都先初始化為0(從0開始上升)

        while e < self.V - 1:        # 在MST中，邊的數量總是 V-1（V 是node的數量），會持續到我們形成 V-1 條邊為止
            u, v, w = self.graph[i]  # 從weight小到大排序好的Graph list中，一一取出邊的資訊
            i = i + 1                # 每取出一條edge就 + 1

            # 加入此edge前，要先檢查是否兩個點在相同集合，利用find()去找他們的父節點，以此來判斷是否相同
            x = self.find(parent, u)   # 每個node都會有一個父點，透過find()可得到 u 的父點
            y = self.find(parent, v)   # 會得到 v 的父點

            # 看u,v 的父點x,y是否相同
            if x != y:                                 # 若是不同set，才可加到Spanning Tree中。 相同的話要放棄，不然會形成cycle
                e = e + 1                              # 累積邊數 + 1
                result.append([u, v, w])               # u,v 為不同set時，加到spanning Tree的邊集合result中
                self.apply_union(parent, rank, x, y)   # 並將u,v所屬的集合作union

        for u, v, weight in result:                    # 遍歷result中的所有edge，印出來
            print("%d - %d: %d" % (u, v, weight))

        return result

    # 非必要
    # Add this visualization method to your Graph class
    def visualize_mst(self, mst_edges):
        G = nx.Graph()
        for u, v, weight in self.graph:
            G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 6))

        # Draw all edges in light gray
        nx.draw_networkx_edges(G, pos, edge_color="gray")
        # Draw MST edges in blue
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges,
                               edge_color="blue", width=2)

        # Draw nodes
        nx.draw_networkx_nodes(G, pos)
        # Draw node labels
        nx.draw_networkx_labels(G, pos)
        # Draw edge weights
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title('MST using Kruskal Algorithm')
        plt.show()


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

# Call the visualization method after kruskal_algo()
mst_edges = g.kruskal_algo()
g.visualize_mst(mst_edges)
```
---
#### Prim's algo 



## Shortest Path Problem - 
### Dijkstar's algo

### Floyd-Warshall algo
### (看杰哥Dynamic Programming)
http://debussy.im.nuu.edu.tw/sjchen/Algorithms_final.html