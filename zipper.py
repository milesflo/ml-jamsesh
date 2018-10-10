# Used to join csv files

import os
import csv

output = open('output.csv', 'wb')

for filename in os.listdir('./dataset'):
  with open('./dataset/{}'.format(filename), 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='\'')
    spamwriter = csv.writer(output, delimiter=',', quotechar='\'')
    for row in spamreader:
      spamwriter.writerow(row)
