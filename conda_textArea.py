import tkinter as tk
from tkinter.constants import END, INSERT, SEL
from tkinter.font import Font
import setting

class textArea(tk.Text):

    def __init__(self,parent,*args, **kwargs):
        tk.Text.__init__(self,*args, **kwargs)
        
        
        self.parent = parent
        self.config(undo=True,wrap="none")

        self.settings = setting.Appplier(parent = self.parent)
        self.bind("<MouseWheel>",self.scrollX)

    def scrollY(self,event=None):
        
        a = list(self.parent.scrolly.get())

        idx = self.index(INSERT).split(".")[0]

        self.parent.lineNumber.yview_moveto(idx + ".0")

        self.parent.scrolly.set(a[0],a[1])

    def scrollX(self,event=None):

        data = list(self.yview())
   
        self.parent.lineNumber.yview_moveto(data[0])

    def transparencyShortcut(self,event=None):

        settings = self.parent.condaLoader.load_setting_data()

        currentLevel = round(settings["transparency_level"],1)

        if event.keysym == "equal":
            if currentLevel == 1.0:
                print("It is MAX")
            else:
                newLevel = currentLevel + 0.1
                self.parent.attributes("-alpha",newLevel)
                settings["transparency_level"] = newLevel
                self.parent.condaLoader.upload_setting(settings)
                try:
                    self.parent.menuBar.setting.themeTab.appplyTranparency(True,event)
                except:
                    pass
        else:
            if currentLevel == 0.1:
                print("It is MIN")
            else:
                newLevel = currentLevel - 0.1
                self.parent.attributes("-alpha",newLevel)
                settings["transparency_level"] = newLevel
                self.parent.condaLoader.upload_setting(settings)
                try:
                    self.parent.menuBar.setting.themeTab.appplyTranparency(True,event)
                except:
                    pass

    def ZoomShortcut(self,event=None):

        settings = self.parent.condaLoader.load_setting_data()

        currentFont = settings["font"]
        currentSize = currentFont["size"]

        if event.keysym == "Up":
            if currentSize == 72:
                print("It is MAX")
                font_ = Font(family=currentFont["family"],size=currentSize)
            else:
                newSize = currentSize + 1
                font_ = Font(family=currentFont["family"],size=newSize)
                settings["font"]["size"] = newSize
        else:
            if currentSize == 1:
                print("It is MIN")
                font_ = Font(family=currentFont["family"],size=currentSize)
            else:
                newSize = currentSize - 1
                font_ = Font(family=currentFont["family"],size=newSize)
                settings["font"]["size"] = newSize

        self.config( font= font_)
        self.parent.lineNumber.config( font= font_)
        self.parent.condaLoader.upload_setting(settings)
        self.parent.lineNumber.update_onKeyPress()
    
