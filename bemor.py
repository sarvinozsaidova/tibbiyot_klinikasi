from doctor import Doctor

class Bemor:
    def __init__(self, ism, familiya, ssn) -> None:
        self._ism = ism
        self._familiya = familiya
        self._ssn = ssn
        self._doctor = None

    @property
    def ssn(self):
        return self._ssn
    
    def setDoctor(self, doctor):
        self._doctor = doctor

    def getDoctor(self):
        return self._doctor

    def __str__(self) -> str:
        return self._ism