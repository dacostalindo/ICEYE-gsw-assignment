#!/usr/bin/env python3



def return_coins(coffee_price, eur_inserted):



    if eur_inserted < 0 or coffee_price < 0 :
        raise ValueError("All numbers must be positive")

    else:

        if eur_inserted < coffee_price :
            raise ValueError("The money inserted into the machine must greater or equal to the price")

        else:

            twos = ones = decimal50 = decimal20 = decimal10 = decimal5 = decimal2 = decimal1 = 0
            change = eur_inserted -  coffee_price

            if change / 2 >= 1:
                twos = change // 2
                change = change - 2.0*twos

            if change / 1  >= 1 :
                ones = change // 1
                change = change - 1.0*ones

            if change / 0.5 >= 1 :
                decimal50 = change // 0.5
                change = change - 0.5*decimal50

            if change / 0.2 >= 1 :
                decimal20 = change // 0.2
                change = change - 0.2*decimal20

            if change / 0.1 >= 1 :
                decimal10 = change // 0.1
                change = change - 0.1*decimal10

            if change / 0.05 >= 1 :
                decimal5 = change // 0.05
                change = change - 0.05*decimal5

            if change / 0.02 >= 1 :
                decimal2 = change // 0.02
                change = mathchange - 0.02*decimal2

            if change > 0 :
                decimal1 = 1

    change_dict = {
        "2s"   : twos,
        "1s"   : ones,
        "0.5s" : decimal50,
        "0.2s" : decimal20,
        "0.1s" : decimal10,
        "0.05s": decimal5,
        "0.02s": decimal2,
        "0.01s": decimal1,
    }

    return (change_dict)



print(return_coins(1, 4.76))
