import tkinter as tk
from tkinter.constants import BOTTOM, DISABLED, END, INSERT, NONE, NORMAL, SE, X

class statusBar(tk.Text):

    def __init__(self,parent,*args, **kwargs):
        tk.Text.__init__(self,*args, **kwargs)

        self.parent = parent
        self.config(height=1,background="blue",
                    foreground="white")
      
    def get_details(self):
        index_of_cursor = self.parent.textArea.index(INSERT)
        column_of_cursor = int(index_of_cursor.split(".")[1])+1
        line_of_cursor = int(index_of_cursor.split(".")[0])
        return [line_of_cursor,column_of_cursor]

    def update_statusbar(self):

        self.config(state=NORMAL)

        details = self.get_details()

        separator = " | "

        status = (" Line : %s %s Col : %s "%(details[0],separator,details[1]))

        self.delete("1.0",END)
        self.insert("1.0",status)

        self.config(state=DISABLED)