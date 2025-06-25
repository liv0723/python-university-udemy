#Banking System

print("*********** Banking System *************")

out_system = input("You want to continue to the banking system (yes/not): ")
out_system = out_system.strip().lower() == 'yes'

if not out_system:
    print("out of system")
else:
    print("Continue in system")


