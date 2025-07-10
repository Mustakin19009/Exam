t= float(input("Temperature: "))
u = input("Unit (C/F): ").upper()
if u == 'C':
    print(f"{(t*9/5)+32:.2f}°F")
elif u == 'F': 
    print(f"{(t-32)*5/9:.2f}°C")
else: print("Invalid unit")