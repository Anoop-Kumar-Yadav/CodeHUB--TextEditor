import json
import os,csv
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter.constants import  END, INSERT, NE, SEL
import condaLoader 
from setting import settingTab
import popup
import highlighter
from pygments.lexers import (LuaLexer,MarkdownLexer,PerlLexer,PythonLexer,RubyLexer,KotlinLexer,
                             CLexer,CppLexer,JavaLexer,PrologLexer,BashLexer,PowerShellLexer,
                             ScalaLexer,CSharpLexer,FSharpLexer,CommonLispLexer,MatlabLexer,
                             BatchLexer,TextLexer,YamlLexer,CssLexer,
                             HtmlLexer,JavascriptLexer,PhpLexer,XmlLexer,HaskellLexer,SwiftLexer,JsonLexer,
                             VBScriptLexer,CobolLexer,ArduinoLexer,RegeditLexer,VbNetLexer,GoLexer)

############################################################################################################
class menuBAR:

    def __init__(self,parent) -> None:

        self.parent = parent
       
        self.OpenedFile = None
        
        self.selectedExtension = ".txt"

        
        
        self.loader = condaLoader.condaLoader(self.parent)

        self.Higlighter = highlighter.HighLighter(self.parent.textArea)
       
        self.popupMsg = popup.PopUps(parent=self)
      
        self.createPopUpMenu()
        self.parent.textArea.bind("<Button-3>",self.launchPopUpMenu)

        self.menubar = tk.Menu(self.parent,
                            fg = "green",
                            bg = "red",
                            activebackground="green",
                            activeforeground="red",
                            borderwidth = 0)
        
        self.parent.config(menu=self.menubar)

