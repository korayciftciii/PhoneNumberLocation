from builtins import print

import phonenumbers
from phonenumbers import geocoder
phoneNumber=input("Enter a Phone Number :")
phoneNumber1=phonenumbers.parse(phoneNumber)

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phoneNumber1,"en"))