import dns.resolver

# setting the resolver
my_resolver = dns.resolver.Resolver()

# list of DNS servers to query for testing with a wrong IP address

try:
    with open(file='servers.txt', mode='r') as server_file:
        dns_list = server_file.read().splitlines()
except FileNotFoundError:
    dns_list = ['8.8.8.8', '8.8.4.4', '192.168.178.1']
    print('No "servers.txt" found, using default DNS-Server list:')
    for i in dns_list:
        print(i)

hostname = input('Please enter a hostname (e.g. google.com):\n')

records_dict_list = []

# iterate through server list

for server in dns_list:
    try:
        my_resolver.nameservers = [server]
        answers = my_resolver.resolve(hostname, 'A')
        records_dict_list.append({str(server): str(answer) for answer in answers})
    except dns.resolver.LifetimeTimeout:
        records_dict_list.append({str(server): 'error'})

print('Nameserver  Resolved IP')

for entry in records_dict_list:
    for key in entry:
        if entry[key] == 'error':
            print('🚫', key, entry[key])
        else:
            print('✅', key, entry[key])