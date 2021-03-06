"""
[A. Dreamoon and Ranking Collection](https://codeforces.com/contest/1330/problem/A)
time limit per test1 second
memory limit per test256 megabytes
input : standard input
output : standard output
Dreamoon is a big fan of the Codeforces contests.

One day, he claimed that he will collect all the places from 1 to 54 after two more rated contests. It's amazing!

Based on this, you come up with the following problem:

There is a person who participated in ๐ Codeforces rounds. His place in the first round is ๐1, his place in the second
round is ๐2, ..., his place in the ๐-th round is ๐๐.

You are given a positive non-zero integer ๐ฅ.

Please, find the largest ๐ฃ such that this person can collect all the places from 1 to ๐ฃ after ๐ฅ more rated contests.

In other words, you need to find the largest ๐ฃ, such that it is possible, that after ๐ฅ more rated contests, for each
1โค๐โค๐ฃ, there will exist a contest where this person took the ๐-th place.

For example, if ๐=6, ๐ฅ=2 and ๐=[3,1,1,5,7,10] then answer is ๐ฃ=5, because if on the next two contest he will take
places 2 and 4, then he will collect all places from 1 to 5, so it is possible to get ๐ฃ=5.

Input
The first line contains an integer ๐ก (1โค๐กโค5) denoting the number of test cases in the input.

Each test case contains two lines. The first line contains two integers ๐,๐ฅ (1โค๐,๐ฅโค100). The second line contains
๐ positive non-zero integers ๐1,๐2,โฆ,๐๐ (1โค๐๐โค100).

Output
For each test case print one line containing the largest ๐ฃ, such that it is possible that after ๐ฅ other contests, for
each 1โค๐โค๐ฃ, there will exist a contest where this person took the ๐-th place.

Example
input
5
6 2
3 1 1 5 7 10
1 100
100
11 1
1 1 1 1 1 1 1 1 1 1 1
1 1
1
4 57
80 60 40 20

output
5
101
2
2
60

Note
The first test case is described in the statement.

In the second test case, the person has one hundred future contests, so he can take place 1,2,โฆ,99 and place 101 on
them in some order, to collect places 1,2,โฆ,101.
"""
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        a = data[it]
        x = data[it + 1]
        array = data[it + 2 : it + 2 + a]
        count = 1
        check = 1
        while x:
            if not check in array:
                count += 1
                x -= 1
            check += 1
        for i in range(a):
            if check in array:
                check += 1
            else:
                break
        print(check - 1)
        it += 2 + a
        T -= 1
