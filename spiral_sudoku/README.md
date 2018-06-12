# Spiral Sudoku 

## Statement 
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9  10
    19  6  1  2  11
    18  5  4  3  12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101. What is
the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the
same way?

## Analysis
We want to find a relationship between the number of rings formed, the width of the
square and the values in the corners. Analyzing the spiral of size 1 we
see what:

    7  8  9
    6  1  2
    5  4  3

Square side has 3 elements. Number of iterations necessary to construct the loop 
n = 1. So we have:

    SIDE = 2n+1 = 3.

The value of the upper right corner (from now on `E4`) coincides with the total 
number of elements in the square. This number can also be expressed in function of 
`SIDE` and therefore the number of iterations necessary to form the loop as:

    E4 = AREA =  3² = (2n+1)².

Verifying this with the `5x5` spiral we see that it is the second iteration `n = 2` where
the size of the side is `2n + 1 = 5` and the area, and therefore value of the corner number
upper right (`E4`) is `(2n + 1) ² = 5² = 25`.

With this we can easily find out the values of all E4 elements of any loop if we have 
its side, the number of iterations needed or the total number of elements. Now we only 
have to relate the value of the other three corners with this, thus obtaining the value 
of the sum of all its elements diagonally.

Note that for `n = 0` we have a special value matrix 1.
    
    1
    SIDE = 1
    AREA = 1
    DIAGONAL = 1

Upper left corner is the value that we already have minus the number of elements on one 
side minus one:

    E4(n) = AREA - SIDE-1 => (2n+1)²-(2n+1-1) = (2n+1)²

Checking for `n = 1`

    E4 (1) = (2n + 1) ²-2n = 7

Checking for `n = 2`

    E4 (2) = (2n + 1) ²-2n = 21

For the other two corners it will be then:

    E3(n) = (2n+1)²-4n
    E3(n) = (2n+1)²-6n

The value of the sum of all the numbers of the corners will be

    CORNERS(n) = E1(n) + E2(n) + E3(n) + E4(n)
    CORNERS(n) = 4(2n+1)²-12n

The value of the sum of all diagonal numbers can be obtained as the iteration 
of the recursive sum of the corners for all iterations from the `n = N` to the 
`n = 0`.

    DIAGONAL(n) = CORNERS(n) + DIAGONAL(n-1)

Checking for `n=1`

    DIAGONAL(1) = 4(2(1)+1)²-12(1) + DIAGONAL(0)
    DIAGONAL(1) = 36        -12    + 1 = 25
    
    DIAGONAL(2) = 4(2(2)+1)²-12(2) + DIAGONAL(1)
    DIAGONAL(1) = 100       -24    + 25 = 101

## Usage
    $> python3 spiral.py
    The sum of all numbers in diagonals for the spiral of 1001x1001 is:
    669171001