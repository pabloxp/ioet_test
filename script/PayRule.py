class PayRule:
    VALID_DAYS = ["MO","TU","WE","TH","FR","SA","SU"]
    def __init__(self,name,days = []):
        self.name = name
        self.days = days

    def loadFromFile(self,path):
        daysFromFile = []

        try:
            file = open(path, "r")
            lines = file.readlines()
            count = 0
            for line in lines:
                line = line.rstrip("\n")
                count += 1
                dayRule = line.split("-")
                dayName = dayRule[0][:2]
                dayStart = dayRule[0][2:]
                dayEnd = dayRule[1]
                dayPrice = dayRule[2]
                if dayName in PayRule.VALID_DAYS:
                    dayFromFile = Day(dayName,dayStart,dayEnd,dayPrice)
                    daysFromFile.append(dayFromFile)

        except Exception as e:
            print("Error",e)

        finally:
            file.close()
            self.days = daysFromFile

    def getPayRule(self):
        return self



class Day:

    def __init__(self, name, start, end, price):
        self.name = name
        self.start = start
        self.end = end
        self.price = price

    def setName(name):
        self.name = name

    def getName():
        return self.name

    def setStart(start):
        self.start = start

    def getStart():
        return self.start

    def setEnd(end):
        self.end = end

    def getEnd():
        return self.end

    def setPrice(price):
        self.Price = price

    def getPrice():
        return self.price

    def getDay():
        return self
