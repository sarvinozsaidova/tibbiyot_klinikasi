class Bemor:
    def __init__(self, ism, familiya, ssn) -> None:
        self._ism = ism
        self._familiya = familiya
        self._ssn = ssn
    
    @property
    def ism(self):
        return self._ism
    
    
    @property
    def familiya(self):
        return self._familiya
    
    
    @property
    def ssn(self):
        return self._ssn
    
