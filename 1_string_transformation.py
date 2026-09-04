booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

parts = booking.strip().split(" | ")
event_code = parts[0]
name = parts[1]
room = parts[2]
time = parts[3]
email = parts[4]
vip_tag = parts[5]

print(f"Event code: {event_code}")

print(f"Name: {name.title()}")

print(f"Room: {room.upper()}")

print(f"Time: {time}")

email_domain = email.split("@")[1].lower()
print(f"Email domain: {email_domain}")

vip_count = vip_tag.count("VIP")
print(f"VIP tag count: {vip_count}")

print(f"Valid event code: {event_code.startswith('EVT-')}")

valid_username = all(c.isalnum() or c == '_' for c in name)
print(f"Valid username: {valid_username}")

valid_room = room[0].isalpha() and "-" in room and room.split("-")[1].isdigit()
print(f"Valid room: {valid_room}")

time_parts = time.split(":")
valid_time = len(time_parts) == 2 and time_parts[0].isdigit() and time_parts[1].isdigit()
print(f"Valid time: {valid_time}")

valid_email = "@" in email and "." in email.split("@")[1]
print(f"Valid email: {valid_email}")

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """

