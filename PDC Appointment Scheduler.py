'''
Program: PDC Appointment Scheduler
Date: April 13, 2022
Purpose: To facilitate the streamlining of the scheduling of the PDC Appointments
Installation Instructions: TBD
'''

from tkinter import *
from random import *

class Appointment():
    def __init__(self, firstname, lastname, major, year, groupsize, appointmentType, date, time, room, coach):
        #__init__ fucntion used to define all of the characteristics of an appointment
        Appointment.firstname = firstname
        Appointment.lastname = lastname
        Appointment.major = major
        Appointment.year = year
        Appointment.groupsize = groupsize
        Appointment.appointmentType = appointmentType
        Appointment.date = date
        Appointment.time = time
        Appointment.room = room
        Appointment.coach = coach
class Room():
    def __init__(self, name):
        #__init__ fucntion used to define all of the characteristics of a room
        Room.name = name
        Room.availability = 'open'
    def assign_room(self):
        #Once the room has been assigned to an appointment this function is used to change the avilability of the room
        self.availability = 'taken'
class Coach():
    def __init__(self, name, major, year, email):
        #__init__ fucntion used to define all of the characteristics of an coach
        Coach.name = name
        Coach.major = major
        Coach.year = year
        Coach.email = email
        Coach.availability = "Open"

class scheduler(Room):
    def __init__(self):
        #The__init__function was inspired by the Loan Calculator example in class
        window = Tk()
        window.title("PDC Appointment Scheduler")
        photo = PhotoImage(file=r'PDClogo.gif') 
        Label(window, image=photo).grid(row = 1, column = 1, sticky = W)  
        Label(window, text = "PDC Appointment Scheduler").grid(row = 1, column = 2, sticky = W)
        Label(window, text = "First Name:").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Last Name:").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Major:").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Year:").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Group Size:").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Appointment Type:").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Date:").grid(row = 8, column = 1, sticky = W)
        Label(window, text = "Time:").grid(row = 9, column = 1, sticky = W)
        Label(window, text = "Coach Name:").grid(row = 11, column = 1, sticky = W)
        Label(window, text = "Room #:").grid(row = 12, column = 1, sticky = W)
      
        #INPUTS
        self.firstname = StringVar()
        Entry(window, textvariable = self.firstname, justify = RIGHT).grid(row = 2, column = 2)
        self.lastname = StringVar()
        Entry(window, textvariable = self.lastname, justify = RIGHT).grid(row = 3, column = 2)
        self.major = StringVar()
        Entry(window, textvariable = self.major, justify = RIGHT).grid(row = 4, column = 2)
        self.year = StringVar()
        Entry(window, textvariable = self.year, justify = RIGHT).grid(row = 5, column = 2)
        self.groupsize = int()
        Entry(window, textvariable = self.groupsize, justify = RIGHT).grid(row = 6, column = 2)
        self.appointmentType = StringVar()
        Entry(window, textvariable = self.appointmentType, justify = RIGHT).grid(row = 7, column = 2)
        self.date = StringVar()
        Entry(window, textvariable = self.date, justify = RIGHT).grid(row = 8, column = 2)
        self.time = StringVar()
        Entry(window, textvariable = self.time, justify = RIGHT).grid(row = 9, column = 2)

        #OUTPUTS
        self.coach = StringVar()
        Label(window, textvariable = self.coach).grid(row = 11, column = 2, sticky = E)
        self.room = StringVar()
        Label(window, textvariable = self.room).grid(row = 12, column = 2, sticky = E)

        #BUTTONS
        Button(window, text = "Schedule", command = self.get_appointment).grid(row = 13, column = 2, sticky = E)
        Button(window, text = "Help").grid(row = 14, column = 2, sticky = E)


        window.mainloop()
        
    def get_appointment(self):
    #This function creates the appointment, calling schedule room and schedule coach, to display the details for the appointment on the interface
        Appointment(self.firstname,self.lastname,self.major,self.year,self.groupsize,self.appointmentType,self.date,self.time,'TBD','TBD')
        self.schedule_room(rooms)
        self.schedule_coach(coaches)

    def get_room_assignment(self,roomlist,takenlist):
    #This function chooses a room to assign to the appointment picking between a list containing all of the PDC's available rooms
        count = len(roomlist)-1
        while count >= 0:
            #if (roomlist[count].availability == 'open'):
            if(roomlist[count] not in takenlist):
                #roomlist[count].assign_room()
                takenRooms.append(roomlist[count])
                #return roomlist[count].name
                return roomlist[count]
            count -=1
        return 'Rooms are Full'
            

    def schedule_room(self, roomlist):
    #This function displays the room assignment
        self.room.set(self.get_room_assignment(roomlist,takenRooms))
        '''
        if(self.time == '8 am'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms8am))
        elif(self.time == '9 am'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms9am))
        elif(self.time == '10 am'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms10am))
        elif(self.time == '11 am'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms11am))
        elif(self.time == '12 pm'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms12pm))
        elif(self.time == '1 pm'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms1pm))
        elif(self.time == '2 pm'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms2pm))
        elif(self.time == '3 pm'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms3pm))
        elif(self.time == '4 pm'):
            self.room.set(self.get_room_assignment(roomlist,takenRooms4pm))
        '''
        
    def get_coach_assignment(self,coachlist, ctakenlist):
        #This function chooses a coach to assign to a given appointment from the list coaches based upon alike majors
        count2 = len(coachlist)-1
        while (count2>=0):
            if(coachlist[count2] not in ctakenlist):
                ctakenlist.append(coachlist[count2])
                return coachlist[count2]
            count2 -=1
        return 'No coaches avilable'

    def schedule_coach(self, coachlist):
        #This function displays the coach assignment
        self.coach.set(self.get_coach_assignment(coachlist,takenCoaches))
        '''
        if(self.time == '8 am'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches8am))
        elif(self.time == '9 am'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches9am))
        elif(self.time == '10 am'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches10am))
        elif(self.time == '11 am'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches11am))
        elif(self.time == '12 pm'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches12pm))
        elif(self.time == '1 pm'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches1pm))
        elif(self.time == '2 pm'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches2pm))
        elif(self.time == '3 pm'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches3pm))
        elif(self.time == '4 pm'):
            self.coach.set(self.get_coach_assignment(coachlist,takenCoaches4pm))
        #else:
            #self.coach.set('Not a valid time input')
        '''

