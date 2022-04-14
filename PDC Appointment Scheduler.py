'''
Program: PDC Appointment Scheduler
Date: April 13, 2022
Purpose: To facilitate the streamlining of the scheduling of the PDC Appointments
Installation Instructions: TBD
'''

from tkinter import *
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

class scheduler():
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
        Appointment(self.firstname,self.lastname,self.major,self.year,self.groupsize,self.appointmentType,self.date,self.time,self.get_room_assignment,'''self.get_coach_assignment''')
        self.schedule_room()
        #self.schedule_coach()

    def get_room_assignment(self):
    #This function chooses a room to assign to the appointment picking between a list containing all of the PDC's available rooms
        room1 = Room('2212E')
        room2 = Room('2212H')
        room3 = Room('2212J')
        room4 = Room('2212K')
        rooms = [room1, room2, room3, room4]
        count = len(rooms)-1
        while count >= 0:
            if (rooms[count].availability == 'open'):
                rooms[count].assign_room()
                return rooms[count].name
            count -= 1
            print('help')
                
    def schedule_room(self):
    #This function displays the room assignment
        self.room.set(self.get_room_assignment())

    '''
    def get_coach_assignment(self):
        #This function chooses a coach to assign to a given appointment from the list coaches based upon alike majors
        coach1 = Coach('Jordan Powell', 'SCM', 'Junior', 'jordan.powell@tcu.edu')
        coach2 = Coach('Abraham Salinas', 'Marketing', 'Senior', 'A.SALINAS@tcu.edu')
        coach3 = Coach('Bridget French','Finance','Senior','BRIDGET.FRENCH@tcu.edu')
        coach4 = Coach('Biffy Totsi','BIS','Junior','ELIZABETH.TOSTI@tcu.edu')
        coaches = [coach1, coach2, coach3, coach4]
        count2 = len(coaches)-1
        while (count2>=0):
            #Currently an infinte loop is occuring
            if(coaches[count2].major == self.major):
                return coaches[count2].name
    '''
    
    #def schedule_coach(self):
        #This function displays the coach assignment
        #self.coach.set(self.get_coach_assignment())
    
scheduler()  # Create GUI



