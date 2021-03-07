#!/usr/bin/env python3
import sys

import dns.resolver, dns.exception

stderr = sys.stderr

class DNSresponse:
    """data object for DNS answer
    response_full - full DNS response raw
    answer - DNS answer to the query
    """
    def __init__(self, response_full=[], answer=[]):
        self.response_full = response_full
        self.answer = answer

class Nslookup:
    """Object for DNS resolver, init with optional specific DNS servers"""
    def __init__(self, dns_servers=[]):
        self.dns_resolver = dns.resolver.Resolver()

        if dns_servers:
            self.dns_resolver.nameservers = dns_servers


    def base_lookup(self, domain, record_type):
        """Get the DNS record, if any, for the given domain.
        https://github.com/xn-twist/xn-twist/pull/31/files
        """
        # set DNS server for lookup
        try:
            # get the dns resolutions for this domain
            answer = self.dns_resolver.query(domain, record_type)
            return answer
        except dns.resolver.NXDOMAIN:
            # the domain does not exist so dns resolutions remain empty
            pass
        except dns.resolver.NoAnswer as e:
            # domains existing but not having AAAA records is common
            if record_type != 'AAAA':
                print("Warning: ", e, file=stderr)
        except dns.resolver.NoNameservers as e:
            print("Warning: ", e, file=stderr)
        except dns.exception.DNSException as e:
            print("Error: DNS exception occurred:", e, file=stderr)


    def base_dns_lookup(self, domain, record_type):
        if record_type in ['A','AAAA']:
            dns_answer = self.base_lookup(domain, record_type)
            if dns_answer:
                dns_response = [answer.to_text() for answer in dns_answer.response.answer]
                ips = [ip.address for ip in dns_answer]
                return DNSresponse(dns_response, ips)
        else:
            raise ValueError("Expected record_type 'A' or 'AAAA'")

        return DNSresponse()


    def dns_lookup(self, domain):
        return self.base_dns_lookup(domain,"A")


    def dns_lookup6(self, domain):
        return self.base_dns_lookup(domain, "AAAA")


    def dns_lookup_all(self, domain):
        resp_a = self.base_dns_lookup(domain,"A")
        resp_aaaa = self.base_dns_lookup(domain,"AAAA")
        return DNSresponse([*resp_a.response_full,*resp_aaaa.response_full],[*resp_a.answer,*resp_aaaa.answer])


    def soa_lookup(self, domain):
        soa_answer = self.base_lookup(domain, "SOA")
        if soa_answer:
            soa_response = [answer.to_text() for answer in soa_answer.response.answer]
            soa = [next(answer.__iter__()).to_text() for answer in soa_answer.response.answer]
            return DNSresponse(soa_response, soa)
        return DNSresponse()
