# from functools import reduce
# l=[]
# for i in range(1,10000001):
#     l.append(i)
# def sum(x,y):
#     return x+y 
# a=reduce(sum,l)
# print(a)

# class math():
#     def __init__(self,num,n):
#         self.num=num
#         self.n =n
#     def show(self):
#        print( self.num + self.n)
#     # @staticmethod
#     # def add(x,y):
#     #     return x+y 
#     # c=add(3,7)
#     # print(c)
# c=math(29308033,8039278934)
# print(c)
# c.show()




# class employee():
    
    
#     def __init__(self,name,amount_raise,company):
#         self.name=name
#         self.raise_amount="0.002 BTC"
#         self.company=company
#     def show(self):
#         print(f"the name of employee is {self.name} and raised amount is {self.raise_amount} works in {self.company}")
# emp=employee("harold"," ","Apple")
# emp.company="microsoft"

# employee.company="GOOGLE"
# emp.show()
# print(emp.company)



# class employee():
#     def __init__(self,name):
#         self.__name= "harold"
#     def show(self):
#         print(self.__name)
# emp=employee(" ")
# # print(emp.__name)
# # print(emp.employee__name)
# emp.show()

# class employee:
#     company="Appulee"
#     def show(self,company):
#         print(f"i don't know what to write but {self.company}")
#     @classmethod
#     def ncompany(cls,ncompany):
#         cls.ncompany=ncompany
#         print(f"transfer to {cls.ncompany}")                                                                                                  #why always me? will i ever make that in life that i always dreamt of ? big question ,answer are inevitable.life going that way as i always hate to lead.at the end im nothing but a loser pretending to be genius.but im happy cause i was alone dealing my problems. should i feel proud of this? (i thing i know all stars closer)
# emp=employee.ncompany(" ttt")
# emp=employee()
# emp.show("ttt")


# print(emp.ncompany)

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def st(cls,np):
#         return cls(np.split("-")[0],np.split("-")[1])
# e=employee.st("Johnathon- $1200")
# print(e.name , e.salary)
# # print(e.__dict__)
# # print(help(employee))



# x={1,2,3}
# print(dir(x))

# l=[1,2,3,4,5,6,7,8,9]
# cube=lambda x:x**3
# print(list(map(cube,l)))
# def func(a):
#     return a>2
#     print(list(filter(func,l)))
# from functools import reduce
# l=[]
# for i in range(1,10001):
#     l.append(i)
#     def su(x,y):
#         return x+y
# print(reduce(su,l))
# l=[1,2,3,4,5]
# def f(a):
#     return a>2
# print(list(filter(f,l)))

# l={ "keys" : "value"

# }
# print(dir(l))


# class employee:
#     def __init__(self,name,icard):
#         self.name=name
#         self.icard=icard
# class programmer(employee):
#     def __init__(self,name,icard,language):
#         self.language=language
#         super().__init__(name,icard)
# p= programmer("Harold","EC49","Python")
# a=(f"candidate name: {p.name}\nidentification: {p.icard}\nfluent in     : {p.language} language")
# print(a)
# print(p.__dict__)

# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def relational(self):
#         return self.x * self.y
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):
#         print( 3.14 * super().relational())
# a=circle(5)
# print(a)
# a.area()



# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def conc(self):
#         return self.x * self.y
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):
#         print(3.14 * super().conc())
# a= circle(3.14)
# a.area()


# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def yo(self):
#         return self.x * self.y
# class circle(shape):
#     def __init__(self,rad):
#         self.rad=rad
#         super().__init__(rad,rad)
#     def area(self):
#         return 3.14 * super().yo()
# a=circle(3.14)
# print(a.area())
                                                     

# class emp:
#     def __init__(self,name):
#         self.name=name
#         i=0
#         for l in self.name:
#             i += 1
#         print(i)
# e = emp("harold")
# print(e.name)

# class emp:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return (f"employee name is {self.name} from str")
#     def __repr__(self):
#         return ( f"employee name is  {self.name} from repr")
#     def __call__(self):
#         print("yowaimo")
# e = emp("harold")
# print(e.__str__())
# print(e.__repr__())
# e()
    
