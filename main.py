# ID- 011012097
import csv
import datetime
from MyHashMap import MyHashMap


class Package:
    def __init__(self, ID, address, city, zip, deadline, weight, status, deliverytime, loadtime):
        self.ID = ID
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.deliverytime = deliverytime
        self.loadtime = loadtime

    def __str__(self):  # needed to keep from printing object references
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.zip, self.deadline, self.weight, self.status)


class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, departtime):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departtime = departtime
        self.time = departtime

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage, self.address, self.departtime)


def loadPackageData(fileName):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "at the Hub"
            pDeliveryTime = ""
            pLoadTime = ""

            # package object
            package = Package(pID, pAddress, pCity, pZip,
                              pDeadline, pWeight, pStatus, pDeliveryTime, pLoadTime)

            # insert into hashmap
            packageHash.insert(pID, package)


def distanceBetween(address1, address2):
    if address2 >= address1:
        return distanceData[address2][address1]
    else:
        return distanceData[address1][address2]


with open("DistanceTable.csv") as csvfile:
    distanceData = csv.reader(csvfile)
    distanceData = list(distanceData)

with open("AddressFile.csv") as csvfile:
    address = csv.reader(csvfile)
    address = list(address)


# hash instance for package
packageHash = MyHashMap()

loadPackageData('PackageFile.csv')

for i in range(len(packageHash.table)):
    print("Key:{} and Package: {}".format(i+1, packageHash.search(i+1)))


print(distanceBetween(2, 0))
print(address[0][2])


# Create Truck objects
truck1 = Truck(16, 18, None, [1, 7, 12, 13, 14, 15, 16, 19, 20, 21, 29, 30,
               31, 34, 39, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))


# Method for delivering packages loaded in trucks
def deliveringPackages(truck):
