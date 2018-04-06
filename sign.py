from tkinter import *
from tkinter import messagebox
import requests
import re
from PIL import Image, ImageTk


def download():
    """"模拟浏览器请求"""
    startUrl = "http://www.uustv.com/"
    # 获取输入的信息
    name = entry.get()
    # 去空格
    name = name.strip()
    print(name)
    # isspace
    if name == "":
        messagebox.showinfo("提示", "请输入信息")
    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000'
        }
        result = requests.post(startUrl, data=data)
        result.encoding = 'utf-8'
        # 网站中的源代码
        html = result.text
        # 正则表达式
        reg = '<div class="tu">.*?<img src="(.*?)"/></div>'
        imagePath = re.findall(reg, html)[0]
        print(imagePath)
        # 获取完整的图片路劲
        imageUrl = startUrl + imagePath
        # print(imageUrl)
        # 获取图片内容
        response = requests.get(imageUrl).content
        # print(response)
        f = open("{}.gif".format(name), 'wb')
        f.write(response)

        bm = ImageTk.PhotoImage(file="{}.gif".format(name))
        label2 = Label(root, image=bm)
        label2.bm = bm
        label2.grid(row=2, columnspan=2)

# 创建窗口
root = Tk()

# 标题
root.title("签名设计")

# 窗口大小
root.geometry("600x300")

# 窗口位置
root.geometry("+400+180")

# 标签控件
label = Label(root, text="签名", font=("华文行楷", 20), fg="red")
# pack, grid, place
label.grid()

# 输入框
entry = Entry(root, font=("微软雅黑", 20))
entry.grid(row=0, column=1)

# 点击按钮
button = Button(root, text="设计签名", font=("微软雅黑", 20), command=download)
button.grid(row=1, column=0)

# 消息循环, 显示窗口
root.mainloop()
