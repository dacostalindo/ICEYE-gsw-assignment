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
                05  : 0,
                02  : 0,
                01  : 0
            }

            change = eur_inserted -  coffee_price
            coins = [200, 100, 50, 20, 10, 5, 2, 1]

            for coin in coins:
                if change / coin >= 1:
                    number_coins = change // coin
                    change_dict[coin] = number_coins
                    change = change - coin * number_coins

            """
            Commenting goes here


            """

            # if change / 2 >= 1:
            #     twos = change // 2
            #     change = change - 2.0*twos
            #
            # if change / 1  >= 1 :
            #     ones = change // 1
            #     change = change - 1.0*ones
            #
            # if change / 0.5 >= 1 :
            #     decimal50 = change // 0.5
            #     change = change - 0.5*decimal50
            #
            # if change / 0.2 >= 1 :
            #     decimal20 = change // 0.2
            #     change = change - 0.2*decimal20
            #
            # if change / 0.1 >= 1 :
            #     decimal10 = change // 0.1
            #     change = change - 0.1*decimal10
            #
            # if change / 0.05 >= 1 :
            #     decimal5 = change // 0.05
            #     change = change - 0.05*decimal5
            #
            # if change / 0.02 >= 1 :
            #     decimal2 = change // 0.02
            #     change = mathchange - 0.02*decimal2


            if change > 0 :
                change_dict[1] = 1



    return (change_dict)
