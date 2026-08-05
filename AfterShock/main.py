# This is a program that i've made from scratch. It contains simple cybersecurity tools. I will be adding more as i get ideas : )
import socket
import apachelogs
import apachelogparse
import time
from ipenrichment import IPEnrichment
import os



print("=" * 40)
print("AfterShock v1.0")
print("Beginner SOC Investigation Tool")
print("=" * 40)

print("Loading IP database...")

if not os.path.exists("ip2asn-v4.tsv"):
    print("IP Database Required...")
    print("Please download the IPv4 database here: ")
    print("--- https://iptoasn.com/cloudflare-blocks-unverified-urls-and-doesnt-respond/ip2asn-v4.tsv.gz ---")
    print("Place the extracted file into the project folder and rerun AfterShock")
    exit()

enrichment= IPEnrichment("ip2asn-v4.tsv") # If you change the IP Database file name then make sure to change it here as well!!!

print("Database Loaded Successfully...")

time.sleep(2)

while True: 
    try: 
        operation = input("1.Apache and Nginx Log Parsing\n2.IP Enrichment\n3.Log Parse + Enrich\nWhich Operation would you like to run?: ")
    except:
        print("\nExiting Program...")

    match operation:

        case "1":
            try:
          
                log = input("Please enter the log that needs to be parsed or press CTRL + c to end program: ")
                event = apachelogparse.logparser(log)

                apachelogparse.display(event)

            except:
                print("\nExiting Program...")
                break


        case "2":
            try:
                ip = input("Please enter the IP that you would like to enrich or press CTRL + C to end program: ")

                info = enrichment.lookup(ip)
                enrichment.display(ip,info)
            except:
                 print("\nExiting Program...")
                 break

        case "3":


            try:
                log = input("Please enter the log that needs to be parsed and enriched or press CTRL + C to end program: ")


                result = apachelogparse.logIP(log)

                print(result)

                info= enrichment.lookup(result)

                enrichment.display(result, info)

            except:
                print("\nExiting Program...")
                break


        case _:
            print("Ending Program...")
            break
                
        





   

