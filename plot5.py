import matplotlib.pyplot as plt
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]
plt.xlabel('X - axis') 
plt.ylabel('Y - axis')
plt.plot(x1,y1, color='blue', linewidth=3, label='Line1- dotted',linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth=5, label='Line2- deshed',linestyle='dashed')
plt.title("Plot with two or more lines with different styles")
plt.legend()
plt.show()