#------------------------------------------------------------------------------------------------------------
        # File Menu
        self.filemenu = tk.Menu(master=self.menubar,tearoff=0)
        self.filemenu.add_command(label="New File",accelerator="Ctrl+N",command=self.new_file)
        self.filemenu.add_command(label="Open File",accelerator="Ctrl+O",command=self.open_file)
        self.filemenu.add_command(label="Recent Files",command = self.popupMsg.recentFiles)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save File",accelerator="Ctrl+S",command=self.save_file)
        self.filemenu.add_command(label="Save File As",accelerator="Ctrl+Shift+S",command=self.save_as_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Setting",accelerator="Ctrl+,",command=self.launchPreferences)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit Editor",accelerator="Ctrl+Q",command=self.exit_editor)
        # Edit Menu
        self.editmenu = tk.Menu(master=self.menubar,tearoff=0)
        self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
        self.editmenu.add_command(label="Redo",accelerator="Ctrl+Y",command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find",accelerator="Ctrl+F",command=self.launchFindpopUp)
        self.editmenu.add_command(label="Find & Replace",accelerator="Ctrl+H",command=self.launchFindpopUp)

        # Selection Menu
        self.selectionmenu = tk.Menu(master=self.menubar,tearoff=0)
        self.selectionmenu.add_command(label="Select All",accelerator="Ctrl+A",command=self.selectAll)
        self.selectionmenu.add_command(label="Delete All",accelerator="Ctrl+D",command=self.deleteAll)

        # View Menu
        self.viewmenu = tk.Menu(master=self.menubar,tearoff=0)
        self.wordwrap_var = tk.BooleanVar()
        self.viewmenu.add_checkbutton(label="Wordwrap",variable=self.wordwrap_var,command=self.wordWrap)
        self.viewmenu.add_separator()
        self.quietmode_var = tk.BooleanVar()
        self.viewmenu.add_checkbutton(label="Quiet Mode",variable=self.quietmode_var,command=self.QuietMode)

        # Help Menu
        self.helpmenu = tk.Menu(master=self.menubar,tearoff=0)
        self.helpmenu.add_command(label="KeyBoard Shortcuts",command = self.popupMsg.keyBoardShortcuts)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Documentation")
        self.helpmenu.add_command(label="About",command=self.popupMsg.about)
        self.helpmenu.add_command(label="Report Issue")

        # Add submenu to menubar
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.menubar.add_cascade(label='Edit', menu=self.editmenu)
        self.menubar.add_cascade(label='Selection', menu=self.selectionmenu)
        self.menubar.add_cascade(label='View', menu=self.viewmenu)
        self.menubar.add_cascade(label='Help', menu=self.helpmenu)

        self.parent.protocol("WM_DELETE_WINDOW",self.exit_editor)

############################################################################################################
    def createPopUpMenu(self,*args, **kwargs):
        self.popupmenu = tk.Menu(self.parent.textArea,tearoff=0,bg="green")
        self.popupmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
        self.popupmenu.add_command(label="Redo",accelerator="Ctrl+Y",command=self.redo)
        self.popupmenu.add_separator()
        self.popupmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.popupmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.popupmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.popupmenu.add_separator()
        self.popupmenu.add_command(label="Find",accelerator="Ctrl+F",command=self.launchFindpopUp)
        self.popupmenu.add_command(label="Find & Replace",accelerator="Ctrl+H",command=self.launchFindpopUp)
        self.popupmenu.add_separator()
        self.popupmenu.add_command(label="Save File",accelerator="Ctrl+S",command=self.save_file)
        self.popupmenu.add_command(label="Save File As",accelerator="Ctrl+Shift+S",command=self.save_as_file)

############################################################################################################
    def getFiletypes(self,*args, **kwargs):
        with open("data\\config\\xtnsion.json","r") as file:
            data = json.load(file)

        filetypes = []

        nw = []
        for i in data["filetypes"]:
            nw.append(i[0])
        nw.sort()
        
        for j in nw:
            for k in data["filetypes"]:
                if j in k:
                    filetypes.append(tuple(k))
        if "required" in kwargs:
            return data["filetypes"]
        else:
            return filetypes
        

           

############################################################################################################
    def launchPopUpMenu(self,event=None):
        try:
            self.popupmenu.tk_popup(event.x_root,event.y_root)
        finally:
            self.popupmenu.grab_release()

############################################################################################################
    def launchFindpopUp(self,*args):
        self.popupMsg.findReplace()

############################################################################################################
    def set_last_menu_settings(self,*args):
        settings = self.loader.load_setting_data()
        if settings["quiet_mode"] == "check":
            self.quietmode_var.set(value=True)
        else:
            self.quietmode_var.set(value=False)

        if settings["wrap"] == "none":
            self.wordwrap_var.set(value=False)
        else:
            self.wordwrap_var.set(value=True)

######################################################  Functions ########################################################################

#----------------------------------------------------------------------------------------------------------------
    def titleModify(self,*args):
        if self.OpenedFile == None:
            self.parent.title("untitled -   condaEditor")
            self.parent.lineNumber.update_onKeyPress()
        else:
            self.parent.title(os.path.basename(self.OpenedFile)+" -  condaEditor")
            self.parent.lineNumber.update_onKeyPress()
            

#----------------------------------------------------------------------------------------------------------------
    def isFileModified(self,*args):
        try:
            with open(file=self.OpenedFile,mode="r") as file:

                fileData = (file.read().split("\n"))
                editorData = (self.parent.textArea.get("1.0",END).split("\n"))

                if fileData == editorData:
                    return False
                else:
                    return True
        except:
            self.OpenedFile = None

#----------------------------------------------------------------------------------------------------------------
    def loadFile(self,path,*args, **kwargs):
        if os.path.exists(path) == True:
            with open(file=path,mode="r") as file:
                data = file.read()
           
                self.parent.textArea.delete("1.0",END)
                self.parent.textArea.insert("1.0",data)
               
                file.close()
                self.OpenedFile = path
                self.titleModify()
                self.parent.lineNumber.update_onKeyPress()
                
                self.parent.textArea.see("end")
                self.parent.textArea.focus_set()
                self.Syntax_Highlight(extension=self.setExtension(path))
            
                if "by" in kwargs:
                    pass
                else:
                    self.uploadRecentFile(path)

    def uploadRecentFile(self,path):
        files = []
       
        with open(file="data\\config\\recentfiles.csv",mode="r+") as file_:
            csvReader = csv.reader(file_)

            try:
                for row in csvReader:
                    if len(row) == 0:
                        pass
                    else:
                        files.append(row)
            except:
                pass

            if csvReader.line_num >= 10:
               files.pop(0)
            else:
                pass
            files.append([path])
            

        with open(file="data\\config\\recentfiles.csv",mode="r+") as file_: 
            csvWriter = csv.writer(file_)
           

            for i in files:
                if len(i) == 0:
                    pass
                else:
                    csvWriter.writerow(i)
#----------------------------------------------------------------------------------------------------------------
    def dumpFile(self,path,*args):
            with open(file=path,mode="w") as file:
                data = self.parent.textArea.get("1.0","end")
                file.write(data)
                file.close()
     
#----------------------------------------------------------------------------------------------------------------
    def warningMsg(self,msg,*args):
        msgbox = tk.messagebox.askyesnocancel(title="Warning",message=msg)
        return msgbox

    def setExtension(self,path=None,**kwargs):
        if "applyExt" in kwargs:
            self.selectedExtension = kwargs["applyExt"]
        else:
            try:
                self.selectedExtension = os.path.splitext(str(path))[1]
            except:
                self.selectedExtension = ".txt"

        

######################################################  Menu Functions ########################################################################


######################################################  New File  ########################################################################

    def new_file(self,*args):
        def clearAndNew(save=None):
            if save == True:
                self.save_file()
                self.parent.textArea.delete("1.0",END)
                self.OpenedFile = None
                self.titleModify()
                self.parent.textArea.focus_set()
                self.parent.textArea.edit_reset()
                self.popupMsg.selectFileType()
            elif save == False:
                self.parent.textArea.delete("1.0",END)
                self.OpenedFile = None
                self.titleModify()
                self.parent.textArea.focus_set()
                self.parent.textArea.edit_reset()
                self.popupMsg.selectFileType()
            else:
                pass
#----------------------------------------------------------------------------------------------------------------
        if self.OpenedFile != None:
            if self.isFileModified() == True:
                response = self.warningMsg(msg="Do you want to save the changes ?")
            else:
                response = False
            if response == True:
                clearAndNew(save=True) 
            elif response == False:
                clearAndNew(save=False)
            else:
                pass
        elif self.OpenedFile == None:
            if self.parent.textArea.edit_modified() == True:
                warning = self.warningMsg("Do you want to save file ?")
                if warning == None:
                    pass
                elif warning == True:
                    clearAndNew(save=True)

                else:
                    clearAndNew(save=False)
            else:
                clearAndNew(save=False)
######################################################  Open File ########################################################################    

    def open_file(self,*args,**kwargs):
#----------------------------------------------------------------------------------------------------------------
        def openfileDialogbox(save=None):
            if save == True:
                self.save_file()                                                   
                filedialog = tk.filedialog.askopenfile(title="Open Dialog",filetypes =self.getFiletypes())   
                if filedialog == None:                                              
                    pass                                                           
                else:              
                    self.parent.textArea.edit_reset() 
                                                                  
                    self.loadFile(filedialog.name)
                    self.parent.textArea.focus_set()
                    self.parent.lineNumber.see(self.parent.textArea.index(INSERT))
                                 
            elif save==False:                                                 
                filedialog = tk.filedialog.askopenfile(title="Open Dialog",filetypes =self.getFiletypes())  
                if filedialog == None:                                              
                    pass                                                           
                else:                  
                    self.parent.textArea.edit_reset()                                          
                    self.loadFile(filedialog.name) 
                    self.parent.textArea.focus_set()
                    self.parent.lineNumber.see(self.parent.textArea.index(INSERT))                              
#----------------------------------------------------------------------------------------------------------------                                
 
        if "file" in kwargs:
            self.OpenedFile = kwargs["file"]
            self.loadFile(kwargs["file"],by = "recent")
            self.parent.textArea.focus_set()
            self.parent.lineNumber.see(self.parent.textArea.index(INSERT)) 
        else:
      
            if self.OpenedFile != None:  
                if self.isFileModified() == True: 
                    response = self.warningMsg(msg="Do you want to save the changes ?") 
                else:
                    response = False
                if response == True:  
                    openfileDialogbox(save=True)

                elif response == False: 
                    openfileDialogbox(save=False)               
                else:                      
                    pass
            elif self.OpenedFile == None:    
                if self.parent.textArea.edit_modified() == True:                                  
                    warning = self.warningMsg("Do you want to save file ?")                
                    if warning == None:                                                     
                        pass                                                                
                    elif warning == True:                                               
                        openfileDialogbox(save=True)                            
                    else:                                                                   
                        openfileDialogbox(save=False)                                
                else:                                                                       
                    openfileDialogbox(save=False)                                    
                                   
######################################################  Save File ########################################################################

    def save_file(self,*args):
        if self.OpenedFile == None:
            self.save_as_file()
            self.Syntax_Highlight()
        else:
            self.dumpFile(self.OpenedFile)
            return True

######################################################  Save As File ########################################################################

    def save_as_file(self,*args):
        filedialog = tk.filedialog.asksaveasfile(title="Save As",filetypes =self.getFiletypes(),initialfile='untitled',defaultextension=("*.*"))
        if filedialog != None:
            
            self.dumpFile(filedialog.name)
            self.OpenedFile = str(filedialog.name)

            self.uploadRecentFile(filedialog.name)
            
            self.titleModify()
            
            return True
        else:
            return False

######################################################  Preferences ########################################################################

    def launchPreferences(self,*args):
        self.setting = settingTab(self.parent)
        self.setting.place(relheight=1,relwidth=0.37,anchor=NE,relx=1,rely=0)
        
    def setNewProperty(self,*args,**kwargs):

        for i in kwargs:
            self.filemenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                 bg=kwargs["background"],fg=kwargs["foreground"])
            self.editmenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                 bg=kwargs["background"],fg=kwargs["foreground"])
            self.selectionmenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                      bg=kwargs["background"],fg=kwargs["foreground"])
            self.viewmenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                 bg=kwargs["background"],fg=kwargs["foreground"])
            self.helpmenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                 bg=kwargs["background"],fg=kwargs["foreground"])
            self.popupmenu.config(activebackground=kwargs["activebackground"],activeforeground=kwargs["activeforeground"],
                                 bg=kwargs["background"],fg=kwargs["foreground"])

