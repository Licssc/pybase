import base64
import tkinter as tk
from tkinter import messagebox

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        output_text.configure(state='normal')
        encoded_text = base64.b64encode(text.encode()).decode()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encoded_text)
        output_text.configure(state='disabled')
    else:
        messagebox.showwarning("警告", "请输入要加密的文本！")

def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        try:
            output_text.configure(state='normal')
            decoded_text = base64.b64decode(text.encode()).decode()
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, decoded_text)
            output_text.configure(state='disabled')
        except:
            messagebox.showerror("错误", "解密失败！请输入有效的Base64编码文本。")
    else:
        messagebox.showwarning("警告", "请输入要解密的文本！")

def copy_output():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("提示", "已复制解密后的内容到剪贴板！")
    else:
        messagebox.showwarning("警告", "没有解密后的内容可供复制！")

# 创建主窗口
root = tk.Tk()
root.title("Base64加密解密系统")
root.geometry("400x300")

# 创建输入文本框
input_text = tk.Text(root, height=5)
input_text.pack(pady=10)

# 创建加密按钮
encrypt_button = tk.Button(root, text="加密", command=encrypt)
encrypt_button.pack()

# 创建解密按钮
decrypt_button = tk.Button(root, text="解密", command=decrypt)
decrypt_button.pack(pady=10)

# 创建输出文本框
output_text = tk.Text(root, height=5,state='disabled')
output_text.pack()

# 创建复制按钮
copy_button = tk.Button(root, text="复制解密后内容", command=copy_output)
copy_button.pack(pady=10)

# 运行主循环
root.mainloop()

