from faker import Faker


def run():
    fake = Faker()
    print(fake.name())
    print(fake.email())
    print(fake.address())


if __name__ == "__main__":
    run()
