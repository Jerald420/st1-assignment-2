class Patient:
    def __init__(self, patient_id, name, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.contact_info = contact_info


class Practitioner:
    def __init__(self, practitioner_id, name, availability):
        self.practitioner_id = practitioner_id
        self.name = name
        self.availability = availability


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status