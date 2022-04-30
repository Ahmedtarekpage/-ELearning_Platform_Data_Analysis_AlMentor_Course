def common_location(students_df):
    common_location = students_df["location"].mode()[0]
    return common_location