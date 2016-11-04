print("Content-type: application/json")
import json
from observer import Observer

'''
response = [{'name':'scooby', 'last':'doo', 'where':'rU'}]
print(json.JSONEncoder().encode(response))
'''

print("\n")


class AlertSniffer:
    def __init__(self):
        self.openObserver = AlertSniffer.OpenObserver(self)
        self.response={'Price':54,'Cost':'99'}
    class OpenObserver(Observer):
        def __init__(self, outer):
            self.outer = outer
        def update(self, observable, arg):
            self.response={'Price':'ALERT ALERT'}

response = AlertSniffer().response
print(json.JSONEncoder().encode(response))
