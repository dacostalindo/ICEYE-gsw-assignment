#!/usr/bin/env python3

def return_coins(coffee_price, eur_inserted):



    if eur_inserted < 0 or coffee_price < 0 :
        raise ValueError("All numbers must be positive")

    else:

        if eur_inserted < coffee_price :
            raise ValueError("The money inserted into the machine must greater or equal to the price")

        else:

            change_dict = {
                200  : 0,
                100  : 0,
                50  : 0,
                20  : 0,
                10  : 0,
                5  : 0,
                2  : 0,
                1  : 0
            }

            change = eur_inserted -  coffee_price
            coins = [200, 100, 50, 20, 10, 5, 2, 1]

            for coin in coins:
                if change / coin >= 1:
                    number_coins = change // coin
                    change_dict[coin] = number_coins
                    change = change - coin * number_coins

            if change > 0 :
                change_dict[1] = 1



    return (change_dict)
