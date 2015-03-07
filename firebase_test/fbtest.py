__author__ = 'Sam'
from firebase import *

firebase = firebase.FirebaseApplication('https://publicdata-weather.firebaseio.com/denver/', None)
result = firebase.get('currently/temperature', None)
print result