import pywhatkit

"""
pywhatkit.sendwhatmsg("phone_number", "message", "time_hour", "time_min", "wait_time", "tab_close", "close_time")
"""
# contact_number = input("Enter any person number: ")
contact_number = "+91 9492230694"

# pywhatkit.sendwhatmsg(contact_number, "Hi", 13, 29)
# 15 sec - default wait time

pywhatkit.sendwhatmsg(contact_number, "Had Lunch", 13, 42, 15,True, 2)

"""
pywhatkit.sendwhatmsg("group_id", "message", "time_hour", "time_min", "wait_time", "tab_close", "close_time")
"""