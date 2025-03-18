## BinaryGap
[풀이 링크](https://app.codility.com/demo/results/trainingRCY2WR-KME/)

A *binary gap* within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation <code>1001</code> and contains a binary gap of length 2. The number 529 has binary representation <code>1000010001</code> and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation <code>10100</code> and contains one binary gap of length 1. The number 15 has binary representation <code>1111</code> and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:
```
def solution(N)
```
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation <code>10000010001</code> and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [1..2,147,483,647].
