def m_f_prec(students_df):
    n_males = students_df[students_df['gendar'] == 'Male']['gendar'].count()
    n_females = students_df[students_df['gendar'] == 'Female']['gendar'].count()
    n_users = n_males + n_females
    prec_m = n_males / n_users * 100
    prec_f = n_females / n_users * 100
    return [n_males,
            n_females,
            n_users,
            str(prec_m)+"%",
            str(prec_f)+"%"]

