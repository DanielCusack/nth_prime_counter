# nth_prime_counter
Find the nth prime number via a sieve of Eratosthenes.
This program was written with Python 3.6.5 and uses the numpy (1.14.3.) module.

numpy can usually be installed using pip using `pip install numpy`. Problems can occur on Windows with installing numpy using pip. In this case, consider using the conda package manager instead.

To use the program, run `python pcounter.py`. You will be prompted to give a number between 1 and 10,000,000.

test_pcounter.py is a test script to test the functionality of the pcounter.py program.


For  the 10000000th prime number, the program took just under 1.5GB of memory and a few minutes to run on my Ryzen 5 2600 Gen2 6 Core AM4 processor. The time efficiency and level of memory usage may not be suitable.

Another, more efficent, method I have seen described involves:
* Estimating the value of nth prime.

* Calculate the number of primes less than this estimate.

* Zero in on the nth prime by testing for primality.

I did not have time to try this method though.
