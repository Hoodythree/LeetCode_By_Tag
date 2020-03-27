def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res

import bisect

def max_len(nums):
        x = [-float('inf')]
        for i in nums:
            if i > x[-1]:
                x += [i]
            else:
                x[bisect.bisect_left(x, i)] = i
        return len(x) - 1

# nums = [1, 3, 5, 2, 9]
# print(max_len(nums))

if __name__ == '__main__': 
    a = []
    n = int(input()) 
    line = input() 
    nums = line.split()
    for i in range(n): 
        a.append(int(nums[i]))
    print(max_len(a))
        

#include <iostream>
#include <cstdio>
#include <algorithm>
 
using namespace std;
long long dp[1000001];
 
int main()
{
    dp[1] = 1;
    dp[2] = 2;
    for(int i = 3; i <= 1000000; i ++)
    {
        if(i&1)
            dp[i] = dp[i-1];
        else
            dp[i] = dp[i-2] + dp[i/2];
    }
    int n;
    scanf("%d", &n);
    printf("%lld\n", dp[n]%1000000000);
    return 0;
}