# class animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
# class dog(animal):
#     def __init__(self,name,bread,species):
#         self.bread=bread
#         super().__init__(name,species="dog")
# d=dog ("dogesh","rotwillwer"," ")
# print(d.name, d.species, d.bread)

# class employee:
#     def __init__(self,name):
#         self.name=name
# class dancer:
#     def __init__(self,style):
#         self.style=style
# class omni(employee,dancer):
#     def __init__(self,name,style):
#         employee.__init__(self,name)
#         dancer.__init__(self,style)
# o=omni("Harold","ZAZ")
# print(f"Dancer name is       :  {o.name}\nAnd dancing style is :  {o.style}")

# class animal:
#     def __init__(self,name):
#         self.name=name
#         print(f"Animal's species is  : {self.name}")
# class dog(animal):
#     def __init__(self,name,bread):
#         self.bread=bread
#         animal.__init__(self,name)
#         print(f"Animal's bread is    : {self.bread}")
# class rotwillwer(dog):
#     def __init__(self,name,bread,colour):
#         self.colour=colour
#         dog.__init__(self,name,bread)
#         print(f"Animal's colour      : {self.colour}")
#     def show(self):
#             print(f"Pet's name is        : Dogesh")
# r = rotwillwer("Dog","Rotwillwer","Black")
# r.show()

# import requests
# t=requests.get("http://www.instagram.com")
# print(t.text)

# import time
# def tfor():
#     i=0
#     for i in range(1,5001):
#         print(i)
        
# def twhile():
#     i=0 
#     while i<=5000:
#         print(i)
#         i+=1
# init= time.time()
# twhile()
# t1=time.time()- init
# print(f"time taken by while loop is : {t1} seconds")
# init2= time.time()
# tfor()
# t2=time.time()- init2
# print(f"time taken by for loop is : {t2} seconds")
# print(t2-t1)
# if t1>t2:
#     print("for loop is faster than while loop")
# else: 
#     print("while loop is faster than for loop")


# import time 
# def tfo():
#     i=0
#     for i in range(1,500001):
#         print(i)
# def twhil():
#     i=0 
#     while i<=500000:
#         print(i)
#         i+=1
# init=time.time()
# tfo()
# t3=time.time()-init
# print(t3)
# init2=time.time()
# twhil()
# t4=time.time()-init2
# print(t4)

# print(t4-t3)
# if t3>t4:
#     print("for loop is faster than while loop")
# else:
#     print("while loop is faster than  for loop")

# import time
# i=0 
# for i in range(1,6):
#     print(i)
#     time.sleep(2)
#     if i in range(1,5):
#         print("printing..... wait for 2 seconds")
#     else:
#         print("the end , iterashai")

# foods= list()
# while print(food:=input("enter your favourite foods : ")) != "quit":
#     foods.append(food)
#     print(foods.__dict__)

# import time 
# t = time.localtime()
# ft=time.strftime("%D, %H : %M : %S")
# print(ft)

# def my_generator():
#     for i in range(1,6):
#         yield i 
    
# g= my_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# print("hello  world bye hey yo bhai kya haal hai accah hai kya ?")


# from functools import reduce 
# l=[]
# for i in range(1,100000001):
#     l.append(i)
# def sum(x,y):
#     return x+y
# a=reduce(sum,l)
# print(a)

# from functools import lru_cache
# import time
# @lru_cache(maxsize=None)
# def fx(x):
#     time.sleep(2)
#     return x*5
# print(fx(20))
# print("done for 20 ")
# print(fx(5))
# print("done for 5 ")
# print(fx(30))
# print("done for 30")
# print(fx(20))
# print(fx(5))
# print(fx(30))

# import time 
# import asyncio
# def f1():
#     time.sleep(5)
#     print("function1")
# def f2():
#     time.sleep(5)
#     print("function2")
# def f3():
#     time.sleep(5)
#     print("function3")
# async def main():
#     l= await asyncio.gather(f1(),f2(),f3())
# asyncio.run(main())

# import requests 
# from bs4 import BeautifulSoup
# r = requests.get("https://www.instagram.com")
# soup= BeautifulSoup(r.text,"html.parser")
# print(soup) 

# import requests
# r=requests.get("https://www.meta.com")
# print(r.text)



# class Solution(object):
#     def rotate(self, matrix):
#         n = len(matrix)

