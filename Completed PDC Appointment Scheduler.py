'''
Program: PDC Appointment Scheduler
Date: April 13, 2022
Purpose: To facilitate the streamlining of the scheduling of the PDC Appointments
Installation Instructions: TBD
'''

from tkinter import *

#Thank you to https://stackoverflow.com/questions/52645557/type-conversion-in-python-stringvar-to-string for the .get() method
    
class Scheduler():
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
        Label(window, text = "Appointment Type:").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Date:").grid(row = 7, column = 1, sticky = W)
        Label(window, text = "Time:").grid(row = 8, column = 1, sticky = W)
        Label(window, text = "Coach Name:").grid(row = 10, column = 1, sticky = W)
        Label(window, text = "Room #:").grid(row = 11, column = 1, sticky = W)
      
        #INPUTS
        self.firstName = StringVar()
        Entry(window, textvariable = self.firstName, justify = RIGHT).grid(row = 2, column = 2)
        self.lastName = StringVar()
        Entry(window, textvariable = self.lastName, justify = RIGHT).grid(row = 3, column = 2)
        self.major = StringVar()
        Entry(window, textvariable = self.major, justify = RIGHT).grid(row = 4, column = 2)
        self.year = StringVar()
        Entry(window, textvariable = self.year, justify = RIGHT).grid(row = 5, column = 2)
        self.appointmentType = StringVar()
        Entry(window, textvariable = self.appointmentType, justify = RIGHT).grid(row = 6, column = 2)
        self.date = StringVar()
        Entry(window, textvariable = self.date, justify = RIGHT).grid(row = 7, column = 2)
        self.time = StringVar()
        Entry(window, textvariable = self.time, justify = RIGHT).grid(row = 8, column = 2)

        #OUTPUTS
        self.coach = StringVar()
        Label(window, textvariable = self.coach).grid(row = 10, column = 2, sticky = E)
        self.room = StringVar()
        Label(window, textvariable = self.room).grid(row = 11, column = 2, sticky = E)

        #BUTTONS
        Button(window, text = "Schedule", command = self.get_appointment).grid(row = 13, column = 2, sticky = E)
        Button(window, text = "Help").grid(row = 14, column = 2, sticky = E)

        window.mainloop()
        
    def get_appointment(self):
    #This function creates the appointment, calling schedule room and schedule coach, to display the details for the appointment on the interface
        #Data Validation for Major
        while (self.major.get() not in majors):
            self.studentMajorErrorMessage()
        #Data Validation for Year
        while (self.year.get() not in years):
            self.studentYearErrorMessage()
        #Data Validation for Appointment Type
        while (self.appointmentType.get() not in appointmentTypes):
            self.appointmentTypeErrorMessage()
        #Data Validation for Time
        while (self.time.get() not in appointmentTimes):
            self.appointmentTimeErrorMessage()
        self.schedule_room(rooms)
        self.schedule_coach(coaches)

    def get_room_assignment(self,roomList,takenList):
    #This function chooses a room to assign to the appointment picking between a list containing all of the PDC's available rooms
        count = len(roomList)-1
        while count >= 0:
            if(roomList[count] not in takenList):
                takenList.append(roomList[count])
                return roomList[count]
            count -=1
        return 'Rooms are Full'
            

    def schedule_room(self, roomList):
    #This function displays the room assignment and removes room avilability based on the time it is reserved for
        if(self.time.get() == '8 am'):
            self.room.set(self.get_room_assignment(roomList,takenRooms8am))
        elif(self.time.get() == '9 am'):
            self.room.set(self.get_room_assignment(roomList,takenRooms9am))
        elif(self.time.get() == '10 am'):
            self.room.set(self.get_room_assignment(roomList,takenRooms10am))
        elif(self.time.get() == '11 am'):
            self.room.set(self.get_room_assignment(roomList,takenRooms11am))
        elif(self.time.get() == '12 pm'):
            self.room.set(self.get_room_assignment(roomList,takenRooms12pm))
        elif(self.time.get() == '1 pm'):
            self.room.set(self.get_room_assignment(roomList,takenRooms1pm))
        elif(self.time.get() == '2 pm'):
            self.room.set(self.get_room_assignment(roomList,takenRooms2pm))
        elif(self.time.get() == '3 pm'):
            self.room.set(self.get_room_assignment(roomList,takenRooms3pm))
        elif(self.time.get() == '4 pm'):
            self.room.set(self.get_room_assignment(roomList,takenRooms4pm))

    def get_coach_assignment(self,coachList, coachTakenList):
        #This function chooses a coach to assign to a given appointment from the list of coaches 
        count2 = len(coachList)-1
        while (count2>=0):
            if(coachList[count2] not in coachTakenList):
                coachTakenList.append(coachList[count2])
                return coachList[count2]
            count2 -=1
        return 'No coaches available'

    def schedule_coach(self, coachList):
        #This function displays the coach assignment and removes coach avilability based on the time they are reserved for
        if(self.time.get() == '8 am'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches8am))
        elif(self.time.get() == '9 am'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches9am))
        elif(self.time.get() == '10 am'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches10am))
        elif(self.time.get() == '11 am'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches11am))
        elif(self.time.get() == '12 pm'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches12pm))
        elif(self.time.get() == '1 pm'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches1pm))
        elif(self.time.get() == '2 pm'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches2pm))
        elif(self.time.get() == '3 pm'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches3pm))
        elif(self.time.get() == '4 pm'):
            self.coach.set(self.get_coach_assignment(coachList,takenCoaches4pm))
    
    #Error messages lines error = Tk() and error.mainloop() inspired by Glamping World Call-in Order Form by Digital Innovators (55-5) from example in class
    def appointmentTypeErrorMessage(self):
        #This function displays an error message if a non supported appointment type format is inputted into the application
        error = Tk()
        error.title("Invalid Appointment Type")
        Label(error, text = "Please input a valid appointment type from the following list:").grid(row = 1, column = 1, sticky = W)
        Label(error, text = "Mock Interview").grid(row = 2, column = 1, sticky = W)
        Label(error, text = "Presentation Coaching").grid(row = 3, column = 1, sticky = W)
        Label(error, text = "Resume Review").grid(row = 4, column = 1, sticky = W)
        Label(error, text = "Room Reservation").grid(row = 5, column = 1, sticky = W)
        error.mainloop()
    
    def appointmentTimeErrorMessage(self):
        #This function displays an error message if a non supported appointment time format is inputted into the application
        error2 = Tk()
        error2.title("Invalid Appointment Time")
        Label(error2, text = "Please input a valid appointment time from the following list:").grid(row = 1, column = 1, sticky = W)
        Label(error2, text = "8 am").grid(row = 2, column = 1, sticky = W)
        Label(error2, text = "9 am").grid(row = 3, column = 1, sticky = W)
        Label(error2, text = "10 am").grid(row = 4, column = 1, sticky = W)
        Label(error2, text = "11 am").grid(row = 5, column = 1, sticky = W)
        Label(error2, text = "12 pm").grid(row = 6, column = 1, sticky = W)
        Label(error2, text = "1 pm").grid(row = 7, column = 1, sticky = W)
        Label(error2, text = "2 pm").grid(row = 8, column = 1, sticky = W)
        Label(error2, text = "3 pm").grid(row = 9, column = 1, sticky = W)
        Label(error2, text = "4 pm").grid(row = 10, column = 1, sticky = W)
        error2.mainloop()

    def studentYearErrorMessage(self):
        #This function displays an error message if a non supported student year format is inputted into the application
        error3 = Tk()
        error3.title("Invalid Student Year")
        Label(error3, text = "Please input a valid year from the following list:").grid(row = 1, column = 1, sticky = W)
        Label(error3, text = "First Year").grid(row = 2, column = 1, sticky = W)
        Label(error3, text = "Second Year").grid(row = 3, column = 1, sticky = W)
        Label(error3, text = "Third Year").grid(row = 4, column = 1, sticky = W)
        Label(error3, text = "Fourth Year").grid(row = 5, column = 1, sticky = W)
        Label(error3, text = "MBA").grid(row = 6, column = 1, sticky = W)
        error3.mainloop()
    
    def studentMajorErrorMessage(self):
        #This function displays an error message if a non supported student major format is inputted into the application
        error4 = Tk()
        error4.title("Invalid Student Major Code")
        Label(error4, text = "Please input a valid major from the following codes:").grid(row = 1, column = 1, sticky = W)
        Label(error4, text = "(If double major, put code most applicable to the appointment)").grid(row = 2, column = 1, sticky = W)
        Label(error4, text = "MKT : Marketing").grid(row = 3, column = 1, sticky = W)
        Label(error4, text = "PRE : Pre-Business").grid(row = 4, column = 1, sticky = W)
        Label(error4, text = "ACT : Accounting").grid(row = 5, column = 1, sticky = W)
        Label(error4, text = "E&I : Entreprenuership and Innovation").grid(row = 6, column = 1, sticky = W)
        Label(error4, text = "FIN : Finance").grid(row = 7, column = 1, sticky = W)
        Label(error4, text = "FRE : Finance with Real Estate").grid(row = 8, column = 1, sticky = W)
        Label(error4, text = "MAN : Management").grid(row = 9, column = 1, sticky = W)
        Label(error4, text = "SCM : Supply Chain Management").grid(row = 10, column = 1, sticky = W)
        error4.mainloop()
