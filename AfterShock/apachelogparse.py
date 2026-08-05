from apachelogs import LogParser, COMBINED
import ipaddress




parser = LogParser(COMBINED)

def logparser(log_line):

    entry = parser.parse(log_line)
    method, path, version = entry.request_line.split()

    return {
        "IP ADDRESS": entry.remote_host,
        "Time Stamp": entry.request_time,
        "Request": entry.request_line,
        "Method": method,
        "Path" : path,
        "Version": version,
        "Status": entry.final_status
    }

def ApachelogIP(log_line):

    entry = parser.parse(log_line)
    return entry.remote_host

def display(event):

    print("=" * 40)
    print("Apache / Nginx Log Analysis")
    print("=" * 40)

    print(f"Source IP : {event['IP ADDRESS']}")
    print(f"Timestamp : {event['Time Stamp']}")

    print()

    print("HTTP Request")
    print("-" * 20)

    print(f"Method    : {event['Method']}")
    print(f"Path      : {event['Path']}")
    print(f"Version   : {event['Version']}")

    print()

    print("Response")
    print("-" * 20)

    print(f"Status    : {event['Status']}")

    print("=" * 40)