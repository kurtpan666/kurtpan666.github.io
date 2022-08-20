#!/usr/bin/env python
# coding: utf-8

# # Python多项式处理基础
# [NumPy](https://numpy.org/) 在[Python](https://www.python.org/) 生态中的地位无需再多言，完全可以说「没有NumPy就没有Python在大数据和机器学习领域的流行」。
# 在NumPy 1.4前，对多项式的操作使用的包是 [numpy.poly1d](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d) ； NumPy 1.4 后（当下版本1.23），推荐使用更方便易用的包[numpy.polynomial](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#module-numpy.polynomial)。
# 
# 引用方法如下：

# In[12]:


from numpy.polynomial import Polynomial
p = Polynomial([3, 2, 1])
print(p)
p


# 具有下述属性：

# In[8]:


# 系数
p.coef


# In[9]:


# 定义域 : 默认为[-1,1]
p.domain


# In[10]:


# 窗口： 默认为[-1,1]
p.window


# ## 基本代数算术操作
# 加/减/乘/乘方

# In[13]:


p + p


# In[14]:


p - p


# In[15]:


p * p


# In[16]:


p ** 2


# 除法

# In[18]:


p // Polynomial([-1, 1])


# In[28]:


p / 2


# 余数

# In[19]:


p % Polynomial([-1, 1])


# 带余除法

# In[21]:


quo, rem = divmod(p, Polynomial([-1, 1]))
print(quo,rem)


# 求值

# In[22]:


x = np.arange(5)
p(x)


# In[23]:


x = np.arange(6).reshape(3,2)
p(x)


# 代换（将x代换为相应值）

# In[24]:


p(p)


# 求根

# In[25]:


p.roots()


# 直接用list表示多项式

# In[26]:


p + [1,2,3]


# In[27]:


[1,2,3] * p


# ## 微积分操作
# 下界-1，积分常数2，二重积分

# In[31]:


p.integ(2,lbnd=-1,k=2)


# 二阶导数

# In[32]:


p.deriv(2)


# ## 其他多项式构造方法
# 从根构造

# In[34]:


p = Polynomial.fromroots([1, 2, 3])
p


# In[35]:


Polynomial.basis(3)


# ## 插值

# In[37]:


rng = np.random.default_rng()
x = np.arange(10)
y = np.arange(10) + rng.standard_normal(10)


# In[41]:


p_fitted = Polynomial.fit(x, y, deg=2)
p_fitted


# ## 参考
# - [Using the Convenience Classes](https://numpy.org/doc/stable/reference/routines.polynomials.classes.html)
# - [numpy.polynomial package](https://numpy.org/doc/stable/reference/routines.polynomials.package.html#module-numpy.polynomial)

# In[ ]:




