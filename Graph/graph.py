import matplotlib.pyplot as plt
import numpy as np

# Insertion Sort

with open('InsertionSortResults.txt') as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y1 = [row.split(',')[1] for row in data]
y2 = [row.split(',')[2] for row in data]

x.pop(0)
y1.pop(0)
y2.pop(0)

x = [i for i in x]
y1 = [float(i) for i in y1]
y2 = [float(i) for i in y2]

plt.plot(x, y1, label='Process')
plt.plot(x, y2, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Insertion Sort')
plt.legend()
plt.show()

# Merge Sort

with open('MergeSortResults.txt') as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y1 = [row.split(',')[1] for row in data]
y2 = [row.split(',')[2] for row in data]

x.pop(0)
y1.pop(0)
y2.pop(0)

x = [i for i in x]
y1 = [float(i) for i in y1]
y2 = [float(i) for i in y2]

plt.plot(x, y1, label='Process')
plt.plot(x, y2, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Merge Sort')
plt.legend()
plt.show()

# Quick Sort

with open('QuickSortResults.txt') as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y1 = [row.split(',')[1] for row in data]
y2 = [row.split(',')[2] for row in data]

x.pop(0)
y1.pop(0)
y2.pop(0)

x = [i for i in x]
y1 = [float(i) for i in y1]
y2 = [float(i) for i in y2]

plt.plot(x, y1, label='Process')
plt.plot(x, y2, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Quick Sort')
plt.legend()
plt.show()

# Radix Sort

with open('RadixSortResults.txt') as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y1 = [row.split(',')[1] for row in data]
y2 = [row.split(',')[2] for row in data]

x.pop(0)
y1.pop(0)
y2.pop(0)

x = [i for i in x]
y1 = [float(i) for i in y1]
y2 = [float(i) for i in y2]

plt.plot(x, y1, label='Process')
plt.plot(x, y2, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Radix Sort')
plt.legend()
plt.show()

# Bubble Sort

with open('BubbleSortResults.txt') as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y1 = [row.split(',')[1] for row in data]
y2 = [row.split(',')[2] for row in data]

x.pop(0)
y1.pop(0)
y2.pop(0)

x = [i for i in x]
y1 = [float(i) for i in y1]
y2 = [float(i) for i in y2]

plt.plot(x, y1, label='Process')
plt.plot(x, y2, label='Threads')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Bubble Sort')
plt.legend()
plt.show()