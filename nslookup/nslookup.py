#!/usr/bin/env python3
import dns.resolver, dns.exception


# adopted from https://github.com/xn-twist/xn-twist/blob/b0316f3af0ffa1121179efc2035cce07cfb8944f/xn_twist/xn_twist.py#L86
def nslookup(domain):
    """Get the DNS record, if any, for the given domain."""
    dns_records = list()

    # set DNS server for lookup
    dns_resolver = dns.resolver.Resolver()

    # CloudFlare public DNS for lookups
    dns_servers = ['1.1.1.1', '1.0.0.1']
    dns_resolver.nameservers = dns_servers

    try:
        # get the dns resolutions for this domain
        dns_results = dns_resolver.query(domain)
        dns_records = [ip.address for ip in dns_results]
    except dns.resolver.NXDOMAIN:
        # the domain does not exist so dns resolutions remain empty
        pass
    except dns.resolver.NoAnswer as e:
        # the resolver is not answering so dns resolutions remain empty
        print("the DNS servers %s did not answer" % dns_servers, e)
    except dns.resolver.NoNameservers as e:
        # the resolver is not answering so dns resolutions remain empty
        print("the nameservers did not answer", e)
    except dns.exception.DNSException as e:
        print("unknown DNS resolving error occurred", e)

    return dns_records