######################################################  Exit Editor ########################################################################

    def exit_editor(self,*args):
#----------------------------------------------------------------------------------------------------------------
        def clearAndExit(save=None,*args):
            if save == True:
                self.save_file()
                self.parent.destroy()
            elif save == False:
                self.parent.destroy()
            else:
                pass
#----------------------------------------------------------------------------------------------------------------
        if self.OpenedFile != None:
            if self.isFileModified() == True:
                response = self.warningMsg(msg="Do you want to save the changes ?")
            else:
                response = False
            if response == True:
                clearAndExit(save=True) 
            elif response == False:
                clearAndExit(save=False)
            else:
                pass
        elif self.OpenedFile == None:
            if self.parent.textArea.edit_modified() == True:
                warning = self.warningMsg("Do you want to save file ?")
                if warning == None:
                    pass
                elif warning == True:
                    clearAndExit(save=True)

                else:
                    clearAndExit(save=False)
            else:
                clearAndExit(save=False)         

######################################################  Edit Menu Function ########################################################################
    def undo(self,*args):
        self.parent.textArea.event_generate("<<Undo>>")
        self.parent.lineNumber.update_onKeyPress()
    
    def redo(self,*args):

       self.parent.textArea.event_generate("<<Redo>>")
       self.parent.lineNumber.update_onKeyPress()


    def cut(self,*args):
        self.parent.textArea.event_generate("<<Cut>>")

    def copy(self,event=None,*args):
        self.parent.textArea.event_generate("<<Copy>>")

    def paste(self,event=None,*args):
        self.parent.textArea.event_generate("<<Paste>>")
        self.parent.lineNumber.update_onKeyPress()
        
