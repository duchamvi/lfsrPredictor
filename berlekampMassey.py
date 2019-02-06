def BerlekampMasseyAlgorithm(stream):
    n = len(stream)

    # polynoms
    s = [stream[i] for i in range(n)]
    b = [1]+[0 for _ in range(n-1)]
    c = [1]+[0 for _ in range(n-1)]

    L = 0 # length of minimal lfsr
    m = -1 # nombre d'iter depuis la dernière update

    for N in range(n):
        # calculate discrepancy
        d = s[N]
        for i in range(1, L+1):
            d ^= c[i] & s[N-i]
        # discrepancy is zero; annihilation continues
        if d==1:
            t = [c[i] for i in range(len(c))]
            for i in range (n-N+m):
                c[i+N-m] ^= b[i]
            if (L <= N//2):
                L = N+1-L
                m = N
                b = t
    return L, c[:(L+1)]