import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number=input("Enter your phone number with +country_code: ")
phone_no=phonenumbers.parse(number)
print(phone_no)
time_zone=timezone.time_zones_for_number(phone_no)
print(time_zone)
carrier_name=carrier.name_for_number(phone_no, "en")
print(carrier_name)
location=geocoder.description_for_number(phone_no, "en")
print(location)
is_valid_number = phonenumbers.is_valid_number(phone_no)

