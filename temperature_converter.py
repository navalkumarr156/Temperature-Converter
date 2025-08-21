print("Temperature Converter")

choice = input("Convert (C/F): ").lower()
temp = float(input("Enter temperature: "))

if choice == "c":
    print(f"{temp}°C = {(temp * 9/5) + 32}°F")
elif choice == "f":
    print(f"{temp}°F = {(temp - 32) * 5/9}°C")
else:
    print("Invalid choice!")