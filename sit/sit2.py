"""SIT run 2: P3' (plans/sit-plan.md). The hemisphere's readings against the products of the two-party readings.
Run: python3 sit/sit2.py   (a second; needs mpmath)
"""
import mpmath as mp
mp.mp.dps = 50
M = mp.mpf
area = mp.quad(lambda th: mp.sin(th), [0, mp.pi / 2])            # the three-party hemisphere, by integration
shadow = mp.quad(lambda r: r, [0, 1])
height = mp.quad(lambda th: mp.cos(th) * mp.sin(th), [0, mp.pi / 2])
outer, inner = area / shadow, height / area
r_out, r_in = outer / (mp.pi / 2) ** 2, inner / (2 / mp.pi) ** 2
w = max(abs(r_out - 8 / mp.pi ** 2), abs(r_in - mp.pi ** 2 / 8))
ok = w < M('1e-45') and abs(8 / mp.pi ** 2 - 1) > M('0.05')
print(f"P3': {'not killed' if ok else 'KILLED'}. at once {mp.nstr(outer, 6)} = (π/2)² × {mp.nstr(r_out, 10)}; one at a time "
      f"{mp.nstr(inner, 6)} = (2/π)² × {mp.nstr(r_in, 10)}; 8/π² = {mp.nstr(8 / mp.pi ** 2, 10)} (to {mp.nstr(w, 2)})")
