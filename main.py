import art
from dnsfunctions import *

# setting the resolver
my_resolver = dns.resolver.Resolver()

# list of DNS servers to query for testing with a wrong IP address

print(art.image)


# Open servers.txt - create new servers.txt if none is found



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
