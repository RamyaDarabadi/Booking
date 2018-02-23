import csv

class Booking(object):
    def main(self):
        with open(self.filename, 'w+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.fields)

