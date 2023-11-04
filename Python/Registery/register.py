
def check_registration_rules(**kwargs):
    valid_users = []
    for key, value in kwargs.items():
        if key.lower() != 'quera' and key.lower() !='codecup' and  len(key) > 3:
             if passwod_check_quera(value):
                 valid_users.append(key)

    return valid_users


def passwod_check_quera(password):
    valid = True
    if len(password) <= 5:
        valid = False
    if number_digit_letter(password)[0] == len(password):
        valid = False
    return valid

def number_digit_letter(value):
    digit = letter = 0
    for ch in value:
        if ch.isdigit():
            digit = digit + 1
        elif ch.isalpha():
            letter = letter + 1
        else:
            pass
    return digit, letter

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

if __name__ == '__main__':
    output = check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$')
    print(output)