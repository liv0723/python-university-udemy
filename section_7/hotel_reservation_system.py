#Hotel Reservation System


print("************* Hotel Reservation System ***************")

ROOM_VIEW = 190.5
ROOM_OUT_VIEW = 150.5

client_name = input("Intro the name of client: ")
days = int(input("Intro the days of reservation:"))
have_sea_view = input("Intro if have sea view (yes/not): ").strip().lower() == 'yes'

if have_sea_view:
    total_amount = days * ROOM_VIEW
else:
    total_amount = days * ROOM_OUT_VIEW

print(f"""
    The client: {client_name}
    Your instance is: {days}
    Have sea view: {'Yes' if have_sea_view else 'Not'}
    Amount by day : {ROOM_OUT_VIEW}
    total Amount: {total_amount}
    """)



