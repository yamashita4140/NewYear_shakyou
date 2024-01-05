# Pythonの教科書 2章6
# 繰り返し for文
# 直線を繰り返し描画

from tkinter import *

w = Canvas(Tk(), width=900, height=400)
w.pack()

for i in range(300):
    x = i * 5
    w.create_line(x, 0, x, 400, fill="#FFFFFF")

mainloop()
