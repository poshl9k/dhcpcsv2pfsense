
import csv

reader = csv.reader(open('result.csv','r',encoding='utf8'))
next(reader, None)
# with open('xmlresult.txt','a') as tp:
    # tp.write('<dhcpd>\n<lan>\n')
for el in reader:
    mac = el[2]
    ipaddr = el[1]
    descr = el[3]
    dnsserver1 = el[4]
    dnsserver2 = el[5]
    gateway = el[7]
    domain = el[6]
    with open('xmlresult.txt','a',encoding='utf8') as tp:
        template = open('template','r').read().format(**locals())
        tp.write(template)

# with open('xmlresult.txt','a') as tp:
#     tp.write('\n</lan>\n</dhcpd>')
