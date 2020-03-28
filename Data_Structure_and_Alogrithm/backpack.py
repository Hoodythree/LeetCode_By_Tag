def knapSack(W , wt , val , n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 


if __name__ == '__main__': 
    val = []
    wt = []
    first_line = input().split()
    n = first_line[0]
    total_val = int(first_line[1])

    for i in range(int(n)):
        x = input()
        line = x.split()
        wt.append(int(line[0]))
        val.append(int(line[1]))
    print(knapSack(total_val , wt , val , len(val)))


