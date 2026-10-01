from abc import ABC, abstractmethod


class AppointmentRepository(ABC):

    @abstractmethod
    def find_by_id(self, appointment_id):
        pass

    @abstractmethod
    def save(self, appointment):
        pass