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
| Merge Sort | O(n logn) | O(n logn)  | O(n logn)    | O(n)             | 是         | Not Sorting in place(需額外空間儲存)，用空間換來了stable的優點 |
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


# Graph 介紹:
https://hackmd.io/@Linnn/BJ7XI9yGa

![image](https://hackmd.io/_uploads/HyDNOojXT.png)



# Graph Traversal
![](https://hackmd.io/_uploads/HJ52awzz6.png =90%x)
## 1. DFS
## 2. BFS
- 以Algorithm版來看

|                   | DFS  | BFS  |
| ----------------- | ---- | ---- |
| 使用adjacent matrix |O(V^2) | O(V^2)|
| 使用adjacent list   |O(V+E) | O(V+E)|

```
# adjacent matrix  表示樣子
G = [[0, 9, 75, 0, 0], 
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
```

```
# adjacent list  表示樣子
graph_dict = {
    '1': ['2', '7'],
    '2': ['1', '4', '5', '6'],
    '3': ['4', '6'],
    '4': ['2', '3', '7'],
    '5': ['2'],
    '6': ['2', '3'],
    '7': ['1', '4'],
}
```
### Tree 的 edge 種類
>邊的分類(Edge classification)
>1. Tree edge : 若可以經由一條邊走訪到新的節點，則稱該邊為Tree edge
>2. Forward edge : 可以直接存取到子孫的邊
>3. Backward edge : 可以直接存取到祖父的邊
>4. Cross edge : 連接了兩棵子樹的邊

| 追蹤方式 | 有向圖 DFS | 無向圖 DFS | 有向圖 BFS    |  無向圖 BFS   |
| -------- | ---------- | --------- | --- | --- |
| 追蹤的edge種類    | Tree edge、Back edge、Foward edge、Cross edge       |Tree edge、Back edge       | Tree edge、Back edge、Cross edge    |Tree edge、Cross edge     |


---
## DFS (Depth First Search,深度先搜尋)
>DFS顧名思義，就是盡量的深入遍歷整張圖。找到一個節點v，遍歷所有v能夠到達的節點，一但v能夠到達的節點都已經被發現，則回朔到v的前驅節點，也就是v的父節點，接著以該節點作為出發的節點，繼續尋找能夠到達的節點，不斷重複這樣的過程，直到整張圖被遍歷
![](ht
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
        if vertex not in visited:  # 如果這個節點還未訪問
            print(vertex, end=" ")  # 印出來
            visited.add(vertex)     # 並標記加入到訪問過的set中
            stack.extend(graph_dict[vertex])  # 先對該node的鄰居全都丟入stack，後續會再處理
            # 利用list.extend()用於將一個list（或任何可迭代對象）的所有元素添加到另一個list的末端
            # 因為是while loop 再回去前面一一pop 檢視是否visited過了


# 測試 dfs_stack 函數
graph_dict = {
    '1': ['2', '7'],
    '2': ['1', '4', '5', '6'],
    '3': ['4', '6'],
    '4': ['2', '3', '7'],
    '5': ['2'],
    '6': ['2', '3'],
    '7': ['1', '4'],
}
dfs('2', graph_dict)

```
Time Complexity: O(V+E)

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
>BFS是用來遍歷一張圖的最簡單演算法，也是很多在圖論演算法的原型，許多演算法都是基於BFS，像是Prim最小生成樹，Dijkstra演算法等等。
>
>給定一張圖G(V,E)，和一個節點s，BFS可以走訪s能夠到達的所有節點v，並且能夠紀錄s到各個節點的最少邊數，也就是最短距離，同時會產生出一棵BST Tree。這個數會以s作為樹的根結點，並且包含s能夠到達的所有節點v。BST可以用在有向圖，也可以用在無向圖中。
> - BFS在undirected graph中,邊的種類只有tree 及 cross edge
>- 在一個unweighted,undirected graph(無加權無向圖)中,只有BFS 可以找到shortest path

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
Time Complexity:O(V+E)

## Spanning Tree (展開樹)
為連結Graph中所有node且不產生任何cycle的tree
![image.png](https://hackmd.io/_uploads/ryiYD1zmT.png)


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

### [性質]:
1. 若G有多個相同cost的邊，則MST可能>=1棵
2. 若G的各邊cost皆不同，則MST才唯一
3. Cycle Theory
>1. 任何Cycle中的最大成本e，必不會出現在MST中
>2. 任何Cycle中的最小成本e，不一定會出現在MST中
>
![](https://hackmd.io/_uploads/H1mUehdzp.png)


4. Cut Theory
>把Graph 頂點set分成兩個cut set，那這兩個set間的cross edge(跨越邊)的最小成本邊，一定要在所有MST中
![](https://hackmd.io/_uploads/rkr9enOfp.png)




- 實際應用: 
4. 電路布局成本最小化
5. 連結n個城市最小的交通建設成本
6. Router在進行Packet傳輸時所使用 eg. Spanning Tree Protocol (STP)

## 求 Min Spanning Tree 的 3個 Algo
### [Algo]:
1. Kruskal's algo (以邊為主)
3. Prim's algo   (以點為主)
4. Sollin's algo (以樹邊為主)

以上皆採用 Greedy Strategy


|  | Kruskal’s algo |Prim's algo|
| -------- | -------- | -------- |
| Time Complexity    | O(E logE) = O(E logV)     | O(E logV)    |

---

#### Kruskal's algo
>G = (V,E),|V| = n,|E| = e
>1. 從E中挑出(刪除) min cost edge(u,v)
>2. 判斷(u,v)加入spanning tree後,是否會形成cycle
>3. 若會,則放棄此edge,否則就加入到S的T(邊集合)中
>4. Repeat (1)~(3) 直到已排出(n-1)條邊或E為空
>5. 若 |T|:Spanning Tree的邊集合 < n-1,代表No Spanning Tree

>時間分析:
>最多做e回合,每回合主要做兩個工作:
>1. 從E 中 Delete-min cost edge(u,v)
    >>利用min heap保存各邊的cost值,則Delete-min cost 花 O(log e)
>2. 判斷(u,v)加入S中是否形成cycle
    >>利用Disjoint sets之Union(i,j)與Find(x)來運作:
    >>>先將各頂點皆視為獨立的disjoint set,並判斷有無形成cycle

### 判斷有無形成cycle 虛擬碼
```
if Find(u) != Find(v) then{   //若u,v屬於不同集合,就不會有cycle 
    add edge(u,v) to S   //加入edge u,v到spanning tree中
    Union(Find(u),Find(v)) //找出他們的root做union,變成同一個set
    }
    else discard edge(u,v) //若在相同集合,捨棄此邊
```




![](https://hackmd.io/_uploads/rkn6uC_fa.png)

Q: 若G有>|V|-1條edges,weight最大的edge,不會被加入到MST中
A: False
![S__21823490.jpg](https://hackmd.io/_uploads/B1DjOTSm6.jpg)

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
Time Complexity:O(E logE) = O(E logV)

https://www.programiz.com/dsa/kruskal-algorithm

---
#### Prim's algo (以點為主)
>假設 G=(V,E), V = {1,2,3,...n},令U = {1} //你想走訪的起點
>
>steps:
>1. 利用與此點相鄰的邊,選出一個最小成本的邊(u,v),其中頂點 u 屬於 U , 頂點v 屬於 V-U
>2. 並將此最小成本邊(u,v)加到spanning tree中
>3. 並將v從 V-U 此集合中移除並將入到U中
>4. 重複1~3 直到 U = V(原來頂點的集合) 或 V-U為空 為

![S__3072015.jpg](https://hackmd.io/_uploads/r1z22k8X6.jpg)

![S__3072017.jpg](https://hackmd.io/_uploads/HkGn3y8Xp.jpg)

![](https://hackmd.io/_uploads/SkctAtPGa.png)

![](https://hackmd.io/_uploads/rJr1HAuM6.png)

```
import networkx as nx
import matplotlib.pyplot as plt

# Initialize
INF = 9999999  # INF 代表一個非常大的數字，用於表示兩個節點之間無邊界的情況（即"無窮大"的距離）
V = 5  # number of vertices in graph

G = [[0, 9, 75, 0, 0],  # adjacency matrix to represent graph
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]  # 代表頂點是否已被選中
no_edge = 0  # 用來追蹤MST已選擇的邊數量，最多只會有(V-1)條邊

selected[0] = True  # 選擇第一個頂點，設為已拜訪
print("Edge : Weight\n")

# Create a graph from the adjacency matrix for the original graph
original_graph = nx.Graph()  # 畫圖用
for i in range(V):
    for j in range(i, V):
        if G[i][j]:
            original_graph.add_edge(i, j, weight=G[i][j])
# Create an empty graph

MST = nx.Graph()  # 畫圖用

while (no_edge < V - 1):  # 用迴圈去跑，直到 MST 中有 V-1 條邊
    minimum = INF  # 設置一個變量 minimum，它將保存當前已知的最小邊的權重
    x = 0  # 保存當前已知的最小邊的兩個頂點
    y = 0
    for i in range(V):  # 對於每個頂點 i
        if selected[i]:  # 如果它已經加入 MST (由 selected 陣列表示)，那麼我們會查看它的所有鄰居
            for j in range(V):  # 對於每個頂點 j
                # 如果它還沒有被加入到 MST，且頂點 i 和 j 之間存在一條邊 (即 G[i][j] 的值不為零)，我們將考慮這條邊
                if ((not selected[j]) and G[i][j]):   # not 0 會變成True
                    # not in selected and there is an edge
                    if minimum > G[i][j]:  # 如果當前邊的權重小於我們之前找到的最小邊，我們更新 minimum 並記錄這條邊的兩個頂點 x 和 y。
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))  # 印出找到的最小邊和它的權重

    # Add the found edge to MST
    MST.add_edge(x, y, weight=G[x][y])  # 畫圖用

    selected[y] = True  # 將頂點 y 加入到 MST (更新 selected 陣列)。
    no_edge += 1  # 增加 MST 中的邊數。
    # 迴圈會再次運行，直到 MST 中有V-1條邊。每次迭代都會加入一條新的邊，直到樹完成為止

# 以下非必要，畫圖用
# Draw the original graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = nx.spring_layout(original_graph)
nx.draw(original_graph, pos, with_labels=True)
labels = nx.get_edge_attributes(original_graph, 'weight')
nx.draw_networkx_edge_labels(original_graph, pos, edge_labels=labels)
plt.title("Original Graph")

# Draw the MST
plt.subplot(1, 2, 2)
pos = nx.spring_layout(MST)
nx.draw(MST, pos, with_labels=True)
labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels)
plt.title("Minimum Spanning Tree")

