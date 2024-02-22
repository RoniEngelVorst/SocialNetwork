from abc import ABC, abstractmethod

class Sender(ABC):
    def __init__(self):
        self._members = []
    #adding a member to the list
    def register(self, member):
        self._members.append(member)

    #removing a member from the list
    def unregister(self, member):
        self._members.remove(member)

    #activing the notify function in each user in the list
    def notify(self, content):
        for member in self._members:
            member.update(content)