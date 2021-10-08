class Individual:
    def __init__(self, id, firstname, lastname, age):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_dict(self):
        """
        Helper method to map everything as a dictionnary
        """
        # TODO: Complete method
