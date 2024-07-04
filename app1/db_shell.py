import datetime

from app1.models import Employee

from django.db.models import Avg
# exec(open(r'C:\Users\ADMIN\Django Framework\first_project\app1\db_shell.py').read())


# CRUD  --Create Read Update Delete

# Read All

 #all_emps = Employee.objects.all()      #[0:3]    #0   1   2  #slicing
 #print(all_emps)


# for emp in all_emps:
#   print(emp.__dict__)

# Single read
#
#try:

 #   emp = Employee.objects.get(id=4)
  #  print(emp)
#except Employee.DoesNotExist:    
 # print("Employee with given id does not exit in database.")

# create

# 1 way
#emp = Employee(
 #   name="s",
 #   email="t@gmail.com",
   # mobile_num=1689563489,
    #designation="tester",
    #salary="78654",
#)
#emp.save()

#2 way

#Employee.objects.create(
 #    name="h",
  #   email="j@gmail.com",
   #  mobile_num=459563489,
    #designation="tester",
    #salary="78654",
#)



# UPDATE

#try:

 #   emp_obj = Employee.objects.get(id=1)
  #  emp_obj.salary = 45892
   # emp_obj.email = "ty"
    #emp_obj.save()
    #print(emp)
#except Employee.DoesNotExist:    
 # print("Employee with given id does not exit in database.")


#delete

#try:

 #   emp_obj = Employee.objects.get(id=3)
  #  emp_obj.delete()
    
    
#except Employee.DoesNotExist:    
 # print("Employee with given id does nt exit in database.")

#emp = Employee.objects.filter(email = "s@gmail.com")


#emp = Employee.objects.get(email = "s@gmail.com")

#emp = Employee.objects.filter(email = "s@gmail.com")
#print(emp)

#emp = Employee.objects.filter(designation__startswith__="p")



#avg_salary = Employee.objects.aggregate(Avg('salary'))
#print(avg_salary)

#mid_salary_employess = Employee.objects.fliter(salary_gte=50000,salary__lte=80000)

# and salary  >=50000   and salary   <=80000


#top_2_heightest_paid = Employee.objects.order_by('salary')[:2]   #[start: stop : stopsize]
#print(top_2_heightest_paid)

#[45322, 56478, 65789, 32456]
#[65789, 56478, 45322, 32456] [:2]  #  0  1  2


#non_developers = Employee.objects.filter(salary__gte=45000).exclude(designation="developer")

#54000 = engineer
#85000 = tester
#56788 = developer


#names_and_designations = Employee.objects.values('name', 'designation')

#distinct_designations = Employee.objects.values('designations').distinct()
#print(distinct_designations)

#from django.utils import timezone
#five_years ago = timezone.now()  -  timezone.timedelta(days=5*365)
#print(five_years_ago)
#long_term_employees = Employee.objects.filter(date__joined__lt=five_years_ago)