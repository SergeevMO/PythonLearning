import math

a	= 6377563.396   # m	    Semi-major axis # Airy 1830 ellipsoid
b	= 6356256.909   # m 	Semi-minor axis # Airy 1830 ellipsoid
E0	= 400000        # m	    Map coordinates of true origin
N0	= -100000       # m
ϕ0	= 49            # ∘N	Longitude of true origin
λ0	= -2             # ∘W	Latitude of true origin
F0	= 0.9996012717  # Scale factor on central meridian

e2 = (a**2 - b**2) / a**2
n = (a - b) / (a + b)
f0 = math.radians(ϕ0)
l0 = math.radians(λ0)

def deg_to_dms2(deg, pretty_print=None, ndp=4):
    """Convert from decimal degrees to degrees, minutes, seconds."""

    m, s = divmod(abs(deg)*3600, 60)
    d, m = divmod(m, 60)
    if deg < 0:
        d = -d
    d, m = int(d), int(m)

    if pretty_print:
        if pretty_print=='latitude':
            hemi = 'N' if d>=0 else 'S'
        elif pretty_print=='longitude':
            hemi = 'E' if d>=0 else 'W'
        else:
            hemi = '?'
        return '{d:d}° {m:d}′ {s:.{ndp:d}f}″ {hemi:1s}'.format(
                    d=abs(d), m=m, s=s, hemi=hemi, ndp=ndp)
    return d, m, s

def fM(fi):
    return b * F0 * ((1 + n + 5 * (n**2 + n**3) / 4)*(fi - f0) -
                     (3*n + 3 * n**2 + 21* n**3 / 8) * math.sin(fi - f0) * math.cos(fi + f0) +
                     (15 * (n**2 + n**3) / 8)*math.sin(2*(fi - f0)) * math.cos(2*(fi + f0)) -
                     35 * n**3 * math.sin(3*(fi - f0)) * math.cos(3*(fi + f0)) / 24
                     )
def nurhoetta(fi):
    ν = a * F0 / math.sqrt(1 - e2 * math.sin(fi) ** 2)
    ρ = a * F0 * (1 - e2) / (1 - e2 * math.sin(fi) ** 2) ** 1.5
    η2 = ν / ρ - 1
    return ν, ρ, η2


def os_to_ll(E, N):
    M, fi = 0, 0

    while abs(N - N0 - M) >= 1e-5:
        fi += (N - N0 - M) / (a * F0)
        M = fM(fi)

    ν, ρ, η2 = nurhoetta(fi)

    tan_phip = math.tan(fi)
    tan_phip2 = tan_phip ** 2

    c1 = tan_phip / (2*ρ*ν)
    c2 = tan_phip * (5 + 3 * tan_phip**2 + η2 * (1 - 9*tan_phip2)) / (24*ρ*ν**3)
    c3 = tan_phip * (61 + 90 * tan_phip**2 + 45*tan_phip2**2) / (720*ρ*ν**5)
    d1 = 1 / (ν * math.cos(fi))
    d2 = (ν / ρ + 2*tan_phip2) / (6*ν**3 * math.cos(fi))
    d3 = (5 + 28 * tan_phip2 + 24 * tan_phip2**2) / (120*ν**5 * math.cos(fi))
    d4 = (61 + 662 * tan_phip2 + 1320 * tan_phip2**2 + 720 * tan_phip2**3) / (5040*ν**7 * math.cos(fi))

    dE = E - E0

    fi = fi - c1*dE**2 + c2*dE**4 - c3*dE**6
    l = l0 + d1*dE - d2*dE**3 + d3*dE**5 - d4*dE**7
    return math.degrees(fi), math.degrees(l)

def ll_to_os(fi, lam):
    v, rho, et2 = nurhoetta(fi)
    M = fM(fi)

    sinfi = math.sin(fi)
    cosfi = math.cos(fi)
    tanfi2 = math.tan(fi)**2

    a1 = M + N0
    a2 = v * sinfi * cosfi / 2
    a3 = v * sinfi * cosfi**3 * (5 - tanfi2 + 9*et2) /24
    a4 = v * sinfi * cosfi**5 * (61 - 58 * tanfi2 + tanfi2**2) /720
    b1 = v * cosfi
    b2 = v * cosfi**3 * (et2 + 1 - tanfi2) / 6
    b3 = v * cosfi**5 * (5 - 18 * tanfi2 + tanfi2**2 + et2* (14 - 58 * tanfi2)) / 120

    dl = lam - l0
    N = a1 + a2*dl**2 + a3*dl**4 + a4*dl**6
    E = E0 + b1*dl + b2*dl**3 + b3*dl**5
    print(b1, b2, b3, dl)

    return E, N

E, N = 544735, 258334    # King's College, Cambridge
print('(E, N) =', (E, N))
phi, lam = os_to_ll(E, N)
print('(φ, λ) = ({:.8f}°, {:.8f}°)'.format(phi, lam))
print('       =', deg_to_dms2(phi, 'latitude'), deg_to_dms2(lam, 'longitude'))

pr, lr = math.radians(phi), math.radians(lam)
E, N = ll_to_os(pr, lr)
print('(E, N) =', (E, N))