# Candidates: math blocks carrying pi or e, from ten Wikipedia articles (DVI)

1. [Spherical coordinate system / Cartesian coordinates] 
   `\begin{align} r &= \sqrt{x^2 + y^2 + z^2} \\ \theta &= \arccos\frac{z}{\sqrt{x^2 + y^2 + z^2}} = \arccos\frac{z}{r}= \begin{cases} \arctan\frac{\sqrt{x^2+y^2}}{z} &\text{if } z > 0 \\ \pi +\arctan\frac{\sqrt{x^2+y^2}}{z} &\text{if } z < 0 \\ +\frac{\pi}{2} &\text{if } z = 0 \text{ and } \sqrt{x^2+y^2} \neq 0 \\ \text{undefined} &\text{if } x=y=z = 0 \\ \end{cases} \\ \varphi &= \sgn(y)\arccos\frac{x}{\sqrt{x^2+y^2}} = \begin{cases} \arctan(\frac{y}{x}) &\text{if } x > 0, \\ \arctan(\frac{y}{x}) + \pi &\text{if } x < 0 \text{ and } y \geq 0, \\ \arctan(\frac{y}{x}) - \pi &\text{if } x < 0 \text{ and } y < 0, \\ +\frac{\pi}{2} &\text{if } x = 0 \text{ and } y > 0, \\ -\frac{\pi}{2} &\text{if } x = 0 \text{ and } y < 0, \\ \text{undefined} &\text{if } x = 0 \text{ and } y = 0. \end{cases} \end{align}`
2. [Spherical coordinate system / Cartesian coordinates] These formulae assume that the two systems have the same origin, that the spherical reference plane is the Cartesian plane, that is inclination from the directi
   `cos ''θ''`
3. [Spherical coordinate system / Cartesian coordinates] These formulae assume that the two systems have the same origin, that the spherical reference plane is the Cartesian plane, that is inclination from the directi
   `sin ''θ''`
4. [Spherical coordinate system / Cartesian coordinates] 
   `\begin{align} x &= r \sin\theta \, \cos\varphi, \\ y &= r \sin\theta \, \sin\varphi, \\ z &= r \cos\theta. \end{align}`
5. [Spherical coordinate system / Cylindrical coordinates] 
   `\begin{align} r &= \sqrt{\rho^2 + z^2}, \\ \theta &= \arctan\frac{\rho}{z} = \arccos\frac{z}{\sqrt{\rho^2 + z^2}}, \\ \varphi &= \varphi. \end{align}`
6. [Spherical coordinate system / Cylindrical coordinates] 
   `\begin{align} \rho &= r \sin \theta, \\ \varphi &= \varphi, \\ z &= r \cos \theta. \end{align}`
7. [Spherical coordinate system / Ellipsoidal coordinates] 
   `\begin{align} x &= \frac{1}{\sqrt{a}} r \sin\theta \, \cos\varphi, \\ y &= \frac{1}{\sqrt{b}} r \sin\theta \, \sin\varphi, \\ z &= \frac{1}{\sqrt{c}} r \cos\theta, \\ r^{2} &= ax^2 + by^2 + cz^2. \end{align}`
8. [Spherical coordinate system / Ellipsoidal coordinates] 
   `\mathrm{d}V = \left|\frac{\partial(x, y, z)}{\partial(r, \theta, \varphi)}\right| \, dr\,d\theta\,d\varphi = \frac{1}{\sqrt{abc}} r^2 \sin \theta \,\mathrm{d}r \,\mathrm{d}\theta \,\mathrm{d}\varphi = \frac{1}{\sqrt{abc}} r^2 \,\mathrm{d}r \,\mathrm{d}\Omega.`
9. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathrm{d}\mathbf{r} = \mathrm{d}r\,\hat{\mathbf r} + r\,\mathrm{d}\theta \,\hat{\boldsymbol\theta } + r \sin{\theta} \, \mathrm{d}\varphi\,\mathbf{\hat{\boldsymbol\varphi}},`
10. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\begin{align} \hat{\mathbf r} &= \sin \theta \cos \varphi \,\hat{\mathbf x} + \sin \theta \sin \varphi \,\hat{\mathbf y} + \cos \theta \,\hat{\mathbf z}, \\ \hat{\boldsymbol\theta} &= \cos \theta \cos \varphi \,\hat{\mathbf x} + \cos \theta \sin \varphi \,\hat{\mathbf y} - \sin \theta \,\hat{\mathbf z}, \\ \hat{\boldsymbol\varphi} &= - \sin \varphi \,\hat{\mathbf x} + \cos \varphi \,\hat{\mathbf y} \end{align}`
11. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `R = \begin{pmatrix} \sin\theta\cos\varphi&\sin\theta\sin\varphi&\hphantom{-}\cos\theta\\ \cos\theta\cos\varphi&\cos\theta\sin\varphi&-\sin\theta\\ -\sin\varphi&\cos\varphi &\hphantom{-}0 \end{pmatrix}.`
12. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\begin{bmatrix}\mathbf{\hat x} \\ \mathbf{\hat y} \\ \mathbf{\hat z} \end{bmatrix} = \begin{bmatrix} \sin\theta\cos\varphi & \cos\theta\cos\varphi & -\sin\varphi \\ \sin\theta\sin\varphi & \cos\theta\sin\varphi & \hphantom{-}\cos\varphi \\ \cos\theta & -\sin\theta & \hphantom{-}0 \end{bmatrix} \begin{bmatrix} \boldsymbol{\hat{r}} \\ \boldsymbol{\hat\theta} \\ \boldsymbol{\hat\varphi} \end{bmatrix}`
13. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathbf{r} = \begin{bmatrix} r \sin\theta \, \cos\varphi \\ r \sin\theta \, \sin\varphi \\ r \cos\theta \end{bmatrix}, x_1=r, x_2=\theta, x_3=\varphi.`
14. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\frac{\partial\mathbf r}{\partial r} = \begin{bmatrix} \sin\theta \, \cos\varphi \\ \sin\theta \, \sin\varphi \\ \cos\theta \end{bmatrix}=\mathbf{\hat r}, \quad \frac{\partial\mathbf r}{\partial \theta} = \begin{bmatrix} r \cos\theta \, \cos\varphi \\ r \cos\theta \, \sin\varphi \\ -r \sin\theta \end{bmatrix}=r\,\hat{\boldsymbol\theta }, \quad \frac{\partial\mathbf r}{\partial \varphi} = \begin{bmatrix} -r \sin\theta \, \sin\varphi \\ \hphantom{-}r \sin\theta \, \cos\varphi \\ 0 \end{bmatrix} = r \sin\theta\,\mathbf{\hat{\boldsymbol\varphi}} .`
15. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\left|\frac{\partial\mathbf r}{\partial r}\right| = 1, \quad \left|\frac{\partial\mathbf r}{\partial \theta}\right| = r, \quad \left|\frac{\partial\mathbf r}{\partial \varphi}\right| = r \sin\theta.`
16. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathrm{d}S_r = \left\|\frac{\partial {\mathbf r}}{\partial \theta} \times \frac{\partial {\mathbf r}}{\partial \varphi}\right\| \mathrm{d}\theta \,\mathrm{d}\varphi = \left|r {\hat \boldsymbol\theta} \times r \sin \theta {\boldsymbol\hat \varphi} \right|\mathrm{d}\theta \,\mathrm{d}\varphi= r^2 \sin\theta \,\mathrm{d}\theta \,\mathrm{d}\varphi ~.`
17. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathrm{d}\Omega = \frac{\mathrm{d}S_r}{r^2} = \sin\theta \,\mathrm{d}\theta \,\mathrm{d}\varphi.`
18. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathrm{d}S_\theta = r \sin\theta \,\mathrm{d}\varphi \,\mathrm{d}r.`
19. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `J =\frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)} =\begin{pmatrix} \sin\theta\cos\varphi & r\cos\theta\cos\varphi & -r\sin\theta\sin\varphi\\ \sin\theta\sin\varphi & r\cos\theta\sin\varphi & \hphantom{-}r\sin\theta\cos\varphi\\ \cos\theta & -r\sin\theta & \hphantom{-}0 \end{pmatrix},`
20. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\mathrm{d}V = \left|\frac{\partial(x, y, z)}{\partial(r, \theta, \varphi)}\right| \,\mathrm{d}r \,\mathrm{d}\theta \,\mathrm{d}\varphi= r^2 \sin\theta \,\mathrm{d}r \,\mathrm{d}\theta \,\mathrm{d}\varphi = r^2 \,\mathrm{d}r \,\mathrm{d}\Omega ~.`
21. [Spherical coordinate system / Integration and differentiation in spherical coordinates] 
   `\int\limits_0^{2\pi} \int\limits_0^\pi \int\limits_0^\infty f(r, \theta, \varphi) r^2 \sin\theta \,\mathrm{d}r \,\mathrm{d}\theta \,\mathrm{d}\varphi ~.`
22. [Spherical coordinate system / Integration and differentiation in spherical coordinates] And it leads to the following expressions for the divergence and curl of vector fields,
   `\begin{align} \nabla f &= {\partial f \over \partial r}\hat{\mathbf r} + {1 \over r}{\partial f \over \partial \theta}\hat{\boldsymbol\theta} + {1 \over r\sin\theta}{\partial f \over \partial \varphi}\hat{\boldsymbol\varphi}, \\[8pt] \nabla^2 f &= {1 \over r^2}{\partial \over \partial r} \left(r^2 {\partial f \over \partial r}\right) + {1 \over r^2 \sin\theta}{\partial \over \partial \theta} \left(\sin\theta {\partial f \over \partial \theta}\right) + {1 \over r^2 \sin^2\theta}{\partial^2 f \over \partial \varphi^2} \\[8pt] & = \left(\frac{\partial^2}{\partial r^2} + \frac{2}{r} \frac{\partial}{\partial r}\right) f + {1 \over r^2 \sin\theta}{\partial \over \partial \theta} \left(\sin\theta \frac{\partial}{\partial \theta}\right) f + \frac{1}{r^2 \sin^2\theta}\frac{\partial^2}{\partial \varphi^2}f ~, \\[8pt] \end{align}`
23. [Spherical coordinate system / Integration and differentiation in spherical coordinates] \begin{align}
   `\nabla \cdot \mathbf{A} = \frac{1}{r^2}{\partial \over \partial r}\left( r^2 A_r \right) + \frac{1}{r \sin\theta}{\partial \over \partial\theta} \left( \sin\theta A_\theta \right) + \frac{1}{r \sin \theta} {\partial A_\varphi \over \partial \varphi},`
