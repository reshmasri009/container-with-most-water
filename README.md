# container-with-most-water
solved today's leetcode problem -container with most water using two pointer technique.
#Algorithm:
-take two pointers left,right
-initialise left=0,right=len(height)-1
-area=min(height(left),height(right))*(right-left)---(if left<right)
-if current area is large ---update max area
-height[left]>height[right]---shift left to forwared or else right backward
##Complexity
time=O(n)
space=O(1)
