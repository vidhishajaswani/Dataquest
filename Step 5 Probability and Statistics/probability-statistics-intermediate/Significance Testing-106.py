## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a=np.mean(weight_lost_a)
mean_group_b=np.mean(weight_lost_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference=mean_group_b-mean_group_a

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)
mean_differences=[]
for i in range(1000):
    group_a=[]
    group_b=[]
    for each in all_values:
        val=np.random.rand()
        if val>=.5:
            group_a.append(each)
        else:
            group_b.append(each)
    iteration_mean_difference=numpy.mean(group_b)-numpy.mean(group_a)
    mean_differences.append(iteration_mean_difference)
plt.hist(mean_differences)

## 7. Dictionary representation of a distribution ##

sampling_distribution ={}
for each in mean_differences:
    if sampling_distribution.get(each,False):
        val=sampling_distribution.get(each)
        inc=val+1
        sampling_distribution[each]=inc
    else:
        sampling_distribution[each]=1
        

## 8. P value ##

frequencies=[]
for each in sampling_distribution:
    if each>=2.52:
        frequencies.append(sampling_distribution[each])
        
s=np.sum(frequencies)
p_value=s/1000