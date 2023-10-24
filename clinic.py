from bemor import Bemor
from doctor import Doctor


class Clinic:
    def __init__(self) -> None:
        self.bemorlar :list[Bemor] = []
        self.doctorlar :list[Doctor] = []

    def addPatient(self,ism, familiya, ssn ):
        bemor = Bemor(ism, familiya, ssn)
        self.bemorlar.append(bemor)
        print('bemor qoshildi')
    
    def getPatient(self, id):
        for bemor in self.bemorlar:
            if bemor.ssn == id:
                return bemor
        return 'NoSuchPatient'
    

    def addDoctor(self, ism, familiya, ssn, doctor_id, mutaxassisligi):
        doctor = Doctor(ism, familiya, ssn, doctor_id, mutaxassisligi)
        self.doctorlar.append(doctor)
        print('shifokor kiritildi')

    def getDoctor(self, doctor_id):
        for doctor in self.doctorlar:
            if doctor.doctor_id == doctor_id:
                return doctor
        return 'NoSuchPatient'


