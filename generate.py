
import csv
from random import randint
def generate():
    with open('BOY.csv', 'w') as f:
        charnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget', 'Minimum_req']
        write = csv.DictWriter(f, fieldnames = charnames)
        write.writeheader()
        for i in range (1,100):
            s = {'Name': 'boy'+str(i), 'Attractiveness': randint(1,50), 'Intelligence': randint(1,50), 'Budget': randint(950,5000), 'Minimum_req': randint(1,10)}
            write.writerow(s)

    with open('GIRL.csv', 'w') as f2:
        charnames = ['Name', 'Attractiveness', 'Intelligence', 'Budget']
        write = csv.DictWriter(f2, fieldnames=charnames)
        write.writeheader()
        for i in range(1,20):
            s = {'Name': 'girl'+str(i), 'Attractiveness': randint(1,50), 'Intelligence': randint(1,50), 'Budget': randint(900,5000) }
            write.writerow(s)