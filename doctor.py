from bemor import Bemor

class Doctor(Bemor):
    def __init__(self, ism, familiya, ssn, doctor_id, mutaxassisligi) -> None:
        super().__init__(ism, familiya, ssn)
        self._doctor_id = doctor_id
        self._mutaxassisligi = mutaxassisligi

    @property
    def doctor_id(self):
        return self._doctor_id
    
    @property
    def mutaxassisligi(self):
        return self._mutaxassisligi
    
    def __str__(self):
        return f"Shifokor Ismi:{self.ism}, Familiyasi:{self.familiya}, SSN:{self.ssn}, ID:{self.doctor_id}, Mutaxassisligi:{self.mutaxassisligi}"
