# Must go right 20
# Must go down 20

# How many ways can 20 'rights' be positioned in 40 'slots'?
# The 'downs' must then fill the gaps left in the instruction set

# The total number of ways to arrange 40 items is 40!
# Since 20 of these are 'rights', and 20 are 'downs', we can divide this number by (20!*20!)
# To get the total number of solutions 40! / (20! * 20!) or 40! / 20!^2

# Or in Python:

import math

print(math.factorial(40) / (math.factorial(20) ** 2))