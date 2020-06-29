import tkinter as tk
from PIL import Image, ImageTk

class mainWindow():
    def __init__(self,root=None):
        self.root=root
        self.root.title("複数frame制御")
        #self.root.geometry("500x600")
        #self.root.propagate(False)

        #フレーム一つ目
        self.frame1 = tk.LabelFrame(self.root,text="menu")
        self.frame1.grid(column=0,row=0,padx=5,sticky=tk.W + tk.E)
        
        #ボタンを作成
        button1 = tk.Button(self.frame1, text="自動ログイン画面",command=self.buttonClick1)
        #button1.pack(side="left")
        button1.grid(column=0,row=0,padx=5,pady=5)
        # ボタンを作成
        button2 = tk.Button(self.frame1, text="URL登録ぅ")
        #button2.pack(side="left")
        button2.grid(column=1,row=0,padx=5,pady=5)
        # ボタンを作成
        button3 = tk.Button(self.frame1,text="大鯨ちゃん！！" )
        #button3.pack(side="right")
        button3.grid(column=2,row=0,padx=5,pady=5,sticky=tk.W + tk.E)
        self.frame1.columnconfigure(2, weight=1)
        # ボタンを作成
        button4 = tk.Button(self.frame1, text="終了",command=self.button_quit)
        # button4.pack(side="left",)
        button4.grid(column=3,row=0,padx=5,pady=5,sticky=tk.E)
        
        # 画像を表示するための準備
        img1 = Image.open('taigei.png')
        img1 = ImageTk.PhotoImage(img1)
        
        # 画像を表示するためのキャンバスの作成（黒で表示）
        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.grid(column=0,row=1) # 左上の座標を指定
        # キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
        canvas.photo1=img1
        canvas.create_image(0, 0,anchor="nw", image = canvas.photo1)
    
    def buttonClick1(self):
        self.window=(tk.Toplevel())
        SubWindow(self.window)
        
    def button_quit(self):
        self.root.destroy()
    
class SubWindow():
  import AutoLogin_Site as site
  def __init__(self,root=None):
    
    self.root=root
    self.root.title("自動ログイン")   
    #self.root.geometry("300x300") 
    
    #フレーム一つ目
    self.frame1 = tk.LabelFrame(self.root,text="menu")
    self.frame1.grid(column=0,row=0,padx=5,pady=5,sticky=tk.W + tk.E)
    
    # label
    label= tk.Label(self.frame1,text="ログインしたいサイトを選んでください")
    label.grid(column=0,row=0, padx=5, pady=5)
        
    # 終了
    # button0= tk.Button(self.frame1,text="終了")
    # button0.grid(column=1,row=0, padx=5, pady=5,sticky=tk.E)

    button1 = tk.Button(self.frame1,text="Eneos電気",command=self.site.Eneos_elec,width=20)
    button1.grid(column=0,row=1, padx=5, pady=5)
    
    button2 = tk.Button(self.frame1,text="Eneosガス",command=self.site.Eneos_gas,width=20)
    button2.grid(column=1,row=1, padx=5, pady=5)     
    
    def button_quit(self):
        self.root.destroy()
         
def main():
    win=tk.Tk()
    mainWindow(win)
    win.mainloop()
    
if __name__ =='__main__':
    main()