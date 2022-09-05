
from . import huey

@huey.task()
def add_numbers(a, b):
    return a + b