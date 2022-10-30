import dns.resolver
from tkinter import *

# setting the resolver
my_resolver = dns.resolver.Resolver()


# Open servers.txt - create new servers.txt if none is found

def open_file():
    try:
        with open(file='servers.txt', mode='r') as server_file:
            dns_list = server_file.read().splitlines()
            return dns_list
    except FileNotFoundError:
        dns_list = ['8.8.8.8', '8.8.4.4', '192.168.178.1']
        print('No "servers.txt" found, using default DNS-Server list:\n'
              'and creating new servers.txt')
        with open(file='servers.txt', mode='w') as server_file:
            for i in dns_list:
                server_file.writelines(f'{i}\n')
                print(i)
            return dns_list


def resolve_host(host, dnsserver):
    records_dict_list_func = {}
    try:
        my_resolver.nameservers = [dnsserver]
        answers = my_resolver.resolve(host, 'A')
        records_dict_list_func = {str(dnsserver): str(answer) for answer in answers}
    except dns.resolver.LifetimeTimeout:
        records_dict_list_func = {str(dnsserver): 'error'}
    finally:
        return records_dict_list_func


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
