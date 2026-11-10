# SRB run 1, post hoc: closed form for B5 (derived after seeing the numbers; not a prediction).
# KL(uniform S^2 || spherical Cauchy rho) = -2 ln(1-rho^2) + [(1+rho)^2 ln(1+rho) - (1-rho)^2 ln(1-rho)]/rho - 2
import mpmath as mp
mp.mp.dps = 50
for e in [mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)]:
    rho = mp.tanh(e/2)
    num = -mp.quad(lambda th: mp.sin(th)*2*mp.log((1-rho**2)/(1+rho**2-2*rho*mp.cos(th))), [0, mp.pi])/2
    cf = -2*mp.log(1-rho**2) + ((1+rho)**2*mp.log(1+rho) - (1-rho)**2*mp.log(1-rho))/rho - 2
    print('eta', mp.nstr(e, 3), 'quad', mp.nstr(num, 25), 'closed', mp.nstr(cf, 25), 'rel', mp.nstr(abs(cf/num-1), 3))
e = mp.mpf('1e-6'); rho = mp.tanh(e/2)
cf = -2*mp.log(1-rho**2) + ((1+rho)**2*mp.log(1+rho) - (1-rho)**2*mp.log(1-rho))/rho - 2
print('KL/eta^2 at eta = 1e-6:', mp.nstr(cf/e**2, 15), '(2/3 means Fisher information 4/3 in eta; the circle has 1/2)')
