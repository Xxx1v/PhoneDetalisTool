#Created by @Xxx1V
#This code finding phone number datalis using python

from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
#importing modules

number = input("Enter phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
#sets variables

print(phone)
print("Timezone:", time)
print("Phone service provider:", car)
print("Country:", reg)
input("To Exit Program Press ENTER")
#printing variables