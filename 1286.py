


# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 

while True:
    val = []
    wt = []
    number_of_orders = int(input())

    if (not number_of_orders):
        break

    max_r_orders = int(input())
    
    print(number_of_orders)
    for i in range(number_of_orders):
        line = list(map(int, input().split()))
        val.append(line[0])
        wt.append(line[1])
    
    print('{} min.'.format(knapSack(max_r_orders, wt, val, len(val))))