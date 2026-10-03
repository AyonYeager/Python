# class Solution:
#     def __init__(self,nums,target):
#         self.nums=nums
#         self.target=target
#     def twoSum(self):
#         for i in range(len(self.nums)):
#             for j in range(i,len(self.nums)):
#                 if self.nums[i]+self.nums[j]==self.target:
#                     print(i,j)
# Solutions=Solution([3,9,2,1,4,5],11)
# Solutions.twoSum()

# class Solution:
#     def find(self,strs=[],common):
#         i=0
#         for i in strs:
#             if strs[0:]==common[strs]:
#                 return common
#         while i <= len(strs.split()):
#             i+=1

# class Solution:
#     def find(self,strs):
#         if not strs:
#             return "" 
#         for i in range(len(strs[0])):
#             c=strs[0][i]
#             for p in strs[1:]:
#                 if i>= len(p) or p[i] !=c:
#                     return strs[0][:i]
#         return strs[0]
# r=Solution()
# print(r.find(["flowers","flow","float"]))

# class Solution:
#     def find(self,nums):
#         l=min(nums)
#         o=nums.index(l)
#         return l
#         return o
# r=Solution()
# print(r.find([1,4,6,5,0,-2,2,-4,9]))


# def find(nums):
#     i=1
#     while i in nums:
#         i+=1
#     return i


# def twosum(nums,tr):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] ==tr:
#                 return [i,j]
# p=twosum([1,3,5,6,7,3,9],16)
# print(p)

# def find(nums):
#     n= len(nums)
#     for i in range(n):
#         if 1<= nums[i] <= n and nums[i]-1 != nums[i]:
#             index=nums[i]-1
#             nums[i],nums[index]=nums[index],nums[i]
#     for i in range(n):
#         if nums[i] != i+1:
#             return i+1
#     return n+1
# print(find([1,3,4,7,9,5,3]))

# def maxarea(height):
#     n=len(height)
#     for i in range(n):
#         for j in range(n):
#             if (height[i] * height[j] >= height[height[i]+1] * height[height[j]+1]) and ( height[i]-height[i+1] * height[j] - height[j+1]>= height[i]-height[j] * height[height[i]+1] - height[height[j]+1]):
#                 return [i,j]
#         if height[i]>height[j]:
#             return height[i]-1
#         else:
#             return height[j]-1
# print(maxarea([1,8,3,0,2,3,9]))



# class Solution:
#     def maxArea(self,height):
#         n=len(height)
#         max_w= 0
#         for i in range(n):
#             for j in range(i + 1 , n):
#                 area= min(height[i] , height[j]) * ( j - i)
#                 max_w= max(max_w , area)

#         return max_w

# class Solution:
#     def maxArea(self, height):
#         left = 0
#         right = len(height) - 1
#         max_w = 0

#         while left < right:
#             area = min(height[left], height[right]) * (right - left)
#             max_w = max(max_w, area)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_w

# r=Solution()
# print(r.maxArea([1,8,3,4,5,8,7,4,7,8]))



# class Solution:
#     def maxArea(self,h):
#         i=0
#         j=len(h)-1
#         max_w=0
#         while i<j:
#             a= min(h[i],h[j])*(j-i)
#             max_w= max(max_w,a)
#             if h[j]>h[i]:
#                 i+=1
#             else:
#                 j-=1
#         return max_w
# r=Solution()
# print(r.maxArea([9,8,3,4,5,8,7,4,7,8,9]))

# class Solution(object):
#     def threeSum(self, nums):
#         i=0
#         j=0
#         k=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):

#                     # while i != j, j != k, i != k :
#                     if nums[i] + nums[j] + nums [k] == 0:
#                          return [i,j,k]
#                     else:
#                         continue
#                 return [nums[i],nums[j],nums[k]]
# r=Solution()
# print(r.threeSum([-1,0,-4,2,-1,-1]))

# class Solution(object):
#     def threeSum(self, nums):
#         result = []
#         n = len(nums)

#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triplet = sorted([nums[i], nums[j], nums[k]])
#                         if triplet not in result:
#                             result.append(triplet)

#         return result
# r=Solution()
# print(r.threeSum([-1,0,-4,2,-1,-1]))


# class Solution(object):
#     def threeSum(self, nums):
#         result = []

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result.append([nums[i], nums[j], nums[k]])

