def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You have not provided the required inputs"
    formated_first_name = f_name.title()
    formated_last_name = l_name.title()
    return f"Result: {formated_first_name} {formated_last_name}"
formated_name = format_name(input("Enter the first name"), input("Enter the last name"))
print(formated_name)