24. [Spherical coordinate system / Integration and differentiation in spherical coordinates] + \frac{1}{r \sin \theta} {\partial A_\varphi \over \partial \varphi},
   `\begin{align} \nabla \times \mathbf{A} = {} & \frac{1}{r\sin\theta} \left[{\partial \over \partial \theta} \left( A_\varphi\sin\theta \right) - {\partial A_\theta \over \partial \varphi}\right] \hat{\mathbf r} \\[4pt] & {} + \frac 1 r \left[{1 \over \sin\theta}{\partial A_r \over \partial \varphi} - {\partial \over \partial r} \left( r A_\varphi \right) \right] \hat{\boldsymbol\theta} \\[4pt] & {} + \frac 1 r \left[{\partial \over \partial r} \left( r A_\theta \right) - {\partial A_r \over \partial \theta}\right] \hat{\boldsymbol\varphi}, \end{align}`
25. [Spherical coordinate system / Distance and angle in spherical coordinates] 
   `\begin{align} D &= \sqrt{r^2+r'^2-2rr'(\sin{\theta}\sin{\theta'}\cos{(\varphi-\varphi')} + \cos{\theta}\cos{\theta'})} \end{align}`
26. [Spherical coordinate system / Distance and angle in spherical coordinates] 
   `\cos \gamma = \cos \theta \cos \theta' + \sin \theta \sin \theta' (\cos \phi \cos \phi' + \sin \phi \sin \phi')`
27. [Spherical coordinate system / Distance and angle in spherical coordinates] 
   `\cos \gamma = \cos \theta \cos \theta' + \sin \theta \sin \theta' \cos(\phi - \phi')`
28. [Spherical coordinate system / Kinematics] 
   `\mathbf{v} = \frac{\mathrm{d}\mathbf{r}}{\mathrm{d}t} = \dot{r} \mathbf{\hat r} + r\,\dot\theta\,\hat{\boldsymbol\theta } + r\,\dot\varphi \sin\theta\,\mathbf{\hat{\boldsymbol\varphi}}`
29. [Spherical coordinate system / Kinematics] 
   `\begin{align} \mathbf{a} = {} & \frac{\mathrm{d}\mathbf{v}}{\mathrm{d}t} \\[1ex] = {} & \hphantom{+}\; \left( \ddot{r} - r\,\dot\theta^2 - r\,\dot\varphi^2\sin^2\theta \right)\mathbf{\hat r} \\ & {} + \left( r\,\ddot\theta + 2\dot{r}\,\dot\theta - r\,\dot\varphi^2\sin\theta\cos\theta \right) \hat{\boldsymbol\theta } \\ & {} + \left( r\ddot\varphi\,\sin\theta + 2\dot{r}\,\dot\varphi\,\sin\theta + 2 r\,\dot\theta\,\dot\varphi\,\cos\theta \right) \hat{\boldsymbol\varphi} \end{align}`
30. [Spherical coordinate system / Kinematics] 
   `\mathbf{L} = \mathbf{r} \times \mathbf{p} = \mathbf{r} \times m\mathbf{v} = m r^2 \left(- \dot\varphi \sin\theta\,\mathbf{\hat{\boldsymbol\theta}} + \dot\theta\,\hat{\boldsymbol\varphi }\right)`
31. [Spherical coordinate system / Kinematics] 
   `\mathbf{L}= -i\hbar ~\mathbf{r} \times \nabla =i \hbar \left(\frac{\hat{\boldsymbol{\theta}}}{\sin(\theta)} \frac{\partial}{\partial\phi} - \hat{\boldsymbol{\varphi}} \frac{\partial}{\partial\theta}\right).`
32. [Spherical coordinate system / Kinematics] 
   `\mathbf{\tau} = \frac{\mathrm{d}\mathbf{L}}{\mathrm{d}t} = \mathbf{r} \times \mathbf{F} = -m \left(2r\dot{r}\dot{\varphi}\sin\theta + r^2\ddot{\varphi}\sin{\theta} + 2r^2\dot{\theta}\dot{\varphi}\cos{\theta} \right)\hat{\boldsymbol\theta} + m \left(r^2\ddot{\theta} + 2r\dot{r}\dot{\theta} - r^2\dot{\varphi}^2\sin\theta\cos\theta \right) \hat{\boldsymbol\varphi}`
33. [Spherical coordinate system / Kinematics] 
   `E_k = \frac{1}{2}m \left[ \left(\dot{r}\right)^2 + \left(r\dot{\theta}\right)^2 + \left(r\dot{\varphi}\sin\theta\right)^2 \right]`
34. [Polar coordinate system / Uniqueness of polar coordinates] Where a unique representation is needed for any point besides the pole, it is usual to limit to positive numbers ( ) and to either the interval or the interval 
   `[0,2\pi)`
35. [Polar coordinate system / Uniqueness of polar coordinates] Where a unique representation is needed for any point besides the pole, it is usual to limit to positive numbers ( ) and to either the interval or the interval 
   `(-\pi,\pi]`
36. [Polar coordinate system / Converting between polar and Cartesian coordinates] 
   `\begin{align} x &= r \cos \varphi, \\ y &= r \sin \varphi. \end{align}`
37. [Polar coordinate system / Converting between polar and Cartesian coordinates] 
   `\operatorname{atan2}(y, x) = \begin{cases} \arctan\left(\frac{y}{x}\right) & \mbox{if } x > 0\\ \arctan\left(\frac{y}{x}\right) + \pi & \mbox{if } x < 0 \mbox{ and } y \ge 0\\ \arctan\left(\frac{y}{x}\right) - \pi & \mbox{if } x < 0 \mbox{ and } y < 0\\ \frac{\pi}{2} & \mbox{if } x = 0 \mbox{ and } y > 0\\ -\frac{\pi}{2} & \mbox{if } x = 0 \mbox{ and } y < 0\\ \text{undefined} & \mbox{if } x = 0 \mbox{ and } y = 0. \end{cases}`
38. [Polar coordinate system / Converting between polar and Cartesian coordinates] 
   `\varphi = \begin{cases} \arccos\left(\frac{x}{r}\right) & \mbox{if } y \ge 0 \mbox{ and } r \neq 0 \\ -\arccos\left(\frac{x}{r}\right) & \mbox{if } y < 0 \\ \text{undefined} & \mbox{if } r = 0. \end{cases}`
39. [Polar coordinate system / Complex numbers] In polar form, the distance and angle coordinate are often referred to as the number's magnitude of modulus and argument, respectively. This can be obtained fro
   `x = r \cos \varphi`
40. [Polar coordinate system / Complex numbers] In polar form, the distance and angle coordinate are often referred to as the number's magnitude of modulus and argument, respectively. This can be obtained fro
   `y = r \sin \varphi`
41. [Polar coordinate system / Complex numbers] 
   `z = r(\cos\varphi + i\sin\varphi) = re^{i\varphi}.`
42. [Polar coordinate system / Complex numbers] The last expression is derived from Euler's formula, where is Euler's number approximately 2.718, and &mdash;expressed in radians&mdash;is the principal value o
   `\cos \varphi + i \sin \varphi`
43. [Polar coordinate system / Complex numbers] * Multiplication:
   `r_0 e^{i\varphi_0}\, r_1 e^{i\varphi_1} = r_0 r_1 e^{i\left(\varphi_0 + \varphi_1\right)}`
44. [Polar coordinate system / Complex numbers] * Division:
   `\frac{r_0 e^{i\varphi_0}}{r_1 e^{i\varphi_1}} = \frac{r_0}{r_1}e^{i(\varphi_0 - \varphi_1)}`
45. [Polar coordinate system / Complex numbers] * Exponentiation or de Moivre's formula:
   `\left(re^{i\varphi}\right)^n = r^n e^{in\varphi}`
46. [Polar coordinate system / Complex numbers] * Root Extraction or principal root:
   `\sqrt[n]{re^{i\varphi}} = \sqrt[n]{r} e^{i\varphi \over n}`
47. [Polar coordinate system / Polar equation of a curve] thumb|A curve on the Cartesian plane can be mapped into polar coordinates. In this animation, <math>y = \sin (6\!\cdot\!x) + 2</math> is mapped onto <math>r = \
   `y = \sin (6\!\cdot\!x) + 2`
48. [Polar coordinate system / Polar equation of a curve] thumb|A curve on the Cartesian plane can be mapped into polar coordinates. In this animation, <math>y = \sin (6\!\cdot\!x) + 2</math> is mapped onto <math>r = \
   `r = \sin (6\!\cdot\!\theta) + 2`
49. [Polar coordinate system / Polar equation of a curve] * If it will be symmetric about the vertical (90°/270°) ray:
   `1=''r''(''π'' − ''φ'') = ''r''(''φ'')`
50. [Polar coordinate system / Circle] 
   `r^2 - 2 r r_0 \cos(\varphi - \gamma) + r_0^2 = a^2.`
51. [Polar coordinate system / Circle] 
   `r = 2 a\cos(\varphi - \gamma).`
52. [Polar coordinate system / Circle] 
   `r = r_0 \cos(\varphi - \gamma) + \sqrt{a^2 - r_0^2 \sin^2(\varphi - \gamma)}`
53. [Polar coordinate system / Conic sections] 
   `r = { \ell\over {1 - \epsilon \cos \varphi}}`
54. [Polar coordinate system / Line] where is the angle of elevation of the line; that is, , where is the slope of the line in the Cartesian coordinate system. The non-radial line that crosses the 
   `\varphi = \arctan m`
55. [Polar coordinate system / Line] 
   `r(\varphi) = r_0 \sec(\varphi - \gamma).`
56. [Polar coordinate system / Polar rose] 
   `\begin{align} r(\varphi) &= a\sin\left(k\varphi\right), \\ r(\varphi) &= a\cos\left(k\varphi\right). \end{align}`
57. [Polar coordinate system / Archimedean spiral] thumb|right|One arm of an Archimedean spiral with equation {{math|1=''r''(''φ'') = ''φ'' / 2''π''}} for {{math|0 < ''φ'' < 6''π''}}
   `1=''r''(''φ'') = ''φ'' / 2''π''`
58. [Polar coordinate system / Archimedean spiral] thumb|right|One arm of an Archimedean spiral with equation {{math|1=''r''(''φ'') = ''φ'' / 2''π''}} for {{math|0 < ''φ'' < 6''π''}}
   `0 < ''φ'' < 6''π''`
59. [Polar coordinate system / Quadratrix] A quadratrix in the first quadrant is a curve with equal to the fraction of the quarter circle with radius determined by the radius through the curve point. Sin
   `y = \rho \sin \theta`
