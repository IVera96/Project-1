from utils.openspace import Openspace
from utils.table import Table
from random import shuffle
import pandas as pd
import math
import fileinput


def extract_file(file_name:str, header: str):
        converted_file = pd.read_excel(file_name)
        return list(converted_file[header])


def calculte_tables_for_unseated(unseated: int, max_capacity: int, min_capacity: int):
    if unseated <= max_capacity:
        
        return [Table(unseated, [])]
    else:
        _max = max_capacity
        while (unseated % _max) <= min_capacity:
            _max -= 1
            if _max < min_capacity:
                _max = min_capacity
                break

        extra_tables = []
        nb_new_tables = math.floor(unseated / _max)
        for table in range(nb_new_tables):
             extra_tables.append(Table(_max, []))
        # extra_tables = [{"tables": nb_new_tables, "seats": _max}]

        remaining_people = unseated % _max
        if remaining_people > 0:
            extra_tables.append(Table(remaining_people, []))
        return extra_tables
        
       
                
        

is_running = True

students_list = extract_file('bouman_8.xlsx', 'Students')
shuffle(students_list)
tables_list = [Table(4, []) for table in range(6)]
open_space = Openspace([], 6)
open_space.organize(students_list,tables_list)
extra_tables = calculte_tables_for_unseated(9,2,6)
print(len(students_list[24:33]))
open_space.organize(students_list[24:33],extra_tables)
open_space.display()


def possybility_to_ask(openspace):
    count_name=0
    count_seat=0
    a=int(input('What do you whant to know? \n 1.how much seats are in the room,\n 2.how much people are in the room, \n 3.how much seats are left:\n Insert the number of the question:'))
    
    if a==1:
        for table in openspace.tables:
            count_seat+=len(table.seats)
        print(f'There are {count_seat} seats in the room')
    elif a==2:
        for name in range(len(students_list)):
            count_name+=1
        print(f'In the room there are {count_name} personne')
    elif a==3:
        print(open_space.get_unseated(len(students_list)))