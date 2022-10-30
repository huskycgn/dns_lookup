import art
from dnsfunctions import *


print(art.image)

# Open servers.txt - create new servers.txt if none is found
# Calling function for servers.txt file

dns_server_list = open_file()

# getting user input

hostname = input('Please enter a hostname (e.g. google.com):\n')
records_dict_list = []

# iterate through server list
print('Nameserver  Resolved IP')

# First ask the default system DNS for an answer.

funcset = resolve_host_local(hostname)
if funcset['Local-DNS'] == 'error':
    # print(records_dict_list)
    print('🚫', 'Local-DNS', '->', funcset['Local-DNS'])
else:
    print('✅', 'Local-DNS', '->', funcset['Local-DNS'])

# Now iterate through the server list.

for server in dns_server_list:
    funcset = resolve_host(hostname, server)
    records_dict_list.append(funcset)
    if funcset[server] == 'error':
        # print(records_dict_list)
        print('🚫', server, '->', funcset[server])
    else:
        print('✅', server, '->', funcset[server])
