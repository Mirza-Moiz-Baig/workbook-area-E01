import random

def guess_items_price(guess):
    
    random_prices = [
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
    ]
    print(F"The prices were: {random_prices}")

    if guess in random_prices:
        return True
    else:
        return False


def guess_car_price(guess):
    """Compares the price of the car with the user guess.
    returns appropiate string based on the comparison.
    """
    car_price = random.randint(10000,50000)
    if guess == car_price :
        return "You win! That's exactly the price! You're a cheater!" 
    elif guess < (car_price + 1000) and guess > (car_price - 1000):
        return "You win!"
    elif guess > (car_price - 5000) and guess < (car_price + 5000):
        return "You're close!"
    else:
        return "Way off!"