import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_STRINGS)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])