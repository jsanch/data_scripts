from sodapy import Socrata
import csv

client = Socrata(site,app_token, username=user, password=passw)


dset = "/resource/xb7i-cvg2.json"
filepath = 'grants-trunc.csv'

client.get(dset)
rowlist = []
with open(filepath,'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rowlist.append(row)

client.replace(dset, rowlist)