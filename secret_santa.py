import pandas as pd
import random

def load_employee_data(file_path):
    return pd.read_csv(file_path)

def load_previous_assignments(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return None

def assign_secret_santa(employees, previous_assignments=None):
    names = employees["Employee_Name"].tolist()      #Assigns Secret Santa pairs while ensuring constraints
    emails = employees["Employee_EmailID"].tolist()
   
    valid_assignment = False
    while not valid_assignment:
        shuffled_indices = list(range(len(names)))
        random.shuffle(shuffled_indices)
        valid_assignment = all(i != shuffled_indices[i] for i in range(len(names)))
    
    assignments = {
        "Employee_Name": names,
        "Employee_EmailID": emails,
        "Secret_Child_Name": [names[i] for i in shuffled_indices],
        "Secret_Child_EmailID": [emails[i] for i in shuffled_indices],
    }
    
    return pd.DataFrame(assignments)

def save_assignments(assignments, output_file):
    assignments.to_csv(output_file, index=False)
    print(f"Assignments saved to {output_file}")
    

employees = load_employee_data("employees.csv")
previous_assignments = load_previous_assignments("previous_santa.csv")
assignments = assign_secret_santa(employees, previous_assignments)
save_assignments(assignments, "secret_santa_assignments.csv")