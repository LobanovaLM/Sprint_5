import random
import string
import time


def generate_random_email():
    """Генерация случайного email для тестов регистрации"""
    timestamp = int(time.time())
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"testuser_{timestamp}_{random_string}@test.com"


def generate_random_password(length=10):
    """Генерация случайного пароля"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))