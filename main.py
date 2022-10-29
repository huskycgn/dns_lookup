import dns.resolver
import art

# setting the resolver
my_resolver = dns.resolver.Resolver()

# list of DNS servers to query for testing with a wrong IP address

print(art.image)


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
        records_dict_list_func = {str(server): str(answer) for answer in answers}
    except dns.resolver.LifetimeTimeout:
        records_dict_list_func = {str(server): 'error'}
    finally:
        return records_dict_list_func


# Calling function for servers.txt file

dns_server_list = open_file()

# getting user input

hostname = input('Please enter a hostname (e.g. google.com):\n')
records_dict_list = []

# iterate through server list
print('Nameserver  Resolved IP')
for server in dns_server_list:
    funcset = resolve_host(hostname, server)
    records_dict_list.append(funcset)
    if funcset[server] == 'error':
        # print(records_dict_list)
        print('🚫', server, '->', funcset[server])
    else:
        print('✅',server, '->', funcset[server])
