import csv
from student import Boy
from student import Girl
from generate import generate
import logging

g = []
b = []


logging.basicConfig(filename='L.log', filemode='w', format='%(asctime)s %(levelname) s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
generate()
with open('GIRL.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        g.append(Girl(row['Name'], row['Attractiveness'], row['Intelligence'], row['Budget']))

with open('BOY.csv','r') as csvfile1:
    reader = csv.DictReader(csvfile1)
    for row in reader:
        b.append(Boy(row['Name'], row['Attractiveness'], row['Intelligence'], row['Minimum_req'], row['Budget']))
for a in g:
    for k in b:
        if ( a.status == 'single' and k.status == 'single' and a.checkElligible(k) and k.checkElligible(a) ):
            k.status = 'in_relation'
            a.status = 'in_relation'
            k.gf = a.name
            a.bf = k.name
            logging.info('Is commited to ' +  a.name + ' with ' + k.name)
            break

for x in g :
    if x.status != 'single':
        print(x.name + ' is a commited to: ' + x.bf)
        