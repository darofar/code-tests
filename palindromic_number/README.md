# Palindromic Numbers

## Statement 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 
3-digit numbers.

## Analysis
Multiplying two N-digit numbers yields a number with a length of 2N or 2N-1. Assuming that after 
multiplying these numbers we can always obtain at least a palindrome of the greater length (2N) 
the search can be reduced to find the greater palindrome of length 2N.

## Usage
```bash
$> python3 palindromes.py
Largest palindromic number is: 906609
As a result of multiply the digits: 913x993
```