from bemor import Bemor

class Doctor(Bemor):
    def __init__(self, ism, familiya, ssn, id, mutaxassisligi) -> None:
        super().__init__(ism, familiya, ssn)
        self._id = id
        self._mutaxassisligi = mutaxassisligi
        self._bemorlar :list[Bemor] = []

    @property
    def id(self):
        return self._id
    
    @property
    def mutaxassisligi(self):
        return self._mutaxassisligi
    
    def getpatients(self):
        return self._bemorlar

    
    def __str__(self) -> str:
        return super().__str__()
