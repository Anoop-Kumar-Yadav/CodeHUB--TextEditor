import csv
import os
import tkinter as tk
from tkinter.constants import ANCHOR,LEFT

############################################################################################################
class PopUps(tk.Frame):
    def __init__(self,parent,*args, **kwargs):

        tk.Frame.__init__(self,*args, **kwargs)
        self.parent = parent.parent.textArea
        
        self.bind("<FocusOut>",self.backtoEditor)
        self.themeColor = parent.Higlighter.definingColor()
        self.config(bg=self.themeColor["statusbar_bg"])

############################################################################################################
    def clearFrame(self,*args):
        _list = self.winfo_children()
        for child in _list:
            if child.winfo_children():
                _list.extend(child.winfo_children())
        for item in _list:
            item.place_forget()
            item.pack_forget()

############################################################################################################
    def about(self,*args, **kwargs):
        self.clearFrame()
        self.place(relx = 0.25,rely=0.2,relwidth=0.5,relheight=0.6)

        aboutFilePath = os.path.abspath("data\\config\\about.txt")
        iconImage = os.path.abspath("data\\images\\ide12.png")

        with open(file=aboutFilePath,mode="r") as file:
            text_ = file.read()

        Quitdialog = tk.Button(self,text=" X ",relief="flat",activebackground="red",background="white",command = self.backtoEditor)
        Quitdialog.place(relx=0.91, rely=0.0, height=35,width=60)

        detailsArea = tk.Label(self,text=text_,font=("Tahoma",10),bg=self.themeColor["statusbar_bg"],fg=self.themeColor["statusbar_fg"])
        detailsArea.place(relx=0.0,rely=0.6,relwidth=1.0,relheight=0.4)

############################################################################################################
    def selectFileType(self,*args, **kwargs):
        self.clearFrame()
        self.place(relx = 0.25,rely=0.2,relwidth=0.5,relheight=0.6)
        aboutFilePath = self.parent.parent.menuBar.getFiletypes()
#------------------------------------------------------------------------------------------------------------
        def intial_list(*args, **kwargs):
            names = []
            xtnsion =[]
            
            for i in aboutFilePath:
                names.append(i[0])
                xtnsion.append(i[1].replace("*",""))
            
            names.pop(0)
            xtnsion.pop(0)
            if kwargs["intial"] == "type" :    
                return names
            
            elif kwargs["intial"] == "ext" :
                return xtnsion

#------------------------------------------------------------------------------------------------------------
        def setExt(*args, **kwargs):  
            selExt = intial_list(intial="ext")[detailsArea.index(ANCHOR)]
            self.parent.parent.menuBar.setExtension(applyExt = selExt)
            instVar.set(detailsArea.get(ANCHOR))

#------------------------------------------------------------------------------------------------------------
        instVar = tk.StringVar()
        instructionLabel = tk.Label(self,textvariable=instVar,font=("Tahoma",15),relief="sunken")
        instructionLabel.place(relx=0.1,rely=0.0,relwidth=0.8,height=35)

        Quitdialog = tk.Button(self,text=" X ",relief="groove",activebackground="red",background="white",bd=5,command = self.backtoEditor)
        Quitdialog.place(relx=0.91, rely=0.0, height=35,width=60)

        extensionList = tk.StringVar(value=intial_list(intial = "type"))
        detailsArea = tk.Listbox(self,listvariable=extensionList,font=("Tahoma",15),relief="sunken",bg=self.themeColor["statusbar_fg"],
                                 fg=self.themeColor["statusbar_bg"])
        detailsArea.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8) 

        detailsArea.bind("<<ListboxSelect>>",setExt) 

