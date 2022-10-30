from dnsfunctions import *

# setting the resolver
my_resolver = dns.resolver.Resolver()


# function for the resolve button
def func_button_go():
    for widgets in frame.winfo_children():
        widgets.destroy()
    queryhost = hostentry.get()
    labelservers = Label(master=frame, anchor='w', text=f'Resolving {queryhost}')
    labelservers.pack()
    for s in open_file():
        result = resolve_host(queryhost, s)
        for server in result:
            if result[server] == 'error':
                resultstring = str(f"🚫 {server} -> {result[server]}")
                labelservers = Label(master=frame, anchor='w', width=20)
                # using pack here for simplicity
                labelservers.pack()
                labelservers.config(text=resultstring)
            else:
                resultstring = str(f"✅ {server} -> {result[server]}")
                labelservers = Label(master=frame, anchor='w', width=20)
                # using pack here for simplicity
                labelservers.pack()
                labelservers.config(text=resultstring)


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

# Explanation label
explabel = Label(frame, text='DNS Servers are configured in servers.txt')
explabel.pack()

window.mainloop()
