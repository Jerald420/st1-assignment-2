from enum import Enum


class Patient:
    def __init__(self, patient_id: str, name: str, contact_info: str):
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name
        self.contact_info = contact_info


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date_time: str
    ):
        if not appointment_id:
            raise ValueError("Appointment ID cannot be empty")

        if patient is None:
            raise ValueError("Appointment must have a patient")

        if practitioner is None:
            raise ValueError("Appointment must have a practitioner")

        if not date_time.strip():
            raise ValueError("Appointment date/time cannot be empty")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self):
        return self._status

    def cancel(self):
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError("Only scheduled appointments can be cancelled")

        self._status = AppointmentStatus.CANCELLED