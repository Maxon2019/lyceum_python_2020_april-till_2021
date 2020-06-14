import matplotlib as plt

product = 'Mobile', 'Laptop', 'Desktop', 'iPhone'
quantity = [45, 30, 20, 5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(quantity, labels=product, colors=colors,
        autopct='% 1.1f%', shadow=True, startangle=140)

plt.show()