plt.show()
```
Time Complexity:O(E logV)

---

## 解題策略: Divide-and-Conquer v.s. Dynamic Programming

#### Divide-and-Conquer 
> 將一個大問題分解成幾個較小的子問題，採Top-down 方式(由繁入簡)，由上到下將問題一一拆分，變成許多小問題再利用Recrusive一一回推去解決
> ![](https://hackmd.io/_uploads/SyxjmPQ9Mp.png)

> [缺點]:
> 可能會有嚴重的"子問題重複計算"(Overlapping Subproblem)問題，若是發生，就必須改用Dynamic Programming
> 
#### Dynamic Programming
> 採用Bottom-up，會使用表格將子問題的計算結果儲存起來，之後若有需要此計算結果，再由此表格直接取出可避免需多重複計算(使用loop+表格)，以提高效率，再進一步以較小的問題解逐步建構出較大的問題解。
> 
> Programming:用表格儲存，以"空間換取時間"的意涵
> ![](https://hackmd.io/_uploads/HkMj_X9zT.png)

#### Divide-and-Conquer v.s. Dynamic Programming 兩者比較
![](https://hackmd.io/_uploads/Sy4kFmcMa.png)

#### Dynamic Programming v.s. Greedy Approach 兩者比較

![](https://hackmd.io/_uploads/S1Nt4E5MT.png)

![](https://hackmd.io/_uploads/SJhWLN9fp.png)



|  Algo   | 求MST algo: Kruskal’s algo (以邊為主)、Prim’s algo (以點為主)、Sollin’s algo (以樹邊為主) | Construct Huffman Coding | Construct an optimal BST | 0~1 knapack problem | 求Topology Sort          | DAG    |  Dijkstra   | Bellman-Ford     |  Floyd-Warshall   |
| ---- | ----------------------------------------------------------------------------------------- | ------------------------ | ------------------------ | ------------------- | ------------------------ | --- | --- | --- | --- |
| 策略 | 皆為 Greedy                                                                               | Greedy                   | DP                       | DP                  | DFS (Depth First Search) | 採Topology Sort  | Greedy |DP     | DP |


---

# Shortest Path Problem (最短路徑問題):
![](https://hackmd.io/_uploads/Bk8XYE9za.png)
### 1. Single pair shortest path = Single source to other destination 
### = 求單一頂點到其他頂點之最短路徑
1. DAG (有向無循環圖,Directed Acycle Graph algorithm)
    >採 Topology Sort
3. Dijkstra algorithm
    >採 Greedy Approach
5. Bellman-Ford algorithm
    >採 Dynamic Programming
### 2. All pair shortest path = All pairs of vertex
### = 求所有頂點之間的最短路徑
1. Floyd-Warshall algorithm
    >採 Dynamic Programming
#### 整理:
![](https://hackmd.io/_uploads/HkGkF49zT.png)

#### 四個Shortest Path 求解Algo比較表
![S__3072024.jpg](https://hackmd.io/_uploads/ryOjRt_m6.jpg)



### 1. DAG (有向無循環圖,Directed Acycle Graph)
>DAGs常用於表示具有順序依賴性的事物，例如課程的先修條件、工程的任務排程、數據處理的工作流等。
> 1. 拓撲排序是有向非循環圖(DAG)的節點的線性排序，使得對於圖中的每一條有向邊(u, v)，節點u都出現在節點v之前。
> 
> 2. 拓撲排序的一個常見算法是使用DFS。當DFS訪問一個節點並完成訪問其所有鄰居後，該節點被推入一個堆疊。因此，最後一個被訪問的節點是最先被推入堆疊的，這實際上給了我們一個拓撲排序
> 3. 最重要的一點：只有directed acyclic graph(DAG)的Topological Sort(拓撲排序)才有意義。

![](https://hackmd.io/_uploads/B1Zqvfczp.jpg)



![](https://hackmd.io/_uploads/rybvrZcGa.jpg)


```
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict  # 有包好的資料結構


class Graph:
    def __init__(self, vertices):  # 類別初始化
        self.adjacencyList = defaultdict(list)  # 相鄰列表，用於儲存邊
        self.vertices = vertices  # 　儲存圖的節點數
        self.visited = [False] * vertices  # 使用bool值=False，來記錄DFS所訪問過的node
        self.stack = []  # 儲存Topology Sort完的結果
        self.G = nx.DiGraph()  # 是 networkx 的有向圖物件，將用它來畫圖

    def createEdge(self, u, v):  # 目的是在圖中添加一條邊，從節點 u 指向節點 v
        # 將node v 添加到node u 的adjacent list中。代表圖中會存在一條從 u 到 v 的邊
        self.adjacencyList[u].append(v)
        self.G.add_edge(u, v)  # 　視覺化用，將邊(u, v)添加到 networkx 的圖中

    def dfs(self, v):   # 先定義DFS，等等要給Topology Sort使用
        self.visited[v] = True   # 將拜訪的該點先設為True

        for i in self.adjacencyList[v]:  # 遍歷該點v的所有相鄰節點
            if not self.visited[i]:  # 若有相鄰節點未被訪問
                self.dfs(i)  # Recrusive，訪問他!

        self.stack.insert(0, v)
        # 使用模仿stack 的行為，但透過insert(0, v)以確保最後完成DFS的節點在拓撲排序中的位置是正確的。如果使用 append，那麼在返回拓撲排序結果之前，我們還需要反轉這個列表
        # 使用 self.stack.insert(0, v)，會將節點 v 放在 "堆疊" 的最底部（也就是list的開頭）。隨著更多的節點完成DFS，它們會持續被放到這個 "堆疊" 的最底部。
        # 所以，最後當DFS完成，self.stack 的第一個元素（也就是最底部）是最後一個完成DFS的節點，而最後一個元素（也就是最頂部）是第一個完成DFS的節點。
        # 這是拓撲排序的核心步驟，因為最依賴於所有其他節點的節點，應該先被處理。所以把它插入到list前端

    def topologicalSort(self):
        for i in range(self.vertices):  # 遍歷Graph中所有點
            if not self.visited[i]:  # 檢查節點 i 是否已被訪問
                self.dfs(i)          # 如果還沒有，則執行 DFS
        return self.stack            # 返回結果堆疊，這是拓撲排序的結果。

    def drawGraph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color="skyblue",
                font_size=15, font_weight='bold', width=2.0, edge_color="gray")
        plt.title("Directed Acyclic Graph (DAG)")
        plt.show()

