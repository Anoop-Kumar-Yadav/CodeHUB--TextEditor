'''
This is the main file that have a class MainEditor that is a parent class of tkinter.Tk 
that is responsible for create top window.
'''

import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, DISABLED, HORIZONTAL, LEFT,VERTICAL, X, Y
import conda_textArea
import conda_lineNumber
import conda_menuBar
import condaLoader
import conda_statusBar

############################################################################################################
class MainEditor(tk.Tk):

    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)

        self.iconPath = "data\\images\\ide1.ico" 
        # This variable store the path of icon.
        
        self.title("untitled -   condaEditor")
        self.geometry("%sx%s"%(self.winfo_screenwidth(),self.winfo_screenwidth()))
        # This will set the windows height and width same as monitor screen
        
        self.iconbitmap(bitmap=self.iconPath)
        # img = tk.PhotoImage(self.iconPath)
        # self.
        #This will set window icon

        self.condaLoader = condaLoader.condaLoader(self)
        # This will create instance of condaLaoder class of condaloader module

        self.scrolly = tk.Scrollbar(self,orient=VERTICAL)
        # This create a instance of scrollbar (vertical).
        self.scrollx = tk.Scrollbar(self,orient=HORIZONTAL)    
        # This create a instance of scrollbar (horizontal).

        self.textArea = conda_textArea.textArea(self,background="cyan",foreground="black")
        # This create a instance of textArea class of conda_textArea module that is actually a parent class of tkinter.Text

        self.menuBar = conda_menuBar.menuBAR(self)
        self.menuBar.Syntax_Highlight()
        # This create a instance of menuBAR class of conda_menuBar module that is actually a parent class of tkinter.Menu

        self.statusbar = conda_statusBar.statusBar(self)
        # This create a instance of statusBar class of conda_statusBar module that is actually a parent class of tkinter.Text

        self.lineNumber = conda_lineNumber.numberLine(self,self.textArea)
        # This create a instance of numberLine class of conda_lineNumber module that is actually a parent class of tkinter.Text

        self.lineNumber.update_onKeyPress()
        # This method update the whole data on press any on textArea
        self.lineNumber.config(state=DISABLED)
        # This will make lineNumber disable so it cant be edited by user 
 
        self.statusbar.pack(fill=X,side=BOTTOM)
        # This will pack the widget on window 

        self.scrolly.config(command=self.EditorViewY)
        # This will set scrollbar (vertical) for both textArea and numberLine 
        self.scrollx.config(command=self.textArea.xview)
        # This will set scrollbar (horizontal) for both textArea
        
        self.scrollx.pack(side=BOTTOM,fill=X)
        # This will pack the widget on window
        self.textArea.config(yscrollcommand=self.scrolly.set,xscrollcommand=self.scrollx.set)
         
        self.lineNumber.pack(side=LEFT,fill=Y)
        # This will pack the widget on window
        self.textArea.pack(side=LEFT,fill=BOTH,expand=True) 
        # This will pack the widget on window
        self.scrolly.pack(side=LEFT,fill=Y)
        # This will pack the widget on window

        self.condaLoader.apply_lastsetting()
        # This will apply last saved settings on text Editor
        self.textArea.focus_set()
        # This will set focus on textArea
        self.bind_All()
        # This will bind all shortcuts to textArea

############################################################################################################
    def EditorViewY(self,*args): 
        
        self.textArea.yview(*args)
        self.lineNumber.yview(*args)

############################################################################################################
    def bind_All(self,*args, **kwargs):
        ''' This Function will bind shortcuts to textArea with respective function. '''

        self.textArea.bind("<Control-n>",self.menuBar.new_file)
        self.textArea.bind("<Control-o>",self.menuBar.open_file)
        self.textArea.bind("<Control-s>",self.menuBar.save_file)
        self.textArea.bind("<Control-Shift-s>",self.menuBar.save_as_file)
        self.textArea.bind("<Control-q>",self.menuBar.exit_editor)
        self.textArea.bind("<Control-z>",self.menuBar.undo)
        self.textArea.bind("<Control-y>",self.menuBar.redo)
        self.textArea.bind("<Control-x>",self.menuBar.cut)
        self.textArea.bind("<Control-c>",self.menuBar.copy)
        self.textArea.bind("<Control-V>",self.menuBar.paste)
        self.textArea.bind("<Control-f>",self.menuBar.launchFindpopUp)
        self.textArea.bind("<Control-g>",self.menuBar.launchFindpopUp)
        self.textArea.bind("<Control-equal>",self.textArea.transparencyShortcut)
        self.textArea.bind("<Control-minus>",self.textArea.transparencyShortcut)
        self.textArea.bind("<Alt-Up>",self.textArea.ZoomShortcut)
        self.textArea.bind("<Alt-Down>",self.textArea.ZoomShortcut)
        self.textArea.bind("<Control-comma>",self.menuBar.launchPreferences)
        self.textArea.bind("<Control-a>",self.menuBar.selectAll)
        self.textArea.bind("<Control-d>",self.menuBar.deleteAll)

