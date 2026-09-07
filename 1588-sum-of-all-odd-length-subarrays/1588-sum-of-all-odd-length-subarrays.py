class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            # Total subarrays containing arr[i]
            total_subarrays = (i + 1) * (n - i)
            # Odd length subarrays containing arr[i]
            odd_subarrays = (total_subarrays + 1) // 2
            
            total_sum += odd_subarrays * arr[i]
            
        return total_sum