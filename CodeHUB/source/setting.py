import os
import tkinter ,json
from tkinter import DoubleVar, Spinbox, StringVar, ttk, IntVar
from tkinter import font
from tkinter.constants import ANCHOR, LEFT, SW

############################################################################################################
class Appplier:
    def __init__(self,*args, **kwargs) -> None:
        
        self.parent = kwargs["parent"]

        self.theme_path = os.path.abspath('data\\themes')

############################################################################################################
    def load_Theme(self,Default=False):
        # theme_data = {}

        try:
            if Default == True:
                theme = self.parent.condaLoader.load_setting_data(Default=True)["theme"].lower()
                path = self.theme_path + "\\" + theme.replace(" ", "_")
                with open(file=path,mode="r") as theme_file:
                    theme_data = json.load(theme_file)
            
                return theme_data

            else:
                theme = self.parent.condaLoader.load_setting_data(Default=False)["theme"].lower()
                path = self.theme_path + "\\" + theme.replace(" ", "_")
                with open(file=path,mode="r") as theme_file:
                    theme_data = json.load(theme_file)
                return theme_data
                
        except FileNotFoundError :
            print(path + "**(")
            return "Corrupted Application"    

############################################################################################################
    def apply_Theme(self,theme_Data):
        
        self.parent.currentTheme = theme_Data
        self.parent.menuBar.popupmenu.config(background = theme_Data["bg_color"],foreground = theme_Data["font_color"])
        self.parent.textArea.config(background = theme_Data["bg_color"],insertbackground = theme_Data["font_color"] )
        self.parent.textArea.config(selectbackground = theme_Data["selection_color"])
        
        self.parent.lineNumber.config(background = theme_Data["bg_color"])
        self.parent.lineNumber.config(foreground = theme_Data["font_color"])
        self.parent.lineNumber.config(selectbackground = theme_Data["selection_color"])
        
        self.parent.statusbar.config(background = theme_Data["statusbar_bg"])
        self.parent.statusbar.config(foreground = theme_Data["statusbar_fg"])
        self.parent.statusbar.config(selectbackground = theme_Data["selection_color"])  
        
        self.parent.scrollx.config(background = theme_Data["scrollbar_bg"],troughcolor = theme_Data["scrollbar_trough"])   
        self.parent.scrolly.config(background = theme_Data["scrollbar_bg"],troughcolor = theme_Data["scrollbar_trough"])  
            
        self.parent.menuBar.setNewProperty(activebackground = theme_Data["menu_bg_active"],
        activeforeground = theme_Data["menu_fg_active"], background= theme_Data["menu_bg"],
        foreground = theme_Data["menu_fg"])
 