#         return result
# r=Solution()
# print(r.threeSum([-1,0,-4,2,-1,-1]))       

# class Solution(object):
#     def threeSum(self, nums):
#         i=0
#         j=0
#         k=0
#         re= []
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):

#                     # while i != j, j != k, i != k :
#                     if nums[i] + nums[j] + nums [k] == 0:
#                         re.append([nums[i],nums[j],nums[k]])
                   
#         return re
# r=Solution()
# print(r.threeSum([0,1,2]))

# class Solution(object):
#     def threeSum(self, nums):
#         result = []

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:

#                         triplet = sorted([nums[i], nums[j], nums[k]])

#                         if triplet  in result:
#                             continue
#                         else:
#                             result.append(triplet)

#         return result
# # 
# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         n = len(nums)
#         closest = 0
#         for i in range(n):
#             for j  in range(i+1,n):
#                 for k in range(j+1,n):
#                     t = nums[i] + nums[j] + nums[k]
#                     if t == target :
#                         continue
#                     elif t < target :
#                         closest += 1
#                     else :
#                         closest -= 1
                    

                        
#         return closest 
# r = Solution()
# print(r.threeSumClosest( [-8, -6, -5, -3],-10))


# def yeap(nums,tr):
#     nums.sort()
#     closest = nums[0] + nums[1] + nums[2]
#     for i in range(len(nums)-2):

#         l = i + 1
#         r = len(nums) - 1

#         while l < r :
#             t = nums[i] + nums[l] + nums[r]

#             if abs(tr - t) < abs(tr - closest) :
#                 closest = t
#             if t < tr :
#                 l += 1
#             elif t > tr :
#                 r -= 1
#             else:
#                 return tr
#     return closest 
# print(yeap([-8,-6,-5,-3],-10))


# def pop( x):

#     s = str(abs(x))
#     reverse = s[::-1]
#     reverse_x = int(reverse)
    
#     if x > 0 and x == reverse_x :
#         return True 
#     else :
#         return False


# print(pop(121))

# def pop(nums):
#     i = 1
#     while i in nums:
#         i += 1
#     return i

# print(pop([1,2,3,4,5,6,7,8,10,11,5,3,9]))
# first missing positive number

# def rd(nums):
#         n = len(nums)

#         if n == 0:
#             return 0 

#         k = 1

#         for i in range(1 , n) :
#             if nums[i] != nums[i-1] :
#                 nums[k] = nums[i]
#                 k += 1
                
#         return k , min(k , n - k)
# print(rd([0,0,1,1,2,3,3,4,4,5,5]))

# def re(nums, val):
#         n = len(nums)

#         if nums == 0 :
#             return 0

#         k = 1
#         for i in range( 1 , n) :

#             if nums[i] != val :
#                 nums[k] == nums[i]
#                 k += 1
#         return k 
# print(re([0,1,2,2,3,0,4,2],2))
            

# class Solution(object):
#     def nextPermutation(self, nums):

#         i = len(nums) - 2
        
#         # step1: find pivot
#         while i >= 0 and nums[i] >= nums[i+1]:
#             i -= 1

#         if i >= 0:
#             j = len(nums) - 1
            
#             # step2: find next greater
#             while nums[j] <= nums[i]:
#                 j -= 1
            
#             nums[i], nums[j] = nums[j], nums[i]

#         # step3: reverse right side
#         nums[i+1:] = reversed(nums[i+1:])
#         return nums
        
# r = Solution()
# print(r.nextPermutation([1,3,5,4,2]))





# def search( nums, target):

#     n = len(nums)
#     k = 0
#     for i in range(n):
#         if nums[i] == target:
#             return i
#         if target not in nums:
#             return -1
# print(search([4,5,6,7,0,1,2],0))

# class Solution(object):
#     def search(self, nums, target):

#         left = 0
#         right = len(nums) - 1

#         while left <= right:

#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid

#             if nums[left] <= nums[mid]:   
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#             else:                         
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return -1
# r= Solution()
# print(r.search([5,6,7,0,1,2],4))

# class Solution(object):
#     def searchRange(self, nums, target):
#         n = len(nums)
#         if not nums:
#             return[-1,-1]

#         l = 0 
#         r = n - 1
        
#         while l <= r :
#             for i in range(n):
#                 for j in range(i,n):
#                     if nums[i] == target and nums[j] == target :
#                         return [i,j]

