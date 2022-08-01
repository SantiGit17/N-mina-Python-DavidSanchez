"""Nómina"""

import re
Stop= True
while Stop:
    Document = str(input("Document Number: "))  
    if len(Document) <5:
        print ("Documento invalido, el rago tiene que ser mayor que 5")
    elif len(Document) >12:
        print ("Documento invalido, el rago tiene que ser menor que 12")
    else:
        Stop=False
Stop1=True
while Stop1:
    Name = str(input("Name: "))
    if len(Name) <2:
        print ("Nombre invalido, el rago tiene que ser mayor que 2")
    elif len(Name) >35:
        print ("Nombre invalido, el rago tiene que ser menor que 35")
    else:
        Stop1=False
Stop2=True
while Stop2:
    Last_Name= str(input("Last Name: "))
    if len(Last_Name) <2:
        print ("Apellido invalido, el rago tiene que ser mayor que 2")
    elif len(Last_Name) >35:
        print ("Apellido invalido, el rago tiene que ser menor que 35")
    else:
        Stop2=False
Stop3=True
while Stop3:
    Daysworked= str(input("Daysworked: "))
    if len(Daysworked) <1:
        print ("Dias Trabajados invalido, el rago tiene que ser mayor que 1")
    elif len(Daysworked) >30:
        print ("Dias Trabajados invalido, el rago tiene que ser menor que 30")
    else:
        Stop3=False
Stop4=True
while Stop4:
    Salary_month= str(input("Salary per month: "))
    if len(Salary_month) <1:
        print ("Salario mensual invalido, el rago tiene que ser mayor que 1")
    elif len(Salary_month) >100000000:
        print ("Salatio Mensual invalido, el rago tiene que ser menor que 10000000")
    else:
        Stop4=False

Base_salary = (int(Salary_month)/30)*float(Daysworked)
Subsidy_Trans= (117100/30)*float(Daysworked)
Salary_and_trans=Base_salary+Subsidy_Trans

if Salary_and_trans>=1000000:
    Descuento= Salary_and_trans*0.8
elif Salary_and_trans<1000001:
    Descuento= Salary_and_trans*0.10
elif Salary_and_trans>=2000000:
    Descuento= Salary_and_trans*0.10
elif  Salary_and_trans<2000001:
    Descuento= Salary_and_trans*0.12
else:
    Descuento= Salary_and_trans*0.12
Total_Salary=float(Salary_and_trans-Descuento)


print("---Payroll---")
print("Document Number: ",Document)
print("Usuary: ",Name, Last_Name)
print("Days worked: ",Daysworked)
print("Salary per month:" ,Salary_month)
print("Base salary: ",Base_salary)
print("Subsidy of transport :",Subsidy_Trans) 
print("Salary and transport :",Salary_and_trans)
print("Discount:",Descuento) 
print("Total Salary:",Total_Salary) 

y="---Nomina----\n"
y+=f"Document Number: {Document}\n"
y+=f"Name: {Name}\n"
y+=f"Last Name:  {Last_Name}\n"
y+=f"Daysworked: {Daysworked}\n"
y+=f"Salary per month: {Salary_month}\n"
y+=f"Base salary: {Base_salary}\n"
y+=f"Subsidy Trans: {Subsidy_Trans}\n"
y+=f"Salary and trans{Salary_and_trans}\n"
y+=f"Discount: {Descuento}\n"
y+=f"Total Salary: {Total_Salary}\n"
x=open("Nomina block.txt","a")
x.write(y)