#List of the rooms available for reservation at the PDC
rooms = ['2212E', '2212H', '2212J', '2212K']  
#Sample list of PDC Coaches
coaches = ['Jordan Powell', 'Abraham Salinas', 'Bridget French', 'Biffy Totsi']
#List containing the student year distinctions at TCU
years = ['First Year', 'Second Year', 'Third Year', 'Fourth Year', 'MBA']
#List of the appointments that the PDC performs
appointmentTypes =['Mock Interview', 'Presentation Coaching', 'Resume Review', 'Room Reservation']
#Hourly list of times that the PDC is open for appointments in a day
appointmentTimes =['8 am', '9 am', '10 am', '11 am', '12 pm', '1 pm', '2 pm', '3 pm', '4 pm']
#List of majors that are available for students to pursue at Neeley
majors = ['MKT', 'PRE', 'ACT', 'E&I', 'FIN', 'FRE', 'MANA', 'SCM']
#Lists that contain taken coaches and rooms at a given hour based on the appointments scheduled
takenRooms8am = []
takenRooms9am = []
takenRooms10am = []
takenRooms11am = []
takenRooms12pm = []
takenRooms1pm = []
takenRooms2pm = []
takenRooms3pm = []
takenRooms4pm = []
takenCoaches8am = []
takenCoaches9am = []
takenCoaches10am = []
takenCoaches11am = []
takenCoaches12pm = []
takenCoaches1pm = []
takenCoaches2pm = []
takenCoaches3pm = []
takenCoaches4pm = []
Scheduler()  # Create GUI