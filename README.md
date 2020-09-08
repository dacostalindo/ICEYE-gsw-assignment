# ICEYE Ground Software Assignment



## Task 1 - LARVIS will not mess with my coffee

In this repository, the task 1 folder is split between the return_coins function and its corresponding test cases.

The return_coins function outputs a dictionary with the amount of coins for each segment (2€, 1€, 0.5€, 0.2€, 0.1€, 0.05€, 0.02€, and 0.01€). While the test cases verify the sum of the coins is equal to the given change.

The unit test

```
Class TestTask1(unittest.TestCase):

    def test_sum(self):
    ...
```

asserts the equality between the theoretical and empirical value returned by

```
def return_coins(coffee_price, eur_inserted):
```
Please keep in mind the dictionary returned from has keys that represent the value of the existing coins in cents. Therefore, the randomly generated number for the price inserted, as well as the the price of coffee are in cents.

### Assumptions:
1. Unlimited amount of coins
2. Standard euros coins
3. 100 cents = 1 euro


## Task2
The class XKCD_SERVICE fetches comics and metadata automatically, through the JSON interface https://xkcd.com/xxx/info.0.json, where xxx is a random number from 0 to 2356. The latter the maximum amount of comic strips available on the xkcd website: https://xkcd.com/

### Assumptions:
1. Only 2356 comic strips
2. Doesn't 
