class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self,amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")

kim = Employee("kim", 5000)
lee = Employee("lee", 6000)

print(f"{kim.name}의 연본은 {kim.salary}")
print(f"{lee.name}의 연본은 {lee.salary}")
kim.raise_salary(2000)
lee.raise_salary(2000)