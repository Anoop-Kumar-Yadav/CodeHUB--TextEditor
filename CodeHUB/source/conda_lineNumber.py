import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, DISABLED, END, INSERT, LEFT, NONE, X, Y
from tkinter.font import NORMAL

############################################################################################################
class numberLine(tk.Text):
    
    def __init__(self,parent,widget,*args, **kwargs):
        tk.Text.__init__(self,*args, **kwargs)

        self.parent = parent
        self.widget = widget



        self.config(relief="groove",padx=5,spacing1=5)

        self.update_onKeyPress()

        self.widget.bind("<KeyRelease>",self.lineIndicator)

        self.widget.bind("<KeyRelease>",self.update_onKeyPress)

############################################################################################################        
    def get_number_of_line(self):
        last_index = self.widget.index(END) 
        total_line = last_index.split(".")[0]
        return total_line

############################################################################################################
    def lineIndicator(self,event=None):

        details = self.parent.statusbar.get_details()
        self.tag_add("lineIndicator","%s.0"%details[0],"%s.%s"%(details[0],len(str(details[0]))))
        self.tag_config("lineIndicator",foreground="white",background = "black")

############################################################################################################
    @staticmethod

    def gn(num_of_lines):
        for no in range(int(num_of_lines)):
            yield no
        
    def update_onKeyPress(self,event=None):
        self.parent.menuBar.Syntax_Highlight()

        self.parent.statusbar.update_statusbar()

        last_index = self.widget.index(END) 
     
        total_line = last_index.split(".")[0]
        
        num_of_lines = int(total_line) -1

        line_numbers_string = "\n".join(str(no + 1) for no in numberLine.gn(int(num_of_lines)))
       
        self.update_width()
        self.configure(state=NORMAL)
        self.delete(1.0, tk.END)
        self.insert(1.0, line_numbers_string)
        self.configure(state=DISABLED)

############################################################################################################
    def update_width(self):
        
        if self.parent.menuBar.quietmode_var.get() == False:
            width = len(self.get("end-1c linestart",END)) 
        else:
            width = len(self.get("end-1c linestart",END))  
        self.config(width=width)     

############################################################################################################    
    def show_linenumber(self,visible="show"):
        if visible == "show":

            self.repack()
            self.pack(side=LEFT,fill=Y)
            self.update_onKeyPress()

            self.update_width()
        elif visible == "hide":
            self.pack_forget()
            self.config(width=0)        
        else:
            pass

############################################################################################################
    def repack(self):

        self.parent.scrollx.pack_forget()
        self.parent.lineNumber.pack_forget()
        self.parent.textArea.pack_forget()
        self.parent.scrolly.pack_forget()

        self.parent.statusbar.pack(fill=X,side=BOTTOM)
        self.parent.scrollx.pack(side=BOTTOM,fill=X)
        self.parent.lineNumber.pack(side=LEFT,fill=Y)
        self.parent.textArea.pack(side=LEFT,fill=BOTH,expand=True) 
        self.parent.scrolly.pack(side=LEFT,fill=Y)