# PyNslookup
[![PyPi package](https://img.shields.io/pypi/v/nslookup.svg)](https://pypi.python.org/pypi/nslookup)

Sensible high-level DNS lookups in Python, using dnspython dns.resolver, code adopted from [XN-Twist](https://github.com/xn-twist/xn-twist/pull/31/files)

The main purpose and uses of this library:
 - `A` record lookups (typical DNS queries)
 - SOA lookups

Returns an object containing two arrays:
 - `response_full`: the full DNS response string(s)
 - `answer`: the parsed DNS answer (list of IPs or SOA string)

#### Usage
```python
from nslookup import Nslookup

domain = "example.com"

# set optional Cloudflare public DNS server
dns_query = Nslookup(dns_servers=["1.1.1.1"])

ips_record = dns_query.dns_lookup(domain)
print(ips_record.response_full, ips_record.answer)

soa_record = dns_query.soa_lookup(domain)
print(soa_record.response_full, soa_record.answer)
```
