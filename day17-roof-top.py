class Solution:
    
    # Function to find maximum number of consecutive steps 
    # to gain an increase in altitude with each step.
    def maxStep(self, arr):
        if len(arr) < 2:
            return 0  # No steps possible if there are fewer than 2 buildings
        
        max_steps = 0
        current_steps = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                current_steps += 1  # Increment the current increasing steps
                max_steps = max(max_steps, current_steps)  # Update max steps if current is greater
            else:
                current_steps = 0  # Reset the count if not increasing
        
        return max_steps
