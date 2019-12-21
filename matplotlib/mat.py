#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Axes container
fig = plt.figure()
fig.suptitle('test', fontsize=16, fontweight='bold')

ax = fig.add_axes([0.1,0.5,0.8,0.5])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('test')
line = ax.plot(range(5))[0]
line.set_color('r')

plt.show()

# Axis container
plt.plot([1,2,3],[4,5,6])
axis=plt.gca().xaxis
axis.get_ticklocs()

axis.get_ticklabels()
axis.get_ticklines()
axis.get_ticklines(minor=True)
for label in axis.get_ticklabels():
    label.set_color('red')
    label.set_rotation(0)
    label.set_fontsize(16)
for lines in axis.get_ticklines():
    lines.set_color('green')
    lines.set_markersize(3)
    lines.set_markeredgewidth(2)
plt.show()


# plot()
# creat a figure object
plt.figure('Sin')
t = np.arange(0.0,4.0,0.1)
s = np.sin(np.pi*t)
plt.plot(t,s,'-go',label='sinx')

plt.legend() #Top right corner note
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
# plt.xlim(-1,3)  //range of label
# plt.ylim(-1.5,1.5)
plt.title('About as simple as it gets,folks')
plt.grid(True)

plt.show()

# subplot (even number)
for i, color in enumerate('rgbyck'):
    plt.subplot(321+i, facecolor = color)
plt.show()

# subplot (odd number)
def f(t):
    return np.exp(-t) * np.sin(2 * np.pi * t)
if __name__ == '__main__':
    t1 = np.arange(-5, 5, 0.1)
    t2 = np.arange(-5, 5, 0.2)
    plt.figure()
    plt.title('Three')
    plt.subplot(221)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'g--')
    plt.subplot(222)
    plt.plot(t2, np.cos(2 * np.pi * t2), 'g--')
    plt.subplot(212)
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.show()

# subplot()
x1=np.arange(0.0,5.0)
x2=np.linspace(0.0,2.0)  #(start,end,point(50))

y1=np.cos(2*np.pi*x1)*np.exp(x1)
y2=np.cos(2*np.pi*x2)

plt.subplot(221)
plt.plot(x1,y1,'-ro')
plt.title('A tale of 2 subplots')
plt.xlabel('Time [s]')
plt.ylabel('Damped oscillation')

plt.subplot(222)
plt.title('It is a empty figure')

plt.subplot(224)
plt.plot(x2,y2,'-go')
plt.xlabel('Time [s]')
plt.ylabel('Undamped')

plt.show()