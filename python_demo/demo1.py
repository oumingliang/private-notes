from tkinter import *
top = Tk()

def clicked():			# 定义命令函数
    print("I'm clicked!")

btn = Button(text="click me!",command=clicked)
btn.pack()		# 打包控件（相当于实例化）

def callback(event):
    print(event.x,event.y)

top.bind("<Button-1>",callback)		# 为控件绑定事件，包括按键和事件函数
# 按键的格式为：<Alt-F4>

mainloop()		# 主循环（不直接退出）