60. [Polar coordinate system / Quadratrix] }} , the curve is given by
   `\frac{2 r \theta}{\pi}`
61. [Polar coordinate system / Quadratrix] }} , the curve is given by
   `\rho (\theta) = \frac{2 r \theta}{\pi \sin \theta}.`
62. [Polar coordinate system / Intersection of two polar curves] # All the points where are solutions to the equation where is an integer.
   `f(\theta+2k\pi)=g(\theta)`
63. [Polar coordinate system / Intersection of two polar curves] # All the points where are solutions to the equation where is an integer.
   `f(\theta+(2k+1)\pi)=-g(\theta)`
64. [Polar coordinate system / Differential calculus] Using and , one can derive a relationship between derivatives in Cartesian and polar coordinates. For a given function, u ( x , y ), it follows that (by computi
   `1=''x'' = ''r'' cos ''φ''`
65. [Polar coordinate system / Differential calculus] Using and , one can derive a relationship between derivatives in Cartesian and polar coordinates. For a given function, u ( x , y ), it follows that (by computi
   `1=''y'' = ''r'' sin ''φ''`
66. [Polar coordinate system / Differential calculus] 
   `\begin{align} r \frac{du}{dr} &= r \frac{\partial u}{\partial x} \cos\varphi + r \frac{\partial u}{\partial y} \sin\varphi = x \frac{\partial u}{\partial x} + y \frac{\partial u}{\partial y}, \\[2pt] \frac{du}{d\varphi} &= - \frac{\partial u}{\partial x} r \sin\varphi + \frac{\partial u}{\partial y} r \cos\varphi = -y \frac{\partial u}{\partial x} + x \frac{\partial u}{\partial y}. \end{align}`
67. [Polar coordinate system / Differential calculus] 
   `\begin{align} \frac{du}{dx} &= \frac{\partial u}{\partial r}\frac{x}{\sqrt{x^2+y^2}} - \frac{\partial u}{\partial \varphi}\frac{y}{x^2+y^2} \\[2pt] &= \cos \varphi \frac{\partial u}{\partial r} - \frac{1}{r} \sin\varphi \frac{\partial u}{\partial \varphi}, \\[2pt] \frac{du}{dy} &= \frac{\partial u}{\partial r}\frac{y}{\sqrt{x^2+y^2}} + \frac{\partial u}{\partial \varphi}\frac{x}{x^2+y^2} \\[2pt] &= \sin\varphi \frac{\partial u}{\partial r} + \frac{1}{r} \cos\varphi \frac{\partial u}{\partial \varphi}. \end{align}`
68. [Polar coordinate system / Differential calculus] 
   `\begin{align} \frac{d}{dx} &= \cos \varphi \frac{\partial}{\partial r} - \frac{1}{r} \sin\varphi \frac{\partial}{\partial \varphi} \\[2pt] \frac{d}{dy} &= \sin \varphi \frac{\partial}{\partial r} + \frac{1}{r} \cos\varphi \frac{\partial}{\partial \varphi}. \end{align}`
69. [Polar coordinate system / Differential calculus] 
   `\begin{align} x &= r(\varphi)\cos\varphi \\ y &= r(\varphi)\sin\varphi \end{align}`
70. [Polar coordinate system / Differential calculus] 
   `\begin{align} \frac{dx}{d\varphi} &= r'(\varphi)\cos\varphi - r(\varphi)\sin\varphi \\[2pt] \frac{dy}{d\varphi} &= r'(\varphi)\sin\varphi + r(\varphi)\cos\varphi. \end{align}`
71. [Polar coordinate system / Differential calculus] Dividing the second equation by the first yields the Cartesian slope of the tangent line to the curve at the point :
   `\frac{dy}{dx} = \frac{r'(\varphi)\sin\varphi + r(\varphi)\cos\varphi}{r'(\varphi)\cos\varphi-r(\varphi)\sin\varphi}.`
72. [Polar coordinate system / Arc length] The arc length (length of a line segment) defined by a polar function is found by the integration over the curve r ( φ ). Let L denote this length along the cur
   `0 < ''b'' − ''a'' < 2''π''`
73. [Polar coordinate system / Area] 
   `\pi \left[r(\varphi_i)\right]^2 \cdot \frac{\Delta \varphi}{2\pi} = \frac{1}{2}\left[r(\varphi_i)\right]^2 \Delta \varphi.`
74. [Polar coordinate system / Area generalization] 
   `J = \det \frac{\partial(x, y)}{\partial(r, \varphi)} = \begin{vmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \varphi} \\[2pt] \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \varphi} \end{vmatrix} = \begin{vmatrix} \cos\varphi & -r\sin\varphi \\ \sin\varphi & r\cos\varphi \end{vmatrix} = r\cos^2\varphi + r\sin^2\varphi = r.`
75. [Polar coordinate system / Area generalization] thumb|right|A graph of <math>f(x) = e^{-x^2}</math> and the area between the function and the <math>x</math>-axis, which is equal to <math>\sqrt{\pi}</math>.
   `f(x) = e^{-x^2}`
76. [Polar coordinate system / Area generalization] thumb|right|A graph of <math>f(x) = e^{-x^2}</math> and the area between the function and the <math>x</math>-axis, which is equal to <math>\sqrt{\pi}</math>.
   `\sqrt{\pi}`
77. [Polar coordinate system / Area generalization] 
   `\int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt\pi.`
78. [Polar coordinate system / Vector calculus] Vector calculus can also be applied to polar coordinates. For a planar motion, let be the position vector , with r and depending on time t .
   `(''r'' cos(''φ''), ''r'' sin(''φ''))`
79. [Polar coordinate system / Vector calculus] 
   `\hat{\mathbf{r}} = (\cos(\varphi), \sin(\varphi))`
80. [Polar coordinate system / Vector calculus] 
   `\hat \boldsymbol \varphi = (-\sin(\varphi), \cos(\varphi)) = \hat{\mathbf{k}} \times \hat{\mathbf{r}} \ ,`
81. [Polar coordinate system / Vector calculus] 
   `\begin{align} \mathbf{r} &= (x,\ y) = r(\cos\varphi,\ \sin\varphi) = r \hat{\mathbf{r}}\ , \\[1.5ex] \dot{\mathbf{r}} &= \left(\dot{x},\ \dot{y}\right) = \dot{r}(\cos\varphi,\ \sin\varphi) + r\dot{\varphi}(-\sin\varphi,\ \cos\varphi) = \dot{r}\hat{\mathbf{r}} + r\dot{\varphi}\hat{\boldsymbol{\varphi}}\ ,\\[1.5ex] \end{align}`
82. [Polar coordinate system / Vector calculus] 
   `\begin{align} \ddot{\mathbf{r}} &= \left(\ddot{x},\ \ddot{y}\right) \\[1ex] &= \ddot{r}(\cos\varphi,\ \sin\varphi) + 2\dot{r}\dot{\varphi}(-\sin\varphi,\ \cos\varphi) + r\ddot{\varphi}(-\sin\varphi,\ \cos\varphi) - r\dot{\varphi}^2(\cos\varphi,\ \sin\varphi) \\[1ex] &= \left(\ddot{r} - r\dot{\varphi}^2\right) \hat{\mathbf{r}} + \left(r\ddot{\varphi} + 2\dot{r}\dot{\varphi}\right) \hat{\boldsymbol{\varphi}} \\[1ex] &= \left(\ddot{r} - r\dot{\varphi}^2\right) \hat{\mathbf{r}} + \frac{1}{r}\; \frac{d}{dt} \left(r^2\dot{\varphi}\right) \hat{\boldsymbol{\varphi}}. \end{align}`
83. [Polar coordinate system / Differential geometry] In the modern terminology of differential geometry, polar coordinates provide coordinate charts for the differentiable manifold , the plane minus the origin. In
   `1=''x'' = ''r'' cos(''θ'')`
84. [Polar coordinate system / Differential geometry] In the modern terminology of differential geometry, polar coordinates provide coordinate charts for the differentiable manifold , the plane minus the origin. In
   `1=''y'' = ''r'' sin(''θ'')`
85. [Polar coordinate system / Differential geometry] Since , and , we get that
   `dx^2=(r_2\cos\theta_2-r_1\cos\theta_1)^2`
86. [Polar coordinate system / Differential geometry] Since , and , we get that
   `dy^2=(r_2\sin\theta_2-r_1\sin\theta_1)^2`
87. [Polar coordinate system / Differential geometry] :
   `ds^2=r_2^2\cos^2\theta_2-2r_1r_2\cos\theta_1\cos\theta_2+r_1^2\cos^2\theta_1+r_2^2\sin^2\theta_2-2r_1r_2\sin\theta_1\sin\theta_2+r_1^2\sin^2\theta_1=`
88. [Polar coordinate system / Differential geometry] :
   `r_2^2(\cos^2\theta_2+\sin^2\theta_2)+r_1^2(\cos^2\theta_1+\sin^2\theta_1)-2r_1r_2(\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2)=`
89. [Polar coordinate system / Differential geometry] :
   `r_1^2+r_2^2-2r_1r_2(1-1+\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2)=`
90. [Polar coordinate system / Differential geometry] :
   `(r_2-r_1)^2+2r_1r_2(1-\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2).`
91. [Polar coordinate system / Differential geometry] Now we use the trigonometric identity to proceed:
   `\cos(\theta_2-\theta_1)=\cos\theta_1\cos\theta_2+\sin\theta_1\sin\theta_2`
92. [Polar coordinate system / Differential geometry] :
   `ds^2=dr^2+2r_1r_2(1-\cos d\theta).`
93. [Polar coordinate system / Differential geometry] :
   `\cos d\theta\approx1-\frac{d\theta^2}{2},`
94. [Polar coordinate system / Differential geometry] so that , and . Therefore, around an infinitesimally small domain of any point,
   `1-\cos d\theta\approx\frac{d\theta^2}{2}`
95. [Polar coordinate system / Differential geometry] so that , and . Therefore, around an infinitesimally small domain of any point,
   `2r_1r_2(1-\cos d\theta)\approx2r^2\frac{d\theta^2}{2}=r^2d\theta^2`
96. [Polar coordinate system / Differential geometry] An orthonormal frame with respect to this metric is given by with dual coframe The connection form relative to this frame and the Levi-Civita connection is give
   `e^r = dr, \quad e^\theta = r d\theta.`
97. [Polar coordinate system / Cylindrical coordinates] 
   `\begin{align} x &= r \, \cos\theta \\ y &= r \, \sin\theta \\ z &= z. \end{align}`
98. [Polar coordinate system / Spherical coordinates] :
   `\begin{align} x &= \rho \, \sin\varphi \, \cos\theta \\ y &= \rho \, \sin\varphi \, \sin\theta \\ z &= \rho \, \cos\varphi. \end{align}`
99. [Quaternions and spatial rotation / ] When used to represent rotation, unit quaternions are also called rotation quaternions as they represent the 3D rotation group. When used to represent an orient
   `C = \cos(\theta/2)`
100. [Quaternions and spatial rotation / ] When used to represent rotation, unit quaternions are also called rotation quaternions as they represent the 3D rotation group. When used to represent an orient
   `S=\sin(\theta/2)`
101. [Quaternions and spatial rotation / ] Compared to rotation matrices, quaternions are more compact, efficient, and numerically stable. Compared to Euler angles, they are simpler to compose. However, 
   `[0,2\pi)`
102. [Quaternions and spatial rotation / Using quaternions as rotations] :
   `\mathbf{q} = e^{\frac{\theta}{2}{(u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k})}} = \cos \frac{\theta}{2} + (u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k}) \sin \frac{\theta}{2} = \cos \frac{\theta}{2} + \mathbf u \sin \frac{\theta}{2}`
103. [Quaternions and spatial rotation / Using quaternions as rotations] :
   `\mathbf r = \left(\cos^2\frac{\theta}{2}-\sin^2\frac{\theta}{2}||\mathbf u||^2 \right)\mathbf p + 2\sin^2\frac{\theta}{2} (\mathbf u \cdot \mathbf p)\mathbf u + 2\cos\frac{\theta}{2}\sin\frac{\theta}{2}(\mathbf u \times \mathbf p),`
104. [Quaternions and spatial rotation / Using quaternions as rotations] using the Hamilton product, where the vector part of the pure quaternion ) = (0, r , r , r )}} is the new position vector of the point after the rotation. In a 
   `(u_x, u_y, u_z)\sin \frac{\theta}{2}`
