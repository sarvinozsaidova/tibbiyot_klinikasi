class NoSuchPatient(Exception):
    def __init__(self, ssn) -> None:
        self._ssn = str(ssn)
        self.message = self._ssn + "  raqamlik bemor yo`q"
        super().__init__(self.message)


class NoSuchDoctor(Exception):
    def __init__(self, id) -> None:
        self._id = str(id)
        self.message = self._id + "  id lik bemor yo`q"
        super().__init__(self.message)