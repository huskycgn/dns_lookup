from dnsfunctions import *
from tkinter import *


# function for the query button
def func_button_go():
    global label_dict
    reset_entries()
    # get host to resolve.
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


def reset_entries():
    global label_dict, local_dns_label
    # fill with dns entries:
    for wi in frame.winfo_children():
        wi.destroy()
    dns_list = open_file()

    # Creating a dict with DNS entries to display in the window.

    for s in dns_list:
        label_dict.update({s: Label(frame, text=str(f'🤷 {s} -> unknown'), width=50, anchor='w')})
    for item in label_dict:
        label_dict[item].pack()


servers_list = open_file()

label_dict = {}

# Define window

window = Tk()
window.title('DNS-Checker')
window.geometry('500x400')
window.config(pady=10, padx=10)

# Define label for Entry

hostnamelabel = Label(window, anchor='e', text='Query Host:')
hostnamelabel.grid(column=0, row=0)

# Define entry box

hostentry = Entry(window)
hostentry.config(width=20)
hostentry.insert(0, 'google.com')
hostentry.focus_set()
hostentry.grid(column=0, row=1)

# Define Button

gobutton = Button(window, text='Query!', anchor='center', command=func_button_go)
gobutton.grid(column=0, row=2)

# Explanation label
explabel = Label(window, width=30, anchor='w', text='DNS Servers are configured in servers.txt')
explabel.grid(column=0, row=3)

# Define frame for output

frame = Frame(window, bd=0, highlightthickness=1, bg='black')
frame.grid(column=0, row=4, columnspan=1, rowspan=2)

reset_entries()

window.mainloop()
