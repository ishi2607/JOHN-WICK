import pyautogui
# import tkinter as tk1
from tkinter.filedialog import *


# root=tk1.Tk()

# canvas5=tk1.Canvas(root, width=300, height=300)
# canvas5.pack()


def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path= asksaveasfilename()
    myscreenshot.save(save_path+"_ss.png")
    


# myButton=tk1.Button(text="Screenshot", command=takeScreenshot,font=10)
# canvas5.create_window(150,150,window=myButton)

#root.mainloop()

# if __name__=="__main__":
#     takeScreenshot()
