from faker import Faker
from typing import NoReturn


def run():
	fake = Faker()
	print(fake.name())
	print(fake.email())
	print(fake.address())

if __name__ == "__main__":
	run()
