class Employee:
    count_Emp = 0  # data member to count the number of the Employees

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count_Emp += 1
        print('Count of the Employee: ', Employee.count_Emp)

    def avg_salary(self):  # finding average of the Employee
        total_salary = 0
        total_salary += float(self.salary)
        avg = total_salary / Employee.count_Emp
        print('average salary of the Employee:', avg)


class Fulltime_Employee(Employee):  # inheriting the Employee class
    def __init__(self, name, family, salary, department, type):
        Employee.__init__(self, name, family, salary, department)
        self.type = type

    def display(self):  # Displaying Employee details
        print('Name of the Employee:', self.name)
        print('Family name of the Employee:', self.family)
        print('Salary of the Employee Annually:', self.salary)
        print('Department Employee working:', self.department)
        print('Type of the Employment', self.type)
        print('***')


emp1 = Fulltime_Employee('Lavanya', 'Gadde', '100000', 'Software Developer', 'Fulltime')  #initiating the fulltime class
emp2 = Fulltime_Employee('Kote', 'R', '1200000', 'Web Developer', 'Fulltime')

emp1.avg_salary()
emp1.display()
emp2.display()
