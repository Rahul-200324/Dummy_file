print("Welcome to Tech Solutions Company.")
def CBSE_per_cal(CBSE_total_marks):
    per = (CBSE_total_marks/500)*100
    print("Percentage : ", per,"%")

def ICSE_per_cal(ICSE_total_marks):
    per = (ICSE_total_marks/1100)*100
    print("Percentage : ", per,"%")

def State_per_cal(State_total_marks):
    per = (State_total_marks/600)*100
    print("Percentage : ", per,"%")

def pu_per_cal(pu_total_marks):
    per = (pu_total_marks/600)*100
    print("Percentage : ", per,"%")

class company:
    company_name= "Tech Solutions"
    def __init__(self,location, Company_type):
        self.location= location
        self.Company_type= Company_type
    @staticmethod
    def company_info():
        print("Welcome to Tech Solutions Company, We mainly provide IT services and solutions to our clients./n We mostly work on Python Programming language and for Testing we do Manual testing and Automation testing using Selenium./n Our company is located in New york USA. Basically it is US based company and We opned our new company in Whitefeild, Bangalore India./n So we are looking for skilled emploies for different roles. Thankyou")

class Development(company):
    @staticmethod
    def development_info():
        print("We are looking for freshers candidates for role of Python Development./n Skills Required : [Python, Django, SQL, HTML, CSS, JavaScript, Git and GitHub] ")

class Testing(company):
    @staticmethod
    def testing_info():
        print("We are looking for freshers candidates for role of Testing./n Skills Required : [Manual Testing, Automation Testing, Selenium, SQL, SDLC and Test Cases] ")


print("Application page : ")

c1=company("New York, USA","US Based Company")
d1=Development()
t1=Testing()

Role = input ("Please specify the role you are applying  for : ")
if Role == "Development":
    d1.development_info()
    print(" \n")
    print("\n ")
    print("Personal Details")
    print(" \n")
    Name= input("Please enter your name : ")
    Email= input("Please enter your email : ")
    Phone= input("Please enter your phone number : ")
    Gender= input("Please enter your gender : ")
    Father_name= input("Please enter your father name : ")
    Mother_name= input("Please enter your mother name : ")
    Age=int(input("Please enter your age : "))
    print(" \n")
    print("\n ")
    print("Educational Details")
    print(" \n")
    print("SSLC Details : ")
    School_name= input("Please enter your school name : ")
    SSLC_board= input("Please enter your SSLC Board name : ")
    if SSLC_board == "CBSE":
        print("Please enter your total marks out of 500 :")
        CBSE_total_marks= int(input())
        CBSE_per_cal(CBSE_total_marks)
    elif SSLC_board == "ICSE":
        print("Please enter your total marks out of 1100 :")
        ICSE_total_marks= int(input())
        ICSE_per_cal(ICSE_total_marks)
    elif SSLC_board == "State Board":
        print("Please enter your total marks out of 600 :")
        State_total_marks= int(input())
        State_per_cal(State_total_marks)

    else:
        print("Invalid board name")

    print("PU Details : ")
    Collage_name= input("Please enter your collage name : ")
    print("Please enter your PU marks out of 600 : ")
    pu_total_marks= int(input())
    pu_per_cal(pu_total_marks)

    print("Engineering Details : ")
    Engineering_college= input("Please enter your engineering college name : ")
    University_name= input("Please enter your University name : ")
    branch= input("Please enter your branch name : ")
    USN = input("Please enter your USN number : ")
    passout_year= int(input("Please enter your passout year : "))
    CGPA= float(input("Please enter your CGPA : "))
    Skills= input("Please enter your skills : [ ]")
    print(" \n")
    print("Thankyou for applying . We will soon contact you..........!")
elif Role == "Testing":
    t1.testing_info()
    print(" \n")
    print("\n ")
    print("Personal Details")
    print(" \n")
    Name= input("Please enter your name : ")
    Email= input("Please enter your email : ")
    Phone= input("Please enter your phone number : ")
    Gender= input("Please enter your gender : ")
    Father_name= input("Please enter your father name : ")  
    Mother_name= input("Please enter your mother name : ")
    Age=int(input("Please enter your age : "))
    print(" \n")
    print("\n ")
    print("Educational Details")
    print(" \n")
    print("SSLC Details : ")
    School_name= input("Please enter your school name : ")
    SSLC_board= input("Please enter your SSLC Board name : ")
    if SSLC_board == "CBSE":
        print("Please enter your total marks out of 500 :")
        CBSE_total_marks= int(input())
        CBSE_per_cal(CBSE_total_marks)
    elif SSLC_board == "ICSE":
        print("Please enter your total marks out of 1100 :")
        ICSE_total_marks= int(input())
        ICSE_per_cal(ICSE_total_marks)
    elif SSLC_board == "State Board":
        print("Please enter your total marks out of 600 :")
        State_total_marks= int(input())
        State_per_cal(State_total_marks)
    
    else:
        print("Invalid board name")
    
    print("PU Details : ")
    Collage_name= input("Please enter your collage name : ")
    print("Please enter your PU marks out of 600 : ")
    pu_total_marks= int(input())
    pu_per_cal(pu_total_marks)
    
    print("Engineering Details : ")
    Engineering_college= input("Please enter your engineering college name : ")
    University_name= input("Please enter your University name : ")
    branch= input("Please enter your branch name : ")
    USN = input("Please enter your USN number : ")
    passout_year= int(input("Please enter your passout year : "))
    CGPA= float(input("Please enter your CGPA : "))
    Skills= input("Please enter your skills : [ ]")
    print(" \n")      
    print("Thankyou for applying . We will soon contact you..........!")



          