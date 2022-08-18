#!/usr/bin/env python
# coding: utf-8

# Python是一门**动态类型**的语言

# ## Unpacking

# In[1]:


attrs = [1,['xi', -1]]
user_id, (username, score) = attrs


# In[2]:


print(user_id,username,score)


# dynamic unpacking : \*variables  **starred expressions** 可以完全代替手动切片赋值

# In[3]:


data = ['jiang','hu','xi','qi', 2049]
username, *huxiqi, year = data
print(username, huxiqi, year)


# In[4]:


username, huxiqi, year = data[0], data[1:-1], data[-1]
print(username, huxiqi, year)


# In[5]:


username, *_, score = data
username


# In[6]:


def magic_bubble_sort(numbers):
    j = len(numbers) - 1
    while j > 0 :
        for i in range(j):
            if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 1:
                numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
                continue
            elif (numbers[i+1] % 2 == numbers[i] % 2) and numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] == numbers[i+1],numbers[i]
                continue
        j -= 1
    return numbers
numbers = [23,32,1,3,4,19,20,2,4]
    


# In[7]:


magic_bubble_sort(numbers)


# In[8]:


def magic_bubble_sort(numbers):
    """有魔力的冒泡排序算法，默认所有的偶数比奇数大
    :param numbers: 需要排序的列表，函数会直接修改原始列表
    """
    stop_position = len(numbers) - 1
    while stop_position > 0 :
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i+1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            shoud_swap = False
            #交换位置的两个条件：
            #前面是偶数，后面是奇数
            #前面和后面同为奇数或偶数，但是前面比后面大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True
                
            if should_swap:
                numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
            stop_position -= 1
    return numbers
magic_bubble_sort(numbers)


# In[ ]:




