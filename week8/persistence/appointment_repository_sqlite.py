from week8.repositories.appointment_repository import AppointmentRepository


class SQLiteAppointmentRepository(AppointmentRepository):

    def __init__(self):
        self.appointments = {}

    def find_by_id(self, appointment_id):
        return self.appointments.get(appointment_id)

    def save(self, appointment):
        self.appointments[appointment.appointment_id] = appointment