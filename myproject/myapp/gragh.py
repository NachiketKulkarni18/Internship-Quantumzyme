from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 18}

plt.rc('font', **font)

figure(num=None, figsize=(14, 7))

t_1 = [854, 1185, 1860, 377, 352]
t_2 = [258005, 385351, 800054, 194111, 99980]
t_3 = [26794, 39706, 78924, 18066, 8666]
t_4 = [1491, 2032, 4358, 765, 469]


Labels=['test-1', 'test-2', 'test-3',  'test-4', 'test-5']
y_pos=np.arange(len(Labels))
plt.bar(y_pos + 0, t_1,width=0.2, color = 'navy' , label='test label-1')
plt.bar(y_pos + 0.2,t_2, width=0.2,color = 'skyblue',label = 'test label-2')
plt.bar(y_pos + 0.4, t_3,width=0.2, color = 'darkcyan' , label='test label-3')
plt.bar(y_pos + 0.6, t_4,width=0.2, color = 'black' , label='test label-4')

plt.xticks(y_pos, Labels)
plt.yscale('log')
plt.legend(('test label-1','test label-2', 'test label-3', 'test label-4'))
plt.ylabel('Number in log10 scale')
plt.xlabel('Different X-Axis labels')
plt.title("Put a title here")
plt.show()