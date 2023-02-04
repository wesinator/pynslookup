# PyNslookup
[![PyPi package](https://img.shields.io/pypi/v/nslookup.svg)](https://pypi.python.org/pypi/nslookup)

Simple, sensible high-level DNS lookups in Python (on top of dnspython dns.resolver).

#### Purpose and scope
This library is a simple wrapper around [dnspython](https://github.com/rthalley/dnspython), 
to provide high level functions with good error/exception handling, for the most common basic DNS lookup cases.

- `A`, `AAAA` record lookups (typical DNS queries)
- SOA lookups

This is not intended to be a complete wrapper around dnspython library or to handle uncommon edge cases.
Features like DoH are out of scope, and should be done using other libraries or dnspython directly.

### Usage

Returns an object containing two arrays:
 - `response_full`: the full DNS response string(s)
 - `answer`: the parsed DNS answer (list of IPs or SOA string)

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

### Note
This library is oriented around regular UDP DNS.

Using TCP modes in this simple library will create a separate TCP session for 
each query, which can be resource intensive for a large number of queries. 
For this it is recommended to use the more granular `dnspython` API directly.
