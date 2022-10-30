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
window.config(pady=10, padx=10)

# Define label for Entry

hostnamelabel = Label(anchor='e', text='Query Host:')
hostnamelabel.grid(column=0, row=0)

# Define entry box

hostentry = Entry()
hostentry.config(width=20)
hostentry.insert(0, 'google.com')
hostentry.focus_set()
hostentry.grid(column=0, row=1)

# Define Button

gobutton = Button(text='Query!', anchor='center', command=func_button_go)
gobutton.grid(column=0, row=2)

# Explanation label
explabel = Label(width=30, anchor='w', text='DNS Servers are configured in servers.txt')
explabel.grid(column=0, row=3)


# Define frame for output

frame = Frame(bd=0, highlightthickness=1, bg='black')
frame.grid(column=0, row=4, columnspan=1, rowspan=2)


# fill with dns entries:
dns_list = open_file()

# Creating a dict with DNS entries to display in the window.
label_dict = {}

for s in dns_list:
    label_dict.update({s: Label(frame, text=str(f'🤷 {s} -> unknown'), width=50, anchor='w')})
for item in label_dict:
    label_dict[item].pack()

window.mainloop()
