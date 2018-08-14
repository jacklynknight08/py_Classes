print("Python Classes Exercise")

# Create a class that contains information about employees of a company and define 
# methods to get/set employee name, job title, and start date.

# Copy this Company class into your module.

# Consider the concept of aggregation, and modify the Company class so that you 
# assign employees to a company.

# Create a company, and three employees, and then assign the employees to the company.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name):
        self.company_name = name
        
        self.employees = list()

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name
    
    def set_company_name(self, name):
        self.company_name = name

class Employee(object):
    """This represents an employee"""

    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job = job_title
        self.start_date = start_date

    def get_employee_name(self):
        """Return the employee name"""

        return self.name

    def set_employee_name(self, name):
        self.name = name

junesCompany = Company("Junie B's Pup Agency")

jackie = Employee("Jackie", "Software Developer", "04-03-18")
kyle = Employee("Kyle", "Cloud Technical Architect", "07-30-18")
june = Employee("June", "Owner/Dog", "05-15-16")

junesCompany.employees.append(jackie)
junesCompany.employees.append(kyle)
junesCompany.employees.append(june)

print(("{} works as a {} and was hired on {}").format(jackie.name, jackie.job, jackie.start_date))
print(("{} works as a {} and was hired on {}").format(kyle.name, kyle.job, kyle.start_date))
print(("{} works as a {} and was hired on {}").format(june.name, june.job, june.start_date))