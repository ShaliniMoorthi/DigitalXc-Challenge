import pandas as pd
import re
from collections import Counter

def extract_group_counts(filepath="C:\\Users\\shalu\\Downloads\\codeXl.xlsx"
, sheet_name="Input Data sheet", output_file="group_counts.csv"):
    
    df = pd.read_excel(filepath, sheet_name=sheet_name)
   
    comments = df["Additional comments"].dropna()
    
    group_pattern = r"Groups : \[code\]<I>(.*?)</I>\[/code\]"
    
    group_counter = Counter()
    
    for comment in comments:
        matches = re.findall(group_pattern, comment)
        for match in matches:
            groups = [group.strip() for group in match.split(",")]
            group_counter.update(groups)
    
    df_groups = pd.DataFrame(group_counter.items(), columns=["Group name", "Number of occurrences"])
    
    df_groups.to_csv(output_file, index=False)
    print(f"Output saved to {output_file}")
    
    return df_groups

extract_group_counts()