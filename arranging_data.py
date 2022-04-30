def arranging_data(courses_df,courses,course_id,course_name,course_instructor,whatsapp_num,gmail):
    courses_dic = courses_df.set_index('course_id').to_dict()
    # print(courses_dic)
    all = [course_id, course_name, course_instructor, whatsapp_num, gmail]

    for index, (key, value) in enumerate(courses_dic.items()):
        if index == 0:
            all[0] = (list(value.keys()))

        for id in all[0]:
            all[index + 1].append(value[id])

    for index, num in enumerate(all[3]):
        all[3][index] = all[3][index].replace('"', '')
    #print("Modified Numbers=", all[3])

    #print("all = ", all)
    for index, id in enumerate(all[0]):
        courses[id] = [all[1][index], all[2][index], all[3][index], all[4][index]]
    return courses
