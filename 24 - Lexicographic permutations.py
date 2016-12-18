import sys
import copy

permutations = []

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for a in digits:
    digits_without_a = copy.copy(digits)
    digits_without_a.remove(a)


    for b in digits_without_a:
        digits_without_ab = copy.copy(digits_without_a)
        digits_without_ab.remove(b)

        for c in digits_without_ab:
            digits_without_abc = copy.copy(digits_without_ab)
            digits_without_abc.remove(c)

            for d in digits_without_abc:
                digits_without_abcd = copy.copy(digits_without_abc)
                digits_without_abcd.remove(d)

                for e in digits_without_abcd:
                    digits_without_abcde = copy.copy(digits_without_abcd)
                    digits_without_abcde.remove(e)

                    for f in digits_without_abcde:
                        digits_without_abcdef = copy.copy(digits_without_abcde)
                        digits_without_abcdef.remove(f)

                        for g in digits_without_abcdef:
                            digits_without_abcdefg = copy.copy(digits_without_abcdef)
                            digits_without_abcdefg.remove(g)

                            for h in digits_without_abcdefg:
                                digits_without_abcdefgh = copy.copy(digits_without_abcdefg)
                                digits_without_abcdefgh.remove(h)

                                for i in digits_without_abcdefgh:
                                    digits_without_abcdefghi = copy.copy(digits_without_abcdefgh)
                                    digits_without_abcdefghi.remove(i)

                                    for j in digits_without_abcdefghi:
                                        permutations.append(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j))

        if len(permutations) >= 1000000:
            print(permutations[999999])
            sys.exit()