#             l += 1
#             r -= 1
#         if target not in nums:
#             return[-1,-1]
        
# r = Solution()
# print(r.searchRange([5,7,7,8,8,10],8))

# def searchRange(nums, target):
#     def find(siuu):
#         l, r = 0, len(nums) - 1
#         owo = -1
        
#         while l <= r:
#             mid = (l + r) // 2
            
#             if nums[mid] == target:
#                 owo = mid
#                 if siuu:
#                     r = mid - 1  
#                 else:
#                     l = mid + 1   
#             elif nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return owo

#     s = find(siuu=True)
#     e = find(siuu=False)
    
#     return [s, e]
# print(searchRange([1],1))


# def b(n):

#     b = format(n , 'b')
#     n = len(b)
#     if n >= 1:
#         for i in range(n):
#             swap = 0
#             if int(b[i]) != (i%2):
#                 swap += 1
#                 # swap = int(swap , 2 )
#     return swap
# print(b(5))

# def b(n):
#     if n == 0 :
#         return 1

#     bi = format(n , 'b')
#     swap = ""
#     a = len(bi)


#     if n >= 1:
            
#         for i in range(a):
                
#             if bi[i] != "0":
#                 swap += "1"
#             else:
#                 swap += "0"
        
#     return int(swap , 2)
# print(b(5))

# def se_a( nums, target):
#         n = len(nums)
#         l = 0
#         r = n - 1
         
         
#         while l <= r :
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target :
#                 l = mid + 1 
#             else:
#                 r = mid - 1
        
    
#         return l
# print(se_a([1,2,3,4,5,6],3))


# def solveNQueens(n):
#     def is_safe(board, row, col):
#         # check column
#         for i in range(row):
#             if board[i] == col:
#                 return False
#         # check diagonals
#         for i, j in enumerate(board[:row]):
#             if abs(j - col) == abs(i - row):
#                 return False
#         return True

#     def backtrack(row, board, solutions):
#         if row == n:
#             solutions.append(["." * c + "Q" + "." * (n - c - 1) for c in board])
#             return
#         for col in range(n):
#             if is_safe(board, row, col):
#                 board[row] = col
#                 backtrack(row + 1, board, solutions)

#     solutions = []
#     board = [-1] * n
#     backtrack(0, board, solutions)
#     return solutions

# print(solveNQueens(8))

# def co( candidates, target):
#         n = len(candidates)
#         re = []


#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):
                    
                
#                     t = candidates[i] + candidates[j] + candidates[k]
#                     if t == target:
#                         re.append([candidates[i], candidates[j] , candidates[k]])
                    
                    

#         return re


# class Solution(object):
#     def co(self, candidates, target):

#         res = []

#         def dfs(start, path, remaining):

#             if remaining == 0:
#                 res.append(path[:])
#                 return

#             if remaining < 0:
#                 return

#             for i in range(start, len(candidates)):

#                 path.append(candidates[i])

#                 dfs(i, path, remaining - candidates[i])

#                 path.pop()

#         dfs(0, [], target)

#         return res
# r = Solution()
# print(r.co([2,3,4,7],7))


# class Solution(object):
#     def so(self, board):

#         def valid(r, c, num):

#             for i in range(9):

#                 if board[r][i] == num:
#                     return False

#                 if board[i][c] == num:
#                     return False

#                 br = (r//3)*3 + i//3
#                 bc = (c//3)*3 + i%3

#                 if board[br][bc] == num:
#                     return False

#             return True


#         def dfs():

#             for r in range(9):
#                 for c in range(9):

#                     if board[r][c] == ".":

#                         for num in "123456789":

#                             if valid(r,c,num):

#                                 board[r][c] = num

#                                 if dfs():
#                                     return True

#                                 board[r][c] = "."

#                         return False

#             return True


#         dfs()

# class Solution(object):
#     def solveSudoku(self, board):

#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         boxes = [set() for _ in range(9)]

#         empty = []

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     empty.append((r,c))
#                 else:
#                     num = board[r][c]
#                     rows[r].add(num)
#                     cols[c].add(num)
#                     boxes[(r//3)*3 + c//3].add(num)

#         def dfs(i):

#             if i == len(empty):
#                 return True

#             r,c = empty[i]
#             box = (r//3)*3 + c//3

#             for num in "123456789":

#                 if num not in rows[r] and num not in cols[c] and num not in boxes[box]:

