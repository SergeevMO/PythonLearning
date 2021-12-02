G = 6.67430e-11  # гравитационная постоянная
G_unc = 1.5e-15  # погрешность
G_units = 'Nm^2/kg^2'

c = 2.99792458e8  # скорость света
c_unc = 0  # погрешность
c_units = 'm/s'

h = 6.62607015e-34  # постоянная Планка
h_unc = 0  # погрешность
h_units = 'Js'

kB = 1.380649e-23  # постоянная Больцмана
kB_unc = 0  # погрешность
kB_units = 'J/K'

NA = 6.02214076e23  # число Авогадро
NA_unc = 0  # погрешность
NA_units = 'mol-1'

ue = -9.28476377e-24  # магнитный момент электрона
ue_unc = 2.3e-31  # погрешность
ue_units = 'J/T'

# а)
print('kB = {:.3e} {:s}'.format(kB, kB_units))

# б)
print('G = {:.16f} {:s}'.format(G, G_units))

# в)
str_format = '{:s} = {:11.4e} {:s}\n' * 4
print(str_format.format('kB', kB, kB_units, '\u03BC', ue, ue_units, 'N_A', NA, NA_units, 'c', c, c_units))

# г)
str_format = '=== {:s} = {:+9.2E} [{:>4s}] ===\n' * 2
print(str_format.format('G', G, G_units, '\u03BC', ue, ue_units))

# д)
import math

exponent = int(math.floor(math.log10(abs(G))))
mantissa = G * 10 ** (-exponent)
# print(exponent, mantissa)

exponent_u = int(math.floor(math.log10(abs(G_unc))))
mantissa_10u = int(10 * G_unc * 10 ** (-exponent_u))
# print(exponent_u, mantissa_10u)

length_d = abs(exponent_u) - abs(exponent) + 3

str_format = '{symb:s} = {mant:<0{length}}({mant_u})e{exp:+} {unit:>4s}\n'
print(str_format.format(symb='G', mant=mantissa, mant_u=mantissa_10u, exp=exponent, unit=G_units, length=length_d))



exponent = int(math.floor(math.log10(abs(ue))))
mantissa = ue * 10 ** (-exponent)

exponent_u = int(math.floor(math.log10(abs(ue_unc))))
mantissa_10u = int(10 * round(ue_unc * 10 ** (-exponent_u), 3))

length_d = abs(exponent_u) - abs(exponent) + 3

str_format = '{symb:s} = {mant:<0{length}}({mant_u})e{exp:+} {unit:>4s}\n'
print(str_format.format(symb='\u03BC', mant=mantissa, mant_u=mantissa_10u, exp=exponent, unit=ue_units, length=length_d))


# вариант ответа из книги
# The number of digits in the uncertainty to output
nsd_digits = 2
# Separate our constant into mantissa * 10^exponent
exponent = int(math.floor(math.log10(abs(G))))
mantissa = G * 10**(-exponent)
# The uncertainty digits relative to the same exponent
sd = G_unc * 10**(-exponent)
# The number of decimal places to output
dp = int(-math.log(sd,10))+nsd_digits
# The uncertainty digits as an integer
sd_digits = int(round(sd*10**dp))
print('G = {mantissa:.{dp:d}f}({sd_digits:d})e{exponent:d} {units:s}'
            .format(mantissa=mantissa, dp=dp, sd_digits=sd_digits,
                    exponent=exponent, units=G_units))