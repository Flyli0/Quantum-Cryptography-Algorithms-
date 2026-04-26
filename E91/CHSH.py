from E91.Correlation import correlation

def chsh(measurements):
    def E(pairs):
        if len(pairs) == 0:
            return 0
        return sum(a*b for a,b in pairs) / len(pairs)

    E_ab  = E(measurements[('a','b')])
    E_ab2 = E(measurements[('a','b2')])
    E_a2b = E(measurements[('a2','b')])
    E_a2b2= E(measurements[('a2','b2')])

    return E_ab + E_ab2 + E_a2b - E_a2b2
