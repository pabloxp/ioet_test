class PayRoll:
    def __init__(self,employees = []):
        self.employees = employees

    def loadFromFile(self,path):
        employeesFromFile = []
        try:
            file = open(path, "r")
            lines = file.readlines()
            count = 0
            for line in lines:
                line = line.rstrip("\n")

                count += 1
                inputline = line.split("=")
                employeename = inputline[0]
                employeedays = inputline[1].split(",")
                workDayList = []
                for days in employeedays:
                    daysplit = days.split("-")
                    dayName = daysplit[0][:2]
                    dayStart = daysplit[0][2:]
                    dayEnd = daysplit[1]
                    workDay = WorkDay(dayName, dayStart, dayEnd)
                    workDayList.append(workDay)

                employeeRow = Employee(employeename,workDayList)
                employeesFromFile.append(employeeRow)

        except Exception as e:
            print("Error",e)

        finally:
            file.close()
            self.employees = employeesFromFile
            #self.days = daysFromFile

    def getPayRoll(self):
        return self


class Employee:
    def __init__(self, name, workdays):
        self.name = name
        self.workdays = workdays

    def setName(name):
        self.name = name

    def getName():
        return self.name

    def setWorkdays(workdays):
        self.workdays = workdays

    def getWorkdays():
        return self.workdays

    def getEmployee():
        return self

class WorkDay:

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

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

    def getDay():
        return self
