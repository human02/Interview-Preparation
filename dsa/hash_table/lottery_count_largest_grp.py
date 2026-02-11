"""

You are given two integers, lowVal and highVal. A lottery is being held where every integer in the inclusive range [lowVal, highVal] represents a ticket.
Each ticket is assigned a Coupon Code based on the sum of its digits.

For example:
    Ticket 10 has a Coupon Code of 1+0=1.
    Ticket 123 has a Coupon Code of 1+2+3=6.

Participants holding tickets that result in the same Coupon Code share a prize pool.
Your task is to determine two things:The maximum number of winners assigned to any single Coupon Code.
The total number of unique Coupon Codes that achieve this maximum number of winners.
Return these two values as an array or a pair: [max_winners, count_of_codes].

Constraints:
    1 <= lowVal <= highVal <= 10^18

"""

