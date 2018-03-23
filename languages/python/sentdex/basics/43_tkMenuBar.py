# Tkinter Menu Bar

'''
' Menus are defined with a bottom-up approach
' the menu items are appended to the menu, appended to menu bar,
' appended to main window, appended to root frame
'''

from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
        
        self.init_window()

    
    def init_window(self):
     
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)
        
        #quitButton = Button(self, text="Quit", command=self.client_exit)
        #quitButton.place(x=0, y=0)
    
        # define a menu bar instance
        menu = Menu(self.master) # this is the menu of the main window
        self.master.config(menu=menu)

        # Create a menu item for the menu bar
        file = Menu(menu)

        # Add a command "Exit" to the menu item
        file.add_command(label="Save") # example
        file.add_command(label="Exit", command=self.client_exit)

        # Add the menu item "File"  to the menu bar as a cascading menu
        menu.add_cascade(label="File", menu=file)
        
        # Add another menu item to the menu bar
        edit = Menu(menu)
        edit.add_command(label="Undo") # not adding a command for now
        menu.add_cascade(label="Edit", menu=edit)
        
    def client_exit(self):
        exit()
        

root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
