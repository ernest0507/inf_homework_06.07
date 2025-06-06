alph = sorted('ЛАЙМ')
line = 0
for a1 in alph:
    for a2 in alph:
        for a3 in alph:
            for a4 in alph:
                for a5 in alph:
                    a = a1 + a2 + a3 + a4 + a5
                    line += 1
                    rule1 = a.count('М') == 0 and a.count('Л') == 0
                    rule2 = 'ЙЙ' not in a
                    if rule1 and rule2:
                        print(line)


