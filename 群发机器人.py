# 群发机器人
# 2023年3月
import time
import socket
import pyinputplus as pyip  # 多行输入用
import requests

print("欢迎访问群发机器人")

# 企业微信机器人webhook地址（注意保密，请勿泄漏）
# url = "自行替换自行替换自行替换自行替换" # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxx
url = input('请输入webhook地址: ')

# 检测是否连网
def check_network():
    while True:
        try:
            s = socket.create_connection(("www.bilibili.com", 80), timeout=5)
            s.close()
            print("网络已连接")
            return True
        except Exception:
            print("请检查网络", end='\r')
            time.sleep(3)
            continue

# 选择图片路径
def select_file():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print("file_path", file_path)
    return file_path

check_network()  # 检测是否连网

msgtype_id = input("请输入消息类型？文本(1)、markdown(2)、图片(3)\n")
while msgtype_id not in ['1', '2', '3']:
    msgtype_id = input("消息类型错误，请重新输入：\n文本(1)、markdown(2)、图片(3)\n")
if msgtype_id == "1":
    msgtype = "text"
elif msgtype_id == "2":
    msgtype = "markdown"
    print("\n")
    print("标题：# 标题一 ## 标题二 ### 标题三")
    print("加粗：**bold**")
    print("链接：[这是一个链接](https://www.baidu.com/)")
    print("代码：`code`")
    print("引用：> 引用文字")
    print("\n")
elif msgtype_id == "3":
    msgtype = "image"
else:
    print("其他错误！")

while 1:
    if (msgtype == "text" or msgtype == "markdown"):
        # 读取多行文本（开始）
        line = input("请输入文本（支持多行文本，以“#”结束）：\n")
        str1 = ""
        # 结束符号
        while line != "#":
            str1 += line + "\n"
            line = input()
        msg_content = str1
        # 读取多行文本（结束）
        payload = {
            "msgtype": msgtype,
            "text": {
                "content": msg_content
            },
            "markdown": {
                "content": msg_content
            }
        }
        if (msg_content != ""):
            response = requests.post(url, json=payload)
            print(response.text)

    elif (msgtype == "image"):
        import base64
        import hashlib

        file_path = ""
        file_path = select_file()  # 选择图片路径
        if file_path:
            # 获取图片的base64、md5值
            with open(file_path, 'rb') as f:
                img_data = f.read()
                img_base64 = base64.b64encode(img_data).decode('utf-8')
                img_md5 = hashlib.md5(img_data).hexdigest()
            payload = {
                "msgtype": msgtype,
                "image": {
                    "base64": img_base64,
                    "md5": img_md5,
                }
                # 成功示例：
                # "msgtype": "image",
                # "image": {
                #     "base64": "",
                #     "md5": "1bf0d144aa88eee8e49462fd2b644b06"
                # }
            }
            response = requests.post(url, json=payload)
            print(response.text)

# 错误代码：
# 93000：机器人webhookurl不合法或者机器人已经被移除出群
