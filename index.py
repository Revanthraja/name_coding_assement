#Question 1 : Leader in the Array

def printleader(arr[],size):
	max_ele=arr[size-1]
	print(max_ele);
	for i in range(size-1,-1,-1):
		if (max_ele<arr[i]):
			max_ele=arr[i]
			print(max_ele)

int arr[] = {7, 10, 4, 10, 6, 5, 2}; 
 int n = sizeof(arr)/sizeof(arr[0]); 


printLeaders(arr, n);


#Question 2 :Best Time to Buy and Sell Stock
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

#Question 3:Sum of All Subset XOR Totals
def xor_total_sum(nums):
    n = len(nums)
    dp = [0] * (1 << n)
    for i in range(n):
        for j in range(1 << n):
            if (j & (1 << i)) != 0:
                dp[j] ^= nums[i]
    return sum(dp)

