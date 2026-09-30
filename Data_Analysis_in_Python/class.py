# import numpy as np
"""
# a1 = np.array([1, 2, 3,4,5])
# a2 = np.array([6, 7, 8,9,10]) 
# np.concat( arr_1, 3)
# print(arr_1)
# print(arr_1)     
# reshaped_arr = arr_1.reshape(2, 3)
# print(reshaped_arr)
# np.insert(arr_1,5,25)
# print(arr_1)
# np.append(arr_1, [[1,2],[3,4]])
# print(arr_1)
# arr_2 = np.array([[7,8,9,10,11,12]])
# np.concat( arr_2, 3)
# print(arr_2)
# print("np.version:", np.__version__)
# value = 5
# result = a1 *a2    
# print(result) 
#// defination : vectorazation is the process of converting operations that  normally 
#  operate on a single
# value at a time to operate on a set of values (vector) at one time.
"""

# logical operations on arrays:
"""
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print(a == b)  
"""
"""
#matrix operations using vectorization:
import numpy as np
a1 = np.array([[1, 2, 3]])
a2 = np.array([[4, 5, 6]])
result = np.dot(a1, a2.T)  
print(result)
"""
"""
#applying custom function on arrays using vectorization:
def custom_function(x):
    return x ** 2 + 2 * x + 1

result = np.vectorize(custom_function)(a1)
a1 = np.array([1, 2, 3, 4, 5])
print(result)
"""
"""
a1 = np.array([1, 2, 3, 4, 5])
result1 = np.sum(a1)
result2 = np.mean(a1)
result3 = np.max(a1)
result4  = np.min(a1)
print(result1)
print(result2)  
print(result3)
print(result4)
"""
#  identifing missing values in  stractured arrays involving -
# nan and other placeholder within filed of the array. :
# import numpy as np 
'''
dtype = [[('name','U20'),('age','f8')],[('height','f6'),('weight','f7')]]
data=[('ram',np.nan)]
structured_array = np.array(data , dtype)
nan_mask=np.isnan(structured_array['age'])
print(nan_mask)
'''
'''

# counting missing values in structured arrays: 
arr =([1,2,np.nan,4,np.nan,],[np.nan,6,7,8,9])
nan_mask=np.isnan(arr)
count_nan = np.sum(nan_mask)
print( count_nan)
'''
# record array in numpy
'''
import numpy as np
structured_array = np.array([('ram', 25), ('sohan', 30)])
record_array = structured_array.view(np.recarray)
print(record_array)
print(record_array.name)
'''
# creating a record array directly:
# import numpy as np
# structured_array_costum = np.recarray([('ram', 25), ('sohan', 30)], dtype=[('name', 'U10')])
# structured_array_costum[0]=('ram',25)
# structured_array_costum[1]=('sohan',30)
# print(structured_array_costum)

'''
assigning values to fields in a record array:

import numpy as np
structured_array_costum = np.recarray((2,) ,dtype=[('name', 'U10'), ('age', 'i4')])
structured_array_costum[0]=('ram',25)
structured_array_costum[1]=('sohan',30)
print(structured_array_costum)
'''
# experiment number 6  write a program to understand the use of numpy structured arrays and tp print mark sheet of 5 students.

# stacking record array  :
# import numpy as np
'''
# dtype = [[('name','U20'),('age','f8')],[('height','f6'),('weight','f7')]]
# data1=np.array([('ram', 25), ('sohan', 30)])
# data2=np.array([('abhinav', 25), ('manvendra', 30)] )
# structured_array1=np.array(data1,dtype).view(np.recarray)
# structured_array2=np.array(data2,dtype).view(np.recarray)
# stack_array = np.stack((structured_array1),(structured_array2))
'''
import pandas as pd
import numpy as np
result=pd.Series(5,index = ["a","b","c","d"])
print(result)
print("hello1")



                            
                            