# 測試
G = Graph(6)
G.createEdge(0, 1)
G.createEdge(0, 2)
G.createEdge(1, 3)
G.createEdge(1, 5)
G.createEdge(2, 3)
G.createEdge(2, 5)
G.createEdge(3, 4)
G.createEdge(5, 4)
print("Topological Sort Order:", G.topologicalSort())
G.drawGraph()
```
[解釋]
1. `__init__` 初始化方法中，你定義了存儲圖的資料結構，包括一個相鄰列表 (adjacency list)、訪問標記 (visited)、存儲拓撲排序結果的堆疊 (stack) 和 networkx 的有向圖物件 (用於視覺化)。

2. `createEdge` 方法允許你在圖中添加一條有向邊。

3. `dfs` 方法是深度優先搜索的實現，當訪問一個節點時，將其標記為已訪問並遞迴訪問其所有未被訪問的相鄰節點。當所有相鄰節點都被訪問後，當前節點被添加到拓撲排序的結果堆疊的前面。

4. `topologicalSort` 方法首先檢查每個節點是否已被訪問。如果還沒有，則從該節點開始進行DFS。最後，返回的拓撲排序結果就是堆疊的內容。

5. `drawGraph` 方法使用 networkx 和 matplotlib 來視覺化有向圖。

---



### 2. Dijkstra algo
[計算題算法]
>1. S[u]代表已走訪過的點
>2. Vertex select 代表該次挑選的點(每次都挑每列的最小成本點當作下一次拜訪的對象)
>3. 在matrix中的最後一列，即代表從起點到各頂點之間的最短距離
>EX. 
>![image](https://hackmd.io/_uploads/SyHPPIjX6.png)

[目標]:找到從某起始點到目標頂點的最短路徑

[做法]:
1. 利用三個Data Structure來輔助:

    a.Cost matrix (n*n 成本矩陣)
    >存放各點到各邊的所有成本值，它是固定的
    
    b. 一維陣列:S[1...n] of Boolean 
    >用來記錄頂點是否已經走過，若為1代表True，表示他們的最短路徑已經確定，不再更改
    
    c. 一維陣列:DIST[1...n] of Integer
    >此array會存從目前起點~頂點Vi的最短路徑長度。
    >
    >會動態調整，每回合都會往下一個頂點移動，直到最後一個點，此array內容即為最終需要的結果
    
    ![](https://hackmd.io/_uploads/BJQYMlYfT.png)
2. 初始化:
    1. 將一維陣列:S[]全設為0
    2. 將一維陣列:Dist[]先設為與二維陣列的成本矩陣Cost的第1列的所有值相同
    3. 再將第一個走訪的點v(也就是起點他自己)的S[v]設為1，代表已經走過
    4. 再將它的DIST[v]設為0，因自己到自己的距離為0
3. 利用 loop 開始找尋Shortest Path，共跑(n-2)回合
    >因為扣除起點與終點不用搜尋，所以只需跑(n-2)回合，所以將num=2，再用(num < n)，代表從2~(n-1)，共跑(n-2)次
4. 選擇程序:
    1. 從那些S[V] = False的點中，找出min DIST值的點，令他為u
    2. 將S[u]設為True，表示起點到u的Shortest Path Length已確定，且假設每邊皆為正邊
![](https://hackmd.io/_uploads/BkNTMeKGa.png)

    3. 針對u的每一個相鄰頂點v且s[v]=False去比較距離長度。
    >實現Greedy精神: 既然經過u會最短，那先經過u再到達其他點是否也會最短 ? 有就更新，沒有就不改變
    
        
        if DIST[v] > DIST[u]+Cost[u,v]

        then DIST[v] = DIST[u]+Cost[u,v]

    ![](https://hackmd.io/_uploads/HyV3fxFMa.png =70%x)      
4. 重複做(n-2)回合即可得到最終的DIST[]       
        
---
#### 範例
![](https://hackmd.io/_uploads/B1-imlYfa.png)

![](https://hackmd.io/_uploads/Hy_iXxKGa.png)

### Pseudocode

![](https://hackmd.io/_uploads/SJ1_GlYzT.jpg)

### Algo - Pseudocode
![](https://hackmd.io/_uploads/SJJrqxqzT.jpg)


---

```
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    # Initialization

    # dist[]:此array用來存起點i到目標的最短路徑長，並將所有頂點的距離初始化為無窮大
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # 自己到自己，距離為0

    # 用來存父節點，初始值皆設為 None
    previous_vertices = {vertex: None for vertex in graph}

    # 用來存尚未訪問的頂點，之後若有訪問過，就會把該點移除
    unvisited_vertices = list(graph.keys())

    while unvisited_vertices:  # 只要還有未訪問的頂點，就繼續循環
        # Find the vertex with the smallest distance
        current_vertex = min(
            unvisited_vertices, key=lambda vertex: distances[vertex]
        )
        """
        傳遞了 unvisited_vertices 的('A', 'B', 'C'...)到min中，而每一個 vertex 在 lambda 函數中都是從 
        unvisited_vertices 裡面得出的，並用來在 distances 字典中查找相對應的距離值，再選出最小值。
        """

        # 如果當前頂點的距離是無窮大，則表示剩下的頂點都不可達，所以跳出循環
        if distances[current_vertex] == float('infinity'):
            break

        # 遍歷當前頂點的所有相鄰頂點和它們之間的邊的權重
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight  # 計算從起始頂點到相鄰頂點的新距離

            # If found shorter path, update the distances and previous vertices
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 將當前頂點設為相鄰頂點在最短路徑中的前一個頂點
                previous_vertices[neighbor] = current_vertex

        # Mark the current vertex as visited，# 將當前頂點從未訪問的頂點列表中移除
        unvisited_vertices.remove(current_vertex)

    return distances, previous_vertices


