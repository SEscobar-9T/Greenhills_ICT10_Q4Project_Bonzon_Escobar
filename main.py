from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# class student list
classlist = []

class StudentAddition():
    def __init__(self, name, section, favsub):
        self.name = name
        self.section = section
        self.favsub = favsub

    def introduce(self):
        return f"{self.name} from {self.section} loves the {self.favsub} subject."


def show_creds(e):
    favsub = document.getElementById('inputlist1').value
    name = document.getElementById('inputlist2').value
    section = document.getElementById('inputlist3').value

    student1 = StudentAddition(name, section, favsub)
    classlist.append(student1)

    display(f'{student1.name} from {student1.section} loves the {student1.favsub} subject.', target='output')

listStudent = [
    StudentAddition('Jalainie Abdullah', '10-Topaz', 'Filipino'),
    StudentAddition('Leona Abeleda', '10-Topaz', 'PE'),
    StudentAddition('Renzo Arce', '10-Topaz', 'CAT'),
    StudentAddition('Caleb Arias', '10-Topaz', 'Music'),
    StudentAddition('Cedric Bonzon', '10-Topaz', 'PE'),
    StudentAddition('Martina Cajucom', '10-Topaz', 'Science'),
    StudentAddition('Phoebe Catimbang', '10-Topaz', 'Music'),
    StudentAddition('Sang-Heon Choi', '10-Topaz', 'Social Studies'),
    StudentAddition('Sean Cotioco', '10-Topaz', 'ICT'),
    StudentAddition('Allen Daradal', '10-Topaz', 'ICT'),
    StudentAddition('Alejandro Enriquez', '10-Topaz', 'Social Studies'),
    StudentAddition('Skyler Escobar', '10-Topaz', 'TLE'),
    StudentAddition('Khloe Espina', '10-Topaz', 'Math'),
    StudentAddition('Prince Gano', '10-Topaz', 'Science'),
    StudentAddition('Calvin Garcia', '10-Topaz', 'Math'),
    StudentAddition('Simrandip Kaur', '10-Topaz', 'PE'),
    StudentAddition('Chilli Ong', '10-Topaz', 'Social Studies'),
    StudentAddition('Carl Rufo', '10-Topaz', 'Social Studies'),
    StudentAddition('Ramon Santos', '10-Topaz', 'ICT'),
    StudentAddition('Miguel Sanchez', '10-Topaz', 'Social Studies'),
    StudentAddition('Deryck Tan', '10-Topaz', 'Math'),
    StudentAddition('Beatrix Vilale', '10-Topaz', 'Social Studies'),
    StudentAddition('Harmony Yao', '10-Topaz', 'Music'),
    StudentAddition('Ivy Zosa', '10-Topaz', 'TLE')
]

def show_class(e):
    list = document.getElementById('output2').innerHTML = ''

    for i in listStudent:
        display(i.introduce(), target='output2')

    for i in classlist:
        display(i.introduce(), target='output2')


# attendance tracker
numby_of_days = np.array([0, 0, 0, 0, 0])
weekdays = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

def attend_track(e):
    document.getElementById('output3').innerHTML = ''
    index_grab = int(document.getElementById("absent_day").value)
    absence_value = int(document.getElementById("inputattend").value)

    numby_of_days[index_grab] += absence_value
    print(dict(zip(numby_of_days, weekdays)))

    weekly_attendance = plt.bar(weekdays, numby_of_days)
    plt.show(weekly_attendance)
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel('Number of Absences')
    plt.ylabel('Workday')