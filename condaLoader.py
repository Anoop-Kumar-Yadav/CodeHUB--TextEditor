import json
import os
from tkinter import font
from tkinter.constants import BOTTOM, NONE, NW, RIGHT, SE
from tkinter.font import Font
import setting

class condaLoader():

    def __init__(self,parent) :

        self.parent = parent
        self.default_setting_path = os.path.abspath("data\\config\\conda_defaultSetting.json")
        self.setting_path = os.path.abspath("data\\config\\conda_lastSetting.json")
        
    def load_setting_data(self,Default = False):
        try:
            if Default == True:
                with open(file=self.default_setting_path,mode="r") as setting_file :
                    data = json.load(setting_file)

                return data
            else:
                with open(file=self.setting_path,mode="r") as setting_file :
                    data = json.load(setting_file)
                    
                return data
                
        except FileNotFoundError:
            return "Corrupted Application"

    def upload_setting(self,newSetting):
        try:
            with open(file=self.setting_path,mode="w") as setting_file :
                return json.dump(newSetting,setting_file)
        except:
            return None

    def apply_lastsetting(self):

        settings = self.load_setting_data()

        self.parent.attributes("-alpha",settings["transparency_level"])
        self.parent.attributes("-topmost",1)

        themeApplier = setting.Appplier(parent = self.parent)

        self.parent.menuBar.set_last_menu_settings()
        themeApplier.apply_Theme(themeApplier.load_Theme())

        font1 = Font( family = settings["font"]["family"],
                      size = settings["font"]["size"],
                      slant = settings["font"]["slant"],
                      weight = settings["font"]["weight"],
                      underline = settings["font"]["underline"])
        
        tabWidth = settings["tab_width"]
        lineSpace = settings["line_space"]
     
        self.parent.textArea.config(font=font1,tabs=tabWidth,spacing1=lineSpace)
        self.parent.lineNumber.config(font=font1,spacing1=lineSpace)


        if settings["linenumber"] == "show":
            self.parent.lineNumber.show_linenumber(visible = "show")
        else:
            self.parent.lineNumber.show_linenumber(visible = "hide")

        if settings["horizontal_scrollbar"] == "show":
            self.parent.scrollx.config(width = 15)
        else:
            self.parent.scrollx.config(width = 0)
            self.parent.scrollx.pack_configure(fill=NONE,anchor = SE)

        if settings["vertical_scrollbar"] == "show":
            self.parent.scrolly.config(width = 15)
        else:
            self.parent.scrolly.config(width = 0)

        if settings["wrap"] == "none":
            self.parent.textArea.config(wrap="none")
        else:
            self.parent.textArea.config(wrap="word")                            