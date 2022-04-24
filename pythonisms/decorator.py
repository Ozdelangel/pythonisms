
from functools import wraps
def cool_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        origin_val = func(*args, **kwargs)
        return f'the best fighter at aka is "{origin_val}"'
    return wrapper

def other_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        origin_val = func(*args, **kwargs)
        return f'you are right "{origin_val}" '
    return wrapper



# @cool_decorator
@other_decorator
def fight_talk(txt):
    return txt
if __name__ == "__main__":
    print(fight_talk('daniel cormier'))