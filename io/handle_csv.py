import csv
import numpy as np


def create_csv():
    with open('../tmp/test.csv', 'w+', newline='') as f:
        wt = csv.writer(f, delimiter=',')
        wt.writerow(['A', 'B', 'C'])
        for i in range(10):
            wt.writerow(np.random.randint(0,100,size=3))

if __name__ == '__main__':
    create_csv()