#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1

from typing import List

def allCombinationForces(n: int) -> List[str]:
    def generate_combinations(n, red_ct, blue_ct, curr_combination):
        if red_ct > n or blue_ct > n:
            return
        
        if len(curr_combination) == 2 * n:
            combination_list.append(curr_combination)
            return
        
        if red_ct < n:
            generate_combinations(n, red_ct + 1, blue_ct, curr_combination + "R")
        if blue_ct < red_ct:
            generate_combinations(n, red_ct, blue_ct + 1, curr_combination + "B")
    
    combination_list = []
    generate_combinations(n, 0, 0, "")
    return combination_list


# In[35]:


# Question 2

def josephus_plot(n: int, m: int) -> int:
    current_index = 0
    m = m - 1 
    soldiers_list = [i for i in range(1, n + 1)] 
    
    def eliminate_soldier(m, current_index):
        if len(soldiers_list) == 1:
            return soldiers_list[0]
        
        current_index = (current_index + m) % len(soldiers_list)
        soldiers_list.remove(soldiers_list[current_index]) 
        return eliminate_soldier(m , current_index)
    
    return eliminate_soldier(m, current_index)


# In[38]:


# Question 3

def shorterBuildings(heights):
    def mergesort(height_index_pairs, result):
        if len(height_index_pairs) > 1:
            mid = len(height_index_pairs) // 2
            left_half = height_index_pairs[:mid]
            right_half = height_index_pairs[mid:]
            
            mergesort(left_half, result)
            mergesort(right_half, result)
            
            i = j = k = 0
            while i<len(left_half) and j < len(right_half):
                if left_half[i][0] > right_half[j][0]:
                    result[left_half[i][1]] += len(right_half) - j
                    height_index_pairs[k] = left_half[i]
                    i += 1
                else:
                    height_index_pairs[k] = right_half[j]
                    j += 1
                k += 1
                
            while i < len(left_half):
                height_index_pairs[k] = left_half[i]
                k += 1
                i += 1

            while j < len(right_half):
                height_index_pairs[k] = right_half[j]
                k += 1
                j += 1
    
    result = [0] * len(heights)
    height_index_pairs = [(heights[i], i) for i in range(len(heights))]
    
    mergesort(height_index_pairs, result)
    
    return result
 


# In[28]:


# Question 4

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isHeightBalanced(root: TreeNode) -> bool:
    def height(root):
        if not root:
            return 0
        else:
            return 1 + max(height(root.left), height(root.right))
        
    if not root:
        return True
    else:
        left_subtree_H = height(root.left)
        right_subtree_H = height(root.right)
        diff = left_subtree_H - right_subtree_H
        if (diff > -2 and diff < 2):
            return True
        return False


# In[75]:


# Question 5

from copy import deepcopy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(preorder: list[int], inorder: list[int]) -> TreeNode:   
    def buildTree(preorder, inorder):
        if not inorder:  
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        
        root.left = buildTree(preorder, inorder[:root_index])
        root.right = buildTree(preorder, inorder[root_index + 1:])
        
        return root
    
    preorder = deepcopy(preorder)
    return buildTree(preorder, inorder)


# In[ ]:


# Question 6

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def palindromic_paths(root: TreeNode) -> int:
    
    def palindrome(path):
        # Check if the path can form a palindrome
        odd_count = sum(path.count(number) % 2 for number in set(path))
        return odd_count <= 1

    def explore(node, current_path, valid_paths):
        if not node:
            return

        current_path.append(node.val)

        # If it's a leaf node, check if the path forms a palindrome
        if not node.left and not node.right:
            if palindrome(current_path):
                valid_paths.append(list(current_path))
            current_path.pop()
            return
        
        # Recursively explore left and right children
        explore(node.left, current_path, valid_paths)
        explore(node.right, current_path, valid_paths)
        current_path.pop()
    
    all_paths = []
    current_path = []
    
    explore(root, current_path, all_paths)

    return len(all_paths)
    
# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(3, TreeNode(3), TreeNode(1))
root1.right = TreeNode(1, None, TreeNode(1))

# Example 2
root2 = TreeNode(2)
root2.left = TreeNode(1, TreeNode(1, TreeNode(3, None, TreeNode(1))), TreeNode(1))
root2.right = TreeNode(1)

print(palindromic_paths(root1))  # Output: 2
print(palindromic_paths(root2))  # Output: 1


# In[36]:


# Question 7

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def minimumTime(root, start: int) -> int:
    def custom(root, ct, v):
        if not root:
            return ct, v
        ct += 1
        if root.val == start:
            v = ct
            ct = 0
        x, a = custom(root.left, ct, v)
        y, b = custom(root.right, ct, v)
        if a != b:
            if a > b:
                return max(y + a - ct - ct, x), a
            else:
                return max(x + b - ct - ct, y), b
        else:
            return max(x, y), v

    x,a=custom(root,-1,0)
    return x        

