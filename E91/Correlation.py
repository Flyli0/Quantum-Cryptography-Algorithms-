def correlation(measurements):  # calculating correlation between basis' value or a certain combination
    total = 0
    for a,b in measurements:  # formula for correlation = 1/N * (sum(Ai * Bi)) for all i
        A = 1 if a == 0 else -1
        B = 1 if b == 0 else -1
        total += A*B
    return total/len(measurements)