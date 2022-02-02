# PyNslookup
[![PyPi package](https://img.shields.io/pypi/v/nslookup.svg)](https://pypi.python.org/pypi/nslookup)

Simple, sensible high-level DNS lookups in Python (on top of dnspython dns.resolver).

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

# Initialize Nslookup
dns_query = Nslookup()
# Alternatively, the Nslookup constructor supports optional
# arguments for setting custom dns servers (defaults to system DNS),
# verbosity (default: True) and using TCP instead of UDP (default: False)
dns_query = Nslookup(dns_servers=["1.1.1.1"], verbose=False, tcp=False)

ips_record = dns_query.dns_lookup(domain)
print(ips_record.response_full, ips_record.answer)

soa_record = dns_query.soa_lookup(domain)
print(soa_record.response_full, soa_record.answer)
```
