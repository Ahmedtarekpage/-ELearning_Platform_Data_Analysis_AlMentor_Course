import pandas as pd
def reading_csv_file(file_paths):
    files_output_var=list()
    for file in file_paths:
        files_output_var.append(pd.read_csv(file))
    return files_output_var