#                     board[r][c] = num
#                     rows[r].add(num)
#                     cols[c].add(num)
#                     boxes[box].add(num)

#                     if dfs(i+1):
#                         return True

#                     board[r][c] = "."
#                     rows[r].remove(num)
#                     cols[c].remove(num)
#                     boxes[box].remove(num)

#             return False

#         dfs(0)

# def ple(digits):
#         n = len(digits)
#         for i in range(n-1,-1,-1):
#             if digits[i] < 9 :

#                 digits[i] += 1
#                 return digits
#             digits[i] = 0

#         return [1] + digits

# print(ple([1,2,9]))

# def trap(height):
#         n = len(height)
#         l = 0
#         r = n - 1
#         lm = rm = 0
#         water = 0
#         while l < r :
#             if height[l] > height[r]:
#                 if height[l] >= lm:
#                     lm = height[l]

#                 else:
#                     water += lm - height[l]
#                 l += 1 

#             else:
#                 if height[r] >= rm:
#                     rm  = height[r]

#                 else:
#                     water += rm - height[r]
#                 r -= 1

             
#         return water
# print(trap([1,8,6,2,5,4,8,3,7]))

# from itertools import combinations
# class Solution(object):
#     def permute(self, nums):
#         n = len(nums)
#         combo = []
#         for i in range(1 , n):
#             all = list(combinations(nums , i))
            
#             combo.append(all)
        

#         return combo

# r = Solution()
# print(r.permute([1,2,3]))

# from itertools import permutations
# class Solution(object):
#     def per(nums):
#         return [list(p) for p in permutations(nums)]

# from itertools import permutations
# class Solution(object):
#     def permute(self, nums):
#         all = permutations(nums)
        
#         unique_way_to_do_so = set(all)

#         p = []
        
        
        
#         for i in unique_way_to_do_so :
#             p.append(list(i))

            

#         return p
            
# r = Solution()
# print(r.permute([1,2,1]))


# def can( grid):
#         m, n = len(grid), len(grid[0])

#         # total sum
#         total = sum(sum(row) for row in grid)

#         # must be even
#         if total % 2 != 0:
#             return False

#         target = total // 2

#         # ---- check horizontal cuts ----
#         prefix = 0
#         for i in range(m - 1):  # must leave bottom non-empty
#             prefix += sum(grid[i])
#             if prefix == target:
#                 return True

#         # ---- check vertical cuts ----
#         prefix = 0
#         for j in range(n - 1):  # must leave right non-empty
#             col_sum = 0
#             for i in range(m):
#                 col_sum += grid[i][j]

#             prefix += col_sum
#             if prefix == target:
#                 return True

#         return False

# print(can([[1,5,5],[7,0,4],[6,0,5]]))
# print(can([[65917,79299]]))
# print(can([[1,5,5],[7,0,4],[6,0,5]]))
# print(can([[65917,79299]]))
# print(can([[1,4],[2,3]]))
# print(can([[2,3],[2,3]]))

# # from functools import reduce
# # class Solution(object):
# #     def canPartitionGrid(self, grid):
# #         nums1 = grid[0]
# #         nums2 = grid[1]
# #         def mysum(x,y):
# #             return x + y

# #         siu1 = reduce(mysum , nums1)
# #         siu2 = reduce(mysum , nums2)
# #         if siu1 == siu2 :
# #             return True
# #         else:
# #             return False
            


# from collections import defaultdict
# class Solution(object):
#     def gr(self, strs):
        
#         re = defaultdict(list)
#         for s in strs:
#             p = "".join(sorted(s))
#             re[p].append(s)

#         return list(re.values())


# r = Solution()
# print(r.gr(["eat","tea","tan","ate","nat","bat"]))
# class Solution(object):
#     def solveNQueens(self, n):
#         rows = [set() for _ in range(n)]
#         cols = [set() for _ in range(n)]
        
#         queens = n
#         directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]
#         if rows == cols :
#             return False
#         for i in range(n):
#             for j in range(i+1,n):

#                 if rows[i][j] == directions or cols[i][j] == directions :
#                     return False 
        
#         def backtrack(start , n , path):
#             queens.append(path[:])
#             for i in range(start,n):
#                 path.append(i)
#                 backtrack(i+1 , n - queens , path)
#                 path.pop()

#         backtrack(0 , n , [])
#         return True

