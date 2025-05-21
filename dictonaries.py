phone = input("Enter the number : ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
Output = ""
for ch in phone:
    Output += digits.get(ch, "!") + (" ")

print(Output)