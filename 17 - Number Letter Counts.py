units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
         'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']
thousands = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
             'quintillion', 'sextillion', 'septillion', 'octillion',
             'nonillion', 'decillion', 'undecillion', 'duodecillion',
             'tredecillion', 'quattuordecillion', 'sexdecillion',
             'septendecillion', 'octodecillion', 'novemdecillion',
             'vigintillion']


def num_to_words(num):
    num = int(num)

    words = ""

    if num < 10:
        words += units[num]
    elif num == 10:
        words += "ten"
    elif num < 20:
        words += teens[num - 10]
    elif num < 100:
        words += tens[int(str(num)[0])]
        words += num_to_words(int(str(num)[1:]))
    elif num < 1000:
        words += units[int(str(num)[0])] + "hundred"
        extra = num_to_words(int(str(num)[1:]))

        if extra != "":
            words += "and" + extra
    elif num == 1000:
        words += "onethousand"
    else:
        print("I can't be bothered to go higher")

    return words

sum = 0
for i in range(1, 1001):
    print(num_to_words(i))
    sum += len(num_to_words(i))

print(sum)