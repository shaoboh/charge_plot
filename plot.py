import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(7,4),facecolor="gray")
fig = plt.figure(figsize=(7,4))
a1 = fig.add_axes([0,0,1,1])
# plt.grid()  # 生成网格
#设置y轴
a1.set_ylim(0,32)
#设置x轴
a1.set_xlim(0,120)
sample_data = pd.read_csv("nature.csv",encoding='gbk')
x,y = sample_data['volt'].values, sample_data['current'].values
plt.plot(range(len(x)),x,color="darkred")
plt.plot(range(len(y)),y,color="green")
plt.axhline(10, color='r', linestyle='--',label="a1")
plt.axhline(22.5, color='r', linestyle='-.',label="a2")
plt.axhline(25, color='r', linestyle='-.',label="a3")

plt.vlines(10, 0,35,color='gray', linestyle='--',label="a1")
plt.vlines(50, 0,35,color='gray', linestyle='--',label="a1")
plt.vlines(80, 0,35,color='gray', linestyle='--',label="a1")
plt.vlines(100, 0,35,color='gray', linestyle='--',label="a1")

# plt.axis('off')
plt.text(3,4,'Pre-charge current = charge termination current',family = "fantasy", color = "g", style = "italic", weight = "light",\
         bbox = dict(facecolor = "g", alpha = 0.2))
plt.text(10,21,'Regulation current',family = "fantasy", color = "g", style = "italic", weight = "light",\
         bbox = dict(facecolor = "g", alpha = 0.2))
plt.text(51,26,'Battery voltage',family = "fantasy", color = "r", style = "italic", weight = "light",\
         bbox = dict(facecolor = "r", alpha = 0.2))
plt.text(70,12,'Battery current',family = "fantasy", color = "g", style = "italic", weight = "light",\
         bbox = dict(facecolor = "g", alpha = 0.2))

#mode 
# plt.text(8,0,'Pre-charge mode',family = "fantasy", color = "b", style = "italic", weight = "light",\
#          bbox = dict(facecolor = "b", alpha = 0.01),rotation=90)
# plt.text(48,0,'Constant current regulation mode',family = "fantasy", color = "b", style = "italic", weight = "light",\
#          bbox = dict(facecolor = "b", alpha = 0.01),rotation=90)
# plt.text(78,0,'Constant voltage regulation mode',family = "fantasy", color = "b", style = "italic", weight = "light",\
#          bbox = dict(facecolor = "b", alpha = 0.01),rotation=90)
# plt.text(98,0,'Charge termination',family = "fantasy", color = "b", style = "italic", weight = "light",\
#          bbox = dict(facecolor = "b", alpha = 0.01),rotation=90)
# plt.text(118,0,'Re-charge mode',family = "fantasy", color = "b", style = "italic", weight = "light",\
#          bbox = dict(facecolor = "b", alpha = 0.01),rotation=90)

# plt.annotate('annotate', xy=(3, 25))
# 使用annotate函数绘制注解，添加指示箭头
plt.annotate('Regulation voltage', xy=(0, 25), xytext=(1,26),
            arrowprops=dict(arrowstyle='->',facecolor='orange')
            )
plt.annotate('Recharge voltage', xy=(0, 22.5), xytext=(1,23.5),
            arrowprops=dict(arrowstyle='->',facecolor='y')
            )
plt.annotate('Pre-charge threshold voltage', xy=(0, 10), xytext=(1,11),
            arrowprops=dict(arrowstyle='->',facecolor='y')
            )
# plt.xticks([])
# plt.yticks([])
plt.title("Charging pictures at different stages", fontsize=15, pad=20)
# plt.save("charge.png")
