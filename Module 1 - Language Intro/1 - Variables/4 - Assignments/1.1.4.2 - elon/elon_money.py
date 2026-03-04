"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
Elons_money = 33e9 #Elon's share of the money 33B
ten_year_rate = 3.96 #percent
twenty_year_rate = 4.32 #percent
ten_years = 10 #10 year increment
twenty_years = 20 #20 year increment

import math

# final answer for 10-year

ten_year_final = (math.pow(((ten_year_rate/100)+1),ten_years)*Elons_money)

print(ten_year_final)

# final answer for 20-year
twenty_year_final = (Elons_money*math.pow(((twenty_year_rate/100)+1),twenty_years))

print(twenty_year_final)