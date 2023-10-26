from bemor import Bemor
from clinicexeptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor


class Clinic:
    def __init__(self) -> None:
        self.bemorlar :list[Bemor] = []
        self.doctorlar :list[Doctor] = []

    def addPatient(self, bemor  ):
        self.bemorlar.append(bemor)
        print('bemor qoshildi')
    
    def getPatient(self, ssn):
        for bemor in self.bemorlar:
            if bemor.ssn == ssn:
                return bemor
        raise NoSuchPatient(ssn)


    def addDoctor(self, doctor):
        self.doctorlar.append(doctor)
        print("doctor tizimga qo`shildi")

    def getDoctor(self, doctor_id):
        for doctor in self.doctorlar:
            if doctor.id == doctor_id:
                return doctor
        raise NoSuchDoctor(doctor_id)
    
    def assignPatientToDoctor(self, bemor_ssn, doctor_id):
        try:
            doctor = self.getDoctor(doctor_id)
        except:
            raise NoSuchDoctor(doctor_id)
        
        try:
            patient = self.getPatient(bemor_ssn)
        except:
            raise NoSuchPatient(bemor_ssn)
        doctor.getpatients(bemor_ssn)
        patient.setDoctor(doctor_id)

    # def assign_patient_to_doctor(self, patient_ssn, doctor_id):
    #     patient = self.getPatient(patient_ssn)
    #     doctor = self.getDoctor(doctor_id)
    #     patient.setDoctor(doctor)
    #     doctor.getpatients().append(patient)

    # def get_doctor_patients(self, doctor_id):
    #     doctor = self.getDoctor(doctor_id)
    #     return doctor.getpatients()