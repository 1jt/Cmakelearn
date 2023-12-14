import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# from matplotlib.pyplot import MultipleLocato
import numpy as np

# plt.figure(figsize=(20, 10), dpi=100)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

fig, ax = plt.subplots()
plt.xlabel("lmax", fontsize=13)

plt.ylabel("通信开销", fontsize=13)
#ax.set_yscale("log")

#plt.ylim(1.4, 4.3)
plt.ylim(0, 13000)


# ax.set_yscale("log")
# ax.set_ylim(1e1, 1e7)

x = ['$2^{4}$', '$2^{5}$', '$2^{6}$', '$2^{7}$', '$2^{8}$']
# x1=[pow(2,i) for i in range(10,20,2)]


# CVC
y5 = [191,292,542,803,2045]


plt.plot(x, y5, marker = 'o', color = '#FF6549', label = '$DVH$')

# [KSS+16]-ACC
y1 = [621,971,1684,3203,6061]


# plt.plot(x1 ,y1, marker = 'o', label = '[KSS+16]-ACC') 
plt.plot(x, y1, marker = '^', color = '#3962E0', label = '$VH-DSSE$')

# [WTS+21]
y2 = [11354,11562,11684,11976,12459]
#y2 = []

plt.plot(x, y2, marker = 'p', color = '#68D968', label = '$2ch_{FB}$')

'''
# VDS1
y3 = [256, 256, 256, 256, 256, 256]
plt.plot(x, y3, marker = '^', color = 'tomato', label = '$\mathregular{VDS_1}$')

# VDS2
y4 = [512, 512, 512, 512, 512, 512] 
plt.plot(x, y4, marker = '*',color = 'royalblue',  label = '$\mathregular{VDS_2}$')
'''

plt.legend(loc='upper left')
plt.grid(linestyle = '--', linewidth = 0.5)
# # plt.xticks(x)
plt.savefig('VH_DSSE_S.pdf')
plt.close()
