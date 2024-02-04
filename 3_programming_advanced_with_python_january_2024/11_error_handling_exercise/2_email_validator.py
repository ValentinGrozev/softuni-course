from colorama import Fore
import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainDigitError(Exception):
    pass


class ContainSpaceError(Exception):
    pass


class InvalidNameError(Exception):
    pass


SEARCHED_SYMBOL = "@"
VALID_DOMAINS = ["com", "bg", "org", "net"]
MIN_LENGTH_OF_NAME = 4
MIN_DIGITS_IN_NAME = 1

email = input()

while email != "End":
    name = email.split("@")[0]
    domain_info = email.split(".")[-1]
    numbers = len([letter for letter in name if letter.isdigit()])
    pattern_for_regex = r"\w+"

    if len(name) <= MIN_LENGTH_OF_NAME:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.count(SEARCHED_SYMBOL) != 1:
        raise MustContainAtSymbolError("Email must contain exactly one @")
    elif domain_info not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    elif numbers < MIN_DIGITS_IN_NAME:
        raise MustContainDigitError("Name must contain at least one digit")
    elif " " in email:
        raise ContainSpaceError("Email must not contain spaces")
    elif name != re.findall(pattern_for_regex, name)[0]:
        raise InvalidNameError("Email must contain only letters, digits and underscores")

    print(f"{Fore.BLUE}Email {email} is valid")

    email = input()
