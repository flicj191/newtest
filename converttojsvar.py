#convert to var points for marker clustering
import csv

output = 'var incidentPoints = [ \n'
# Read in raw data from csv
rawData = csv.reader(open('randompoints.csv', 'r'))


# the template. where data from the csv will be formatted to list of points
template1 = \
''' \
[%s,%s,"%s"],
'''

templateLast = \
    ''' \
[%s,%s,"%s"]
];
    '''

# loop through the csv by row skipping the first
iter = 0
for row in rawData:
    iter += 1
    if iter <50:
        lat = row[0]
        lon = row[1]
        dist = str(row[2])
        output += template1 % (lat,lon,dist)
    else:
        lat = row[0]
        lon = row[1]
        dist = str(row[2])
        output += templateLast % (lat,lon,dist)
    
# opens js file to write the output to
outFileHandle = open("points.js", "w")
outFileHandle.write(output)
outFileHandle.close()
