from clinic import Clinic

clinic = Clinic()

clinic.addPatient('Sarvinoz', 'Saidova', 3)
print(clinic.getPatient(1))
print(clinic.getPatient(3))

clinic.addDoctor('Madina', 'Rustamova', 23, 12, 'kardiolog')
clinic.addDoctor('Guljahon', 'Abdurashidova', 14, 24, 'dermatolog')
print(clinic.getDoctor(12))
print(clinic.getDoctor(24))

