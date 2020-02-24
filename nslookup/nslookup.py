#!/usr/bin/env python3
import dns.resolver, dns.exception


def base_lookup(domain, record_type, dns_servers=["1.1.1.1", "1.0.0.1"]):
    """Get the DNS record, if any, for the given domain.
    https://github.com/xn-twist/xn-twist/pull/31/files
    """
    dns_records = list()

    # set DNS server for lookup
    dns_resolver = dns.resolver.Resolver()
    dns_resolver.nameservers = dns_servers

    try:
        # get the dns resolutions for this domain
        answer = dns_resolver.query(domain, record_type)
        dns_records = [answer.to_text() for answer in answer.response.answer]
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
        print("DNS resolving error occurred", e)

    return dns_records


def dns_lookup(domain, dns_servers=["1.1.1.1", "1.0.0.1"]):
    return base_lookup(domain, "A", dns_servers)


def soa_lookup(domain, dns_servers=["1.1.1.1", "1.0.0.1"]):
    return base_lookup(domain, "SOA", dns_servers)
