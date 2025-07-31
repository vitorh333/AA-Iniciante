#FUI MOGGADO

import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache

def is_bad(seq):
    if len(seq) < 5:
        return False
    last5 = seq[-5:]
    return all(last5[i] < last5[i+1] for i in range(4)) or all(last5[i] > last5[i+1] for i in range(4))

def solve(p):
    n = len(p)

    @lru_cache(None)
    def dp(l, r, last4):
        if l > r:
            return True, ""

        last4l = last4 + (p[l],)
        if not is_bad(last4l[-5:]):
            resl, seql = dp(l+1, r, last4l[-4:])
            if resl:
                return True, "L" + seql

        last4r = last4 + (p[r],)
        if not is_bad(last4r[-5:]):
            res_r, seq_r = dp(l, r-1, last4r[-4:])
            if res_r:
                return True, "R" + seq_r

        return False, ""

    ok, ans = dp(0, n-1, ())
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = tuple(map(int, input().split()))
    ans = solve(p)
    print(ans)

#COMECA A REZAR TODO MUNDO AI

