'''STUDENT PERFORMANCE ANALYTICS TOOLKIT'''


#Add and Validate Records
def add_student(student_id, name, marks):

    if student_id == "" or name == "":
        return None

    if len(marks) == 0:
        return None

    for mark in marks:
        if mark < 0 or mark > 100:
            return None

    Student_Record = {
        "Name": name,
        "Marks": marks
    }

    return Student_Record


# CALCULATE TOTALS AND AVERAGE
def calculate_total(marks):
    
    total = sum(marks)
    return total

def calculate_average(marks):
    
    if len(marks)==0:
        return 0
    
    total = calculate_total(marks)
    average = total/len(marks)
    
    return round(average,2)
        
#GRADE CALCULATION
def get_grade(average):
    
    if average>=75:
        return "Distinction"
    
    elif average>=60:
        return "First Division"
    
    elif average>=40:
        return "Pass"
    
    else:
        return "Fail"
    
    
#STUDENT REPORT
def build_report(studentId,Student_Record):
    
    total = calculate_total(Student_Record['Marks'])
    
    average = calculate_average(Student_Record["Marks"])
    
    grade = get_grade(average)
    
    report= {"Student ID":studentId, "Name":Student_Record['Name'],             "Marks":Student_Record["Marks"], "Total":total, "Average":average, "Grade":grade}
    
    return report


# HIGH PERFORMERS
def get_top_students(records):
    
    
    high_performers=list(filter(lambda student: calculate_average(student["Marks"])>=75, records.values()))
    
    return high_performers
    
    
'''Calculate the average of any number of supplied marks'''
def average_of_marks(*marks):
    
    if len(marks)==0:
        return 0
    
    total = sum(marks)
    
    average = total/len(marks)
    
    return round(average, 2)


'''Function using ***kwargs to accept named summary options '''
def class_summary(records,**options):
    
    title = options.get('title','Class Report')
    
    passing_mark = options.get('Passing mark', 40)
    
    if len(records)==0:
        print("No Records found")
        return
    
    print("\n"+"="*50)
    print(f"                {title} ")
    print("\n"+"="*50)
    
    total_students=len(records)
    
    class_average_list = list(map(lambda student: calculate_average(student["Marks"]),records.values()))
    
    class_Average = average_of_marks( *class_average_list )
    
    passed_students = 0
    
    for average in class_average_list:
        
        if average>=passing_mark:
            passed_students+=1
            
    print("Total Students in the Class:", total_students)
    print("Number of students passed:", passed_students)
    print("Number of students failed:", total_students-passed_students)
    print("Class Average:",class_Average)
    
    

'''Recursive function to calculate sum from 1 to n'''
def n_sum(n):
    
    if n==0:
        return 0
    
    return n + n_sum(n-1)
    

def main():
    
    Student_Records={}
    
    
    print("\n","="*55) 
    print("\n         STUDENT PERFORMANCE ANALYTICS TOOLKIT")   
    print("\n","="*55)
    
    n = int(input("Enter number of students to be added: "))
    
    for i in range(n):
        
        while True:
            
            student_id = input("Enter student ID: ")
            
            if student_id in Student_Records:
                print("Student ID already exists in Records.")    
                continue
            
            student_name = input("Enter name of the student: ")
            
            subjects = int(input("Enter number of subjects: "))
                        
            marks =[]
            
            for i in range(subjects):
                
                mark = float(input(f"Enter marks in subject {i+1}: "))
                marks.append(mark)
             
            #Calling function to add Students
            student = add_student(student_id,student_name,marks)
            
            if student == None:
                print("Invalid student details. please Enter again")
            else:
                Student_Records[student_id]={"Name":student_name, "Marks":marks}
                
                break
    
    print("\n========STUDENT PERFORMANCE REPORT========") 
         
    for student_id, student in Student_Records.items():
        
        report = build_report(student_id, student)
        
        print(f"\nStudent ID: {report["Student ID"]} | Name: {report['Name']} | Marks: {report["Marks"]}")
        
        print(f"\nTotal: {report["Total"]} | Average: {report["Average"]} | Garde: {report['Grade']} ")
        
     
    high_performers = get_top_students(Student_Records) 
    
    top_student_names = list(map(lambda student: student["Name"],high_performers))   
    
    print("\nHigh performers (average >= 75):", top_student_names)
    
    class_summary(Student_Records,title="Student Class Summary",passing_mark=40)
    
    
    print("\n========== *args DEMONSTRATION ==========")

    result = average_of_marks(98, 55, 84, 90)

    print("Average of supplied marks:", result)

    
    
    print("\n========== RECURSION DEMONSTRATION ==========")

    print("Recursive sum from 1 to 5:", n_sum(5))
    

main()

        
         

   
    


    