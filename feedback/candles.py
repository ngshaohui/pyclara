"""
Count Candles

Each time a wax candle is burnt, it leaves some residual wax.
This residual wax can be collected to make a new candle.

Let the number of initial candles be n.

Let the number of residuals needed to make a new candle be k.
Every k candles burnt will allow us to burn an additional candle.

Write a program that calculates the total number of candles that can be burnt, given n and k.

Example

When n = 9 and k = 5, this will allow us to burn a total of 11 candles.
Let us start by burning 5 candles, so 4 candles remain unburnt.
(Candles burnt: 5)
After 5 of the initial 9 candles have been burnt, we will be able to make an additional candle.
This leaves us with 5 unburnt candles.
After burning the 5 candles, we can make an additional candle
(Candles burnt: 10)
This leaves us with 1 unburnt candle.
After burning the 1 candle, we do not have enough residual to make an additional candle.
(Candles burnt: 11)
"""


def count_candles(n: int, k: int) -> int: 
    if(n<k):                                #if initial candles is less than k, return intial candles
        return n 

    elif(n==0):                             #if initial candles is 0, return n (which is equivalent to 0 too)
        return n

    else:
        # SH: (Design - Naming) What does counter represent?
        # SH: Can opt for a more descriptive variable name that describes its purpose
        # SH: In this case, counter seems to indicate the number of new candles formed from the residuals
        # SH: candles_from_residuals
        counter = 1
        new_total = n - k + counter              #once we enter this loop, new_total = initial candles deducted by k and counter = 1
        while(new_total>=k):                #while new_total is less than k, we will increment counter
            counter += 1
            
            new_total = new_total - k + 1  #this is to add in additional candle after burning k
        # SH: Can simplify the return statement rather than storing it in a variable first
        # SH: return n + counter
        n = n + counter                     #to calculate the total number of candles burnt, add counter into initial candles 
        return n

def main():
    print("results", count_candles(100, 7))


if __name__ == "__main__":
    main()