105. [Quaternions and spatial rotation / Using quaternions as rotations] : .
   `\left(\cos^2\frac{\theta}{2} -\sin^2\frac{\theta}{2}\right) \mathbf{n} + 2 \left(\cos\frac{\theta}{2}\sin\frac{\theta}{2} \right)\mathbf{n}_T = \cos\theta \mathbf{n} + \sin\theta \mathbf{n}_T`
106. [Quaternions and spatial rotation / Using quaternions as rotations] :
   `\mathbf{r} = \mathbf{p} + 2\cos\frac{\theta}{2}\sin\frac{\theta}{2}(\mathbf u \times \mathbf p) + 2 \sin^2\frac{\theta}{2} \mathbf u \times (\mathbf u \times \mathbf p) .`
107. [Quaternions and spatial rotation / Using quaternions as rotations] A geometric fact independent of quaternions is the existence of a two-to-one mapping from physical rotations to rotational transformation matrices. If 0 ⩽ ⩽ , a
   `2\pi`
108. [Quaternions and spatial rotation / Using quaternions as rotations] A geometric fact independent of quaternions is the existence of a two-to-one mapping from physical rotations to rotational transformation matrices. If 0 ⩽ ⩽ , a
   `2\pi-\theta`
109. [Quaternions and spatial rotation / Using quaternions as rotations] A geometric fact independent of quaternions is the existence of a two-to-one mapping from physical rotations to rotational transformation matrices. If 0 ⩽ ⩽ , a
   `(\theta=\pi)`
110. [Quaternions and spatial rotation / Using quaternions as rotations] A geometric fact independent of quaternions is the existence of a two-to-one mapping from physical rotations to rotational transformation matrices. If 0 ⩽ ⩽ , a
   `\pi`
111. [Quaternions and spatial rotation / Using quaternions as rotations] :
   `\mathbf{q}^{-1} = e^{-\frac{\theta}{2}{(u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k})}} = \cos \frac{\theta}{2} - (u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k}) \sin \frac{\theta}{2} .`
112. [Quaternions and spatial rotation / Example conjugation operation] :
   `\alpha = \frac{2 \pi}{3}`
113. [Quaternions and spatial rotation / Example conjugation operation] The length of is , the half angle is (60°) with cosine , ( ) and sine |2}}, ( ). We are therefore dealing with a conjugation by the unit quaternion
   `1=cos 60° = 0.5`
114. [Quaternions and spatial rotation / Example conjugation operation] The length of is , the half angle is (60°) with cosine , ( ) and sine |2}}, ( ). We are therefore dealing with a conjugation by the unit quaternion
   `1=sin 60° ≈ 0.866`
115. [Quaternions and spatial rotation / Example conjugation operation] :
   `\begin{align} u &= \cos\frac{\alpha}{2} + \sin\frac{\alpha}{2}\cdot \frac{1}{\| \vec{v} \| }\vec{v}\\ &= \cos \frac{\pi}{3} + \sin \frac{\pi}{3}\cdot \frac{1}{\sqrt{3}}\vec{v}\\ &= \frac{1}{2} + \frac{\sqrt{3}}{2}\cdot \frac{1}{\sqrt{3}}\vec{v}\\ &= \frac{1}{2} + \frac{\sqrt{3}}{2}\cdot \frac{\mathbf{i}+\mathbf{j}+\mathbf{k}}{\sqrt{3}}\\ &= \frac{1 + \mathbf{i} + \mathbf{j} + \mathbf{k}}{2} \end{align}`
116. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `S = \cos\frac{\varphi}{2} + \mathbf{S}\sin\frac{\varphi}{2}.`
117. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `A = \cos\frac{\alpha}{2} + \mathbf{A}\sin\frac{\alpha}{2} \quad \text{and} \quad B = \cos\frac{\beta}{2} + \mathbf{B}\sin\frac{\beta}{2},`
118. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `C = \cos\frac{\gamma}{2} + \mathbf{C}\sin\frac{\gamma}{2} = \left(\cos\frac{\beta}{2} + \mathbf{B} \sin\frac{\beta}{2}\right) \left(\cos\frac{\alpha}{2} + \mathbf{A}\sin\frac{\alpha}{2}\right).`
119. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `\cos\frac{\gamma}{2} + \mathbf{C}\sin\frac{\gamma}{2} = \left( \cos\frac{\beta}{2} \cos\frac{\alpha}{2} - \mathbf{B} \cdot \mathbf{A} \sin\frac{\beta}{2} \sin\frac{\alpha}{2}\right) + \left(\mathbf{B} \sin\frac{\beta}{2} \cos\frac{\alpha}{2} + \mathbf{A} \sin\frac{\alpha}{2} \cos\frac{\beta}{2} + \mathbf{B} \times \mathbf{A} \sin\frac{\beta}{2} \sin\frac{\alpha}{2} \right).`
120. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `\cos\frac{\gamma}{2} = \cos\frac{\beta}{2} \cos\frac{\alpha}{2} - \mathbf{B} \cdot \mathbf{A} \sin\frac{\beta}{2} \sin\frac{\alpha}{2},`
121. [Quaternions and spatial rotation / The composition of spatial rotations] 
   `\mathbf{C} \tan\frac{\gamma}{2} = \frac{ \mathbf{B} \tan\frac{\beta}{2} + \mathbf{A} \tan\frac{\alpha}{2} + \mathbf{B} \times \mathbf{A} \tan\frac{\beta}{2}\tan\frac{\alpha}{2} }{1 - \mathbf{B} \cdot \mathbf{A} \tan\frac{\beta}{2}\tan\frac{\alpha}{2}}.`
122. [Quaternions and spatial rotation / Axis–angle composition] The normalized rotation axis, removing the from the expanded product, leaves the vector which is the rotation axis, times some constant. Care should be taken no
   `\cos\frac{\gamma}{2}`
123. [Quaternions and spatial rotation / Axis–angle composition] The normalized rotation axis, removing the from the expanded product, leaves the vector which is the rotation axis, times some constant. Care should be taken no
   `k 2\pi`
124. [Quaternions and spatial rotation / Axis–angle composition] 
   `\begin{align} \gamma &= 2\cos^{-1}\left(\cos\frac{\beta}{2} \cos\frac{\alpha}{2} - \mathbf{B} \cdot \mathbf{A} \sin\frac{\beta}{2} \sin\frac{\alpha}{2}\right) \\ \mathbf{D} &= \mathbf{B} \sin\frac{\beta}{2} \cos\frac{\alpha}{2} + \mathbf{A} \sin\frac{\alpha}{2} \cos\frac{\beta}{2} + \mathbf{B} \times \mathbf{A} \sin\frac{\beta}{2} \sin\frac{\alpha}{2} \end{align}`
125. [Quaternions and spatial rotation / Axis–angle composition] 
   `\begin{align} \gamma &= 2 \cos^{-1} \left(\left(1 - \mathbf{A} \cdot \mathbf{B}\right) \cos\frac{\beta - \alpha}{2} + \left(1 + \mathbf{A}\cdot \mathbf{B}\right) \cos\frac{\beta + \alpha}{2}\right) \\ \mathbf{D} &= \left(\sin\frac{\beta + \alpha}{2} + \sin\frac{\beta - \alpha}{2}\right) \mathbf{A} + \left(\sin\frac{\beta + \alpha}{2} - \sin\frac{\beta - \alpha}{2}\right) \mathbf{B} + \left(\cos\frac{\beta - \alpha}{2} - \cos\frac{\beta + \alpha}{2}\right) \mathbf{B} \times \mathbf{A} \end{align}`
126. [Quaternions and spatial rotation / Axis–angle composition] finally normalizing the rotation axis: or .
   `\frac{\mathbf{D}}{2 \sin\frac{1}{2}\gamma}`
127. [Quaternions and spatial rotation / Rotation identity] Let be a unit vector (the rotation axis) and let . Our goal is to show that
   `q = \cos \frac{\alpha}{2} + \vec{u} \sin \frac{\alpha}{2}`
128. [Quaternions and spatial rotation / Rotation identity] :
   `\vec{v}' = q \vec{v} q^{-1} = \left( \cos \frac{\alpha}{2} + \vec{u} \sin \frac{\alpha}{2} \right) \, \vec{v} \, \left( \cos \frac{\alpha}{2} - \vec{u} \sin \frac{\alpha}{2} \right)`
