
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:

        width = right - left
        current_water = min(height[left], height[right]) * width
        max_water = max(max_water, current_water)
        
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
print("Enter the heights of lines (space-separated):")
    
arr = list(map(int, input().split()))
    
result = max_area(arr)
print("Maximum water that can be contained:", result)
