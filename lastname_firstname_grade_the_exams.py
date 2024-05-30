# task 1
while True:
    class_file = input("Enter a class file to grade (i.e class1 for class1.txt): ")
    file_name = f"{class_file}.txt"

    try:
        with open(file_name, "r") as file:
            print(f"Successfully open {file_name}")
            break
    except FileNotFoundError:
        print("File cannot be found.")

# task 2
import re


def analyze_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    invalid_lines = 0

    print("\n**** Analyzing File ****")

    for line in lines:
        line = line.strip()
        parts = line.split(",")
        if len(parts) != 26:
            print(f"\nInvalid line of data: does not contain exactly 26 values: \n{line}")
            invalid_lines += 1
        elif not re.match(r"^N\d{8}", parts[0]):
            print(f"\nInvalid line of data: N# is invalid \n{line}")
            invalid_lines += 1
            
    if invalid_lines == 0:
        print("\nNo errors found!")

    print("\n**** Report ****")
    print(f"\nTotal valid lines of data: {total_lines - invalid_lines}")
    print(f"Total invalid lines of data: {invalid_lines}")


while True:
    class_file = input("\nEnter a class file to grade (i.e class1 for class1.txt): ")
    file_name = f"{class_file}.txt"

    try:
        with open(file_name, "r") as file:
            print(f"Successfully open {file_name}")
            analyze_file(file_name)
            break
    except FileNotFoundError:
        print("File cannot be found.")

# task 3
import re
import numpy as np

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")

def analyze_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    invalid_lines = 0
    valid_lines = []

    print("\n**** Analyzing File ****")

    for line in lines:
        line = line.strip()
        parts = line.split(",")
        if len(parts) != 26:
            print(f"\nInvalid line of data: does not contain exactly 26 values: \n{line}")
            invalid_lines += 1
        elif not re.match(r"^N\d{8}", parts[0]):
            print(f"\nInvalid line of data: N# is invalid \n{line}")
            invalid_lines += 1
        else:
            valid_lines.append(parts)
            
    if invalid_lines == 0:
        print("\nNo errors found!")    

    print("\n**** Report ****")
    print(f"\nTotal valid lines of data: {total_lines - invalid_lines}")
    print(f"Total valid lines of data: {invalid_lines}")

    if total_lines - invalid_lines > 0:
        grade_exams(valid_lines)

def grade_exams(valid_lines):
    scores = []
    question_status = np.zeros((25, 3)) # skip, incorrect, total

    for line in valid_lines:
        student_id = line[0]
        answers = line[1:]
        score = 0

        for i, answer in enumerate(answers):
            if answer == "":
                question_status[i, 0] += 1 # skip
            elif answer == answer_key[i]:
                score += 4
            else:
                score -= 1
                question_status[i, 1] += 1 # incorrect
            question_status[i, 2] +=1 # total

        scores.append(score)

    scores = np.array(scores)
    high_scores = np.sum(scores >80)
    mean_scores = np.mean(scores)
    highest_score = np.max(scores)
    lowest_score = np.min(scores)
    score_range = highest_score - lowest_score
    median_score = np.median(scores)

    print(f"\nTotal students of high scores: {high_scores}")
    print(f"Mean (average) score: {mean_scores:.2f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Range of scores: {score_range}")
    print(f"Median score: {median_score}")

    skipped_questions = np.where(question_status[:, 0] == np.max(question_status[:, 0]))[0]
    results = []
    for q in skipped_questions:
        skip_count = question_status[q, 0]
        skip_rate = skip_count / question_status[q, 2]
        results.append(f"{q+1} - {int(skip_count)} - {skip_rate:.2f}")
    result_string = ", ".join(results)
    print(f"\nQuestion that most people skip: {result_string}")

    incorrect_questions = np.where(question_status[:, 1] == np.max(question_status[:, 1]))[0]
    results = []
    for q in incorrect_questions:
        incorrect_count = question_status[q, 1]
        incorrect_rate = incorrect_count / question_status[q, 2]
        results.append(f"{q+1} - {int(incorrect_count)} - {incorrect_rate:.2f}")
    result_string = ", ".join(results)
    print(f"Question that most people answer incorrectly: {result_string}")

while True:
    class_file = input("\nEnter a class file to grade (i.e class1 for class1.txt): ")
    file_name = f"{class_file}.txt"

    try:
        with open(file_name, "r") as file:
            print(f"Successfully open {file_name}")
            analyze_file(file_name)
            break
    except FileNotFoundError:
        print("File cannot be found.")

# task 4
import re
import numpy as np

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")

def analyze_file(file_name):
    with open(file_name,"r") as file:
        lines =  file.readlines()

    total_lines = len(lines)
    invalid_lines = 0
    valid_lines = []

    for line in lines:
        line = line.strip()
        parts = line.split(",")

        if len(parts) != 26 or not re.match(r"^N\d{8}", parts[0]):
            invalid_lines += 1
        else:    
            valid_lines.append(parts)

    if total_lines - invalid_lines > 0:
        grade_exams(valid_lines, file_name)

def grade_exams(valid_lines, file_name):
    scores = []
    question_status = np.zeros((25,3)) # skip, incorrect, total

    for line in valid_lines:
        student_id = line[0]
        answers = line[1:]
        score = 0

        for i, answer in enumerate(answers):
            if answer == "":
                question_status[i, 0] += 1 # skip
            elif answer == answer_key[i]:
                score += 4
            else:
                score -=1
                question_status[i, 1] += 1 # incorrect
            question_status[i, 2] += 1 # total

        scores.append((student_id, score))

    output_file = file_name.replace(".txt", "_grades.txt")
    with open(output_file,"w") as writefile:
        for student_id, score in scores:
            writefile.write(f"{student_id},{score}\n")
            
    print(f"Successfully create {output_file}")   

while True:
    class_file = input("\nEnter a class file to grade (i.e class1 for class1.txt): ")
    file_name = f"{class_file}.txt"
    try:
        with open(file_name,"r") as file:
            analyze_file(file_name)
            break
    except FileNotFoundError:
        print("File cannot be found.")
