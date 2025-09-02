temp = float(input("Enter Temperature: "))
unit = input("Celsius or Farenheit or Kelvin (C/F/K)?: ")
convert_to = input("Convert to (C/F/K): ")

if unit == convert_to:
    print("No need to convert\n")
    temp = temp
    unit = unit

elif unit == "C" and convert_to == "F":
    temp = (9/5)*temp+32
    unit = "F"
    print(f"{round(temp,2)} {unit}")

elif unit == "C" and convert_to == "K":
    temp = temp+273.15
    unit = "K"
    print(f"{round(temp,2)} {unit}")

elif unit == "F" and convert_to == "C":
    temp = (5/9)*(temp-32)
    unit = "C"
    print(f"{round(temp,2)} {unit}")

elif unit == "F" and convert_to == "K":
    temp = (5/9)*(temp-32)+273.15
    unit = "K"
    print(f"{round(temp,2)} {unit}")

elif unit == "K" and convert_to == "C":
    temp = temp - 273.15
    unit = "C"
    print(f"{round(temp,2)} {unit}")

elif unit == "K" and convert_to == "F":
    temp = (9/5)*(temp-273.15)+32
    unit = "F"
    print(f"{round(temp,2)} {unit}")

else:
    print("Invalid input")