import tkinter as tk
import tkinter.ttk as ttk
import re, webbrowser

class MainApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.initUI()
    
    
    def prepString(self, string):

        xclusive_list = ['AND', 'OR', 'NOT', 'NOR', 'XNOR', 'NAND']
        final = ''
        string = re.sub('[^A-Za-z0-9]+', ' ', string)
        word_list = string.split(' ')
        for word in word_list:
            if (word.upper() in xclusive_list) or (word == ''):
                final+= word.upper()+' '
                
            else:
                word = '"' + word + '"'
                final+=word + ' '
        return final
  

    def runQuery(self, website):
    
        what_and_where = self.entry_what.get() + " " + self.entry_where.get()
        string = self.prepString(what_and_where)
        query = r'https://www.google.com/search?q='
        query+=string.replace(' ', '+') + website
        webbrowser.open_new_tab(query)
                    
    def initUI(self):
        #GUI init
        self.master.title("PySearch v1.0")
        self.pack(fill='both', expand=1)
        
        #gridconfig
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        
        
        self.what_label = ttk.Label(self, text='What:')
        self.what_label.grid(column=0, row=0, padx=5, pady=5, sticky='e')
        
        self.entry_what = ttk.Entry(self, width=35)
        self.entry_what.grid(column=1, row=0, sticky='ew', padx=5, pady=5)
        
        self.where_label = ttk.Label(self, text='Where:')
        self.where_label.grid(column=0, row=1, padx=5, pady=5, sticky='e')
        
        self.entry_where = ttk.Entry(self, width=25)
        self.entry_where.grid(column=1, row=1, sticky='ew', padx=5, pady=5)
        
        #Buttons
        self.lever_btn = ttk.Button(self, text='jobs.lever.co')
        self.lever_btn.config(command=lambda: self.runQuery('site:+https://jobs.lever.co/*'))
        self.lever_btn.grid(column=2, row=0, padx=10, pady=10, sticky='ew')
        
        self.work_btn = ttk.Button(self, text='apply.workable.com')
        self.work_btn.config(command=lambda: self.runQuery('site:+https://apply.workable.com/*'))
        self.work_btn.grid(column=3, row=0, padx=10, pady=10, sticky='ew')
        
        self.green_btn = ttk.Button(self, text='boards.greenhouse.io')
        self.green_btn.config(command=lambda: self.runQuery('site:+https://boards.greenhouse.io/*'))
        self.green_btn.grid(column=2, row=1, padx=10, pady=10, sticky='ew')
        
        self.job_btn = ttk.Button(self, text='jobs.jobvite.com')
        self.job_btn.config(command=lambda: self.runQuery('site:+https://jobs.jobvite.com/*/job/*'))
        self.job_btn.grid(column=3, row=1, padx=10, pady=10, sticky='ew')
        
        self.clear_btn = ttk.Button(self, text='clear')
        
        self.clear_btn.grid(column=0, row=4, columnspan=4, sticky='ew', padx=10, pady=10)
    
    

        

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp()
    root.geometry('700x150')
    root.minsize(700, 150)
    root.mainloop()