######################################################  Edit Menu Function ########################################################################
######################################################  Selection Menu Function ########################################################################

    def selectAll(self,*args):
        self.parent.textArea.tag_add(SEL,"1.0",END)
        self.parent.textArea.mark_set(INSERT,"1.0")
        self.parent.textArea.see(INSERT)
        return "break"

    def deleteAll(self,*args):
        self.parent.textArea.delete("1.0",END)
        self.parent.lineNumber.update_onKeyPress()

######################################################  View Menu Function ########################################################################

    def wordWrap(self,*args):
        settings = self.loader.load_setting_data()
        if settings["wrap"] == "none":
            self.parent.textArea.config(wrap="word")
            settings["wrap"] = "word"
        else:
            self.parent.textArea.config(wrap="none")
            settings["wrap"] = "none"

        self.loader.upload_setting(newSetting=settings)
######################################################  Quiet Mode ########################################################################

    def QuietMode(self,*args):

        settings = self.loader.load_setting_data()

        if settings["linenumber"] == "show":
            self.parent.lineNumber.show_linenumber(visible = "hide")
            settings["linenumber"] = "hide"
        else:
            settings["linenumber"] = "show"
            self.parent.lineNumber.show_linenumber(visible = "show")

        if settings["horizontal_scrollbar"] == "show":
            self.parent.scrollx.config(width = 0)
            settings["horizontal_scrollbar"] = "hide"
        else:
            settings["horizontal_scrollbar"] = "show"
            self.parent.scrollx.config(width = 20)

        if settings["vertical_scrollbar"] == "show":
            self.parent.scrolly.config(width = 0)
            settings["vertical_scrollbar"] = "hide"
        else:
            settings["vertical_scrollbar"] = "show"
            self.parent.scrolly.config(width = 20)

        if settings["quiet_mode"] == "check":
            settings["quiet_mode"] = "uncheck"
        else:
            settings["quiet_mode"] = "check"

        self.loader.upload_setting(newSetting=settings)