# r = Solution()
# print(r.solveNQueens(8))

# class Solution(object):
#     def solveNQueens(self, n):
#         re = []
#         board = [["."] * n for _ in range(n)]

#         cols = set()
#         light_square_bishop = set()  
#         dark_square_bishop = set()  

#         def backtrack(row):
#             if row == n:
#                 re.append(["".join(r) for r in board])
#                 return

#             for col in range(n):
#                 if col in cols or (row - col) in light_square_bishop or (row + col) in dark_square_bishop:
#                     continue

                
#                 board[row][col] = "Q"
#                 cols.add(col)
#                 light_square_bishop.add(row - col)
#                 dark_square_bishop.add(row + col)

#                 backtrack(row + 1)

                
#                 board[row][col] = "."
#                 cols.remove(col)
#                 light_square_bishop.remove(row - col)
#                 dark_square_bishop.remove(row + col)

#         backtrack(0)
       
#         return re
# class Solution(object):
#     def solveNRooks(self, n):
#         re = []
#         board = [["."] * n for _ in range(n)]

#         cols = set()
          

#         def backtrack(row):
#             if row == n:
#                 re.append(["".join(r) for r in board])
#                 return

#             for col in range(n):
#                 if col in cols :
#                     continue

                
#                 board[row][col] = "R"
#                 cols.add(col)
                

#                 backtrack(row + 1)

                
#                 board[row][col] = "."
#                 cols.remove(col)
                

#         backtrack(0)
       
#         return re



# class Solution(object):
#     def roman(self, num):
#         roman_nums = [
#             (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
#             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
#             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
#         ]
        
#         re = ""

#         for val , symb in roman_nums:
#             while num >= val :
#                 re += symb
#                 num -= val
                 


#         return re




# r = Solution()
# print(r.roman(3453))



# def spiral(nums):
#     n = len(nums)
#     l1 = nums[0]
#     l2 = nums[1]
#     l3 = nums[2]
#     re = []
    
#     re.extend(l1)
    
#     re.append(l2[-1])
    
#     re.extend(l3[::-1])
#     re.extend(l2[0:len(l2)-1])
#     return re

# print(spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


# class Solution(object):
#     def spiralOrder(self , matrix):
#         left , right = 0 , len(matrix) - 1
#         top , bottom = 0 , len(matrix[0]) - 1

#         re = []

#         while top <= bottom and left <= right :
#             for i in range(left , top + 1):
#                 re.append(matrix[top][i])
#             top += 1

#             for i in range(top , bottom + 1):
#                 re.append(matrix[bottom][i])
#             bottom -= 1
            
#             for i in range(bottom , left - 1):
#                 re.append(matrix[left][i])
#             left -= 1

#             for i in range(top , right + 1):
#                 re.append(matrix[right][i])
#             right += 1
        
#         return re


    


# class Solution(object):
#     def merge(self, intervals):
#         intervals.sort()
#         n = len(intervals)

#         re = []
#         st, end = intervals[0]   # start with first interval

#         for i in range(1, n):
#             cur_start = intervals[i][0]
#             cur_end = intervals[i][1]

#             # overlap
#             if cur_start <= end:
#                 end = max(end, cur_end)
#             else:
#                 # no overlap → save previous interval
#                 re.append([st, end])
#                 st, end = cur_start, cur_end

#         # add last interval
#         re.append([st, end])

#         return re

# r = Solution()

# print(r.merge([[1,3],[6,9],[2,5]]))




# class Solution(object):
#     def minPathSum(self, grid):

#         r = len(grid)
#         d = len(grid[0])

#         memo = {}

#         def backtrack(i, j):

           
#             if i >= r or j >= d:
#                 return float('inf')

            
#             if i == r - 1 and j == d - 1:
#                 return grid[i][j]

            
#             if (i, j) in memo:
#                 return memo[(i, j)]

#             right = backtrack(i, j + 1)
#             down = backtrack(i + 1, j)

#             memo[(i, j)] = grid[i][j] + min(right, down)

#             return memo[(i, j)]

#         return backtrack(0, 0)

# r = Solution()
# print(r.minPathSum([[1,2,3],[1,2,4],[3,3,5]]))





# class Solution(object):
#     def reverse(self, x):

#         sign = -1 if x < 0 else 1 

#         x = abs(x)

#         re = 0

#         while x != 0 :

#             digit = x % 10
#             x = x // 10