#         for i in range(n):
#             for j in range(i+1,n):
#                 matrix[i][j]  , matrix[j][i] = matrix[j][i] , matrix[i][j]

#         for i in range(n):
#             matrix[i].reverse()

            

#         return matrix

# r = Solution()
# print(r.rotate([[1,2,3],[4,5,6],[7,8,9]]))

            
        
# from collections import defaultdict
# def gr( strs):
#         re = defaultdict(list)
#         for s in strs:
#             p = "".join(sorted(s))
#             re[p].append(s)

#         return list(re.values())
# print(gr(["eat","tea","tan","ate","nat","bat"]))

# class Solution(object):
#     def jump(self, nums):
#         far = 0 
#         cur = 0
#         jumps = 0 
#         n = len(nums)
#         for i in range(n - 1):
#             far = max(far , i + nums[i] )

#             if i == cur :
#                 jumps += 1
#                 cur = far
                
#         return jumps
# r = Solution()
# print(r.jump([2,3,0,1,4]))

# class Solution(object):
#     def canJump(self, nums):
#         n = len(nums)
#         far = 0 
#         jumps = 0
        
        
        
#         for i in range(n-1):
#             if nums[i] == nums[i] and nums[i] >= nums[i+1] and nums[i] <= nums[i+1] :
#                 far = max(far , i + nums[i])
                    
                    

#             if far >= n:
#                 return True
        
        
#         return False



# class Solution(object):
#     def canJump(self, nums):
#         n = len(nums)
#         far = 0 
#         for i in range(n):
#             if i > far :
#                 return False 

#             far = max(far , i + nums[i])

#         return True

# r = Solution()
# print(r.canJump([2,4,0,1,4]))

# class Solution(object):
#     def insert(self, intervals, newInterval):
#         intervals.append(newInterval)
#         intervals.sort()

#         re = []

#         st , end = intervals[0]

#         n = len(intervals)

#         for i in range(1,n):

        
#             fi = intervals[i][0]
#             se = intervals[i][1]
            
#             if fi <= end:
#                 end = max(end , se)

#             else:
#                 re.append([st,end])
#                 st , end = fi , se
        
#         re.append([st,end])

#         return re



# r = Solution()
# print(r.insert([[1,3],[6,9]],[2,5]))


# class Solution(object):
#     def solveNQueens(self, n):
#         re = []
#         board = [[" * "] * n for _ in range(n)]

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

                
#                 board[row][col] = " * "
#                 cols.remove(col)
#                 light_square_bishop.remove(row - col)
#                 dark_square_bishop.remove(row + col)

#         backtrack(0)
#         # unique_way_to_do_so = set(re)  #--------------
#                                                         #|
#                                                         #|
#         # p = []                                        #|#------> #trying to avoids duplicates but showing errors
#                                                         #|
#         # for i in unique_way_to_do_so :                #|
#         #     p.append(list(i))          #--------------

            

#         # return p
#         return re
# r = Solution()
# print(r.solveNQueens(8)) #['Q.......', '....Q...', '.......Q', '.....Q..', '..Q.....', '......Q.', '.Q......', '...Q....']




# def gm( n):
    
#         m = [[0]*n for _ in range(n)]
    
#         left , right = 0 , n - 1
#         top , bottom = 0 , n - 1

#         num = 1
        

#         while top <= bottom and left <= right :
#             for i in range(left , right + 1):
#                 m[top][i] = num
                
#                 num += 1 
#             top += 1
            
#             for i in range(top , bottom + 1):
#                 m[i][right] = num
                
#                 num += 1
#             right -= 1

#             if top <= bottom :
#                 for i in range(right , left -1 ,  -1):
#                     m[bottom][i] = num
#                     num += 1
#                 bottom -= 1
#             if left <= right :
#                 for i in range(bottom , top -1 , -1):
#                     m[i][left] = num
#                     num += 1
#                 left += 1

#         return m
    

# print(gm(4))

        
# class Solution(object):
#     def minPathSum(self, grid):

#         # ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] ] 

#         top , left = 0 , 0
#         right , bottom = len(grid[0])  - 1 , len(grid) - 1
         
#         combined = 0

        
#         for i in range(left , right + 1):
#                 combined += grid[0][i]

