# Python File CSV.
# csv � CSV File Reading and Writing.
# The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.
# CSV format was used for many years prior to attempts to describe the format in a standardized way in RFC 4180.
# The lack of a well-defined standard means that subtle differences often exist in the data produced and consumed by different applications.
# These differences can make it annoying to process CSV files from multiple sources.
# Still, while the delimiters and quoting characters vary, the overall format is similar enough that it is possible to write a single module
# which can efficiently manipulate such data, hiding the details of reading and writing the data from the programmer.
# The csv module implements classes to read and write tabular data in CSV format.
# It allows programmers to say, �write this data in the format preferred by Excel,� or �read data from this file which was generated by Excel,�
# without knowing the precise details of the CSV format used by Excel.
# Programmers can also describe the CSV formats understood by other applications or define their own special-purpose CSV formats.
# The csv module�s reader and writer objects read and write sequences.
# Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes.
# csv.reader(csvfile, dialect='excel', **fmtparams) 
# Return a reader object which will iterate over lines in the given csvfile. csvfile can be any object which supports the iterator protocol and
# returns a string each time its __next__() method is called � file objects and list objects are both suitable. If csvfile is a file object, it
# should be opened with newline=''. 

import csv
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:

            print(', '.join(row))

#
# OUTPUT:
#
# Spam, Spam, Spam, Spam, Spam, Baked Beans
# Spam, Lovely Spam, Wonderful Spam