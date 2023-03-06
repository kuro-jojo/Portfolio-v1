from dataclasses import dataclass

from src.models.UserMessage import UserMessage


def is_data_valid(data: dict, value):
    if value not in data:
        return False
    return True


def fetch_contact_data(data: dict):
    if (
        not is_data_valid(data, "name")
        or not is_data_valid(data, "email")
        or not is_data_valid(data, "message")
    ):
        raise Exception("Invalid form.")

    return UserMessage(data["name"], data["email"], data["message"])
