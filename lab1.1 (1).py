import numpy as np
import math
import matplotlib.pyplot as plt

Ox = float(input("Enter the x сoordinate of circle center\n"))
Oy = float(input("Enter the y сoordinate of circle center\n"))
R = float(input("Enter the radius of circle\n"))

Ax = float(input("Enter the x сoordinate of the starting point\n"))
Ay = float(input("Enter the y сoordinate of the starting point\n"))

distance = math.sqrt((Ax - Ox) ** 2 + (Ay - Oy) ** 2)

while distance < R:
    Ax = float(input("Wrong input! Point A is within the circle\nEnter the x сoordinate of the starting point\n"))
    Ay = float(input("Enter the y сoordinate of the starting point\n"))
    distance = math.sqrt((Ax - Ox) ** 2 + (Ay - Oy) ** 2)

N = int(input("Enter the number of recurrences\n"))

fig, ax = plt.subplots()

x_min = min(Ox - 2 * R, Ax) - R
x_max = max(Ox + 2 *  R, Ax) + R
y_min = min(Oy - 2 *  R, Ay) - R
y_max = max(Oy + 2 *  R, Ay) + R

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

ax.set_aspect('equal')

ax.plot(Ax, Ay, 'bo')
ax.text(Ax + 0.2, Ay + 0.2, f"A", fontsize=12, color='blue')

for i in range(N):
    AO = math.sqrt((Ax - Ox) ** 2 + (Ay - Oy) ** 2)#обчислюємо довжину від центру кола до довільної точки
    AP = math.hypot(AO, R)
    th = math.acos(R / AP)# визначення кута між ОА та AP
    d = math.atan2(Ay - Oy, Ax - Ox) #визначаємо напрямок від О до А
    d1 = d + th

    Tx = Ox + R * math.cos(d1)#переводимо з полярних координатів в декартові
    Ty = Oy + R * math.sin(d1)

    Bx = 2 * Tx - Ax#тобчислення розсташування точки В
    By = 2 * Ty - Ay

    ax.plot(Tx, Ty, 'bo')
    ax.text(Tx + 0.2, Ty + 0.2, f"T{i+1}", fontsize=12, color='blue')

    ax.plot(Bx, By, 'bo')
    ax.text(Bx + 0.2, By + 0.2, f"P{i+1}", fontsize=12, color='blue')

    ax.plot([Ax, Bx], [Ay, By], 'r-')

    Ax, Ay = Bx, By

theta = np.linspace(0, 2 * np.pi, 360)
x = Ox + R * np.cos(theta)
y = Oy + R * np.sin(theta)



ax.plot(x, y)
plt.grid()
plt.show()