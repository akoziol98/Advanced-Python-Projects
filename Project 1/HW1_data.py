### List of example records.
records = [
    {
        'name': 'Jane Doe',
        'gender': 'F',
        'student_id': 1,
        'program': [('Cognitive Science', 2)],
        'date_of_birth': 1996,
        'classes': [1, 2]
    },
    {
        'name': 'John Smith',
        'gender': 'M',
        'student_id': 2,
        'program': [('Mathematics', 4)],
        'date_of_birth': 1995,
        'classes': [1, 77, 18]
    },
    {
        'name': 'Han Solo',
        'gender': 'M',
        'student_id': 99,
        'program': [('Aerospace Engineering', 2)],
        'date_of_birth': 1977,
        'classes': [18, 20, 21, 33]
    },
    {
        'name': 'Jane Doe',
        'gender': 'F',
        'student_id': 11,
        'program': [('Computer Science', 3), ('Physics', 2)],
        'date_of_birth': 1995,
        'classes': [1, 77, 18, 20, 21]
    },
    {
        'name': 'Uesugi Kenshin',
        'student_id': 10101,
        'program': [('History', 1)],
        'date_of_birth': 1530,
        'classes': [303, 304, 308]
    }
]



### Here we generate 10000 student records randomly.
### This set can be used to test performance of the implementation.

import random as rnd
import hashlib

PROGRAMS = ('Cognitive Science', 'Computer Science', 'Psychology', 'Mathematics', 'Physics', 'Engineering', 'History')
GENDERS = ('M', 'F')
N = 100000

def hash_obj(x):
    m = hashlib.md5()
    m.update(str(x).encode())
    return m.hexdigest()

def sample_record(idx):
    return {
        'name': hash_obj(rnd.randint(0, int(N*1.5))),
        'gender': rnd.choice(GENDERS),
        'student_id': idx+1,
        'program': [ (p, rnd.randint(1, 5)) for p in rnd.sample(PROGRAMS, k=rnd.randint(1, 2)) ],
        'date_of_birth': rnd.randint(1990, 2002),
        'classes': [ rnd.randint(1, 1000) for _ in range(rnd.randint(1, 10)) ]
    }

rnd.seed(303)
records_many = [ sample_record(i) for i in range(N) ]
