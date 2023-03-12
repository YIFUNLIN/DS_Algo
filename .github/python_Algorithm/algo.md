# **Factorial N!**
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