############################################################################################################
    def keyBoardShortcuts(self):
        self.clearFrame()   
        self.place(relx = 0.5,rely=0.0,relheight=0.6,relwidth=0.5)
        textArea = tk.Text(self,bg=self.themeColor["statusbar_bg"],fg=self.themeColor["statusbar_fg"])
        textArea.focus_set() 
        textArea.pack(side=LEFT,fill="both",expand=True)

        sortcutDescription = [
                            "Alt + Up           | This will Iecrease text size by 1 unit.",
                            "Alt + Down         | This will Decrease text size by 1 unit.",
                            "Ctrl + A           | This will select all text.",
                            "Ctrl + C           | This will copy the selected text.",
                            "Ctrl + D           | This will deletes all the text.",
                            "Ctrl + F           | This will open 'find and replace' box.",
                            "Ctrl + H           | This will open 'find and replace' box.",
                            "Ctrl + N           | This will create a new file.",
                            "Ctrl + O           | This will open an existing file.",
                            "Ctrl + Q           | This will close the Editor.",
                            "Ctrl + S           | This will save your changes.",
                            "Ctrl + V           | This will paste the copied text.",
                            "Ctrl + X           | This will cut the selected text.",
                            "Ctrl + Y           | This will  REDO the changes.",
                            "Ctrl + Z           | This will  UNDO the changes.",
                            "Ctrl + Shift + S   | This will save a file.",
                            "Ctrl + Shift + Z   | This will redu the changes you have made."]
                   
        txt_ = "\n".join(sortcutDescription)
        textArea.insert("1.0",txt_)
        textArea.config(state="disabled")
        textArea.bind("<FocusOut>",self.backtoEditor)

############################################################################################################
    def recentFiles(self):
        self.clearFrame()   

#------------------------------------------------------------------------------------------------------------
        def intial_list(*args, **kwargs):
            files = []
       
            FilePath = os.path.abspath("data\\config\\recentfiles.csv")

            with open(file=FilePath,mode="r") as file:
                csvReader = csv.reader(file)

                for row in csvReader: 
                    if len(row) == 0:
                        pass
                    else:
                        files.append(row[0])                   

            files.reverse()

            for file_ in files:
                if os.path.isfile(file_) == True:
                    pass
                else:
                    files.remove(file_)

            return files

#------------------------------------------------------------------------------------------------------------
        self.place(relx = 0.5,rely=0.0,relwidth=0.5,relheight=0.3)
        filesVar = tk.StringVar(value=intial_list())
        textArea = tk.Listbox(self,listvariable=filesVar,bg=self.themeColor["statusbar_bg"],
                                 fg=self.themeColor["statusbar_fg"])
        textArea.focus_set() 
        textArea.pack(side=LEFT,fill="both",expand=True) 
        textArea.bind("<FocusOut>",self.backtoEditor) 
        textArea.bind("<<ListboxSelect>>",lambda x : self.parent.parent.menuBar.open_file(file = textArea.get(ANCHOR))) 

############################################################################################################
    def backtoEditor(self,event=None):
        self.clearFrame()
        self.place_forget()

        self.parent.tag_remove("found","1.0","end")
        self.parent.tag_remove("replace","1.0","end")
        self.parent.tag_remove("move","1.0","end")

############################################################################################################
    def findReplace(self):
        global n
        self.clearFrame()
        self.place(relx = 0.7,rely=0.0,relheight= 0.2,relwidth=0.3)

        findEntryLabel = tk.Label(self,justify=LEFT,text= "Find..",bg=self.themeColor["statusbar_bg"],
                                 fg=self.themeColor["statusbar_fg"])
        findEntryLabel.place(relx=0.017, rely=0.029, height=20)

        replaceEntryLabel = tk.Label(self,text= "Replace with..",justify=LEFT,bg=self.themeColor["statusbar_bg"],
                                 fg=self.themeColor["statusbar_fg"])
        replaceEntryLabel.place(relx=0.017, rely=0.429, height=20 )

        findVar = tk.StringVar()
        findEntry = tk.Entry(self,textvariable=findVar,bg=self.themeColor["statusbar_fg"],
                                 fg=self.themeColor["statusbar_bg"])
        findEntry.place(relx=0.017, rely=0.229, height=20, relwidth=0.678)

        replaceVar = tk.StringVar()
        replaceEntry = tk.Entry(self,textvariable=replaceVar,bg=self.themeColor["statusbar_fg"],
                                 fg=self.themeColor["statusbar_bg"])
        replaceEntry.place(relx=0.017, rely=0.629, height=20, relwidth=0.678)

        indecies = []
        replaceText = {}
        n = 0
