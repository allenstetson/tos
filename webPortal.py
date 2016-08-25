print("Content-type: application/json")
import json
'''
response = [{'name':'scooby', 'last':'doo', 'where':'rU'}]
print(json.JSONEncoder().encode(response))
'''

print("\n")
response={'Price':54,'Cost':'99'}
print(json.JSONEncoder().encode(response))

'''
from Observer import Observer, Observable

class Flower:
    def __init__(self):
        self.isOpen = 0
        self.openNotifier = Flower.OpenNotifier(self)
        self.closeNotifier= Flower.CloseNotifier(self)
    def open(self): # Opens its petals
        self.isOpen = 1
        self.openNotifier.notifyObservers()
        self.closeNotifier.open()
    def close(self): # Closes its petals
        self.isOpen = 0
        self.closeNotifier.notifyObservers()
        self.openNotifier.close()
    def closing(self): return self.closeNotifier

    class OpenNotifier(Observable):
        def __init__(self, outer):
            Observable.__init__(self)
            self.outer = outer
            self.alreadyOpen = 0
        def notifyObservers(self):
            if self.outer.isOpen and \
            not self.alreadyOpen:
                self.setChanged()
                Observable.notifyObservers(self)
                self.alreadyOpen = 1
        def close(self):
            self.alreadyOpen = 0
'''