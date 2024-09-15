#!/usr/bin/env python
# coding: utf-8

# In[324]:


import copy

def maxWaterStorage(pillarsHeight: list[int]) -> int:
    area = []
    size = len(pillarsHeight)
    left = 0; right = size -1

    while left < right:
            minimum = min(pillarsHeight[left], pillarsHeight[right])
            area.append(minimum*(right-left))
            if pillarsHeight[left] < pillarsHeight[right]:
                left += 1
            elif pillarsHeight[left] > pillarsHeight[right]: 
                right -= 1
            else:
                left += 1; right -= 1
            # print(j-i)
    return max(area)
    pass


def bollywoodCharm(scripts: list[int],expectedCharm: int)->list[int]:
    # Expects index1 and index2 as a list [idx1,idx2]
    idx1 = 0; idx2 = len(scripts)-1; flag = 0; total = 0
    while(flag == 0):
        print(idx1,idx2,total)
        total = scripts[idx1] + scripts[idx2]
        if total > expectedCharm:
            idx2 -= 1
        elif total < expectedCharm:
            idx1 += 1
        else:
            flag = 1
    return [idx1,idx2]



def cheapestWarhead(valuations: list[int])->int:
    idx1 = 0; idx2 = 1; launch = 0; buy = 0; maxdamage = 0
    while(idx1!=len(valuations)-1 and idx2!=len(valuations)):
        diff = valuations[idx2] - valuations[idx1]
        if diff <= 0:
            idx1+=1; idx2+=1
        elif diff > 0:
            if idx2!=len(valuations)-1: 
                idx2+=1
            else:
                idx1+=1
            if diff > maxdamage:
                maxdamage = diff
            
    return maxdamage

# The below is O(n^2)

# def shiftingCharacters(inputStr: str, moves: list[int]) -> str:
    
#     def modify(character,pos):
#         asci = ord(character) + pos
#         if asci > ord("z"):
#             asci -= 26
#         return chr(asci)
        
#     for i in range(len(moves)):
#         subjects = list(inputStr[0:i+1])
#         final_string = [modify(j,moves[i]) for j in subjects]
#         final_string = ''.join(final_string)
#         inputStr = inputStr.replace(inputStr[0:i+1], final_string, 1)
        
#     return final_string



# The below is O(n)

def shiftingCharacters(inputStr: str, moves: list[int]) -> str:
    def modify(character,pos):
        asci = ord(character) + pos%26
        if asci <= ord("z"):
            return chr(asci)
        else:
            return chr(asci-26)
        
        
    size = len(moves)
    final_string = []
    for i in range(size):
        letter = modify(inputStr[i],sum(moves[i::]))
        final_string.append(letter)
    final_string = ''.join(final_string)        
    return final_string       
        
def specialString(n: int) -> int:
    def countones(seq):
        count = 0
        for i in seq:
            if i == 1:
                count+=1
        return count
        
    s = [1,2,2]
    if n>3:
        k=2
        while(len(s)<n):
            if s[-1] == 1:
                s += [2] * s[k]
            else:
                s += [1] * s[k]
            k+=1 
    s = s[0:n]
    print(s)
    return countones(s)        
    pass

def checkIsGeneDerived(G1: str,G2: str)->bool:
# Expects a boolean indicating if G1's variation present in G2
    G1_dict = {e:G1.count(e) for e in G1}
    G1_copy = copy.copy(G1_dict)
    G1_size = len(G1)
    print(G1_dict)

    for i in range(len(G2)):
        if G1_dict.get(G2[i],-1) >= 0:
            G1_dict[G2[i]] -= 1
            if sum(G1_dict.values()) == 0:
                return True
        else:
            G1_dict = copy.copy(G1_copy)
    return False

class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

def cycle_buster(head):
    p1_fast = head
    p2_slow = head
    while p1_fast != None and p2_slow != None and p1_fast.next != None:
        p1_fast = p1_fast.next.next
        p2_slow = p2_slow.next
        if p1_fast == p2_slow:
            p1_fast.next = None
    return head

