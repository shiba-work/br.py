import tkinter as tk    #画面作成
import pyperclip

def btnBR_click():
    print("コピーする")
    str = pyperclip.paste()
    str_br = str.replace("\n","<br>\n")
    str_br1='\n'

    pyperclip.copy(str_br+str_br1)

#画面作成
MainGamen = tk.Tk()
MainGamen.geometry('250x150')
MainGamen.title('<BR>')
#クリップ<BR>ONモード
btnCopy = tk.Button(MainGamen,text="<br>に変換",font=("ＭＳ ゴシック", 16, "bold"),command=btnBR_click)
btnCopy.place(x=50, y=40)
MainGamen.attributes("-topmost", True)
MainGamen.mainloop() 