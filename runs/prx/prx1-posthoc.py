# PRX run 1, post hoc (not a prediction): the least deviation against the skew of ln rho over the turn.
import numpy as np
N = 64000
ph = (np.arange(N) + 0.5) * 2 * np.pi / N
shapes = {
    'mixed 1,2': np.log(1.5) + 0.5*np.cos(ph) + 0.25*np.cos(2*ph),
    'mixed 2,4': np.log(1.5) + 0.4*np.cos(2*ph) + 0.3*np.cos(4*ph),
    'ellipse 1:2': np.log(2.0) - 0.5*np.log(4*np.cos(ph)**2 + np.sin(ph)**2),
}
for n in (3, 4, 6, 8):
    w = 2*np.pi/n
    shapes[f'{n}-gon'] = -np.log(np.cos(np.mod(ph, w) - w/2))
devs = {'mixed 1,2': 6.850e-3, 'mixed 2,4': 5.356e-3, 'ellipse 1:2': 8.042e-4,
        '3-gon': 1.001e-3, '4-gon': 1.237e-4, '6-gon': 8.795e-6, '8-gon': 1.451e-6}
for k, l in shapes.items():
    x = l - l.mean(); m2 = np.mean(x**2); m3 = np.mean(x**3)
    print(f"{k:12s} sd {np.sqrt(m2):.4f}  third central moment {m3:+.3e}  least dev {devs[k]:.3e}  dev/|m3| {devs[k]/abs(m3):.3f}")
