import dns.resolver

# setting the resolver
my_resolver = dns.resolver.Resolver()

# list of DNS servers to query for testing with a wrong IP address
dns_list = ['8.8.8.8', '8.8.4.4', '1.2.3.4', '192.168.178.1']
records_dict_list = []

for server in dns_list:
    try:
        my_resolver.nameservers = [server]
        answers = my_resolver.resolve('google.com', 'A')
        records_dict_list.append({str(server): str(answer) for answer in answers})
    except dns.resolver.LifetimeTimeout:
        records_dict_list.append({str(server): 'error'})

print('Nameserver Status')

for entry in records_dict_list:
    for key in entry:
        if entry[key] == 'error':
            print('🚫', key, entry[key])
        else:
            print('✅', key, entry[key])
print('Done')