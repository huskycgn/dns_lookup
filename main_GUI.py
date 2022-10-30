from dnsfunctions import *
from tkinter import *

# setting the resolver
my_resolver = dns.resolver.Resolver()


# function for the resolve button
def func_button_go():
    global label_dict
    queryhost = hostentry.get()
    for srv in open_file():
        result = resolve_host(queryhost, srv)
        for server in result:
            if result[server] == 'error':
                resultstring = str(f"🚫 {server} -> {result[server]} -> {queryhost}")
                label_dict[srv].config(text=resultstring)
                label_dict[srv].update()
            else:
                resultstring = str(f"✅ {server} -> {result[server]} -> {queryhost}")
                label_dict[srv].config(text=resultstring)
                label_dict[srv].update()


servers_list = open_file()

# Define window

window = Tk()
window.title('DNS-Checker')
window.geometry('500x350')
window.config(pady=20, padx=20)

# Define label for Entry

hostnamelabel = Label(text='Query Host:')
hostnamelabel.grid(column=0, row=0)

# Define entry box

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

# Explanation label
explabel = Label(frame, width=30, anchor='w', text='DNS Servers are configured in servers.txt')
explabel.pack()

# fill with dns entries:
dns_list = open_file()

# Creating a dict with DNS entries to display in the window.
label_dict = {}

for s in dns_list:
    label_dict.update({s: Label(frame, text=str(f'🤷 {s} -> unknown'), width=35, anchor='w')})
for item in label_dict:
    label_dict[item].pack()

window.mainloop()
