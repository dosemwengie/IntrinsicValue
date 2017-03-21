# IntrinsicValue

This is a simple processing script that calculates the most "intrinsic valued" stocks at runtime. What is meant by intrinsic is subjective to the user. Hence, one can use the google stock screener apply their criteria and paste that url into the get_intrinsic.sh script.

The formulas for the 3 intrinsic values can be found in the parser.py script
Intrinsic Value Buffett:10 = 1x, 15 = 2x, 20 = 4x

Intrinsic Value Alternative: Price-to-Book*Value<22, the lower the better, since that means it is either undervalued or we are paying less per dollar of earning(more bang for the buck!)

Intrinsic Value Graham: Future value of the stock.

DISCLAIMER: As with any investments, there are always risks involved, these formulas/numbers are not guaranteed to be in any way shape or form accurate. It is just to provide a guidance/direction of where a stock can "potentially" reach objectively based on numbers. Use discretion.

In my implementation, I added the script to launch at close of stock exchange 4:30 pm EST and observed any persistence tickers.

![Main](https://github.com/dosemwengie/IntrinsicValue/blob/master/img/main.png)