#room1 = Room('2212E')
#room2 = Room('2212H')
#room3 = Room('2212J')
#room4 = Room('2212K')
#rooms = [room1, room2, room3, room4]
rooms = ['2212E', '2212H', '2212J', '2212K']  
#coach1 = Coach('Jordan Powell', 'SCM', 'Junior', 'jordan.powell@tcu.edu')
#coach2 = Coach('Abraham Salinas', 'Marketing', 'Senior', 'A.SALINAS@tcu.edu')
#coach3 = Coach('Bridget French','Finance','Senior','BRIDGET.FRENCH@tcu.edu')
#coach4 = Coach('Biffy Totsi','BIS','Junior','ELIZABETH.TOSTI@tcu.edu')
coaches = ['Jordan Powell', 'Abraham Salinas', 'Bridget French', 'Biffy Totsi']
takenRooms = []
takenRooms8am = []
takenRooms9am = []
takenRooms10am = []
takenRooms11am = []
takenRooms12pm = []
takenRooms1pm = []
takenRooms2pm = []
takenRooms3pm = []
takenRooms4pm = []
takenCoaches = []
takenCoaches8am = []
takenCoaches9am = []
takenCoaches10am = []
takenCoaches11am = []
takenCoaches12pm = []
takenCoaches1pm = []
takenCoaches2pm = []
takenCoaches3pm = []
takenCoaches4pm = []
scheduler()  # Create GUI



