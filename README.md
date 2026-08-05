# AfterShock

AfterShock is a beginner SOC Analyst tool. Its main function is to help myself (and other beginner cybersecurity students) understand IP Enrichment and Log Analysis.

# Why did I make this?

I made this tool because when I first got into cybersecurity through my university course and TryHackMe, I was able to understand the material and what was being presented. Yet, I wished I had tools with some training wheels attached — something that fed my curiosity a bit further. TryHackMe SOC simulations were great, but I found that when it came to IP Enrichment specifically, there wasn't a lot of hands-on material (or at least, not that I could find). So I made AfterShock for myself, and for others who might have the same level of curiosity or a desire for simple, beginner-friendly tools.

# How does it work?

It's quite straightforward! Upon running main.py, the user is prompted with 3 choices:

1.Parse an Apache or Nginx log
2.Enrich an IP
3.Extract an IP from a log and enrich it

Upon selecting any of the above operations, a digestible report is generated, filled with various bits of information that the tool has managed to find. I'll be expanding the amount of information it can generate over time!

# Example output

Log parsing:

========================================
Apache / Nginx Log Analysis
========================================
Source IP : 127.0.0.1
Timestamp : 2026-08-05 19:40:00+03:00
HTTP Request
--------------------
Method    : GET
Path      : /index.html
Version   : HTTP/1.1
Response
--------------------
Status    : 200
========================================

IP enrichment:

========================================
IP Enrichment
========================================
IP          : 8.8.8.8
Start IP    : 8.8.8.0
End IP      : 8.8.8.255
Reverse DNS : dns.google
ASN         : 15169
Country     : US
Organisation: GOOGLE
========================================
End Of Enrichment
========================================
Requirements
Python 3.x

Getting started
bash
git clone https://github.com/<LuckyCookie707>/aftershock.git
cd aftershock
python main.py

You'll also need a local copy of the ip2asn-v4.tsv database for IP enrichment to work — place it in AfterShock and update the path in main.py line 18 if needed.

# Features
Apache and Nginx log parsing
IP enrichment (ASN, country, organisation, reverse DNS)
Combined mode: extract an IP straight out of a log line and enrich it
User-friendly, beginner-friendly CLI output
# Under the hood
Binary search over the ip2asn IP range dataset for fast lookups
# Rough roadmap
Batch processing: run the tool against a full log file, enrich all unique IPs (with deduplication), and generate a summary table instead of one report per IP
Output explanations: add context to enrichment results so beginners understand why a given ASN, country, or org matters, not just what it is
Suspicious vs. normal flagging: surface possible red flags (e.g. high request volume, known bad ASN) with the reasoning shown, not just a black-box score
Practice mode: bundle sanitized sample logs (including simulated scan/attack patterns) so users can see what a real anomaly looks like end-to-end

# Feedback

This project is very much a work in progress, and I'd love feedback from anyone in the security community — especially fellow students or beginner analysts. Feel free to open an issue or reach out directly.

# License

MIT
