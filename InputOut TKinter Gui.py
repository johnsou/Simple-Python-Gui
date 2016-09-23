


from Tkinter import *
import tkFileDialog, tkMessageBox
import datetime, os
import StringIO



class App:

    def __init__(self, master):
        self.packet = StringIO.StringIO()
        self.master = master
        self.start()

    def start(self):
        self.master.title("Write your Title")

        self.now = datetime.datetime.now()
        label01 = "Write your application what it's going to do!"
        Label(self.master, text=label01).grid(row=0, column=1, sticky=W)

        Label(self.master, text="Input file: ").grid(row=1)
        self.fileloc = Entry(self.master)
        self.fileloc["width"] = 60
        self.fileloc.focus_set()
        self.fileloc.grid(row=1, column=1)

        self.open_file = Button(self.master, text="Browse...", command=self.browse_file)
        self.open_file.grid(row=1, column=2)


        Label(self.master, text="Output directory: ").grid(row=3)
        self.outdir = Entry(self.master)
        self.outdir["width"] = 60
        self.outdir.grid(row=3, column=1)

        self.open_dir = Button(self.master, text="Browse...", command=self.browse_dir)
        self.open_dir.grid(row=3, column=2)

        self.adj = StringVar()
        self.adj.set("1")

        label02 = ()
        Label(self.master, text=label02).grid(row=7, column=1, sticky=W)

        self.submit = Button(self.master, text="SUBMIT", command=self.start_processing, fg="red")
        self.submit.grid(row=8, column=2, sticky=E)

    def browse_file(self):
        self.filename = tkFileDialog.askopenfilename(title="Open DATA file...")
        self.fileloc.insert(0,self.filename )#set the location to fileloc var

    def browse_dir(self):
        self.outdir_path = tkFileDialog.askdirectory(title="Open Dir file...")
        self.outdir.insert(0,self.outdir_path)#set the location to fileloc var

    def start_processing(self):
        #print "start processing file..."
        try:

            self.import_data(self.filename)
            self.done_processing()
        except:
            print "Any Error",
            tkMessageBox.showerror("")

    def done_processing(self):
        tkMessageBox.showinfo("Successful" % (self.generate_filename(), self.filename,self.adj.get()))
        self.start()


root = Tk()
app = App(root)
root.mainloop()