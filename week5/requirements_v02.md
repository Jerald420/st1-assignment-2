# SmartCare v0.2 – Requirements Specification

## 1. Problem and Scope

### Problem

SmartCare currently uses spreadsheets and paper records to manage patient information and appointments. Staff experience duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. These problems make appointment management less reliable and harder to maintain.

### Scope

The system will provide a small, maintainable application for managing:

- Patient information
- Practitioner information
- Appointments

The system will focus on the clinic's core patient, practitioner and appointment management needs rather than becoming a complex hospital information system.

### In Scope

- Patient information management
- Practitioner information management
- Appointment management
- Booking appointments
- Viewing practitioner availability
- Appointment status management
- Appointment history

### Out of Scope

- Complex hospital information-system functionality
- AI diagnosis or treatment recommendations
- Facial-recognition login
- Online payment
- Insurance processing

### Provisional Features

The following features require further clarification before being treated as confirmed requirements:

- SMS appointment reminders
- Exact handling of cancelled appointments in appointment history

---

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Receptionist | Manage patient information and appointments | Reception staff are affected by the current manual appointment process |
| Patient | Have accurate appointment information and records | Patients are affected by appointment and patient-record problems |
| Practitioner | View appointments and availability | The case identifies limited visibility of practitioner availability |
| Clinic manager | Reliable appointment information and basic operational reporting | Management wants a simple system to improve current processes |

---

## 3. Functional Requirements

- **FR-01:** The system shall allow staff to create a patient record.

- **FR-02:** The system shall allow staff to search for a patient record.

- **FR-03:** The system shall allow staff to update patient information.

- **FR-04:** The system shall allow staff to create an appointment for a patient with a practitioner.

- **FR-05:** The system shall allow staff to view appointments for a practitioner.

- **FR-06:** The system shall prevent a practitioner from being booked for two appointments at the same time.

- **FR-07:** The system shall allow staff to change an appointment's status.

- **FR-08:** The system shall allow staff to cancel an appointment.

- **FR-09:** The system shall retain appointment history.

- **FR-10:** The system shall allow authorised users to view practitioner availability.

---

## 4. Non-Functional Requirements

- **NFR-01:** The system shall maintain accurate appointment information when appointments are created, changed or cancelled.

- **NFR-02:** The system shall prevent inconsistent appointment data from being stored.

- **NFR-03:** The system shall provide a simple interface that allows staff to complete common appointment-management tasks without unnecessary steps.

- **NFR-04:** The core business logic shall be independently testable.

- **NFR-05:** The system shall be maintainable so that individual components can be updated without requiring unnecessary changes to unrelated functionality.

---

## 5. User Stories

### US-01 — Create Patient Record

As a receptionist, I want to create a patient record so that patient information can be stored and managed in SmartCare.

### US-02 — Search for Patient

As a receptionist, I want to search for a patient so that I can find their information when managing an appointment.

### US-03 — Book Appointment

As a receptionist, I want to book an appointment for a patient with a practitioner so that the patient's appointment is recorded correctly.

### US-04 — View Practitioner Schedule

As a practitioner, I want to view my appointments so that I can see my scheduled patients.

### US-05 — Cancel Appointment

As a receptionist, I want to cancel an appointment so that the appointment status remains accurate.

---

## 6. Acceptance Criteria

### US-01 — Create Patient Record

**Given** the receptionist has entered the required patient information

**When** the receptionist creates the patient record

**Then** the system shall store the patient information.

**Given** required patient information is missing

**When** the receptionist tries to create the patient record

**Then** the system shall not create the record and shall indicate that required information is missing.

### US-02 — Search for Patient

**Given** a patient record exists

**When** the receptionist searches for the patient

**Then** the system shall display the matching patient record.

### US-03 — Book Appointment

**Given** a patient and practitioner are available

**When** the receptionist books an appointment

**Then** the system shall record the appointment for that patient and practitioner.

**Given** the practitioner already has an appointment at the selected time

**When** the receptionist tries to book another appointment for that practitioner

**Then** the system shall prevent the conflicting appointment from being created.

### US-04 — View Practitioner Schedule

**Given** a practitioner has recorded appointments

**When** the practitioner views their schedule

**Then** the system shall display their appointments.

### US-05 — Cancel Appointment

**Given** an appointment exists

**When** the receptionist cancels the appointment

**Then** the system shall update the appointment status to cancelled.

---

## 7. Microsoft Copilot Requirements Review — Verification

| Microsoft Copilot Suggestion | Decision | Reason |
|---|---|---|
| FR-09 should not confirm how cancelled appointments are handled because this is not specified in the case study. | Modified | The case supports keeping appointment history, but the exact treatment of cancelled appointments is not confirmed. FR-09 was changed to require appointment history generally, while cancellation-history behaviour remains provisional. |
| NFR-03 uses ambiguous terms such as "simple" and "unnecessary steps". | Accepted | The case says management wants a simple system, but these terms are difficult to test without clearer criteria. |
| NFR-05 needs clearer criteria for maintainability. | Accepted | The case states that management wants a maintainable system, but it does not define how maintainability should be measured. |
| US-02 uses the word "quickly". | Accepted | "Quickly" is ambiguous because no response-time expectation is provided in the case study. The word was removed. |
| FR-10 should clarify who counts as an "authorised user". | Unverified | The case identifies stakeholders but does not specify an authorisation model. This needs clarification before changing the requirement. |
| FR-07 and FR-08 may overlap because cancellation is an appointment status change. | Modified | Both requirements are supported by the appointment-management scope, but the relationship between changing status and cancelling an appointment should be clarified. |
| NFR-01 and NFR-02 overlap because both address appointment accuracy and consistency. | Modified | Both are supported by the case's problem with inconsistent appointment status, but they should be made more distinct and testable. |

---

## 8. Assumptions and Open Questions

- Who should be considered an authorised user for viewing practitioner availability?
- What specific behaviour is required for cancelled appointments in appointment history?
- How should usability of common appointment-management tasks be assessed?
- What criteria should be used to determine whether the system is maintainable?
- Should SMS appointment reminders be included in the system?

---

## 9. Reflection

Microsoft Copilot helped me identify several areas where my requirements were unclear or difficult to test. One issue it identified was FR-09, which originally stated that cancelled appointments would be retained in appointment history. The case study mentions limited appointment history, but it does not clearly confirm how cancelled appointments should be handled. I therefore modified FR-09 to only require appointment history and kept the cancellation behaviour as an open question.

Microsoft Copilot also identified ambiguous wording such as "quickly" in the patient search user story and "simple" and "unnecessary steps" in the usability requirement. These terms may be difficult to test because they do not have specific definitions or measures.

Some Microsoft Copilot suggestions also needed to be treated as questions rather than confirmed requirements. For example, the meaning of "authorised users" is not clearly defined in the case study.

This review showed me that Microsoft Copilot can help identify gaps and ambiguity, but an AI suggestion is not automatically a valid requirement. Requirements need evidence from the client or stakeholders. Microsoft Copilot can make assumptions that are not supported by the original problem, so human verification is still necessary.