#This Code is Developed For Almentor Website Course (Python Warm-Up for Machine Learning)
#Developed by : Ahmed Tarek
#Date Developed in : 30/4/2022


from colorama import Fore, init
from reading_csv_files import reading_csv_file
from m_f_prec import m_f_prec
from arranging_data import arranging_data
from the_best_of import the_best_of, best_student
from common_location import common_location
from send_message import gmail_message,whatsapp_message
init(autoreset=True)

##########################################################################################################
# Reading CSV Files and Converting it to Pandas DataFrames


courses_file_path = "courses.csv"
student_file_path = "students.csv"
courses_df, students_df = reading_csv_file([courses_file_path, student_file_path])
# print(courses_df)
# print()
# print(students_df)
print(Fore.GREEN + "Reading \"{}\" and \"{}\" Files Completed Successfully ✅".format(courses_file_path,
                                                                                     student_file_path))
print("\n######################################################")

##########################################################################################################
# Calculating The Prec of Males & Females in our Platform


print(Fore.GREEN + "Calculating The Prec of Males & Females in our Platform Completed Successfully ✅")
# Prec of Males & Females in our Platform
m_f_prec_out = m_f_prec(students_df)
print("Number of Males =", m_f_prec_out[0])
print("Number of Females =", m_f_prec_out[1])
print("Total Users =", m_f_prec_out[2])
print("Prec Males =", m_f_prec_out[3])
print("Prec Females =", m_f_prec_out[4])
print("\n######################################################\n")

###########################################################
# Making Dictionary have all Data in that arranged Way
# courses={course_id:[Course_Name,Course_Instructor,Whatsapp_num,Gmail,Course_total_hours]}


print(Fore.GREEN + "Arranging Courses Data in our Platform Completed Successfully ✅")
courses = dict()
course_id = []
course_name = []
course_instructor = []
whatsapp_num = []
gmail = []

arranged_data = arranging_data(courses_df, courses, course_id, course_name, course_instructor, whatsapp_num, gmail)
print("Courses dic=", courses)
print("\n######################################################")

#########################################################################################
"""
Calculating 
"1-Total Hour Spent in our Platform Completed Successfully ✅\n"
                  "2-Best Course in our Platform Completed Successfully ✅\n"
                  "3-Most Studied Course in our Platform Completed Successfully ✅\n"
                  "4-Most Selling Online Course in our Platform Completed Successfully ✅\n"
                  "5- The Best Seller Instructor in our Platform Completed Successfully ✅",end="")"""

print(Fore.GREEN + "Calculating:\n"
                   "1-Total Hour Spent in our Platform Completed Successfully ✅\n"
                   "2-Best Course in our Platform Completed Successfully ✅\n"
                   "3-Most Studied Course in our Platform Completed Successfully ✅\n"
                   "4-Most Selling Online Course in our Platform Completed Successfully ✅\n"
                   "5- The Best Seller Instructor in our Platform Completed Successfully ✅", end="")
course_total_hours = dict()
tmp_courses_token = list(students_df['course_id'])
tmp_num_of_hours = list(students_df['hours_spent'])
courses_token = list()
num_of_hours = list()

the_best = the_best_of(course_total_hours, tmp_courses_token, tmp_num_of_hours, courses_token, num_of_hours, courses)
print("\nTotal Hours Spent in the Website=", the_best[0])
print("Best Course ID:", the_best[1])
print("Most studied (dependent in hours):", the_best[2])
print("Best Selling Online Course:", the_best[3])
print("Best Seller Instructor:", the_best[4])

print("\n######################################################")

####################################################################################
# Knowing the best Student in our Platform depended on the effort he did


print(Fore.GREEN + "Knowing the best Student in our Platform Completed Successfully ✅")
total_student_hours = list()
students_study_hours = dict()

best_student = best_student(total_student_hours, students_study_hours, tmp_num_of_hours, students_df)
print("Best Student in our Platform is :{} \nShe Studied {} hours \n"
      "her Index is {} and her Index in Excel Sheet is {}".format(best_student[0],
                                                                  best_student[1],
                                                                  best_student[2],
                                                                  best_student[3]))
print("\n######################################################")

####################################################################################
# Knowing The Most Common Location our Students lives in

print(Fore.GREEN + "Knowing the Location of our Most Users in our Platform Completed Successfully ✅")
common_location = common_location(students_df)
print("Our Most Users From :", common_location)

print("\n######################################################")

################################################
print("The Gmail Message Sender Example & Whatsapp Message You Can Find in Send Message File")