# =======================================================================
    def Syntax_Highlight(self,*args, **kwargs):

        if self.selectedExtension in (".ino",):
            self.Higlighter.initial_highlight(lexer=ArduinoLexer())

        elif self.selectedExtension in (".ps1",".psm1",):
            self.Higlighter.initial_highlight(lexer=PowerShellLexer())
        elif self.selectedExtension in (".pro",".pl",):
            self.Higlighter.initial_highlight(lexer=PrologLexer())
        elif self.selectedExtension in (".py",".pyw",):
            self.Higlighter.initial_highlight(lexer=PythonLexer())
        elif self.selectedExtension in (".reg ",):
            self.Higlighter.initial_highlight(lexer=RegeditLexer())
        elif self.selectedExtension in (".rb",".rbw",):
            self.Higlighter.initial_highlight(lexer=RubyLexer())
        elif self.selectedExtension in (".scala",):
            self.Higlighter.initial_highlight(lexer=ScalaLexer())
        elif self.selectedExtension in (".swift",):
            self.Higlighter.initial_highlight(lexer=SwiftLexer())
        elif self.selectedExtension in (".txt",):
            self.Higlighter.initial_highlight(lexer=TextLexer())
        elif self.selectedExtension in (".vbs",):
            self.Higlighter.initial_highlight(lexer=VBScriptLexer())
        elif self.selectedExtension in (".vb",):
            self.Higlighter.initial_highlight(lexer=VbNetLexer())
        elif self.selectedExtension in (".xml",".xsl",):
            self.Higlighter.initial_highlight(lexer=XmlLexer())
        elif self.selectedExtension in (".yml",".yaml",):
            self.Higlighter.initial_highlight(lexer=YamlLexer())
# --------------------------------------------------------------------
# --------------------------------------------------------------------
        elif self.selectedExtension in (".html",".htm", ".xhtml" ,".xslt",):
            self.Higlighter.initial_highlight(lexer=HtmlLexer())
        elif self.selectedExtension in (".hs",):
            self.Higlighter.initial_highlight(lexer=HaskellLexer())
        elif self.selectedExtension in (".java",):
            self.Higlighter.initial_highlight(lexer=JavaLexer())
        elif self.selectedExtension in (".js",):
            self.Higlighter.initial_highlight(lexer=JavascriptLexer())
        elif self.selectedExtension in (".json",):
            self.Higlighter.initial_highlight(lexer=JsonLexer())
        elif self.selectedExtension in (".kt",):
            self.Higlighter.initial_highlight(lexer=KotlinLexer())
        elif self.selectedExtension in (".lua",".wlua",):
            self.Higlighter.initial_highlight(lexer=LuaLexer())
        elif self.selectedExtension in (".m",):
            self.Higlighter.initial_highlight(lexer=MatlabLexer())
        elif self.selectedExtension in (".m",):
            self.Higlighter.initial_highlight(lexer=MarkdownLexer())
        elif self.selectedExtension in (".pl",".perl",):
            self.Higlighter.initial_highlight(lexer=PerlLexer())
        elif self.selectedExtension in (".php",):
            self.Higlighter.initial_highlight(lexer=PhpLexer())
# --------------------------------------------------------------------
        elif self.selectedExtension in (".bash" ,".sh" ,".ksh",):
            self.Higlighter.initial_highlight(lexer=BashLexer())
        elif self.selectedExtension in (".bat" ,".cmd",):
            self.Higlighter.initial_highlight(lexer=BatchLexer())
        elif self.selectedExtension in (".c" ,".h",):
            self.Higlighter.initial_highlight(lexer=CLexer())
        elif self.selectedExtension in (".lisp" ,".cl",):
            self.Higlighter.initial_highlight(lexer=CommonLispLexer())
        elif self.selectedExtension in (".cpp" ,".c++",".cxx",):
            self.Higlighter.initial_highlight(lexer=CppLexer())
        elif self.selectedExtension in (".css",):
            self.Higlighter.initial_highlight(lexer=CssLexer())
        elif self.selectedExtension in (".cs",):
            self.Higlighter.initial_highlight(lexer=CSharpLexer())
        elif self.selectedExtension in (".cob",):
            self.Higlighter.initial_highlight(lexer=CobolLexer())
        elif self.selectedExtension in (".lisp",".cl",):
            self.Higlighter.initial_highlight(lexer=CommonLispLexer())
        elif self.selectedExtension in (".fs",):
            self.Higlighter.initial_highlight(lexer=FSharpLexer())
        elif self.selectedExtension in ".go":
            self.Higlighter.initial_highlight(lexer=GoLexer())
        else:
            self.Higlighter.initial_highlight(lexer=TextLexer())

######################################################  ######################################################
