'''
Program: PDC Appointment Scheduler
Date: April 13, 2022
Purpose: To facilitate the streamlining of the scheduling of the PDC Appointments
Installation Instructions: 
'''

from tkinter import *
class scheduler:
    def __init__(self):
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
        self.firstname = StringVar()
        Entry(window, textvariable = self.firstname, justify = RIGHT).grid(row = 2, column = 2)
        self.lastname = StringVar()
        Entry(window, textvariable = self.lastname, justify = RIGHT).grid(row = 3, column = 2)
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
        Label(window, textvariable = self.coach).grid(row = 9, column = 2, sticky = E)
        self.room = StringVar()
        Label(window, textvariable = self.room).grid(row = 10, column = 2, sticky = E)

        #BUTTONS
        Button(window, text = "Schedule").grid(row = 12, column = 2, sticky = E)
        Button(window, text = "Help").grid(row = 13, column = 2, sticky = E)

        window.mainloop()

scheduler()  # Create GUI