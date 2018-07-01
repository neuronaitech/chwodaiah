# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:06:14 2018

@author: nandavari
"""

# floor, ceiling and truncate values
import numpy as np
p = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 2.8, 3.0])
print(p)
print("Floor values of the above array elements:")
print(np.floor(p))
print("Ceil values of the above array elements:")
print(np.ceil(p))
print("Truncated values of the above array elements:")
print(np.trunc(p))



#subtract the mean of each row of a matrix.
import numpy as np
k=np.matrix([[5,7],[6,9]])
n=k-k.mean(axis=1)
print(k)
print(n)





#three elements that sum to zero
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


#matrix mulitiplication using two matrix
import numpy as np
p = np.array([1+2j,3+4j]) #first array
print(p)
q= np.array([5+6j,7+8j])#second array
print(q)
w = np.vdot(p, q)
print(w)

