# **Factorial N!**
![](https://i.imgur.com/MwpsYeW.png)

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
![](https://i.imgur.com/cujoRiY.png)

- iterative
```
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
```
- recrusive
```
def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a = b               #注意!!要先把b給a才行
            b = c
        return c
```

### Fibonacci遞迴function calls 為: **Fib(n-1) + Fib(n-2) + 1次**

(看不太懂程式)
Ex.台大資工考題:
```
#include<stdio.h>
#define N 10

int count[N+1];
int fab(int n){
	count[n]++;
	if(n==0 || n==1)
		return 1;
	else
		return (fab(n-1) + fab(n-2));
} 
int main(){
	int i;
	for (i=0;i<=N;i++)      #先叫出次數 
		count[i] = 0;
	fab(N);
	
	for(i=0;i<=N;i++)
		printf("count[%d] = %d\n",i,count[i]);
}
```
![](https://i.imgur.com/jVlCL10.png)

- Dynamic Programming
 =  Divide and  Conquer + Memorization組成
 將問題切分，並且依序解答，每次得到一小部分的答案就儲存起來
 ，省去遇到同樣問題又重複運算的時間成本
 
- 用DP來解Fibonacci number
```
def Fib(n):
    f = [0,1]       #資料儲存在list中
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2] )
    return f[n]
```
Time Complexity = O(n)


# **Binomial Coefficient**
Def: 
![](https://i.imgur.com/3tGuvLc.png)


- Recrusive
```
def Bin(n,m):
    if(m == n or m == 0):
        return 1
    else:
        return Bin(n-1,m) + Bin(n-1,m-1)
```

- Dynamic Programming for C(n,k)

Time complexity = O(n*k)


Auxiliary space = O(n*k)          #輔助空間

![](https://i.imgur.com/1fN0PNH.png)


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

GCD(A,B) 最大公因數(Greatest Common Divisor)


<定義>

![](https://i.imgur.com/g0AxLSQ.png)

          
```
def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b,a%b)
```

Ackerman Function : A(m,n)

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