129. [Quaternions and spatial rotation / Rotation identity] :
   `\begin{align} \vec{v}' &= \vec{v} \cos^2 \frac{\alpha}{2} + \left(\vec{u}\vec{v} - \vec{v}\vec{u}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \vec{u}\vec{v}\vec{u} \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \left(\left(\vec{u} \times \vec{v}\right) - \left(\vec{u} \cdot \vec{v}\right)\right)\vec{u} \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \left(\left(\vec{u} \times \vec{v}\right)\vec{u} - \left(\vec{u} \cdot \vec{v}\right)\vec{u}\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \left(\left(\left(\vec{u} \times \vec{v}\right) \times \vec{u} - \left(\vec{u} \times \vec{v}\right) \cdot \vec{u}\right) - \left(\vec{u} \cdot \vec{v}\right)\vec{u}\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \left(\left(\vec{v} - \left(\vec{u} \cdot \vec{v}\right)\vec{u}\right) - 0 - \left(\vec{u} \cdot \vec{v}\right)\vec{u}\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} - \left(\vec{v} - 2 \vec{u} \left(\vec{u} \cdot \vec{v}\right)\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} + \left(2 \vec{u} \left(\vec{u} \cdot \vec{v}\right) - \vec{v}\right) \sin^2 \frac{\alpha}{2} \\[6pt] \end{align}`
130. [Quaternions and spatial rotation / Rotation identity] :
   `\begin{align} \vec{v}' &= \vec{v} \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} + \left(2 \vec{u} \left(\vec{u} \cdot \vec{v}\right) - \vec{v}\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \left(\vec{v}_{\|} + \vec{v}_{\bot}\right) \cos^2 \frac{\alpha}{2} + 2 \left(\vec{u} \times \vec{v}\right) \sin \frac{\alpha}{2} \cos \frac{\alpha}{2} + \left(\vec{v}_{\|} - \vec{v}_{\bot}\right) \sin^2 \frac{\alpha}{2} \\[6pt] &= \vec{v}_{\|} \left(\cos^2 \frac{\alpha}{2} + \sin^2 \frac{\alpha}{2}\right) + \left(\vec{u} \times \vec{v}\right) \left(2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}\right) + \vec{v}_{\bot} \left(\cos^2 \frac{\alpha}{2} - \sin^2 \frac{\alpha}{2}\right) \\[6pt] \end{align}`
131. [Quaternions and spatial rotation / Rotation identity] :
   `\begin{align} \vec{v}' &= \vec{v}_{\|} \left(\cos^2 \frac{\alpha}{2} + \sin^2 \frac{\alpha}{2}\right) + \left(\vec{u} \times \vec{v}\right) \left(2 \sin \frac{\alpha}{2} \cos \frac{\alpha}{2}\right) + \vec{v}_{\bot} \left(\cos^2 \frac{\alpha}{2} - \sin^2 \frac{\alpha}{2}\right) \\[6pt] &= \vec{v}_{\|} + \left(\vec{u} \times \vec{v}\right) \sin \alpha + \vec{v}_\bot \cos \alpha \end{align}`
132. [Quaternions and spatial rotation / Parameterizing the space of rotations] It can be shown that no two-parameter coordinate system can avoid such degeneracy. We can avoid such problems by embedding the sphere in three-dimensional space
   `\alpha= 2 \cos^{-1} w = 2 \sin^{-1} \sqrt{x^2+y^2}`
133. [Quaternions and spatial rotation / Parameterizing the space of rotations] In the same way the hyperspherical space of 3D rotations can be parameterized by three angles (Euler angles), but any such parameterization is degenerate at som
   `\alpha = 2 \cos^{-1} w = 2 \sin^{-1} \sqrt{x^2+y^2+z^2}.`
134. [Haversine formula / ] These names follow from the fact that they are customarily written in terms of the haversine function, given by sin 2 θ }}. The formulas could equally be writte
   `sin<sup>2</sup>`
135. [Haversine formula / Formulation] 
   `\operatorname{hav}\theta = \operatorname{hav}\left(\Delta \varphi \right) + \cos\left(\varphi_1\right)\cos\left(\varphi_2\right)\operatorname{hav}\left(\Delta \lambda \right)`
136. [Haversine formula / Formulation] 
   `\operatorname{hav}\theta= \sin^2\left(\frac{\theta}{2}\right) = \frac{1 - \cos(\theta)}{2}.`
137. [Haversine formula / Formulation] 
   `\theta= 2 \arcsin\left(\sqrt{\operatorname{hav}\theta}\right),`
138. [Haversine formula / Formulation] 
   `\begin{align} \operatorname{hav}\theta &= \operatorname{hav}\left(\Delta \varphi \right) + \cos\left(\varphi_1\right)\cos\left(\varphi_2\right)\operatorname{hav}\left(\Delta \lambda \right) \\ &= \operatorname{hav}(\Delta \varphi ) + ( 1 - \operatorname{hav}(\Delta \varphi) - \operatorname{hav}(2 \varphi_\text{m} ))\cdot\operatorname{hav}(\Delta \lambda) \\ &= \sin^2\left(\frac{\Delta \varphi }{2}\right) + \left(1- \sin^2\left(\frac{\Delta \varphi }{2}\right) - \sin^2\left(\varphi_\text{m}\right)\right) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right) \\ &= \sin^2\left(\frac{\Delta \varphi }{2}\right) + \cos \varphi_1 \cdot \cos \varphi_2 \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right) \\ &= \sin^2\left(\frac{\Delta \varphi }{2}\right) \cdot \cos^2\left(\frac{\Delta \lambda}{2}\right) + \cos^2\left(\varphi_\text{m}\right) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right) \\ &= \frac{1 - \cos\left(\Delta \varphi \right) + \cos \varphi_1 \cdot \cos \varphi_2 \cdot \left(1 - \cos\left(\Delta \lambda\right)\right)}{2} \end{align}`
139. [Haversine formula / Formulation] When using these formulae, one must ensure that hav( &theta; )}} does not exceed 1 due to a floating point error ( is real only for ). only approaches 1 for ant
   `π''R''`
140. [Haversine formula / Formulation] As described below, a similar formula can be written using cosines (sometimes called the spherical law of cosines, not to be confused with the law of cosines fo
   `cos({{sfrac|''d''|''R''`
141. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] 
   `\operatorname{hav}(c) = \operatorname{hav}(a - b) + \sin(a)\sin(b)\operatorname{hav}(C).`
142. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] In order to obtain the haversine formula of the previous section from this law, one simply considers the special case where is the north pole, while and are the
   `{{sfrac|π|2`
143. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] In order to obtain the haversine formula of the previous section from this law, one simply considers the special case where is the north pole, while and are the
   `sin({{sfrac|π|2`
144. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] 
   `\cos(c) = \cos(a)\cos(b) + \sin(a)\sin(b)\cos(C). \,`
145. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] As mentioned above, this formula is an ill-conditioned way of solving for when is small. Instead, we substitute the identity that 1 − 2 hav( θ )}}, and also emp
   `cos(''θ'') {{=`
146. [Haversine formula / <span class="anchor" id="Law"></span> The law of haversines] As mentioned above, this formula is an ill-conditioned way of solving for when is small. Instead, we substitute the identity that 1 − 2 hav( θ )}}, and also emp
   `cos(''a'' − ''b'') {{=`
147. [Haversine formula / Proof] 
   `\operatorname{hav}\left(\theta\right) = \operatorname{hav}\left(\Delta \varphi \right) + \cos\left(\varphi_1\right)\cos\left(\varphi_2\right)\operatorname{hav}\left(\Delta \lambda\right)`
148. [Haversine formula / Proof] 
   `\begin{align} {\bf p_2} &= (\cos(\lambda_2)\cos(\varphi_2), \;\sin(\lambda_2)\cos(\varphi_2), \;\sin(\varphi_2)) \\ {\bf p_1} &= (\cos(\lambda_1)\cos(\varphi_1), \;\sin(\lambda_1)\cos(\varphi_1), \;\sin(\varphi_1)) \end{align}`
149. [Haversine formula / Proof] 
   `\begin{align} {\bf p_2'} &= (\cos(\lambda')\cos(\varphi_2), \;\sin(\lambda')\cos(\varphi_2), \;\sin(\varphi_2)) \\ {\bf p_1'} &= (\cos(0)\cos(\varphi_1), \;\sin(0)\cos(\varphi_1), \;\sin(\varphi_1)) \\ &= (\cos(\varphi_1), \;0, \;\sin(\varphi_1)) \end{align}`
150. [Haversine formula / Proof] 
   `\begin{align} \cos(\theta) &= \langle{\bf p_1},{\bf p_2}\rangle = \langle{\bf p_1'},{\bf p_2'}\rangle = \cos(\lambda')\cos(\varphi_1)\cos(\varphi_2) + \sin(\varphi_1)\sin(\varphi_2) \\ &= \sin(\varphi_2)\sin(\varphi_1) + \cos(\varphi_2)\cos(\varphi_1) - \cos(\varphi_2)\cos(\varphi_1) + \cos(\lambda')\cos(\varphi_2)\cos(\varphi_1) \\ &= \cos(\Delta \varphi) + \cos(\varphi_2)\cos(\varphi_1)(-1 + \cos(\lambda')) \Rightarrow \\ \operatorname{hav}\left(\theta\right) &= \operatorname{hav}\left(\Delta \varphi \right) + \cos(\varphi_2)\cos(\varphi_1)\operatorname{hav}\left(\lambda' \right) \end{align}`
151. [Haversine formula / Example] 
   `\begin{align} \operatorname{hav}\left(\theta\right) &= \operatorname{hav}(\Delta \varphi ) + \cos(\varphi_1)\cos(\varphi_2)\operatorname{hav}(\Delta \lambda) \\[5mu] &= \operatorname{hav}(9.960^\circ) + \cos(38.898^\circ)\cos(48.858^\circ)\operatorname{hav}(79.331^\circ) \\[5mu] &\approx 0.0075356 + 0.77827 \times 0.65793 \times 0.40743 \\[5mu] &\approx 0.21616 \\[5mu] \theta &\approx 55.411^\circ. \end{align}`
152. [Total internal reflection / Critical angle] The critical angle is the smallest angle of incidence that yields total reflection, or equivalently the largest angle for which a refracted ray exists. Jenkins 
   `\theta_\text{c} = \arcsin(n_2/n_1)`
153. [Total internal reflection / Critical angle] When a wavefront is refracted from one medium to another, the incident (incoming) and refracted (outgoing) portions of the wavefront meet at a common line on th
   `v_1 = u \sin\theta_1.`
154. [Total internal reflection / Critical angle] When a wavefront is refracted from one medium to another, the incident (incoming) and refracted (outgoing) portions of the wavefront meet at a common line on th
   `v_2 = u \sin\theta_2.`
155. [Total internal reflection / Critical angle] {{NumBlk|:| | }}
   `\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}.`
156. [Total internal reflection / Critical angle] {{NumBlk|:| | }}
   `\theta_\text{c} = \arcsin(v_1/v_2).`
