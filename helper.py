from faker import Faker

faker = Faker()

def generate_registration_data():
    first_name = faker.first_name().lower()
    last_name = faker.last_name().lower()
    digits = faker.random_int(min=100, max=999)
    email = f"{first_name}{last_name}21{digits}@yandex.kz"
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password

def generate_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return password