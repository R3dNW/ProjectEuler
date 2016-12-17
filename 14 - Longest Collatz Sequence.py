import utilities

longest_chain_start = 0
longest_chain_length = 0

for i in range(1, 1000000):
    length = utilities.collatz_length(i)

    if length > longest_chain_length:
        longest_chain_start = i
        longest_chain_length = length

print("Start = " + str(longest_chain_start) + ", Length = " + str(longest_chain_length))