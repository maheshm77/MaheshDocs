class Employee:
    empCnt = 0
    __emps = 0

    def __init__(self, name, dept):
        self.name=name
        self.dep=dept
        Employee.empCnt += 1
        Employee.__emps = Employee.empCnt
    
    def displayCount(self):
        print ("Count : ", self.empCnt)
    
    def dispEmp(self):
        print ("Name : ", self.name, "Department : ", self.dep)
    def __del__(self):
        print ("Before deletion ID : ", self.__emps)
        print ("Deleted : ", self.name)


class Engg(Employee):
    def __init__(self):
        print ("In Engineer class")

class RunE:
    e1 = Employee("Foo", "HR")

    print ("E1 : ", e1.name, e1.dep)
    print (Employee.empCnt)
    
    e2 = Employee("Bar", "Fin")
    print ("E2 : ", e2.name, e2.dep)
    print (e2.empCnt)

    e1.age = 32
    #del e1.age
    print ("E1 : ", e1.name, e1.dep, e1.age)
    setattr(e1, 'loc', 'Blore')
    print ("E1 : ", e1.name, e1.dep, e1.age, e1.loc)
    #print ("Employee.__dict__:", Employee.__dict__)
    #del e1
    #del e2
    #e2.name
    eng = Engg()
    setattr(eng, "name", "mahes")
    print ("Engineer employee name : " + eng.name)