157. [Total internal reflection / Critical angle] }}
   `n_1 \sin\theta_1 = n_2 \sin\theta_2`
158. [Total internal reflection / Critical angle] {{NumBlk|:| | }}
   `\theta_\text{c} = \arcsin(n_2/n_1).`
159. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\mathbf{E_k} e^{i(\mathbf{k\cdot r} - \omega t)},`
160. [Total internal reflection / Derivation of evanescent wave] where is the (constant) complex amplitude vector, is the imaginary unit, is the wave vector (whose magnitude is the angular wavenumber), is the position vector,
   `\mathbf{E_k} e^{j(\omega t - \mathbf{k \cdot r})};`
161. [Total internal reflection / Derivation of evanescent wave] If ℓ is the component of in the direction of the field ( ) can be written If the argument of is to be constant, ℓ must increase at the velocity known as the pha
   `\mathbf{E_k}e^{i(k\ell-\omega t)}.`
162. [Total internal reflection / Derivation of evanescent wave] If ℓ is the component of in the direction of the field ( ) can be written If the argument of is to be constant, ℓ must increase at the velocity known as the pha
   `e^{i(\cdots)}`
163. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\mathbf{E}_\text{t} = \mathbf{E}_{\mathbf{k}\text{t}} e^{i(\mathbf{k_\text{t} \cdot r} - \omega t)},`
164. [Total internal reflection / Derivation of evanescent wave] 
   `\mathbf{k}_\text{t} = n_2 k_0 (\mathbf{i} \sin\theta_\text{t} + \mathbf{j} \cos\theta_\text{t}) = k_0 (\mathbf{i}\,n_1 \sin\theta_\text{i} + \mathbf{j}\,n_2 \cos\theta_\text{t}),`
165. [Total internal reflection / Derivation of evanescent wave] 
   `\mathbf{k}_\text{t} \cdot \mathbf{r} = k_0 (n_1 x \sin\theta_\text{i} + n_2 y \cos\theta_\text{t}),`
166. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\mathbf{E}_\text{t} = \mathbf{E}_{\mathbf{k}\text{t}} \exp[i(n_1 k_0 x \sin\theta_\text{i} + n_2 k_0 y \cos\theta_\text{t} - \omega t)].`
167. [Total internal reflection / Derivation of evanescent wave] In the case of TIR, the angle θ t does not exist in the usual sense. But we can still interpret ( ) for the transmitted (evanescent) wave by allowing θ t }} to 
   `cos{{tsp`
168. [Total internal reflection / Derivation of evanescent wave] In the case of TIR, the angle θ t does not exist in the usual sense. But we can still interpret ( ) for the transmitted (evanescent) wave by allowing θ t }} to 
   `sin{{tsp`
169. [Total internal reflection / Derivation of evanescent wave] 
   `\cos\theta_\text{t} = \sqrt{1 - \sin^2\theta_\text{t}} = \sqrt{1 - (n_1/n_2)^2 \sin^2\theta_\text{i}}.`
170. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\cos\theta_\text{t} = \pm i\,\sqrt{(n_1/n_2)^2 \sin^2\theta_\text{i} - 1}.`
171. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\mathbf{E}_\text{t} = \mathbf{E}_{\mathbf{k}\text{t}} e^{\mp\sqrt{n_1^2\sin^2\theta_\text{i} - n_2^2}\, k_0 y} e^{i[(n_1 k_0 \sin\theta_\text{i})x - \omega t]},`
172. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\mathbf{E}_\text{t} \propto e^{-\kappa y} e^{i(k_x x - \omega t)},`
173. [Total internal reflection / Derivation of evanescent wave] {{NumBlk|:| | }}
   `\begin{align} \kappa &= k_0 \sqrt{n_1^2 \sin^2\theta_\text{i} - n_2^2}, \\ k_x &= n_1 k_0 \sin\theta_\text{i}, \end{align}`
174. [Total internal reflection / Derivation of evanescent wave] 
   `d = \frac{\lambda_0}{2\pi \sqrt{n_1^2 \sin^2\theta_\text{i} - n_2^2}},`
175. [Total internal reflection / Derivation of evanescent wave] where λ 0 is the wavelength in vacuum, i.e. Born & Wolf, 1970, p. 16. Dividing the numerator and denominator by yields
   `2\pi/k_0.`
176. [Total internal reflection / Derivation of evanescent wave] 
   `d = \frac{\lambda_2}{2\pi \sqrt{(n_1/n_2)^2 \sin^2\theta_\text{i} - 1}},`
177. [Total internal reflection / Derivation of evanescent wave] 
   `d_\text{min} = \frac{\lambda_2}{2\pi \sqrt{(n_1/n_2)^2 - 1}}.`
178. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] In equations ( ), ( ), ( ), ( ), and ( ), we advance the phase by the angle ϕ if we replace by (that is, if we replace by ), with the result that the (complex) 
   `\mathbf{E_k} e^{i\mathbf{k\cdot r}} e^{-i\omega t},`
179. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `r_s = \frac{n_1\cos\theta_\text{i} - n_2\cos\theta_\text{t}}{n_1\cos\theta_\text{i} + n_2\cos\theta_\text{t}},`
180. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {n_1\cos\theta_\text{i} + n_2\cos\theta_\text{t}}, | }}
   `t_s = \frac{2n_1\cos\theta_\text{i}}{n_1\cos\theta_\text{i} + n_2\cos\theta_\text{t}},`
181. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `r_p = \frac{n_2\cos\theta_\text{i} - n_1\cos\theta_\text{t}}{n_2\cos\theta_\text{i} + n_1\cos\theta_\text{t}},`
182. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {n_2\cos\theta_\text{i} + n_1\cos\theta_\text{t}}. | }}
   `t_p = \frac{2n_1\cos\theta_\text{i}}{n_2\cos\theta_\text{i} + n_1\cos\theta_\text{t}}.`
183. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] 
   `r_s = \frac{n\cos\theta_\text{i} - i\sqrt{n^2\sin^2\theta_\text{i} - 1}}{n\cos\theta_\text{i} + i\sqrt{n^2\sin^2\theta_\text{i} - 1}},`
184. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] 
   `-2\arctan\frac{\sqrt{n^2\sin^2\theta_\text{i} - 1}}{n\cos\theta_\text{i}},`
185. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `\delta_s = 2\arctan\frac{\sqrt{n^2\sin^2\theta_\text{i} - 1}}{n\cos\theta_\text{i}}.`
186. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] 
   `r_p = \frac{\cos\theta_\text{i} - in\sqrt{n^2\sin^2\theta_\text{i} - 1}}{\cos\theta_\text{i} + in\sqrt{n^2\sin^2\theta_\text{i} - 1}},`
187. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] 
   `-2\arctan\frac{n\sqrt{n^2\sin^2\theta_\text{i} - 1}}{\cos\theta_\text{i}},`
188. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `\delta_p = 2\arctan\frac{n\sqrt{n^2\sin^2\theta_\text{i} - 1}}{\cos\theta_\text{i}}.`
189. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] In ( ), if we put (Snell's law) and multiply the numerator and denominator by sin θ t }}, we obtain Fresnel, 1866, pp. 773, 789n. Born & Wolf, 1970, p. 40, eqs.
   `n_2 = n_1\sin\theta_\text{i}/\sin\theta_\text{t}`
190. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `r_s = -\frac{\sin(\theta_\text{i} - \theta_\text{t})}{\sin(\theta_\text{i} + \theta_\text{t})},`
191. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] {{NumBlk|:| | }}
   `r_p = \frac{\tan(\theta_\text{i} - \theta_\text{t})}{\tan(\theta_\text{i} + \theta_\text{t})},`
192. [Total internal reflection / <span class="anchor" id="Phase shift upon total internal reflection"></span>Phase shifts] In Fig. 13, is computed by a final subtraction; but there are other ways of expressing it. Fresnel himself, in 1823, Buchwald, 1989, pp. 394, 453; Fresnel, 1866
   `tan{{hsp`
193. [Stereographic projection / First formulation] In spherical coordinates on the sphere (with the zenith angle, , and the azimuth, ) and polar coordinates on the plane, the projection and its inverse are
   `0\leq\varphi\leq\pi`
194. [Stereographic projection / First formulation] In spherical coordinates on the sphere (with the zenith angle, , and the azimuth, ) and polar coordinates on the plane, the projection and its inverse are
   `0\leq\theta\leq 2\pi`
195. [Stereographic projection / First formulation] :
   `\begin{align}(R, \Theta) &= \left(\frac{\sin \varphi}{1 - \cos \varphi}, \theta\right) = \left(\cot\frac{\varphi}{2}, \theta\right),\\ (\varphi, \theta) &= \left(2 \arctan \frac{1}{R}, \Theta\right).\end{align}`
196. [Stereographic projection / First formulation] Here, is understood to have value when . Also, there are many ways to rewrite these formulas using trigonometric identities. In cylindrical coordinates on the s
   `\pi`
197. [Stereographic projection / Properties] :
   `R = e^{\Theta/a},\,`
198. [Stereographic projection / Tangent half-angle substitution] The pair of trigonometric functions can be thought of as parametrizing the unit circle. The stereographic projection gives an alternative parametrization of the
   `(sin ''x'', cos ''x'')`
199. [Stereographic projection / Tangent half-angle substitution] :
   `\cos x = \frac{1 - t^2}{1 + t^2},\quad \sin x = \frac{2 t}{t^2 + 1}.`
200. [Lorentz factor / Rapidity] 
   `\tanh \varphi = \beta`
201. [Lorentz factor / Rapidity] 
   `\gamma = \cosh \varphi = \frac{1}{\sqrt{1 - \tanh^2 \varphi}} = \frac{1}{\sqrt{1 - \beta^2}}.`
202. [Waveplate / Principles of operation] 
   `\Gamma = \frac{2 \pi\, \Delta n\, L}{\lambda_0},`
