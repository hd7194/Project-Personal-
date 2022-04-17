from tkinter.filedialog import *
from tkinter import messagebox
from Spellcheck import Spelling
from stringcolor import *
class LE:
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisSpellCheck = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None


    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad-Bloc-notes-icon.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled - Language Enhancer")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-align
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-align
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",command=self.__newFile,accelerator="Ctrl+N")

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",command=self.__openFile,accelerator="Ctrl+O")
                  
        # To save current file
        self.__thisFileMenu.add_command(label="Save",command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

        # TO give a feature of undo
        self.__thisEditMenu.add_command(label="Undo",command=self.__undo,accelerator="Ctrl+Z")

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut,accelerator="Ctrl+X")

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy, accelerator="Ctrl+C")

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste, accelerator="Ctrl+V")
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # Configuring Menu Bar
        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # Adding SpellCheck
        self.__thisSpellCheck.add_command(label="Spelling",
                                          command=self.__retrieve_input,accelerator="Ctrl+F")

        self.__thisMenuBar.add_cascade(label="SpellCheck",
                                          menu=self.__thisSpellCheck)

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Language Enhancer")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")


            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Language Enhancer")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

            # Change the window title
            self.__root.title(os.path.basename(self.__file) + " - Language Enhancer")

    def __retrieve_input(self):
        input = self.__thisTextArea.get(1.0, END)
        b = str(input)
        z = Spelling.scan(b)
        for i in z:
            self.__thisTextArea.replace(1.0, END, self.__thisTextArea.get(1.0, END).replace(i, "\u0332".join(i)))


    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def __undo(self):
        self.__thisTextArea.event_generate("<<Undo>>")

    def run(self):
        # Run main application
        self.__root.mainloop()

    # Run main appLication
    __root.bind_all("<Control-f>",__retrieve_input)
    __root.bind_all("<Control-n>",__newFile)
    __root.bind_all("<Control-o>", __openFile)

le= LE(width=600, height=400)
le.run()

