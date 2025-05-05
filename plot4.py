import matplotlib.pyplot as plt

Unemployment_Rate = [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2]
Stock_Index_Price = [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
plt.scatter(Unemployment_Rate, Stock_Index_Price, color='green')
plt.title('Unemployment_Rate Vs Stock_Index_Price', fontsize=14)
plt.xlabel('Unemployment_Rate', fontsize=14)
plt.ylabel('Stock_Index_Price', fontsize=14)
plt.grid(True)
plt.show()