# Test the function
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5},
    'F': {'C': 3}
}

distances, previous_vertices = dijkstra(graph, 'A')
print(distances)  # {'A': 0, 'B': 1, 'C': 4, 'D': 3, 'E': 6, 'F': 7}

# 畫圖用
G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue")
plt.show()
```

### Bellman-Ford algorithm 
> 1. 解single source to other destionations 最短路徑問題，Graph允許有負邊，但不可有negative cycle edge
> 2. 利用Dynamic Programming 求解
> 3. 有V個頂點，最多經過V-1個邊
> 
> [計算題求法]
> 
> 1.利用Matrix與k(經過edge數量)形成的表格來計算
> 
> 2. 利用k:代表從起點出發到各點經過的邊數(k)範圍內，去求出最小成本值
> 2. ![image](https://hackmd.io/_uploads/H1RtHIoQp.png)



> 




![](https://hackmd.io/_uploads/SJHkxDqMT.jpg)

#### Algo:

(Algo方式-走法)EX. 
![](https://hackmd.io/_uploads/HkrJgvqGp.jpg)

![](https://hackmd.io/_uploads/S1BygDqz6.jpg)

![](https://hackmd.io/_uploads/H1SJxPqMa.jpg)


![](https://hackmd.io/_uploads/rkBJlP9f6.jpg)

>Relax():
檢查從來源點到點v的目前已知最短路徑是否可以通過先到達點u然後通過邊(u,v)到達v來更短。如果可以，演算法會更新到達點v的最短路徑的長度
>
>Detect negative cycle的步驟如下： 
對每條邊(u,v)檢查是否有較短的路徑到達v，也就是看是否有dist[u] + weight(u,v) < dist[v]的情況。如果有，那麼就表示存在一個負權重循環，因為在最短路徑已經計算完成之後仍然可以找到更短的路徑。
>
>Algo步驟如下： 
>1. 初始化：將所有頂點的距離值設為無窮大，除了源點的距離值設為0，因為從源點到自己的距離當然是0。
>2. Relax步驟：對圖中的所有邊進行V-1次relax()，其中V是頂點。每次relax()都會遍歷圖中的所有邊，並嘗試更新頂點的最短路徑估計值。 
>3. detect negative cycle：在執行了V-1次relax()後，理論上所有頂點的最短路徑已經找到。如果圖中沒有negative cycle，那麼再執行一次relax()應該不會再改變任何頂點的最短路徑估計值。但是，如果還能繼續relax()出較短的路徑，那麼就表示存在一條總權重為負的循環。

---
### Bellman-Ford detect negative cycle

> 執行(v-1)次 應該得到所有頂點的shortest path ,若有negative cycle 的話,則執行第V次的cost會 < 前(v-1)次


Python code:

https://www.programiz.com/dsa/bellman-ford-algorithm

---

### Floyd-Warshall Algorithm = Floyd's Algorithm for shortest paths
> 也採用Dynamic Programming，用來求All pairs of vertex的Shotest Path Length
> 假設G=(V,E)，|V| = n , V = {1,2,3,...n}

[定義]
>1. A^k:是一個n*n 矩陣，其中A^k[i,j] = i到j的最短路徑長，且途中經過的節點編號數值要<=k
>

[計算題直接算]
> 用多個矩陣，利用DP特性，每個矩陣都會從前一個矩陣的資訊中取值，A^k : n*n矩陣，k從0~n，k有限制
> A^0: 為Cost matrix (單純紀錄圖上點對點之間的權重)
> 
> A^1: k=1，代表經過節點編號必須<=1，且第一列第一行照抄即可，其餘才要算
> 
> A^2: k=2 代表經過節點編號必須<=2，且第二列第二行照抄即可，其餘才要算
> 
> A^3: k=3 代表經過節點編號必須<=3，且第三列第三行照抄即可，其餘才要算
> 
> 以此類推 ... 最後算到k=n(節點總數)即為最終結果

![image](https://hackmd.io/_uploads/rJganci7p.png)



---
[詳細解釋版]
![](https://hackmd.io/_uploads/SykCGO9G6.jpg)

![](https://hackmd.io/_uploads/B1yCGd9GT.jpg)

EX.

![](https://hackmd.io/_uploads/SykRfO5M6.jpg)

![](https://hackmd.io/_uploads/HyyAzd9f6.jpg)

### 分析

![](https://hackmd.io/_uploads/Hyy0M_5Ga.jpg)

![](https://hackmd.io/_uploads/ByJAGu9Gp.jpg)

### Algo

![](https://hackmd.io/_uploads/S1xlUOcG6.jpg)

##### Python: 

https://www.programiz.com/dsa/floyd-warshall-algorithm

### A* ,  A^+ 矩陣
>A* 算法是一個非常知名的圖搜索算法，特別用於路徑規劃和遊戲開發中的移動物件尋找路徑。它結合了最好的Dijkstra算法（確保找到一個最短路徑）和貪婪搜索（確保有快速的搜索速度）的特性。
>>
>A*算法的實用性：
>
>遊戲開發：在遊戲中，當一個角色需要找到它和目標之間的路徑時，通常使用A*算法。
地圖應用：路徑規劃，例如找到兩個城市之間的最短路徑。
機器人規劃：例如，當機器人需要在物理空間中導航到某個點時。

![](https://hackmd.io/_uploads/rkzFF_qG6.jpg)

![](https://hackmd.io/_uploads/HyMFFu5M6.jpg)

![](https://hackmd.io/_uploads/SJzttu5GT.jpg)

# Hashing
>是一種Data儲存與搜尋(擷取)的機制，想存入或取出Data X之前，需先經過Hashing function求算出Hashing address(bucket位置)，再去Hash Table 中找到對應的bucket位置，存入或取出Data X

![](https://hackmd.io/_uploads/BybAe23GT.png)

- Hashing Table
>是由B個Buckets(桶)組成，每個bucket再由S個slots(槽)組成，每個slot可存一筆Data
![](https://hackmd.io/_uploads/Sy5sz22Ga.png)

[相關術語]

1. Collision (碰撞)
> 不同的Data，經由Hashing function 計算後，得出相同的Hashing address

2. Overflow(溢位)
>當Collision 發生且對應的Bucket中無多餘的空間可存Data時

>Note:
>1. 有Collision 不一定有overflow，可能slot夠多可以存
>2. 發生overflow一定有collision
>3. 若每個bucket只有1個slot，則collision = overflow

### 常見的Hash function Design方法
1. Middle square (平方值取中間位數)
2. Division (or Mod) (取餘數)
3. Folding Additions (摺疊相加)
4. Digits Analysis (位數值分析)

#### 1. Middle square (平方值取中間位數)
![](https://hackmd.io/_uploads/HJfMHnnGp.jpg)

#### 2. Division (or Mod) (取餘數)
>最好是mod 質數，但不要mod 2(因為很容易發生collision)
![](https://hackmd.io/_uploads/B1izH2hz6.jpg)

#### 3. Folding Additions (摺疊相加)
![](https://hackmd.io/_uploads/rJ-7B22GT.jpg)

#### 4. Digits Analysis (位數值分析)
![](https://hackmd.io/_uploads/SJsgS3hfT.jpg)

### Overflow 時的處理方法
1. Linear Probing 線性探測
2. Quadratic Probing 二次方探測
3. Double Hashing 雙重雜湊
4. Chain (又稱Link list)
5. rehashing (冷門)

### 1. Linear Probing 線性探測
>又稱Linear open addressing mode
>此方式將散置的空間視為環狀使用，當發生overflow時，則用Linear方式從下一個位置繼續探測，若有空位則將Data填入。
>
>若Search一個循環後，未能找到空餘的儲存區，代表位置皆被填滿了
>f
>![](https://hackmd.io/_uploads/ryJUba3zT.jpg)
![](https://hackmd.io/_uploads/S14UZT2M6.jpg)

>[優點]:
>
>1.簡單、易於實施
>
>2.保證空間能充分利用
>
>[缺點]:
>
>1. 易發生"Primary clustering"(資料群聚)問題
>>即相同Hashing address的Data易儲存於鄰近附近的bucket，會增加searching/deleting/insert 的時間

改善方法:Quadratic Probing 二次方探測


--------

### 2. Quadratic Probing 二次方探測
>當H(X)發生overflow時，則探測 (H(X)+-i**2)%B, B為Bucket數量,而i=1,2,3...,(B-1)/2 依序代入直到有空的bucket可存或探測格皆滿(不代表表格全滿)，無法存入為止
 ![](https://hackmd.io/_uploads/S175Bp3G6.jpg =60%x)
 
EX.  

![](https://hackmd.io/_uploads/Hyhora3fa.jpg) 

![](https://hackmd.io/_uploads/Bk3jra3Ga.jpg)

>[優點]:
>1. 解決Primary Clusting
>[缺點]:
>1. 不保證table空間可充分利用 (因為是用跳的去放Data)
>2. 易發生 "Secondary Clusting(次要群聚)"
>> 即相同Hashing address的Data 其overflow 之探測位置皆相同，具規律性，也會增加searching - time
> 
>[政大資科]: Q: Secondary clusing原因?
>> Ans: The sequence of step length is always the same. 探測方式皆相同
---

### 3. Double Hashing 雙重雜湊
![](https://hackmd.io/_uploads/H11Pn62f6.jpg)

![](https://hackmd.io/_uploads/B1kv26nzp.jpg)

![](https://hackmd.io/_uploads/SJyP2anMa.jpg)

>[優點]:
>
> 解決Secondary Clusting => 也就沒有Primary Clusting
> 
>[缺點]:
>
>不保證table 空間能充分利用


### 4. Chain (又稱Link list)
>具有相同的Hashing address的Data皆放在同一個bucket中，彼此用Link list方式串連，屬於Close addressing mode(封閉型)
>
>其餘皆為open addressing (開放型)
![](https://hackmd.io/_uploads/SkFHCTnG6.jpg)

![](https://hackmd.io/_uploads/BJ-IAT2fT.jpg)

![](https://hackmd.io/_uploads/rJHdxRnfT.jpg)

### 5. rehashing
> 提供一系列的Hashing function: H1,H2,H3,..Hm，
> 若使用H1發生overflow，則改用H2
> 使用H2發生overflow，則改用H3  以此類推，
> 直到有bucket可存或Hashing function 全部用完，無法存入為止


---
[Hashing 考古題]
![](https://hackmd.io/_uploads/ryz7sR3Gp.jpg)

![](https://hackmd.io/_uploads/H1PmjA3zp.jpg)

![](https://hackmd.io/_uploads/Hk6osRnfa.jpg)


#### Q: Every deterministic algorithm have a correspondent non-deterministic version algorithm

#### A: True
>對於每一個確定性算法（deterministic algorithm），都有一個相對應的非確定性版本（non-deterministic algorithm）。
> - 確定性算法（Deterministic algorithm）:在給定一個特定輸入時，其行為（包括操作和結果）是完全預測的算法。這類算法在每次執行時都會產生相同的輸出結果。
> - 非確定性算法（Non-deterministic algorithm）:在相同輸入下可能會產生不同的行為或結果。非確定性不是說算法本身隨機或不可預測，而是在執行過程中可能會有多個可能的選擇點，在這些選擇點上，算法可以“同時”探索所有可能的選擇。
> 
>從理論上講，每個確定性算法都可以轉化為一個非確定性算法，只要你允許非確定性算法在每步都做出“正確的”選擇。非確定性算法模型通常被用來描述一些複雜類別，例如非確定性多項式時間（NP）。任何確定性算法都可以看作是一種特殊情況的非確定性算法，其中不存在多個選擇，或者說，非確定性算法在每個決策點上只有一條路徑可走。
>然而，在實際應用中，確定性算法通常是首選，因為它們可以實際實現和預測。而非確定性算法更多地用於理論探索和證明某些問題的可解性。在實際實施時，非確定性算法通常透過隨機化（比如Monte Carlo方法）或搜索算法（如回溯搜索）來近似。



----------------
---
## 出題方向統計

![](https://hackmd.io/_uploads/B1QGJnvfp.png)


![](https://hackmd.io/_uploads/rJXWk2wf6.png)





### 112 政大資管-科技組
Dynamic Programming

LCS

AVL Tree sorting、Splay Binary Tree 排序結果

AVL Tree sorting algo

Hashing 
collision 用 linear probing
collision 用 double hashing
Tree Traversal 

### 111 政大資管-科技組
Heap Sort
BST-sort
Merge-sort
Quick-sort


### 112 成大資管-管理組
0、1背包問題
Big-O 過程推演、解釋