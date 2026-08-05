import csv
import ipaddress
import bisect
import socket

class IPEnrichment:

    def __init__(self,database_file):
        self.records = []
        self.starts = []


        with open(database_file, newline="", encoding="utf-8") as file:
            reader= csv.reader(file, delimiter="\t")



            for row in reader:

                start = ipaddress.ip_address(row[0])
                end = ipaddress.ip_address(row[1])

                self.starts.append(int(start))
                self.records.append({
                    "start": int(start),
                    "end": int(end),
                    "asn": row[2],
                    "country": row[3],
                    "organisation": row[4]
                })



    def lookup(self, ip):

        ip = int(ipaddress.ip_address(ip))
       #print(type(self.starts[0])) ---diagnostics
        #print(self.starts[0]) ---- diagnostics

        idx = bisect.bisect_right(self.starts, ip) - 1

        if idx < 0:
            return None
        record = self.records[idx]
        if record['start'] <= ip <= record['end']:
            return record
        return None




    def reverse_dns_search(self, ip):
        try:
            hostname,_,_= socket.gethostbyaddr(ip)
            return hostname
        except socket.herror:
            return "No PTR Record Found"

    

    def display(self,ip,record): 
        if record is None:
            print("No record found")
            return
        print("=" * 40)
        print("IP Enrichment")
        print("=" * 40)
        print(f"IP          : {ip}")
        print(f"Start IP    : {ipaddress.ip_address(record['start'])}")
        print(f"End IP      : {ipaddress.ip_address(record['end'])}")
        print(f"Reverse DNS: {self.reverse_dns_search(ip)}")
        print(f"ASN         : {record['asn']}")
        print(f"Country     : {record['country']}")
        print(f"Organisation: {record['organisation']}")
        print("=" * 40)
        print("End Of Enrichment")
        print("=" * 40)