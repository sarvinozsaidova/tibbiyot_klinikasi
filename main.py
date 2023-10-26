from clinic import Clinic
from bemor import Bemor
from doctor import Doctor

kasalxona = Clinic()

bemor1 = Bemor('Madina', 'Rustamova', 123432)
kasalxona.addPatient(bemor1)
print(kasalxona.getPatient(123434))

# doctor1 = Doctor('Guljahon', "Abdurashidova", 123432, 1, "Stomatolog")
# kasalxona.addDoctor(doctor1)
# print(kasalxona.getDoctor(2))

doctor2 = Doctor('Guljahon', "Abdurashidova", 1234321, 1, "Stomatolog")
kasalxona.addDoctor(doctor2)

kasalxona.assignPatientToDoctor(1234321, 1)

patient = kasalxona.getPatient(123432)
print(patient._ism())
print(patient._familiya())
print(patient._ssn())