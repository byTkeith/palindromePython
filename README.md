# Palindromic Prime Finder

## Author: Tendai Nyevedzanai 

This Python program finds palindromic prime numbers between two specified integers. It checks whether each number within the given range is both a prime number and a palindrome.

### Usage

1. Ensure that you have Python installed on your system.

2. Run the program:
   ```bash
   python palindromic_primes.py
   ```

3. Follow the prompts to enter the starting point (N) and ending point (M) for the search range.

### Algorithm

1. The program checks whether a number is prime using the Lucas-Lehmer primality test.
2. It then verifies if the number is a palindrome (reads the same forwards and backwards).

### Example

```
Enter the starting point N:
10
Enter the ending point M:
100
The palindromic primes are:
11
101
131
151
181
191
313
353
373
383
727
757
787
797
919
929
```

### Note

- The program uses recursion to check for palindromes.
- Adjust the range as needed for your specific use case.
