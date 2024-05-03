temp_val = float(input("Enter temperature value : "))
temp_unit = input("Enter temperature unit (C/F) : ")
if temp_unit == "C":
    temp_val = (temp_val * 9 / 5) + 32
    print(f"Temperature in Fahrenheit : {temp_val}")
elif temp_unit == "F":
    temp_val = (temp_val - 32) * 5 / 9
    print(f"Temperature in Celsius : {temp_val}")
