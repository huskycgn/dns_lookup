import dns.resolver


def open_file():
    """Open servers.txt - create new servers.txt if none is found."""
    try:
        with open(file='./servers.txt', mode='r') as server_file:
            dns_list = server_file.read().splitlines()
            return dns_list
    except FileNotFoundError:
        dns_list = ['8.8.8.8', '8.8.4.4', '192.168.178.1']
        print('No "servers.txt" found, using default DNS-Server list\n'
              'and creating new servers.txt')
        with open(file='./servers.txt', mode='w') as server_file:
            for i in dns_list:
                server_file.writelines(f'{i}\n')
                print(i)
            return dns_list


def resolve_host_local(host):
    """resolves the request with system DNS."""
    records_dict_list_local = {}
    # Find a way to get the local DNS IP address
    local_resolver = dns.resolver.Resolver()
    try:
        answers = local_resolver.resolve(host, 'A')
        records_dict_list_local = {'Local-DNS': str(answer) for answer in answers}
    except:
        records_dict_list_local = {str('Local-DNS'): 'error'}
    finally:
        return records_dict_list_local


def resolve_host(host, dnsserver):
    """Does the actual resolving - expects hostname and dnsserver as strings."""
    my_resolver = dns.resolver.Resolver()
    records_dict_list_func = {}
    try:
        my_resolver.nameservers = [dnsserver]
        answers = my_resolver.resolve(host, 'A')
        records_dict_list_func = {str(dnsserver): str(answer) for answer in answers}
    except dns.resolver.LifetimeTimeout:
        records_dict_list_func = {str(dnsserver): 'error'}
    finally:
        return records_dict_list_func