################################################################################################################################################################################################
################################################################################################################################################################################################
class fontFrame(tkinter.Frame):

    def __init__(self,parent,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.parent = parent
        self.themeDirectory = os.path.abspath("data\\themes")
        self.IconDirectory = os.path.abspath("data\\icons")

        self.backToEditorButton = tkinter.Button(self,text="<<<< Back",command=self.backtoEditor)
        self.backToEditorButton.place(relx=0, rely=0)
        self.backToEditorButton.configure(foreground="dark blue",relief="flat",justify="left",activeforeground="red")
        self.backToEditorButton.configure(justify=LEFT,font=("Arial",10,"bold"))

        self.fontSizeLabel = tkinter.Label(self,text="Size")
        self.fontSizeLabel.place(relx=0.717, rely=0.065 )

        self.fontFamilyLabel = tkinter.Label(self,text="Family")
        self.fontFamilyLabel.place(relx=0.017, rely=0.065 )

        self.lineSpacingLabel = tkinter.Label(self,text="Sapce Between Lines : ")
        self.lineSpacingLabel.place(relx=0.017, rely=0.229 )

        self.tabSpacingLabel = tkinter.Label(self,text="Tab width : ")
        self.tabSpacingLabel.place(relx=0.017, rely=0.329 )

        self.fontFamilyScrolledList = ttk.Combobox(self,state="readonly")
        self.fontFamilyScrolledList.place(relx=0.017, rely=0.129, height=20, relwidth=0.678)

        self.lineSpacingCombo = ttk.Combobox(self,state="readonly")
        self.lineSpacingCombo.place(relx=0.017, rely=0.270, height=20, relwidth=0.167 )

        self.tabSpacingCombo = ttk.Combobox(self,state="readonly")
        self.tabSpacingCombo.place(relx=0.017, rely=0.370, height=20, relwidth=0.167 ) 

        self.fontSizeEntry = ttk.Combobox(self,state="readonly")
        self.fontSizeEntry.place(relx=0.717, rely=0.129, height=20, relwidth=0.167 )

        self.fontFamilyScrolledList.bind("<<ComboboxSelected>>",self.apply_font)
        self.fontSizeEntry.bind("<<ComboboxSelected>>",self.apply_font)
        self.tabSpacingCombo.bind("<<ComboboxSelected>>",self.apply_font)
        self.lineSpacingCombo.bind("<<ComboboxSelected>>",self.apply_font)
        self.fontVariableIntializer()
        self.seePrevious()

#########################################################################################################################
    def backtoEditor(self,event=None):
        self.parent.place_forget()

#########################################################################################################################
    def fontVariableIntializer(self):
                
        self.fontFamilyListVar = StringVar()
        self.fontSizeEntryVar = IntVar()
        self.tabWidthVar = IntVar()
        self.lineSpacingVar = IntVar()

        self.fontFamilyScrolledList.config(textvariable=self.fontFamilyListVar)
        self.fontSizeEntry.config(textvariable=self.fontSizeEntryVar)
        self.tabSpacingCombo.config(textvariable=self.tabWidthVar)
        self.lineSpacingCombo.config(textvariable=self.lineSpacingVar)

        self.fontFamilyScrolledList["values"] = tuple(self.getAvailabeFont())
        self.fontSizeEntry["values"] = tuple(self.getAvailabeSize())
        self.tabSpacingCombo["values"] = tuple(self.getAvailableTabWidth())
        self.lineSpacingCombo["values"] = tuple(self.getAvailableLineSpace())

#########################################################################################################################
    def getAvailableTabWidth(self,event=None):
        availableWidth = list()
        for width in range(1,201):
            availableWidth.append(width)
        return availableWidth

#########################################################################################################################
    def getAvailableLineSpace(self,event=None):
        availableSpace = list()
        for space in range(1,100):
            availableSpace.append(space)
        return availableSpace

#########################################################################################################################
    def getAvailabeFont(self,event=None):
        availableFamily = list(font.families())
        availableFamily.sort()
        return availableFamily

#########################################################################################################################        
    def getAvailabeSize(self):
        availableSize = list()
        for size in range(1,73):
            availableSize.append(size)
        return availableSize

#########################################################################################################################
    def seePrevious(self):

        settings = self.parent.parent.condaLoader.load_setting_data()
    
        familyIndex = self.getAvailabeFont().index(settings["font"]["family"])
        SizeIndex = self.getAvailabeSize().index(settings["font"]["size"])
        tabWidth = self.getAvailabeSize().index(settings["tab_width"])
        lineSpace = self.getAvailabeSize().index(settings["line_space"])

        self.fontFamilyScrolledList.current(familyIndex)
        self.fontSizeEntry.current(SizeIndex)
        self.tabSpacingCombo.current(tabWidth)
        self.lineSpacingCombo.current(lineSpace)

#########################################################################################################################

    def apply_font(self,event=None):
        
        

        settings = self.parent.parent.condaLoader.load_setting_data()

        selected_family = self.fontFamilyListVar.get()
        selected_size = self.fontSizeEntryVar.get()
        selected_tabWidth = self.tabWidthVar.get()
        selected_lineSpace = self.lineSpacingVar.get()

        settings["tab_width"] = selected_tabWidth
        settings["line_space"] = selected_lineSpace
        settings["font"]["family"] = selected_family
        settings["font"]["size"] = selected_size
        

                
            

        self.parent.parent.condaLoader.upload_setting(settings)
        self.parent.parent.condaLoader.apply_lastsetting()
        

################################################################################################################################################################################################
#########################################################################################################################
class themeFrame(tkinter.Frame):
    def __init__(self,parent,*args, **kwargs):

        super().__init__(*args, **kwargs)
        self.parent = parent
        self.themeDirectory = os.path.abspath("data\\themes")
        self.IconDirectory = os.path.abspath("data\\icons")

        self.backToEditorButton = tkinter.Button(self,text="<<<< Back",command=self.backtoEditor)
        self.backToEditorButton.place(relx=0, rely=0)
        self.backToEditorButton.configure(foreground="dark blue",relief="flat",justify="left",activeforeground="red")
        self.backToEditorButton.configure(justify=LEFT,font=("Arial",10,"bold"))

        self.themeScrolledListVar = StringVar()
        self.themeScrolledList = tkinter.Listbox(self,activestyle="none")
        self.themeScrolledList.place(relx=0.017, rely=0.172, relheight=0.366 , relwidth=0.525 )
        
        self.themeEntry = tkinter.Entry(self)
        self.themeEntry.place(relx=0.017, rely=0.129, height=20, relwidth=0.523)

        self.themeLabel = tkinter.Label(self,text="Themes :",justify="left")
        self.themeLabel.place(relx=0.017, rely=0.065)

        self.searchOnlineButton = tkinter.Button(self)
        self.searchOnlineButton.place(relx=0.65, rely=0.500, height=21, width=94)
        self.searchOnlineButton.configure(foreground="#0080ff",relief="flat")
        self.searchOnlineButton.configure(text='''Search Online.''')

        self.transparencyLabel = tkinter.Label(self,text="Transparency :",justify="left")
        self.transparencyLabel.place(relx=0.017, rely=0.57)
        
        values_ = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

        self.transparency = Spinbox(self,values=tuple(values_),command=self.appplyTranparency,relief="groove")
        self.transparency.place(relwidth=0.1,relheight=0.05,relx=0.017,rely=0.67,anchor=SW)

        self.themeVariableIntializer()
        self.setCurrentThemeOnEntry()

        self.themeScrolledList.bind("<<ListboxSelect>>",self.applyTheme)
        self.parent.parent.textArea.bind("<Button-1>",self.backtoEditor)

#########################################################################################################################
    def themeVariableIntializer(self):

        self.transparent = DoubleVar()
        self.themeEntryVar = StringVar()
        
        for i in self.getAvailableTheme()[::-1]:
            self.themeScrolledList.insert(-1,i)

        self.transparency.config(textvariable=self.transparent)
        self.themeEntry.config(textvariable=self.themeEntryVar)

        lastTransparency = self.parent.parent.condaLoader.load_setting_data()["transparency_level"]
        self.transparent.set(round(lastTransparency,1))

#########################################################################################################################
    def setCurrentThemeOnEntry(self,event=None):
        settings = self.parent.parent.condaLoader.load_setting_data()
        currentTheme  = (settings["theme"][1:].split(".")[0]).replace("_", " ")
        self.themeEntryVar.set(currentTheme)

#########################################################################################################################
    def getAvailableTheme(self):
        themesList = os.listdir(self.themeDirectory)
        lst = []
        for i in themesList:
            lst.append(i.split(sep=".")[0].title().replace("_", " "))
        return lst

#########################################################################################################################
    def backtoEditor(self,event=None):
        self.parent.place_forget()

#########################################################################################################################
    def appplyTranparency(self,load=False,event=None):

        if load == False:

            transparencyValue = self.transparent.get()

            settings = self.parent.parent.condaLoader.load_setting_data()
            settings["transparency_level"] = transparencyValue
            self.parent.parent.condaLoader.upload_setting(settings)
            self.parent.parent.attributes("-alpha",transparencyValue)

        else:
            settings = self.parent.parent.condaLoader.load_setting_data()
            self.transparent.set(settings["transparency_level"])

            transparencyValue = self.transparent.get()
            self.parent.parent.attributes("-alpha",transparencyValue)

#########################################################################################################################
    def applyTheme(self,event=None):

        theme = self.themeScrolledList.get(ANCHOR) + ".json"

        settings = self.parent.parent.condaLoader.load_setting_data()

        settings["theme"] = "\\" + theme

        self.parent.parent.condaLoader.upload_setting(settings)

        themeApplier = Appplier(parent = self.parent.parent)
        theme_Data = themeApplier.load_Theme()
        themeApplier.apply_Theme(theme_Data=theme_Data)

        self.setCurrentThemeOnEntry()

#########################################################################################################################
class settingTab(ttk.Notebook):

    def __init__(self,parent,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.fontTab = fontFrame(self)
        self.fontTab.place(relheight=1,relwidth=1)
        self.themeTab = themeFrame(self)
        self.themeTab.place(relheight=1,relwidth=1)

        self.add(self.fontTab,text="Font")
        self.add(self.themeTab,text="Theme")
#########################################################################################################################