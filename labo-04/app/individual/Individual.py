class Individual:
    def __init__(self,firstname, lastname, age, id=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_dict(self):
        """
        Helper method to map everything as a dictionnary
        """
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "age": self.age
        }
