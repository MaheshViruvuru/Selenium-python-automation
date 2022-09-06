# str = "Mynameismahesh"
#
# str_split = str.split(str[4])
# print(str_split[0])

# If day is the first day of the month
week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
max_index = 7
weeks = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for i in range(1000):
    day = str(input("Enter a week: "))
    if day in week_days:
        date = int(input("Enter date to check : "))
        reminder = (date % 7)
        day_index = week_days.index(day)
        print(f"Day index is : {day_index}")
        required_day_index = reminder+(day_index-1)
        print(required_day_index)
        if required_day_index >= max_index:
            required_day_index = max_index-reminder
        required_week = weeks[required_day_index]
        print(required_week)
    else:
        print("Allowed to enter only week days. Thank you!")
    continue_input = input("Do you need to check again: ")
    if continue_input == "Yes":
        print("Start checking again")
    if continue_input == "no":
        print("Thank you")
        break
