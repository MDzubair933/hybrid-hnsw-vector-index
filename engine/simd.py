# SIMD vector distance routines
def fast_dot(u, v):
    return sum(a*b for a,b in zip(u,v))
