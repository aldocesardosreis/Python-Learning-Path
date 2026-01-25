#Exercise 013 - Write an algorithm reads an employee's salary and displays their new salary, which includes a 15% increase.

salary = float(input("Enter emplyee's salary: R$ "))
newsalary = salary * 1.15

print('The new salary is: R$ {:.2f}'.format(newsalary))