#             if re > 214748364 or (re == 214748364 and digit > 7):
                 
#                 return 0
            
#             re = re * 10 + digit

#         return sign * re


        
         


# r = Solution()
# print(r.reverse(-120))


# class Solution(object):
#     def re(self, nums):
#         n = len(nums)

        
        
#         index = 2 
#         for i in range(2 , n):
#             if nums[i - 2] != nums[i] :
#                 nums[index] = nums[i]
#                 index +=  1

#         return index

# r = Solution()
# print(r.re([0,0,1,1,1,1,2,3,3]))

# class Solution(object):
#     def search(self, nums, target):
       

        
#         for i in range(len(nums) ):
#             if nums[i] - target == 0 :
#                 return True

#         return False

# r = Solution()
# print(r.search([1],1))


# class Solution(object):
#     def laa(self, heights):
#         n = len(heights)
#         l = 0 
#         r = len(heights) - 1
#         max_area = 0  
#         while l < r:
#             if heights[l] <= heights[r] :
#                 area = max(heights , heights[l]) * heights[l]
            
#             l += 1

#             else:
#                 area = max(heights , heights[r]) * height[r]
            
#             r -= 1

#         return area * 2
# r = Solution()
# print(r.laa([2,1,5,6,2,3]))



# class Solution(object):
#     def largestRectangleArea(self, heights):
#         n = len(heights)
#         l = 0 
#         r = len(heights) - 1
#         width = 0 
#         while l < r:
#             mid = (l + r) // 2
#             if heights[l] < heights[mid]:
                
                
                
            

#         return 


# class Solution(object):
#     def la(self, heights):

#         n = len(heights)
#         max_area = 0

#         for i in range(n):

#             height = heights[i]

#             l = i
#             r = i

#             # expand left
#             while l > 0 and heights[l - 1] >= height:
#                 l -= 1

#             # expand right
#             while r < n - 1 and heights[r + 1] >= height:
#                 r += 1

#             width = r - l + 1

#             area = height * width

#             max_area = max(max_area, area)

#         return max_area

# r = Solution()
# print(r.la([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

# import math
# import time
# import sys

# def main():
#     a = 0.0
#     while True:
        
#         p1 = int(15 + math.sin(a) * 10)
#         p2 = int(15 + math.sin(a + 3.14) * 10)

#         line = ""
#         for i in range(40):
#             if i == p1:
                
#                 line += "\033[1;35m1\033[0m"
#             elif i == p2:
                
#                 line += "\033[1;36m0\033[0m"
#             elif (p1 < i < p2) or (p2 < i < p1):
                
#                 line += "="
#             else:
#                 line += " "
        
#         print(line)
        
#         a += 0.2
        
#         time.sleep(0.06)

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
        
#         sys.exit()



# class Solution(object):
#     def buildTree(self, preorder, inorder):

#         if not preorder or not inorder:
#             return None

#         root_val = preorder[0]

#         root = TreeNode(root_val)

#         tr = inorder.index(root_val)

#         left_inorder = inorder[:tr]
#         right_inorder = inorder[tr + 1:]

#         left_preorder = preorder[1 : 1 + len(left_inorder)]
#         right_preorder = preorder[1 + len(left_inorder):]

#         root.left = self.buildTree(left_preorder, left_inorder)

#         root.right = self.buildTree(right_preorder, right_inorder)

#         return root

# r = Solution()
# print(r.buildTree([3,5,6,4,9],[9,4,6,3,5]))


# class Solution(object):
#     def minimumTotal(self, triangle):
#         # Start from the second-to-last row and move upwards
#         for row in range(len(triangle) - 2, -1, -1):
#             for col in range(len(triangle[row])):
#                 # Add the minimum of the two adjacent children below it
#                 triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
#         # The top element now contains the total minimum path sum
#         return triangle[0][0]

# r = Solution()
# print(r.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

# class Solution(object):
#     def maxProfit(self, prices):
#         min_p = prices[0]
#         max_p = 0
        
#         for price in prices:

#             if price < min_p:
#                 min_p = price
            
#             profit = max_p - min_p

#             if profit > max_p :
#                 max_p = profit

#         return max_p


# r = Solution()
# print(r.maxProfit([7,6,5,4,3,2,1]))


def p(nums):
    i = 1
    while i in nums:
        i += 1
    return i
print(p([1,2,3,4,6]))