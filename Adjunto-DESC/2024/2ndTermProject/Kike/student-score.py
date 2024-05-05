def parse_raw_data(raw_data):
    students = []
    lines = raw_data.strip().split('\n')
    for line in lines:
        name, score = line.split(', ')
        student = {'name': name.strip(), 'score': int(score)}
        students.append(student)
    return students

def find_common_students(class1, class2):
    common_students = []
    for student in class1:
        for student2 in class2:
            if student['name'] == student2['name']:
                common_students.append({'name': student['name'], 'score1': student['score'], 'score2': student2['score']})
                break
    return common_students

def find_unique_students(class1, class2):
    unique_students = []
    for student in class1:
        found = False
        for student2 in class2:
            if student['name'] == student2['name']:
                found = True
                break
        if not found:
            unique_students.append(student)
    for student in class2:
        found = False
        for student2 in class1:
            if student['name'] == student2['name']:
                found = True
                break
        if not found:
            unique_students.append(student)
    return unique_students

def calculate_average_score(students):
    total_score = 0
    for student in students:
        total_score += student['score']
    return total_score / len(students)

def main():
    class1_raw_data = '''
    John Doe, 85
    Jane Smith, 78
    Michael Brown, 92
    Emily Johnson, 88
    Daniel Wilson, 74
    Olivia Jones, 95
    William Garcia, 81
    Ava Martinez, 87
    Isabella Rodriguez, 90
    Sophia Anderson, 77
    Mason Lee, 83
    Ella Young, 79
    James Hernandez, 84
    Charlotte Gonzalez, 91
    Benjamin Perez, 75
    Amelia Lopez, 89
    Ethan White, 93
    Mia Thompson, 80
    Alexander Harris, 85
    Aria Clark, 82
    Henry Lewis, 76
    Evelyn Walker, 94
    Sebastian Hall, 72
    Abigail Allen, 86
    Liam Scott, 78
    Sophie Adams, 73
    Oscar Nelson, 88
    Luna King, 91
    Jack Wright, 79
    Lucas Green, 84
    '''

    class2_raw_data = '''
    Isaac Moore, 89
    Eva Turner, 88
    Nathan Martin, 76
    Grace Hill, 92
    Samuel Adams, 85
    Zoe Davis, 81
    Aiden Robinson, 87
    Chloe Campbell, 90
    Gabriel Mitchell, 77
    Lily Anderson, 83
    Jane Smith, 82
    Emily Johnson, 90
    Daniel Wilson, 78
    Olivia Jones, 97
    Ella Young, 81
    Charlotte Gonzalez, 89
    Amelia Lopez, 91
    Mia Thompson, 82
    Alexander Harris, 88
    Sophia Anderson, 79
    Lucas Green, 86
    Jack Wright, 82
    Luna King, 93
    Oscar Nelson, 90
    Sophie Adams, 75
    Liam Scott, 80
    Henry Lewis, 88
    Aria Clark, 84
    Ethan White, 95
    Benjamin Perez, 77
    '''

    class1 = parse_raw_data(class1_raw_data)
    class2 = parse_raw_data(class2_raw_data)

    print("Class 1 average score:", calculate_average_score(class1))
    print("Class 2 average score:", calculate_average_score(class2))

    common_students = find_common_students(class1, class2)
    print("\nCommon students:")
    for student in common_students:
        avg_score = (student['score1'] + student['score2']) / 2
        print(f"{student['name']}: {avg_score}")

    unique_students_class1 = find_unique_students(class1, class2)
    unique_students_class2 = find_unique_students(class2, class1)
    print("\nClass 1 unique students average score:", calculate_average_score(unique_students_class1))
    print("Class 2 unique students average score:", calculate_average_score(unique_students_class2))

    all_unique_students = unique_students_class1 + unique_students_class2
    print("\nAll unique students average score:", calculate_average_score(all_unique_students))

if __name__ == "__main__":
    main()
