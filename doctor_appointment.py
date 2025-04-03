class DoctorAppointmentSystem:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, patient_name, date, time):
        appointment = {"patient_name": patient_name, "date": date, "time": time}
        self.appointments.append(appointment)
        print(f"Appointment booked for {patient_name} on {date} at {time}.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Scheduled Appointments:")
            for idx, appointment in enumerate(self.appointments, start=1):
                print(f"{idx}. {appointment['patient_name']} - {appointment['date']} at {appointment['time']}")

    def cancel_appointment(self, index):
        if 0 <= index < len(self.appointments):
            removed = self.appointments.pop(index)
            print(f"Cancelled appointment for {removed['patient_name']} on {removed['date']} at {removed['time']}.")
        else:
            print("Invalid appointment index.")

if __name__ == "__main__":
    system = DoctorAppointmentSystem()
    while True:
        print("\n1. Book Appointment\n2. View Appointments\n3. Cancel Appointment\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter patient name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            system.book_appointment(name, date, time)
        elif choice == "2":
            system.view_appointments()
        elif choice == "3":
            system.view_appointments()
            index = int(input("Enter the appointment number to cancel: ")) - 1
            system.cancel_appointment(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
