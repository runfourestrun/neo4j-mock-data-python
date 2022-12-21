from random import choices


class Schedule:
    def __init__(self,id,technician):
        self.id = id
        self.status = self.status()
        self.schedule_capacity = self.capacity()
        self.technician = technician

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(id={self.id},status = {self.status},schedule_capacity={self.schedule_capacity},technician={self.technician})'

    def capacity(self):
        capacity = range(0, 8)
        weighted_probabilities = [.05, .35, .1, .01, .35, .05, .04, .05]
        choice = choices(capacity, weighted_probabilities, k=1)
        return choice[0]


    def status(self):
        status = ('completed','incompleted','unassigned','assigned')
        weighted_probabilities = [.5,.25,.05,.2]
        choice = choices(status,weighted_probabilities,k=1)
        return choice[0]


class Capacity:
    def __init__(self,id,technician):
        self.id = id
        self.time_available = self.capacity()
        self.technician = technician

    def capacity(self):
        capacity = range(0, 8)
        weighted_probabilities = [.05, .35, .1, .01, .35, .05, .04, .05]
        choice = choices(capacity, weighted_probabilities, k=1)
        return choice[0]

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(id={self.id!r},time_available={self.time_available!r})'