#------------------------------------------------------------------------------------------------------------
        def find(event=None,*args, **kwargs):
            indecies.clear()
            
            self.parent.tag_remove("found","1.0","end")

            findText =  findVar.get()
            if findText:
                idx = "1.0"
                while 1:
                    idx = self.parent.search(findText,idx,nocase = 1,stopindex = "end")

                    if not idx: break

                    lastidx = "%s + %dc"%(idx,len(findText))
                    self.parent.tag_add("found",idx,lastidx)
                    indecies.insert(-1,[idx,lastidx])
                    idx = lastidx
                    
                self.parent.tag_config("found",foreground="white")
#------------------------------------------------------------------------------------------------------------
        def moveDown(event=None,*args):
            global n

            if len(indecies) == 0:
                pass
            else:
                try:
                    self.parent.tag_remove("move",indecies[n-1][0],indecies[n-1][1])
                    self.parent.tag_add("move",indecies[n][0],indecies[n][1])

                    self.parent.tag_config("move",foreground="green",background="yellow")
                    replaceText[findVar.get()] = [indecies[n][0],indecies[n][1]]
                except:
                    pass

                if n == len(indecies)-1:
                    n=0
                else:
                    n = n + 1
#------------------------------------------------------------------------------------------------------------
        def onChange(*args):
            global n
            self.parent.tag_delete("move") 
            n=0          
#------------------------------------------------------------------------------------------------------------
        def replace(*args, **kwargs):
            global n
            taxtThatReplace = replaceVar.get()
            print(len(indecies))

            try:
                if len(indecies) == 0:
                    pass
                else:
                    index1 = replaceText[findVar.get()][0]
                    index2 = replaceText[findVar.get()][1]
                    self.parent.get(index1,index2)

                    self.parent.delete(index1,index2)
                    self.parent.insert(index1,taxtThatReplace)

                    indecies.remove([index1,index2])

                    n = n - 1
                    print(index1,index2)
                    moveDown()
                   
            except:
                pass
#------------------------------------------------------------------------------------------------------------
        def replaceAll(*args, **kwargs):
            global n
            taxtThatReplace = replaceVar.get()
            if len(indecies) == 0:
                pass
            else:
                while len(indecies) != 0:
                    for index_ in  indecies:
                        index1 = index_[0]
                        index2 = index_[1]
                        self.parent.delete(index1,index2)
                        self.parent.insert(index1,taxtThatReplace)  
                        indecies.remove([index1,index2])
                    n = 0 
#------------------------------------------------------------------------------------------------------------

        searchButton = tk.Button(self,text=" Find ",command = find)
        replaceButton = tk.Button(self,text=" Replace ",command=replace)
        replaceAllButton = tk.Button(self,text=" Replace All ",command=replaceAll)
   
        downButton = tk.Button(self,text=" Next ",command=moveDown)
        Quitdialog = tk.Button(self,text=" X ",relief="flat",activebackground="red",background="white",command = self.backtoEditor)

        searchButton.place(relx=0.01, rely=0.829, height=20, relwidth=0.25)
        replaceButton.place(relx=0.26, rely=0.829, height=20, relwidth=0.25)
        replaceAllButton.place(relx=0.51, rely=0.829, height=20, relwidth=0.25)
        downButton.place(relx=0.829, rely=0.529, relheight=0.21,relwidth=0.12)
        Quitdialog.place(relx=0.88, rely=0.0, relheight=0.21,relwidth=0.12)

        self.bind("<FocusOut>",self.backtoEditor)
        findVar.trace_add("write",find)
        findVar.trace_add("write",onChange)
        findEntry.focus_set()
############################################################################################################