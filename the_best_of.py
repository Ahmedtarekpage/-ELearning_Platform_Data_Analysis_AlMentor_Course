def the_best_of(course_total_hours,tmp_courses_token,tmp_num_of_hours,courses_token,num_of_hours,courses):
    #Target >>  course_total_hour={id:hours}

    # print("courses id in series before edit",tmp_courses_token)
    for c_id in tmp_courses_token:
        str_list = c_id.split(',')
        for num in str_list:
            courses_token.append(int(num))
    # print("course id in series",courses_token)

    for c_hours in tmp_num_of_hours:
        str_list = c_hours.split(',')
        for num in str_list:
            num_of_hours.append(int(num))
    # print("hours spent in series",num_of_hours)

    for index, id in enumerate(courses_token):
        if id not in list(course_total_hours.keys()):
            course_total_hours[id] = num_of_hours[index]
        else:
            course_total_hours[id] = course_total_hours[id] + num_of_hours[index]
    # print("{Course_id:total hours} >>",course_total_hours)

    best_id, mode_hours, total_hours = 0, 0, 0
    users = dict()
    for index, (id, hours) in enumerate(course_total_hours.items()):
        total_hours = total_hours + hours
        if hours > mode_hours:
            best_id, mode_hours = id, hours
    return [total_hours,best_id,mode_hours,courses[best_id][0],courses[best_id][1]]

def best_student(total_student_hours,students_study_hours,tmp_num_of_hours,students_df):
    mode_hours_usr = 0

    for index, c_hours in enumerate(tmp_num_of_hours):
        str_list = c_hours.split(',')
        for num in str_list:
            total_student_hours.append(int(num))
        students_study_hours[index] = sum(total_student_hours)
        total_student_hours = []
    # print("hours spent in series",num_of_hours)
    # print("{Studnt index:studied hours} >> ",students_study_hours)
    for usr_indx, hours in students_study_hours.items():
        if hours > mode_hours_usr:
            mode_hours_usr = hours
            best_student_indx = usr_indx
    best_student = students_df["name"].iloc[best_student_indx]
    # print("best student index:",best_student_indx)
    # print("Number_of_hours_studied:",mode_hours_usr)
    return [best_student,mode_hours_usr,best_student_indx,best_student_indx + 2]


