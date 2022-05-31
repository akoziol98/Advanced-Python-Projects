from HW1_data import records, records_many
import pprint

def build_data_structure(record):
    new_dict, dict_name, dict_id, dict_program, dict_class = {}, {}, {}, {}, {}
   
    for student in record:
        if isinstance(student['name'], str) == False: raise TypeError("Student's name must be a string")
        if isinstance(student['student_id'], int) == False: raise TypeError("Student's index must be an integer")
       
        if student['name'] in dict_name:
            dict_name[student['name']].append(student)
        else:
            dict_name[student['name']] = [student]
          
        for program in student['program']:
            if isinstance(program[0], str) == False: raise TypeError("Name of the program must be a string")
            if isinstance(program[1], int) == False: raise TypeError("Year must be an integer")
            if program in dict_program:
                dict_program[program].append(student)
            else:
                dict_program[program] = [student]
       
        for classes in student['classes']:
            if isinstance(classes, int) == False: raise TypeError("Name of the class must be an integer")
            if classes in dict_class:
                dict_class[classes].append(student)
            else:
                dict_class[classes] = [student]  
       
        dict_id[student['student_id']] = [student]
   
    new_dict.update({ 'name':dict_name, 'id':dict_id, 'program':dict_program, 'classes':dict_class})
   
    return new_dict


def find_by_name(data, name):
    if isinstance(name, str) == False: raise TypeError("Student's name must be a string")
    try:
        list = [x for x in data['name'][name.strip()]]
        print(f"Students with name: {name}")
        pprint.pprint(list)
    except KeyError:
        print(f"There is no student with name: {name}")
   
  

def find_by_idx(data, idx):
    if isinstance(idx, int) == False: raise TypeError("Student's index must be an integer")
    try:
        index = data['id'][idx]
        print(f"Student with index: {idx}")
        pprint.pprint(index)
    except KeyError:
        print(f"There is no student with index: {idx}")


def list_students_by_program_and_year(data, program, year):
    if isinstance(year, int) == False: raise TypeError("Year must be an integer")
    if isinstance(program, str) == False: raise TypeError("Name of the program must be a string")
    tupl = (program.strip(), year)
    try:
        list = [x for x in data['program'][tupl]]
        print(f"Students in {program} on year {year}")
        pprint.pprint(list)
    except KeyError:
        print(f"There are no students in {program} on year {year}")


def list_students_enrolled_in_class(data, idx):
    if isinstance(idx, int) == False: raise TypeError("Name of the class must be an integer")
    try:
        list = [x for x in data['classes'][idx]]
        print(f"Students in class: {idx}")
        pprint.pprint(list)
    except KeyError:
        print(f"There is no student in class: {idx}")
        
dane = build_data_structure(records_many)
#find_by_name(dane, ' Jane Doe ')
#find_by_idx(dane, 1)
#list_students_by_program_and_year(dane, 'Mathematics', 4)
#list_students_enrolled_in_class(dane, 1) 