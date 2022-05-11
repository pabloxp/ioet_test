import PayRoll
import PayRule
import datetime

class Operations:
    def __init__(self,payroll, payrule):
        self.payroll = payroll
        self.payrule = payrule

    def getPaidbyName(self,name):

        for employee in self.payroll.employees:
            print(employee.name)
            if name in employee.name:
                print (name,"FOUND")

    def getPaid(self):
        now = datetime.datetime.now()
        paidList = []
        for employee in self.payroll.employees:
            employeepaidvalue = 0
            for workdays in employee.workdays:
                for workdaysrule in self.payrule.days:
                    if workdays.name == workdaysrule.name:
                        if workdaysrule.end == "00:00":
                            ruleTimeStop = datetime.datetime.strptime(workdaysrule.end,'%H:%M') + datetime.timedelta(days=1)
                        else:
                            ruleTimeStop = datetime.datetime.strptime(workdaysrule.end,'%H:%M')
                        ruleTimeStart = datetime.datetime.strptime(workdaysrule.start,'%H:%M')
                        timeStart = datetime.datetime.strptime(workdays.start,'%H:%M')
                        if workdays.end == "00:00":
                            timeStop = datetime.datetime.strptime(workdays.end,'%H:%M') + datetime.timedelta(days=1)
                        else:
                            timeStop = datetime.datetime.strptime(workdays.end,'%H:%M')


                        if timeStart >= ruleTimeStart:
                            if timeStop <= ruleTimeStop:
                                dif=timeStop-timeStart
                                dif_seg = dif.total_seconds()
                                employeepaidvalue = employeepaidvalue + divmod(dif_seg, 3600)[0]*int(workdaysrule.price)
            print(employee.name,employeepaidvalue)


    #def getEmployeePaid(self, employee)
