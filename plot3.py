import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]
plt.plot(x,y,label='First line')
x2 = [1,2,3]
y2 = [10,11,14]
plt.plot(x2,y2,label='Second line')
plt.xlabel('Plot number')
plt.ylabel('Important variables')
plt.title('New Graph')
plt.legend()
plt.show()