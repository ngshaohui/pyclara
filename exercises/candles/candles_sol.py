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


def count_candles(num_candles: int, residuals: int) -> int:
    "count the total number of candles burnt"
    burnt = 0
    if residuals == 0:
        return num_candles
    while num_candles >= residuals:
        burnt += residuals
        num_candles -= residuals
        # add new candle after burning enough for a residual
        num_candles += 1
    # add in remaining candles that don't have enough residual to form a candle
    burnt += num_candles
    return burnt


def main():
    print(count_candles(9, 5))


if __name__ == "__main__":
    main()
