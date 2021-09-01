txt = r'([[[ (([])) ]]])()()()(){}{}{}{}[][][][][()((((){}{}[][][{}][])))]'

# txt = '[_]()'

def balanced(txt) -> bool:
    l = len(txt)

    bo = '([{'
    bc = ')]}'

    def till_i_die(start = 0, symb = -1):
        bb = [0, 0, 0]

        if symb != -1:
            bb[symb] += 1

        i = start
        while (i < l) and ((symb != -1 and bb[symb]) or (symb == -1)):
            if txt[i] in bo:
                i = till_i_die(i + 1, bo.index(txt[i]))
                if not i:
                    return 0
            elif txt[i] in bc:
                bb[bc.index(txt[i])] -= 1
                if -1 in bb:
                    return 0
            i += 1
        
        if (bb[0] or bb[1] or bb[2]):
            return 0

        return i - 1
    
    return bool(till_i_die())

print(balanced(txt))
