# soaparse
Sensible high-level DNS lookups in Python, using dnspython dns.resolver, code adopted from [XN-Twist](https://github.com/xn-twist/xn-twist/pull/31/files)

The main purpose and uses of this library:
 - `A` record lookups (typical DNS queries)
 - SOA lookups

A list of raw response string(s) is returned.

#### Usage
```python
import nslookup

domain = "example.com"

# DNS servers default to cloudflare public DNS
ips_record = nslookup.dns_lookup(domain)

soa_record = nslookup.soa_lookup(domain, dns_servers=["10.1.1.1"])

```
