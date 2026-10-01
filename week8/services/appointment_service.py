from week8.repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def cancel_appointment(self, appointment_id: str):
        appointment = self.appointment_repository.find_by_id(appointment_id)

        if appointment is None:
            raise ValueError("Appointment not found")

        appointment.cancel()
        self.appointment_repository.save(appointment)