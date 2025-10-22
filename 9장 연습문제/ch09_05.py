class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCount += 1

    def displayEmp(self):
        print(f"name: {self.name}, salary: {self.salary}")

emp1= Employee("kim", 5000)
emp2= Employee("lee", 6000)
emp1.displayEmp()
emp2.displayEmp()

print(f"Total: {Employee.empCount}")