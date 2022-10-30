import dns.resolver
from tkinter import *
from dnsfunctions import *

# setting the resolver
my_resolver = dns.resolver.Resolver()


def func_button_go():
    queryhost = hostentry.get()
    for s in open_file():
        result = resolve_host(queryhost, s)
        for server in result:
            if result[server] == 'error':
                resultstring = '🚫', server, '->', result[server]
                labelservers = Label(master=frame, anchor='w')
            else:
                resultstring = '✅', server, '->', result[server]
                labelservers = Label(master=frame, anchor='w')
            labelservers.pack()
            labelservers.config(text=resultstring)


# Open servers.txt - create new servers.txt if none is found


servers_list = open_file()

# Define window

window = Tk()
window.title('DNS-Checker')
window.geometry('400x300')
window.config(pady=20, padx=20)

# Define label for Entry

hostnamelabel = Label(text='Query Host:')
hostnamelabel.grid(column=0, row=0)

# Define entrybox

hostentry = Entry()
hostentry.insert(0, 'google.com')
hostentry.focus_set()
hostentry.grid(column=1, row=0)

# Define Button

gobutton = Button(text='Query!', command=func_button_go)
gobutton.grid(column=2, row=0)

# Define frame for output

frame = Frame(bd=4, highlightthickness=4)
frame.grid(column=0, row=1, columnspan=2, rowspan=2)

window.mainloop()
