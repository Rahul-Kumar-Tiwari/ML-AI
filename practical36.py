import matplotlib.pyplot as plt
labels='s1','s2','s3'
sections=[30,50,20]
colors=['c','g','y']

plt.pie(sections,labels=labels,colors=colors,
        startangle=45
        ,explode=(0,0,0.1),
        autopct='%1.2f%%')

plt.title("Pie Chart Example")
plt.show()