#         top += 1

#         for i in range(top  , bottom + 1):
#                 combined += grid[i][right]

#         right -= 1

#         return combined
            


        
# r = Solution()
# print(r.minPathSum([[1,2,3],[1,2,6]]))


# class Solution(object):
#     def minPathSum(self, grid):


#         n =  len(grid) - 1
#         r , d = len(grid) , len(grid[0])
#         memo  = {}
        

        

#         def backtrack(i , j):

            

#             if i >= r or j >= d :
#                 return float('inf')
            
#             if i == r - 1 and j == d - 1 :
#                 return grid[i][j]
            
#             if (i , j) in memo :
#                 return memo [(i , j)]
            

                

#             right = backtrack(i , j + 1)
#             down  = backtrack(i + 1 , j)

#             memo[(i , j)] =  grid[i][j] + min(right , down) 


#             return memo[(i, j)]
    
#         return backtrack(0,0)
        
    
# r = Solution()
# print(r.minPathSum([[1,2,3],[1,2,4],[3,3,5]]))


                    
                
            
# def strpttn(n):
    
#     for i in range(n):
#         x = "*"
#         x = x * i
#         print(f'{x :<10}')
# strpttn(10)
    


# class Solution(object):
#     def sm(self, matrix, target):
#         n = len(matrix)

#         row = len(matrix)
#         col = len(matrix[0])

#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == target:
#                     return True

        
#         return False


# r = Solution()
# print(r.sm([[3]], 3))


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
        
#         ml1 = int("".join(map(str , l1)))
#         ml2 = int("".join(map(str , l2)))

#         ml = ml1 + ml2

#         mml = str(ml)
#         m = mml[::-1]

#         return [int(d) for d in m]

            
# r = Solution()
# print(r.addTwoNumbers([1,2,3],[4,8,8,0]))


# class Solution(object):
#     def la(self, heights):

#         stack = []
#         max_area = 0

#         heights.append(0)

#         for i in range(len(heights)):

#             while stack and heights[stack[-1]] > heights[i]:

#                 h = heights[stack.pop()]

#                 if stack:
#                     width = i - stack[-1] - 1
#                 else:
#                     width = i

#                 max_area = max(max_area, h * width)

#             stack.append(i)

#         return max_area


# r = Solution()
# print(r.la([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):

#         nums1[m:] = nums2[0:n]
#         nums1.sort()

        
#         return nums1

# r = Solution()
# print(r.merge([1,2,3,0,0,0],3,[2,5,6],3))



# from itertools import combinations
# class Solution(object):
#     def subsetsWithDup(self, nums):
#         n = len(nums)
#         nums.sort()
#         combos = set()
#         for i in range(n + 1):
#             for combo in combinations(nums,i) :
#                 combos.add(combo)
        
#         return [list(x) for x in combos]
# r = Solution()
# print(r.subsetsWithDup([1,2,2]))



# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
# import math
# class Solution(object):
#     def generate(self, numRows):
#         triangle = []

# for n in range(numRows):

#     row = []

#     for r in range(n + 1):

#         value = math.factorial(numRow) / ( math.factorial(i) * math.factorial(numRows - i))
#         row.append(value)

#     triangle.append(row)

# return triangle


import re

# text = "catsandog"
# words = ["cats","dog","sand","and","cat"]

# # Creates the pattern "apple|pen"
# pattern = "|".join(words) 

# # Finds all matches in order
# result = re.findall(pattern, text)

# print(result)


class Solution(object):
    def wordBreak(self, s, wordDict):
        all_com = "|".join(wordDict)
        result = re.findall(all_com , s)
        print(result)

        if result not in wordDict:
            return False

        return True
r = Solution()
print(r.wordBreak("applepenapple",["apple","pen"]))


import re

class Solution(object):
    def wordBreak(self, s, wordDict):
        # 1. Join words with '|' to mean "apple" OR "pen"
        # 2. Wrap in parentheses and add '*' so it can match multiple times
        # 3. Use '^' and '$' to ensure the ENTIRE string is matched perfectly
        pattern = "^(" + "|".join(wordDict) + ")*$"
        
        # re.match returns a match object if successful, or None if it fails
        if re.match(pattern, s):
            return True
            
        return False