203. [Waveplate / Principles of operation] For a single waveplate changing the wavelength of the light introduces a linear error in the phase. Tilt of the waveplate enters via a factor of (i.e., {{tmath|
   `\textstyle {1\over\cos{\theta}}`
204. [Waveplate / Half-wave plate] 
   `\mathbf{E}e^{i(kz-\omega t)} = E\mathbf{\hat p}e^{i(kz-\omega t)} = E (\mathbf{\hat f}\cos\theta + \mathbf{\hat s}\sin\theta) e^{i(kz-\omega t)},`
205. [Waveplate / Half-wave plate] where lies along the waveplate's slow axis. The effect of the half-wave plate is to introduce a phase shift term between the {{tmath|\mathbf{\hat f} }} and {{tm
   `e^{i\Gamma} =`
206. [Waveplate / Half-wave plate] where lies along the waveplate's slow axis. The effect of the half-wave plate is to introduce a phase shift term between the {{tmath|\mathbf{\hat f} }} and {{tm
   `e^{i\pi} = -1`
207. [Waveplate / Half-wave plate] 
   `E (\mathbf{\hat f}\cos\theta - \mathbf{\hat s}\sin\theta)e^{i(kz-\omega t)} = E [ \mathbf{\hat f}\cos(-\theta) + \mathbf{\hat s}\sin(-\theta)] e^{i(kz-\omega t)}.`
208. [Waveplate / Quarter-wave plate] 
   `(E_\mathrm{f} \mathbf{\hat f} + E_\mathrm{s} \mathbf{\hat s})e^{i(kz-\omega t)},`
209. [Waveplate / Quarter-wave plate] The effect of the quarter-wave plate is to introduce a phase shift term between the and components of the wave, so that upon exiting the crystal the wave is now
   `e^{i\pi/2} = i`
210. [Waveplate / Quarter-wave plate] 
   `(E_\mathrm{f} \mathbf{\hat f} + i E_\mathrm{s} \mathbf{\hat s})e^{i(kz-\omega t)}.`
211. [Waveplate / Quarter-wave plate] 
   `E(\mathbf{\hat f}+i\mathbf{\hat s})e^{i(kz-\omega t)},`
212. [Waveplate / Quarter-wave plate] The output of a quarter-wave plate depends on the polarization of the input. Suppose polarization axes and parallel with the slow axis and the fast axis of the 
   `''π''`
213. [Waveplate / Quarter-wave plate] The output of a quarter-wave plate depends on the polarization of the input. Suppose polarization axes and parallel with the slow axis and the fast axis of the 
   `''π''/2`
214. [Precession / Torque-free or torque neglected] 
   `\boldsymbol\omega_\mathrm{p} = \frac{\boldsymbol I_\mathrm{s} \boldsymbol\omega_\mathrm{s} } {\boldsymbol I_\mathrm{p} \cos(\boldsymbol \alpha)}`
215. [Precession / Torque-free or torque neglected] 
   `\boldsymbol R_\text{new} = \exp\left(\left[\boldsymbol\omega\left(\boldsymbol R_\text{old}\right)\right]_{\times} dt\right) \boldsymbol R_\text{old}`
216. [Precession / Torque-free or torque neglected] 
   `E\left(\exp\left(\left[\boldsymbol v\right]_{\times}\right) \boldsymbol R\right) \approx E\left(\boldsymbol R\right) + \left(\boldsymbol \omega\left(\boldsymbol R\right) \times \boldsymbol L\right) \cdot \boldsymbol v`
217. [Precession / Classical (Newtonian)] :
   `\boldsymbol\omega_\mathrm{p} = \frac{\ mgr}{I_\mathrm{s}\boldsymbol\omega_\mathrm{s}} = \frac{ \tau}{I_\mathrm{s}\boldsymbol\omega_\mathrm{s}\sin(\theta)}`
218. [Precession / Classical (Newtonian)] where is the moment of inertia, is the angular velocity of spin about the spin axis, is the mass, is the acceleration due to gravity, is the angle between the s
   `1='''''ω''''' = {{sfrac|2π|''T''`
219. [Precession / Classical (Newtonian)] 
   `T_\mathrm{p} = \frac{4\pi^2 I_\mathrm{s}}{\ mgrT_\mathrm{s}} = \frac{4\pi^2 I_\mathrm{s}\sin(\theta)}{\ \tau T_\mathrm{s}}`
220. [Ellipse / ] 
   `(x,y) = (a\cos(t),b\sin(t)) \quad \text{for} \quad 0\leq t\leq 2\pi.`
221. [Ellipse / Standard equation] 
   `y = \pm\frac{b}{a}\sqrt{\vphantom{\left(a^2 - x^2\right)} a^2 - x^2} = \pm \sqrt{\left(a^2 - x^2\right)\left(1 - e^2\right)}.`
222. [Ellipse / Semi-latus rectum] 
   `\ell = \frac{b^2}a = a \left(1 - e^2\right).`
223. [Ellipse / General ellipse] 
   `\begin{align} A &= a^2 \sin^2\theta + b^2 \cos^2\theta & B &= 2\left(b^2 - a^2\right) \sin\theta \cos\theta \\[1ex] C &= a^2 \cos^2\theta + b^2 \sin^2\theta & D &= -2A x_\circ - B y_\circ \\[1ex] E &= - B x_\circ - 2C y_\circ & F &= A x_\circ^2 + B x_\circ y_\circ + C y_\circ^2 - a^2 b^2. \end{align}`
224. [Ellipse / General ellipse] 
   `\begin{align} X &= \left(x - x_\circ\right) \cos\theta + \left(y - y_\circ\right) \sin\theta, \\ Y &= -\left(x - x_\circ\right) \sin\theta + \left(y - y_\circ\right) \cos\theta. \end{align}`
225. [Ellipse / Standard parametric representation] 
   `(x,\, y) = (a \cos t,\, b \sin t),\ 0 \le t < 2\pi\, .`
226. [Ellipse / Standard parametric representation] The parameter t (called the eccentric anomaly in astronomy) is not the angle of with the x -axis, but has a geometric meaning due to Philippe de La Hire (see be
   `\frac{y(t)}{x(t)} = \frac{b \,\sin t}{a \, \cos t} = \frac{b}{a} \tan t \ne \tan t`
227. [Ellipse / Rational representation] With the substitution and trigonometric formulae one obtains
   `u = \tan\left(\frac{t}{2}\right)`
228. [Ellipse / Rational representation] 
   `\cos t = \frac{1 - u^2}{1 + u^2}\ ,\quad \sin t = \frac{2u}{1 + u^2}`
229. [Ellipse / Tangent slope as parameter] can be obtained from the derivative of the standard representation :
   `\vec x(t) = (a \cos t,\, b \sin t)`
230. [Ellipse / Tangent slope as parameter] 
   `\vec x'(t) = (-a\sin t,\, b\cos t) \quad \rightarrow \quad m = -\frac{b}{a}\cot t\quad \rightarrow \quad \cot t = -\frac{ma}{b}.`
231. [Ellipse / Tangent slope as parameter] 
   `\cos t = \frac{\cot t}{\pm\sqrt{1 + \cot^2t}} = \frac{-ma}{\pm\sqrt{m^2 a^2 + b^2}}\ ,\quad\quad \sin t = \frac{1}{\pm\sqrt{1 + \cot^2t}} = \frac{b}{\pm\sqrt{m^2 a^2 + b^2}}.`
232. [Ellipse / Tangent slope as parameter] Replacing and of the standard representation yields:
   `\cos t`
233. [Ellipse / Tangent slope as parameter] Replacing and of the standard representation yields:
   `\sin t`
234. [Ellipse / General ellipse] An affine transformation of the Euclidean plane has the form , where is a regular matrix (with non-zero determinant) and is an arbitrary vector. If are the colu
   `(\cos(t), \sin(t))`
235. [Ellipse / General ellipse] An affine transformation of the Euclidean plane has the form , where is a regular matrix (with non-zero determinant) and is an arbitrary vector. If are the colu
   `0 \leq t \leq 2\pi`
236. [Ellipse / General ellipse] 
   `\vec x = \vec p(t) = \vec f\!_0 + \vec f\!_1 \cos t + \vec f\!_2 \sin t \, .`
237. [Ellipse / General ellipse] The four vertices of the ellipse are , for a parameter defined by:
   `\vec p(t_0),\;\vec p\left(t_0 \pm \tfrac{\pi}{2}\right),\; \vec p\left(t_0 + \pi\right)`
238. [Ellipse / General ellipse] 
   `\cot (2t_0) = \frac{\vec f\!_1^{\,2} - \vec f\!_2^{\,2}}{2\vec f\!_1 \cdot \vec f\!_2}.`
239. [Ellipse / General ellipse] 
   `\vec p\,'(t) = -\vec f\!_1\sin t + \vec f\!_2\cos t \ .`
240. [Ellipse / General ellipse] 
   `0 = \vec p'(t) \cdot \left(\vec p(t) -\vec f\!_0\right) = \left(-\vec f\!_1\sin t + \vec f\!_2\cos t\right) \cdot \left(\vec f\!_1 \cos t + \vec f\!_2 \sin t\right).`
241. [Ellipse / General ellipse] Expanding and applying the identities gives the equation for
   `\; \cos^2 t -\sin^2 t=\cos 2t,\ \ 2\sin t \cos t = \sin 2t\;`
242. [Ellipse / General ellipse] The area of an ellipse is
   `\;\vec x = \vec f_0 +\vec f_1 \cos t +\vec f_2 \sin t\;`
243. [Ellipse / General ellipse] 
   `A=\pi \left|\det(\vec f_1, \vec f_2)\right| .`
244. [Ellipse / General ellipse] Solving the parametric representation for by Cramer's rule and using , one obtains the implicit representation
   `\; \cos t,\sin t\;`
245. [Ellipse / General ellipse] Solving the parametric representation for by Cramer's rule and using , one obtains the implicit representation
   `\;\cos^2t+\sin^2t -1=0\;`
246. [Ellipse / General ellipse] : with
   `x^2+2cxy+d^2y^2-e^2=0\ ,`
247. [Ellipse / General ellipse] For one obtains a parametric representation of the standard ellipse rotated by angle :
   `\vec f_0= {0\choose 0},\;\vec f_1= a {\cos \theta\choose \sin \theta},\;\vec f_2= b{-\sin \theta\choose \;\cos \theta}`
248. [Ellipse / General ellipse] 
   `\begin{align} x &= x_\theta(t) = a\cos\theta\cos t - b\sin\theta\sin t \, , \\ y &= y_\theta(t) = a\sin\theta\cos t + b\cos\theta\sin t \, . \end{align}`
249. [Ellipse / Polar form relative to center] 
   `r(\theta) = \frac{ab}{\sqrt{(b \cos \theta)^2 + (a\sin \theta)^2}}=\frac{b}{\sqrt{1 - (e\cos\theta)^2}}`
250. [Ellipse / Polar form relative to focus] 
   `r(\theta)=\frac{a (1-e^2)}{1\pm e\cos\theta }`
251. [Ellipse / Polar form relative to focus] The angle is called the true anomaly of the point. The numerator is the semi-latus rectum.
   `\ell=a (1-e^2)`
252. [Ellipse / Eccentricity and the directrix property] Let , and assume is a point on the curve. The directrix has equation . With , the relation produces the equations
   `|PF|^2 = e^2|Pl|^2`
253. [Ellipse / Eccentricity and the directrix property] : and
   `(x - f)^2 + y^2 = e^2\left(x + \frac{f}{e}\right)^2 = (ex + f)^2`
254. [Ellipse / Eccentricity and the directrix property] : and
   `x^2\left(e^2 - 1\right) + 2xf(1 + e) - y^2 = 0.`
255. [Ellipse / Eccentricity and the directrix property] 
   `x^2\left(e^2 - 1\right) + 2px - y^2 = 0.`
256. [Ellipse / Eccentricity and the directrix property] If , introduce new parameters so that , and then the equation above becomes
   `1 - e^2 = \tfrac{b^2}{a^2}, \text{ and }\ p = \tfrac{b^2}{a}`
257. [Ellipse / Eccentricity and the directrix property] 
   `\left(x - f_1\right)^2 + \left(y - f_2\right)^2 = e^2 \frac{\left(ux + vy + w\right)^2}{u^2 + v^2}\ .`
258. [Ellipse / Definition of conjugate diameters] 
   `\vec x = \vec p(t) = \vec f\!_0 +\vec f\!_1 \cos t + \vec f\!_2 \sin t,`
259. [Ellipse / Definition of conjugate diameters] any pair of points belong to a diameter, and the pair belong to its conjugate diameter.
   `\vec p(t),\ \vec p(t + \pi)`
260. [Ellipse / Definition of conjugate diameters] any pair of points belong to a diameter, and the pair belong to its conjugate diameter.
   `\vec p\left(t + \tfrac{\pi}{2}\right),\ \vec p\left(t - \tfrac{\pi}{2}\right)`
261. [Ellipse / Definition of conjugate diameters] For the common parametric representation of the ellipse with equation one gets: The points
   `(a\cos t,b\sin t)`
262. [Ellipse / Definition of conjugate diameters] : (signs: (+,+) or (−,−) )
   `(x_1,y_1)=(\pm a\cos t,\pm b\sin t)\quad`
263. [Ellipse / Definition of conjugate diameters] : (signs: (−,+) or (+,−) )
   `(x_2,y_2)=({\color{red}{\mp}} a\sin t,\pm b\cos t)\quad`
264. [Ellipse / Theorem of Apollonios on conjugate diameters] :# The triangle with sides (see diagram) has the constant area , which can be expressed by , too. is the altitude of point and the angle between the half diamet
   `A_\Delta=\tfrac 1 2 c_2d_1=\tfrac 1 2 c_1c_2\sin\alpha`
265. [Ellipse / Theorem of Apollonios on conjugate diameters] :# The triangle with sides (see diagram) has the constant area , which can be expressed by , too. is the altitude of point and the angle between the half diamet
   `A_{el}=\pi ab=\pi c_2d_1=\pi c_1c_2\sin\alpha`
266. [Ellipse / Theorem of Apollonios on conjugate diameters] 
   `\vec p(t) = (a\cos t,\, b\sin t).`
267. [Ellipse / Theorem of Apollonios on conjugate diameters] The two points are on conjugate diameters (see previous section). From trigonometric formulae one obtains and
   `\vec c_1 = \vec p(t),\ \vec c_2 = \vec p\left(t + \frac{\pi}{2}\right)`
268. [Ellipse / Theorem of Apollonios on conjugate diameters] The two points are on conjugate diameters (see previous section). From trigonometric formulae one obtains and
   `\vec c_2 = (-a\sin t,\, b\cos t)^\mathsf{T}`
269. [Ellipse / de La Hire's point construction] The following construction of single points of an ellipse is due to de La Hire. K. Strubecker: Vorlesungen über Darstellende Geometrie. Vandenhoeck & Ruprecht, 
   `(a\cos t,\, b\sin t)`
270. [Ellipse / Steiner generation] : Given two pencils of lines at two points (all lines containing and , respectively) and a projective but not perspective mapping of onto , then the intersectio
   `\pi`
271. [Ellipse / Circles] : In order to measure the angle between two lines with equations one uses the quotient:
   `\frac{1 + m_1 m_2}{m_2 - m_1} = \cot\theta\ .`
272. [Ellipse / Ellipses] 
   `{\color{blue}q} = \frac{a^2}{b^2} = \frac{1}{1 - e^2},`
273. [Ellipse / Area] {{NumBlk2|| |2}}
   `A_\text{ellipse} = \pi ab`
274. [Ellipse / Area] where and are the lengths of the semi-major and semi-minor axes, respectively. The area formula is intuitive: start with a circle of radius (so its area is ) an
   `\pi a b`
275. [Ellipse / Area] where and are the lengths of the semi-major and semi-minor axes, respectively. The area formula is intuitive: start with a circle of radius (so its area is ) an
   `\pi b^2`
276. [Ellipse / Area] where and are the lengths of the semi-major and semi-minor axes, respectively. The area formula is intuitive: start with a circle of radius (so its area is ) an
   `\pi b^2(a/b) = \pi a b.`
277. [Ellipse / Area] The second integral is the area of a circle of radius that is, So
   `\pi a^2.`
278. [Ellipse / Area] 
   `A_\text{ellipse} = \frac{b}{a}\pi a^2 = \pi ab.`
279. [Ellipse / Area] An ellipse defined implicitly by has area
   `2\pi / \sqrt{4AC - B^2}.`
280. [Ellipse / Area] The area can also be expressed in terms of eccentricity and the length of the semi-major axis as (obtained by solving for flattening, then computing the semi-mi
   `a^2\pi\sqrt{1-e^2}`
281. [Ellipse / Area] thumb|The area enclosed by a tilted ellipse is <math>\pi\; y_\text{int}\, x_\text{max}</math>.
   `\pi\; y_\text{int}\, x_\text{max}`
282. [Ellipse / Area] {{NumBlk2|| |3}}
   `A_\text{ellipse} = \pi\; y_\text{int}\, x_\text{max} = \pi\; x_\text{int}\, y_\text{max}`
283. [Ellipse / Circumference] 
   `C \,=\, 4a\int_0^{\pi/2}\sqrt {1 - e^2 \sin^2\theta}\ d\theta \,=\, 4 a \,E(e)`
284. [Ellipse / Circumference] 
   `E(e) \,=\, \int_0^{\pi/2}\sqrt {1 - e^2 \sin^2\theta}\ d\theta`
285. [Ellipse / Circumference] 
   `\begin{align} \frac C{2\pi a} &= 1 - \left(\frac{1}{2}\right)^2e^2 - \left(\frac{1\cdot 3}{2\cdot 4}\right)^2\frac{e^4}{3} - \left(\frac{1\cdot 3\cdot 5}{2\cdot 4\cdot 6}\right)^2\frac{e^6}{5} - \cdots \\ &= 1 - \sum_{n=1}^\infty \left(\frac{(2n-1)!!}{(2n)!!}\right)^2 \frac{e^{2n}}{2n-1} \\ &= -\sum_{n=0}^\infty \left(\frac{(2n-1)!!}{(2n)!!}\right)^2 \frac{e^{2n}}{2n-1}, \end{align}`
286. [Ellipse / Circumference] 
   `\begin{align} \frac{C}{\pi(a+b)} &= \sum_{n=0}^\infty {\frac 12 \choose n}^2 h^n \\ &= \sum_{n=0}^\infty \left(\frac{(2n-3)!!}{(2n)!!}\right)^2 h^n \\ &= \sum_{n=0}^\infty \left(\frac{(2n-3)!!}{2^n n!}\right)^2 h^n \\ &= \sum_{n=0}^\infty \left(\frac{1}{(2n-1)4^n}\binom{2n}{n}\right)^2 h^n \\ &= 1 + \frac{h}{4} + \frac{h^2}{64} + \frac{h^3}{256} + \frac{25\,h^4}{16384} + \frac{49\,h^5}{65536} + \frac{441\,h^6}{2^{20}} + \frac{1089\,h^7}{2^{22}} + \cdots. \end{align}`
287. [Ellipse / Circumference] The coefficients are slightly smaller (by a factor of ), but also is numerically much smaller than except at and . For eccentricities less than 0.5 the error is
   `e^4/16 \le h \le e^4`
288. [Ellipse / Circumference] 
   `\frac C\pi \approx 3(a + b) - \sqrt{(3a + b)(a + 3b)} = 3(a + b) - \sqrt{3(a+b)^2 + 10ab}`
289. [Ellipse / Circumference] 
   `\frac C{\pi(a+b)} \approx 1+\frac{3h}{10+\sqrt{4-3h}},`
290. [Ellipse / Circumference] where takes on the same meaning as above. The errors in these approximations, which were obtained empirically, are of order and respectively. In particular, the
   `\pi(a+b)h^5\theta(h),`
291. [Ellipse / Circumference] where takes on the same meaning as above. The errors in these approximations, which were obtained empirically, are of order and respectively. In particular, the
   `22.888\cdot 10^{-6} < 3\cdot 2^{-17} < \theta(h) \le 4\left(1 - \frac{7\pi}{22}\right) < 1.60935\cdot10^{-3}`
292. [Ellipse / Circumference] quote=the relative error when 1}} and varies ... is bound by 0.00051227…}}.
   `4/''π'' − 14/11 {{=`
293. [Ellipse / Arc length] 
   `s = -b\int_{\arccos \frac{x_1}{a}}^{\arccos \frac{x_2}{a}} \sqrt{\ 1 + \left( \tfrac{a^2}{b^2} - 1 \right)\ \sin^2 z ~} \; dz ~.`
294. [Ellipse / Arc length] 
   `s = b\ \left[ \; E\left(z \;\Biggl|\; 1 - \frac{a^2}{b^2} \right) \; \right]^{\arccos \frac{x_1}{a}}_{z\ =\ \arccos \frac{x_2}{a}}`
295. [Ellipse / Arc length] 
   `\begin{align} 2\pi b &\le C \le 2\pi a\ , \\ \pi (a+b) &\le C \le 4(a+b)\ , \\ 4\sqrt{a^2+b^2\ } &\le C \le \sqrt{2\ } \pi \sqrt{a^2 + b^2\ } ~. \end{align}`
296. [Ellipse / Arc length] Here the upper bound is the circumference of a circumscribed concentric circle passing through the endpoints of the ellipse's major axis, and the lower bound is
   `\ 2\pi a\`
297. [Ellipse / Curvature] where e is the eccentricity.
   `R(\theta)=\frac{a^2}{b}\biggl(\frac{1-e^2(2-e^2)(\cos\theta)^2}{1-e^2(\cos\theta)^2}\biggr)^{3/2}\,,`
