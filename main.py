import dns.resolver

my_resolver = dns.resolver.Resolver()

reply_list = []
dns_list = ['8.8.8.8', '8.8.4.4', '1.2.3.4']
resp = []

for server in dns_list:
    try:
        my_resolver.nameservers = [server]
        answer = my_resolver.resolve('google.com')
        print(answer.response)
    except dns.resolver.LifetimeTimeout:
        print('Error')