def validate_name(name) :
    if not name :
        return False
    if len(name) > 15 :
        return False
    if not name.isalpha() :
        return False
    return True
def validate_phone_no(phoneno) :
    if len(phoneno) != 10 :
        return False
    if not phoneno.isdigit() :
        return False
    if len(set(phoneno)) == 1 :
        return False
    return True
def validate_email_id(email_id) :
    if email_id.count('@') != 1 or '.com' not in email_id :
        return False
    username, domain = email_id.split('@')
    domain_name, extension = domain.split('.')
    if extension != 'com' :
        return False
    if domain_name not in ['gmail', 'yahoo', 'hotmail'] :
        return False
    return True
def validate_all(name, phone_no, email_id) :
    name_valid = validate_name(name)
    phone_valid = validate_phone_no(phone_no)
    email_valid = validate_email_id(email_id)
    if name_valid and phone_valid and email_valid :
        print("All details are valid. Registration successful!")
    else:
        print("Invalid details! Registration failed.")
name_input = input("Enter your name : ")
phone_input = input("Enter your phone number : ")
email_input = input("Enter your email address : ")
validate_all(name_input, phone_input, email_input)