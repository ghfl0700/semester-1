# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
       
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

        """Initialise a Person with name and birth date."""
        if type(name) is not str:
            raise TypeError
        if type(birth) is not date:
            raise TypeError
        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """Return the initials of the name."""
        name_part = self.name.split()
        result = ""
        for part in name_part:
            first_letter = part[0].upper()
            result = result + first_letter
        return result 

    def is_birthday(self):
        """Check if today is the birthday."""
        today = date.today()
        if today.month == self.birth.month and today.day == self.birth.day:
            return True
        else:
            return False


        