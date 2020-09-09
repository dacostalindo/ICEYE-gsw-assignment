# ICEYE Ground Software Assignment

Before you start install all the dependencies:

```
pip3 install .

```

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

In this repository, the task 2 folder is split between the XKCD_SERVICE class and its corresponding test cases and service.

The class XKCD_SERVICE fetches comics and metadata automatically, through the JSON interface https://xkcd.com/xxx/info.0.json, where xxx is a random number from 0 to 2356. The latter the maximum amount of comic strips available on the xkcd website: https://xkcd.com/

```
class  XKCD_SERVICE(object) :

    def __init__(self, max_comics):
```

The services stores a new comic every hour (3600 seconds), and randomly removes a comic from the local filesytem.  If last url retrieve is equal to the previous, it keeps randomly seeking a new image until it finds it.

```
class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
```

### Assumptions:
1. Only 2356 comic strips
2. Service randomly removes one of the two pictures, to keep them at a maximum in the local filesytem.


## Act 3
This is a django project that can be started, within the act3 folder, using

```
pipenv shell

docker-compose up -d --build
```

Then, the web application can be accessed through the following link:

- http://0.0.0.0:8000/saveworld/list/

The website's layout should be easy to understand. 
