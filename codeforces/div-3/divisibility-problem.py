"""
[A. Divisibility Problem](https://codeforces.com/contest/1328/problem/A)
time limit per test 1 second
memory limit per test256 megabytes
input: standard input
output: standard output
You are given two positive integers ๐ and ๐. In one move you can increase ๐ by 1 (replace ๐ with ๐+1). Your task
is to find the minimum number of moves you need to do in order to make ๐ divisible by ๐. It is possible, that you have
 to make 0 moves, as ๐ is already divisible by ๐. You have to answer ๐ก independent test cases.

Input
The first line of the input contains one integer ๐ก (1โค๐กโค104) โ the number of test cases. Then ๐ก test cases follow.

The only line of the test case contains two integers ๐ and ๐ (1โค๐,๐โค109).

Output
For each test case print the answer โ the minimum number of moves you need to do in order to make ๐ divisible by ๐.

Example

input
5
10 4
13 9
100 13
123 456
92 46

output
2
5
4
333
0
"""

# Solution

# cook your dish here
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        a = data[it]
        b = data[it + 1]
        if a % b == 0:
            print(0)
        else:
            next_num = b * ((a // b) + 1)
            print(next_num - a)
        it += 2
        T -= 1
