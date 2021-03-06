"""
[A. Nastya and Rice](https://codeforces.com/contest/1341/problem/A)
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

Nastya just made a huge mistake and dropped a whole package of rice on the floor. Mom will come soon. If she sees this,
then Nastya will be punished.

In total, Nastya dropped ๐ grains. Nastya read that each grain weighs some integer number of grams from ๐โ๐ to ๐+๐,
inclusive (numbers ๐ and ๐ are known), and the whole package of ๐ grains weighs from ๐โ๐ to ๐+๐ grams, inclusive
(numbers ๐ and ๐ are known). The weight of the package is the sum of the weights of all ๐ grains in it.

Help Nastya understand if this information can be correct. In other words, check whether each grain can have such a
mass that the ๐-th grain weighs some integer number ๐ฅ๐ (๐โ๐โค๐ฅ๐โค๐+๐), and in total they weigh from ๐โ๐ to ๐+๐,
inclusive (๐โ๐โคโ๐=1๐๐ฅ๐โค๐+๐).

Input
The input consists of multiple test cases. The first line contains a single integer ๐ก (1โค๐กโค1000)  โ the number of test
cases.

The next ๐ก lines contain descriptions of the test cases, each line contains 5 integers: ๐ (1โค๐โค1000)  โ the number of
grains that Nastya counted and ๐,๐,๐,๐ (0โค๐<๐โค1000,0โค๐<๐โค1000)  โ numbers that determine the possible weight of
one grain of rice (from ๐โ๐ to ๐+๐) and the possible total weight of the package (from ๐โ๐ to ๐+๐).

Output
For each test case given in the input print "Yes", if the information about the weights is not inconsistent, and print
"No" if ๐ grains with masses from ๐โ๐ to ๐+๐ cannot make a package with a total mass from ๐โ๐ to ๐+๐.

Example
inputCopy
5
7 20 3 101 18
11 11 10 234 2
8 9 7 250 122
19 41 21 321 10
3 10 8 6 1

outputCopy
Yes
No
Yes
No
Yes

Note
In the first test case of the example, we can assume that each grain weighs 17 grams, and a pack 119 grams, then really
Nastya could collect the whole pack.

In the third test case of the example, we can assume that each grain weighs 16 grams, and a pack 128 grams, then really
Nastya could collect the whole pack.

In the fifth test case of the example, we can be assumed that 3 grains of rice weigh 2, 2, and 3 grams, and a pack is 7
grams, then really Nastya could collect the whole pack.

In the second and fourth test cases of the example, we can prove that it is impossible to determine the correct weight
of all grains of rice and the weight of the pack so that the weight of the pack is equal to the total weight of all collected grains.


"""


import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        n = data[it]
        a = data[it + 1]
        b = data[it + 2]
        c = data[it + 3]
        d = data[it + 4]
        mini = c - d
        maxi = c + d
        min_rice = mini / n if n != 0 else 0
        max_rice = maxi / n if n != 0 else 0
        if max_rice < (a - b) or min_rice > (a + b):
            print("No")
        else:
            print("Yes")
        it += 5
        T -= 1
