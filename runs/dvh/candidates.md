# Candidates: math blocks carrying pi or e, from ten Wikipedia articles (DVH)

1. [Rotation matrix / ] 
   `R = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}\cdot`
2. [Rotation matrix / ] 
   `R\mathbf{v} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = x\begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix} + y\begin{bmatrix} -\sin \theta \\ \cos \theta \end{bmatrix} = \begin{bmatrix} x\cos\theta-y\sin\theta \\ x\sin\theta+y\cos\theta \end{bmatrix}.`
3. [Rotation matrix / ] If and are the coordinates of the endpoint of a vector with the length r and the angle with respect to the -axis, so that and , then the above equations become 
   `x = r \cos \phi`
4. [Rotation matrix / ] If and are the coordinates of the endpoint of a vector with the length r and the angle with respect to the -axis, so that and , then the above equations become 
   `y = r \sin \phi`
5. [Rotation matrix / ] If and are the coordinates of the endpoint of a vector with the length r and the angle with respect to the -axis, so that and , then the above equations become 
   `R\mathbf{v} = r\begin{bmatrix} \cos\phi\cos\theta-\sin\phi\sin\theta \\ \cos\phi\sin\theta+\sin\phi\cos\theta \end{bmatrix} = r\begin{bmatrix} \cos(\phi+\theta)\\ \sin(\phi+\theta) \end{bmatrix}.`
6. [Rotation matrix / In two dimensions] 
   `R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \\ \end{bmatrix}.`
7. [Rotation matrix / In two dimensions] 
   `\begin{bmatrix} x' \\ y' \\ \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \\ \end{bmatrix}\begin{bmatrix} x \\ y \\ \end{bmatrix}.`
8. [Rotation matrix / In two dimensions] 
   `\begin{align} x' &= x \cos\theta - y \sin\theta\, \\ y' &= x \sin\theta + y \cos\theta\, \end{align}.`
9. [Rotation matrix / Examples] 
   `\begin{bmatrix} \cos\theta \\ \sin\theta \\ \end{bmatrix},`
10. [Rotation matrix / Examples] 
   `\begin{bmatrix} -\sin\theta \\ \cos\theta \\ \end{bmatrix}.`
11. [Rotation matrix / Sense] R(\theta) . Thus the clockwise rotation matrix is found as (by replacing with and using the trigonometric symmetry of and )
   `\sin(-\theta) = - \sin(\theta)`
12. [Rotation matrix / Sense] R(\theta) . Thus the clockwise rotation matrix is found as (by replacing with and using the trigonometric symmetry of and )
   `\cos( - \theta) = \cos(\theta)`
13. [Rotation matrix / Sense] 
   `R(-\theta) = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \\ \end{bmatrix}.`
14. [Rotation matrix / Relationship with complex plane] (where corresponds to ) is a ring isomorphism from this ring to the field of the complex numbers (incidentally, this shows that this ring is a field). Under thi
   `\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \\ \end{bmatrix} = \cos t \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \sin t \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}`
15. [Rotation matrix / Relationship with complex plane] = \cos t \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \sin t \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} correspond to the circle of the unit complex number
   `\cos t^2 + \sin t^2 = 1`
16. [Rotation matrix / Relationship with complex plane] = \cos t \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \sin t \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} correspond to the circle of the unit complex number
   `e^{it} = \cos t + i\sin t = \cos t \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \sin t \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{pmatrix}\cos t&-\sin t\\ \sin t&\cos t\end{pmatrix}`
17. [Rotation matrix / Basic 3D rotations] A basic 3D rotation (also called elemental rotation) is a rotation about one of the axes of a coordinate system. The following three basic rotation matrices rot
   `sin ''θ''`
18. [Rotation matrix / Basic 3D rotations] 
   `\begin{alignat}{1} R_x(\theta) &= \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos \theta & -\sin \theta \\[3pt] 0 & \sin \theta & \cos \theta \\[3pt] \end{bmatrix} \\[6pt] R_y(\theta) &= \begin{bmatrix} \cos \theta & 0 & \sin \theta \\[3pt] 0 & 1 & 0 \\[3pt] -\sin \theta & 0 & \cos \theta \\ \end{bmatrix} \\[6pt] R_z(\theta) &= \begin{bmatrix} \cos \theta & -\sin \theta & 0 \\[3pt] \sin \theta & \cos \theta & 0 \\[3pt] 0 & 0 & 1 \\ \end{bmatrix} \end{alignat}`
19. [Rotation matrix / Basic 3D rotations] 
   `R_z(90^\circ) \begin{bmatrix} 1 \\ 0 \\ 0 \\ \end{bmatrix} = \begin{bmatrix} \cos 90^\circ & -\sin 90^\circ & 0 \\ \sin 90^\circ & \quad\cos 90^\circ & 0\\ 0 & 0 & 1\\ \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \\ \end{bmatrix} = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0\\ 0 & 0 & 1\\ \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \\ \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \\ 0 \\ \end{bmatrix}`
20. [Rotation matrix / General 3D rotations] 
   `\begin{align} R = R_z(\alpha) \, R_y(\beta) \, R_x(\gamma) &= \overset\text{yaw} {\begin{bmatrix} \cos \alpha & -\sin \alpha & 0 \\ \sin \alpha & \cos \alpha & 0 \\ 0 & 0 & 1 \\ \end{bmatrix}} \overset\text{pitch} {\begin{bmatrix} \cos \beta & 0 & \sin \beta \\ 0 & 1 & 0 \\ -\sin \beta & 0 & \cos \beta \\ \end{bmatrix}} \overset\text{roll} {\begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos \gamma & -\sin \gamma \\ 0 & \sin \gamma & \cos \gamma \\ \end{bmatrix}} \\ &= \begin{bmatrix} \cos\alpha\cos\beta & \cos\alpha\sin\beta\sin\gamma - \sin\alpha\cos\gamma & \cos\alpha\sin\beta\cos\gamma + \sin\alpha\sin\gamma \\ \sin\alpha\cos\beta & \sin\alpha\sin\beta\sin\gamma + \cos\alpha\cos\gamma & \sin\alpha\sin\beta\cos\gamma - \cos\alpha\sin\gamma \\ -\sin\beta & \cos\beta\sin\gamma & \cos\beta\cos\gamma \\ \end{bmatrix} \end{align}`
21. [Rotation matrix / General 3D rotations] 
   `\begin{align} \\ R = R_x(\alpha) \, R_y(\beta) \, R_z(\gamma) &= \overset\text{roll} {\begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos \alpha & -\sin \alpha \\ 0 & \sin \alpha & \cos \alpha \\ \end{bmatrix}} \overset\text{pitch} {\begin{bmatrix} \cos \beta & 0 & \sin \beta \\ 0 & 1 & 0 \\ -\sin \beta & 0 & \cos \beta \\ \end{bmatrix}} \overset\text{yaw} {\begin{bmatrix} \cos \gamma & -\sin \gamma & 0 \\ \sin \gamma & \cos \gamma & 0 \\ 0 & 0 & 1 \\ \end{bmatrix}} \\ &= \begin{bmatrix} \cos\beta\cos\gamma & -\cos\beta\sin\gamma & \sin\beta \\ \cos\alpha\sin\gamma + \sin\alpha\sin\beta\cos\gamma & \cos\alpha\cos\gamma - \sin\alpha\sin\beta\sin\gamma & -\sin\alpha\cos\beta \\ \sin\alpha\sin\gamma - \cos\alpha\sin\beta\cos\gamma & \sin\alpha\cos\gamma + \cos\alpha\sin\beta\sin\gamma & \cos\alpha\cos\beta \\ \end{bmatrix} \end{align}`
22. [Rotation matrix / Determining the angle] 
   `\operatorname{tr} (R) = 1 + 2\cos\theta ,`
23. [Rotation matrix / Determining the angle] 
   `|\theta| = \arccos\left(\frac{\operatorname{tr}(R) - 1}{2}\right).`
24. [Rotation matrix / Determining the angle] 
   `\left\{\begin{matrix} \cos \theta&=&\dfrac{\operatorname{tr}(R) - 1}{2}\\ \sin \theta&=&-\dfrac{\operatorname{tr}(K_n R)}{2} \end{matrix}\right.`
25. [Rotation matrix / Rotation matrix from axis and angle] 
   `R = \begin{bmatrix} u_x^2 \left(1-\cos \theta\right) + \cos \theta & u_x u_y \left(1-\cos \theta\right) - u_z \sin \theta & u_x u_z \left(1-\cos \theta\right) + u_y \sin \theta \\ u_x u_y \left(1-\cos \theta\right) + u_z \sin \theta & u_y^2\left(1-\cos \theta\right) + \cos \theta & u_y u_z \left(1-\cos \theta\right) - u_x \sin \theta \\ u_x u_z \left(1-\cos \theta\right) - u_y \sin \theta & u_y u_z \left(1-\cos \theta\right) + u_x \sin \theta & u_z^2\left(1-\cos \theta\right) + \cos \theta \end{bmatrix}.`
26. [Rotation matrix / Rotation matrix from axis and angle] 
   `R = (\cos\theta)\,I + (\sin\theta)\,[\mathbf u]_{\times} + (1-\cos\theta)\,(\mathbf{u}\otimes\mathbf{u}),`
27. [Rotation matrix / Rotation matrix from axis and angle] 
   `R_{jk}=\begin{cases} \cos^2\frac{\theta}{2}+\sin^2\frac{\theta}{2}\left(2u_j^2-1\right), \quad &\text{if }j=k\\ 2u_ju_k\sin^2\frac{\theta}{2}-\varepsilon_{jkl}u_l\sin\theta, \quad &\text{if }j\neq k \end{cases}`
28. [Rotation matrix / Rotation matrix from axis and angle] 
   `\mathbf{R} = \mathbf{I} + (\sin\theta) [\mathbf u]_{\times} + (1-\cos\theta)\bigl( [\mathbf u]_{\times}\bigr)^2.`
29. [Rotation matrix / Rotation matrix from axis and angle] 
   `R_{\mathbf{u}}(\theta)\mathbf{x}=\mathbf{u}(\mathbf{u}\cdot\mathbf{x})+\cos\left(\theta\right)(\mathbf{u}\times\mathbf{x})\times\mathbf{u}+\sin\left(\theta\right)(\mathbf{u}\times\mathbf{x})`
30. [Rotation matrix / Rotation matrix from axis and angle] 
   `R_{\mathbf{u}}(\theta)\mathbf{x}= \mathbf{x} \cos(\theta) + \mathbf{u}(\mathbf{x} \cdot \mathbf{u})(1- \cos(\theta)) - \mathbf{x} \times \mathbf{u} \sin{\theta}`
31. [Rotation matrix / Rotation matrix from axis and angle] 
   `(R_{\mathbf{u}}(\theta)\mathbf{x})_i = (R_{\mathbf{u}}(\theta))_{ij} {\mathbf{x}}_{j} \quad \text{with} \quad (R_{\mathbf{u}}(\theta))_{ij} = \delta_{ij}\cos(\theta) + \mathbf{u}_i\mathbf{u}_j (1- \cos(\theta)) - \sin{\theta} \varepsilon_{ijk} \mathbf{u}_{k}`
32. [Rotation matrix / Rotation matrix from axis and angle] 
   `R_{\mathbf{u}}(\theta)\boldsymbol{\alpha}= \cos\left(\theta\right) \boldsymbol{\alpha} + \sin\left(\theta\right) \boldsymbol{\beta}, \quad R_{\mathbf{u}}(\theta)\boldsymbol{\beta}= - \sin\left(\theta\right) \boldsymbol{\alpha} + \cos\left(\theta\right) \boldsymbol{\beta}, \quad R_{\mathbf{u}}(\theta)\mathbf{u}=\mathbf{u}.`
33. [Rotation matrix / Properties] The trace of a rotation matrix is equal to the sum of its eigenvalues. For 2}}, a rotation by angle has trace . For 3}}, a rotation around any axis by angle has
   `2 cos ''θ''`
34. [Rotation matrix / Properties] The trace of a rotation matrix is equal to the sum of its eigenvalues. For 2}}, a rotation by angle has trace . For 3}}, a rotation around any axis by angle has
   `1 + 2 cos ''θ''`
35. [Rotation matrix / Properties] The trace of a rotation matrix is equal to the sum of its eigenvalues. For 2}}, a rotation by angle has trace . For 3}}, a rotation around any axis by angle has
   `2(cos ''θ'' + cos ''φ'')`
36. [Rotation matrix / Properties] The trace of a rotation matrix is equal to the sum of its eigenvalues. For 2}}, a rotation by angle has trace . For 3}}, a rotation around any axis by angle has
   `4 cos ''θ''`
37. [Rotation matrix / Examples] :
   `Q = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \frac{\sqrt{3}}{2} & \frac12 \\ 0 & -\frac12 & \frac{\sqrt{3}}{2} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos 30^\circ & \sin 30^\circ \\ 0 & -\sin 30^\circ & \cos 30^\circ \\ \end{bmatrix}`
38. [Rotation matrix / Ambiguities] :
   `R(\theta) = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \\ \end{bmatrix}`
39. [Rotation matrix / Nested dimensions] 
   `Q_{3 \times 3} = \begin{bmatrix} \cos \theta & -\sin \theta & {\color{CadetBlue}0} \\ \sin \theta & \cos \theta & {\color{CadetBlue}0} \\ {\color{CadetBlue}0} & {\color{CadetBlue}0} & {\color{CadetBlue}1} \end{bmatrix}`
40. [Rotation matrix / Nested dimensions] 
   `Q_{2 \times 2} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix},`
41. [Rotation matrix / Nested dimensions] 
   `\begin{align} Q_{\mathbf{x}}(\theta) &= \begin{bmatrix} {\color{CadetBlue}1} & {\color{CadetBlue}0} & {\color{CadetBlue}0} \\ {\color{CadetBlue}0} & \cos \theta & -\sin \theta \\ {\color{CadetBlue}0} & \sin \theta & \cos \theta \end{bmatrix}, \\[8px] Q_{\mathbf{y}}(\theta) &= \begin{bmatrix} \cos \theta & {\color{CadetBlue}0} & \sin \theta \\ {\color{CadetBlue}0} & {\color{CadetBlue}1} & {\color{CadetBlue}0} \\ -\sin \theta & {\color{CadetBlue}0} & \cos \theta \end{bmatrix}, \\[8px] Q_{\mathbf{z}}(\theta) &= \begin{bmatrix} \cos \theta & -\sin \theta & {\color{CadetBlue}0} \\ \sin \theta & \cos \theta & {\color{CadetBlue}0} \\ {\color{CadetBlue}0} & {\color{CadetBlue}0} & {\color{CadetBlue}1} \end{bmatrix}, \end{align}`
42. [Rotation matrix / Nested dimensions] 
   `\begin{align} Q_\mathbf{u}(\theta) &= \begin{bmatrix} 0 & -z & y \\ z & 0 & -x \\ -y & x & 0 \end{bmatrix} \sin\theta + \left(I - \mathbf{u}\mathbf{u}^\mathsf{T}\right) \cos\theta + \mathbf{u}\mathbf{u}^\mathsf{T} \\[8px] &= \begin{bmatrix} \left(1 - x^2\right) c_\theta + x^2 & -z s_\theta - x y c_\theta + x y & y s_\theta - x z c_\theta + x z \\ z s_\theta - x y c_\theta + x y & \left(1 - y^2\right) c_\theta + y^2 & -x s_\theta - y z c_\theta + y z \\ -y s_\theta - x z c_\theta + x z & x s_\theta - y z c_\theta + y z & \left(1 - z^2\right) c_\theta + z^2 \end{bmatrix} \\[8px] &= \begin{bmatrix} x^2 (1 - c_\theta) + c_\theta & x y (1 - c_\theta) - z s_\theta & x z (1 - c_\theta) + y s_\theta \\ x y (1 - c_\theta) + z s_\theta & y^2 (1 - c_\theta) + c_\theta & y z (1 - c_\theta) - x s_\theta \\ x z (1 - c_\theta) - y s_\theta & y z (1 - c_\theta) + x s_\theta & z^2 (1 - c_\theta) + c_\theta \end{bmatrix}, \end{align}`
43. [Rotation matrix / Decomposition into shears] 
   `\begin{align} R(\theta) &{}= \begin{bmatrix} 1 & -\tan \frac{\theta}{2}\\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0\\ \sin \theta & 1 \end{bmatrix} \begin{bmatrix} 1 & -\tan \frac{\theta}{2}\\ 0 & 1 \end{bmatrix} \end{align}`
44. [Rotation matrix / Decomposition into shears] 
   `\begin{align} R(\theta) &{}= \begin{bmatrix} 1 & 0\\ \tan\theta & 1 \end{bmatrix} \begin{bmatrix} 1 & -\sin\theta\cos\theta\\ 0 & 1 \end{bmatrix} \begin{bmatrix} \cos\theta & 0\\ 0 & \frac{1}{\cos\theta} \end{bmatrix} \end{align}`
45. [Rotation matrix / Exponential map] Connecting the Lie algebra to the Lie group is the exponential map, which is defined using the standard matrix exponential series for For any skew-symmetric mat
   `exp(''A'')`
46. [Rotation matrix / Exponential map] 
   `e^{2A} - \frac{I+A}{I-A}=- \tfrac{2}{3} A^3 +\mathrm{O} \left(A^4\right) .`
47. [Rotation matrix / Exponential map] Conversely, a skew-symmetric matrix specifying a rotation matrix through the Cayley map specifies the same rotation matrix through the map .
   `exp(2 artanh ''A'')`
48. [Rotation matrix / Exponential map] 
   `\begin{align} \exp( A ) &= \exp\bigl(\theta(\mathbf{u}\cdot\mathbf{L})\bigr) \\ &= \exp \left( \begin{bmatrix} 0 & -z \theta & y \theta \\ z \theta & 0&-x \theta \\ -y \theta & x \theta & 0 \end{bmatrix} \right) \\ &= I + \sin \theta \ \mathbf{u}\cdot\mathbf{L} + (1-\cos \theta)(\mathbf{u}\cdot\mathbf{L} )^2 , \end{align}`
49. [Rotation matrix / Axis and angle] 
   `\begin{align} c &= \cos \theta\\ s &= \sin \theta\\ C &= 1-c \end{align}`
50. [Rotation matrix / Axis and angle] Determining an axis and angle, like determining a quaternion, is only possible up to the sign; that is, and correspond to the same rotation matrix, just like an
   `[[atan2]](sin ''θ'', cos ''θ'')`
51. [Rotation matrix / Voigt notation] 
   `T = \begin{bmatrix} \cos^2\theta & \sin^2\theta & 2\sin\theta\cos\theta \\ \sin^2\theta & \cos^2\theta & 2\sin\theta\cos\theta \\ -\sin\theta\cos\theta & \sin\theta\cos\theta & \cos^2\theta - \sin^2\theta \end{bmatrix} .`
52. [Rotation matrix / Uniform random rotation matrices] We sometimes need to generate a uniformly distributed random rotation matrix. It seems intuitively clear in two dimensions that this means the rotation angle is
   `{{sfrac|1|π`
53. [Rotation matrix / Uniform random rotation matrices] We sometimes need to generate a uniformly distributed random rotation matrix. It seems intuitively clear in two dimensions that this means the rotation angle is
   `0 ≤ ''θ'' ≤ π`
54. [Bloch sphere / Definition] : , where and .
   `|\psi\rangle = \cos\left(\theta /2\right) |0 \rangle \, + \, e^{i\phi} \sin\left(\theta /2\right) |1\rangle = \cos\left(\theta /2\right) |0 \rangle \, + \, (\cos\phi + i\sin\phi) \, \sin\left(\theta /2\right) |1\rangle`
55. [Bloch sphere / Definition] \cos\left(\theta /2\right) |0 \rangle \, + \, (\cos\phi + i\sin\phi) \, \sin\left(\theta /2\right) |1\rangle , where and .
   `0 \leq \theta \leq \pi`
56. [Bloch sphere / Definition] \cos\left(\theta /2\right) |0 \rangle \, + \, (\cos\phi + i\sin\phi) \, \sin\left(\theta /2\right) |1\rangle , where and .
   `0 \leq \phi < 2 \pi`
57. [Bloch sphere / Definition] :
   `\vec{a} = (\sin\theta \cos\phi,\; \sin\theta \sin\phi,\; \cos\theta) = (u, v, w)`
58. [Bloch sphere / Definition] :
   `\frac{1}{2}(\mathbb{I} + \vec a \cdot \vec \sigma) = \begin{pmatrix} \cos^2 \theta/2 & \sin \theta/2 ~ \cos\theta/2 ~e^{-i\phi} \\ \sin \theta/2 ~ \cos\theta/2 ~e^{i\phi} & \sin^2 \theta/2 \end{pmatrix}`
59. [Bloch sphere / Definition] acts on the state eigenvector with eigenvalue 1, so like a projection operator for it.
   `(\cos\theta/2, e^{i\phi} \sin\theta/2)`
60. [Bloch sphere / Cylindrical coordinates and Born probabilities] With , the probability of finding the state in a measurement in the standard basis depends linearly on the height: . By Archimedes' hat-box theorem, the project
   `z = \cos\theta`
61. [Bloch sphere / Cylindrical coordinates and Born probabilities] With , the probability of finding the state in a measurement in the standard basis depends linearly on the height: . By Archimedes' hat-box theorem, the project
   `|\langle 0|\psi\rangle|^2 = \cos^2\tfrac{\theta}{2} = \tfrac{1+z}{2}`
62. [Bloch sphere / Rotation operators about the Bloch basis] :
   `\begin{align} R_x(\theta) &= e^{(-i \theta X/2)} = \cos(\theta /2)I - i\sin(\theta/2)X = \begin{bmatrix} \cos \theta/2 & -i \sin \theta/2 \\ -i \sin \theta/2 & \cos \theta/2 \end{bmatrix} \\ R_y(\theta) &= e^{(-i \theta Y/2)} = \cos(\theta /2)I - i\sin(\theta/2)Y = \begin{bmatrix} \cos \theta/2 & -\sin \theta/2 \\ \sin \theta/2 & \cos \theta/2 \end{bmatrix} \\ R_z(\theta) &= e^{(-i \theta Z/2)} = \cos(\theta /2)I - i\sin(\theta/2)Z = \begin{bmatrix} e^{-i \theta/2} & 0 \\ 0 & e^{i \theta/2} \end{bmatrix} \end{align}`
63. [Bloch sphere / Rotations about a general axis] :
   `R_{\hat{n}}(\theta) = \exp\left(-i\theta\hat{n} \cdot \frac{1}{2}\vec{\sigma}\right)`
64. [Bloch sphere / Rotations about a general axis] :
   `\mathbf{q} = e^{\frac{1}{2}\theta(u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k})} = \cos \frac{\theta}{2} + (u_x\mathbf{i} + u_y\mathbf{j} + u_z\mathbf{k}) \sin \frac{\theta}{2}`
65. [Bloch sphere / Derivation of the Bloch rotation generator] :
   `U(s)=e^{iKs}.`
66. [Bloch sphere / Derivation of the Bloch rotation generator] :
   `R_{\hat{n}}(\theta)=\exp\left(-i\theta\,\hat{n}\cdot\vec{\sigma}/2\right).`
67. [Stokes parameters / Definitions] :
   `\begin{align} S_0 &= I \\ S_1 &= I p \cos 2\psi \cos 2\chi \\ S_2 &= I p \sin 2\psi \cos 2\chi \\ S_3 &= I p \sin 2\chi \end{align}`
68. [Stokes parameters / Properties] :
   `\begin{align} L & \equiv |L|e^{i2\theta} \\ & \equiv Q +iU. \\ \end{align}`
69. [Stokes parameters / Properties] :
   `\begin{align} L & \rightarrow e^{i2\theta'}L, \\ Q & \rightarrow \mbox{Re}\left(e^{i2\theta'}L\right), \\ U & \rightarrow \mbox{Im}\left(e^{i2\theta'}L\right).\\ \end{align}`
70. [Stokes parameters / Relation to the polarization ellipse] :
   `\begin{align} I_p & = A^2 + B^2, \\ Q & = (A^2-B^2)\cos(2\theta), \\ U & = (A^2-B^2)\sin(2\theta), \\ V & = 2ABh. \\ \end{align}`
71. [Stokes parameters / Measurement] 
   `\begin{align} I_l(0) &= \frac12 (I + Q)\\ I_l(\frac{\pi}4) &= \frac12 (I + U)\\ I_l(\frac{\pi}2) &= \frac12 (I - Q)\\ I_q(\frac{\pi}4) &= \frac12 (I + V),\\ \end{align}`
72. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] Generally, a linear polarization at angle θ has a pure quantum state ; therefore, the transmittance of a linear polarizer/analyzer at angle θ for a mixed state 
   `|\theta\rangle =\cos{\theta}|H\rangle+\sin{\theta}|V\rangle`
73. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] Generally, a linear polarization at angle θ has a pure quantum state ; therefore, the transmittance of a linear polarizer/analyzer at angle θ for a mixed state 
   `tr(\rho|\theta\rangle\langle\theta|) = \frac{1}{2}\left(1 + a_x \sin{2\theta} + a_z \cos{2\theta}\right)`
74. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] = \frac{1}{2}\left(1 + a_x \sin{2\theta} + a_z \cos{2\theta}\right) , with a maximum transmittance of at if , or at if ; the minimum transmittance of is reached
   `\theta_0 = \frac{1}{2}\arctan{ (a_x/a_z) }`
75. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] = \frac{1}{2}\left(1 + a_x \sin{2\theta} + a_z \cos{2\theta}\right) , with a maximum transmittance of at if , or at if ; the minimum transmittance of is reached
   `\theta_0 = \frac{1}{2}\arctan{ (a_x/a_z) }+\frac{\pi}{2}`
76. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] = \frac{1}{2}\left(1 + a_x \sin{2\theta} + a_z \cos{2\theta}\right) , with a maximum transmittance of at if , or at if ; the minimum transmittance of is reached
   `A\cos^2{(\theta- \theta_0)} + B`
77. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] = \frac{1}{2}\left(1 + a_x \sin{2\theta} + a_z \cos{2\theta}\right) , with a maximum transmittance of at if , or at if ; the minimum transmittance of is reached
   `a_x=DOLP\sin{2\theta_0}, \, a_z=DOLP\cos{ 2\theta_0}, \, DOLP=(ER-1)/(ER+1)`
78. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] It's also worth noting that a rotation of polarization axis by angle θ corresponds to the Bloch sphere rotation operator . For example, the horizontal polarizat
   `R_y (2\theta) = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}`
79. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] \end{bmatrix} . For example, the horizontal polarization state would rotate to . The effect of a quarter-wave plate aligned to the horizontal axis is described 
   `R_z (\pi /2)= \begin{bmatrix} e^{ -i\pi/4 } & 0 \\ 0 & e^{ +i\pi/4 } \end{bmatrix}`
80. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] The effect of a quarter-wave plate rotated by angle θ can be determined by Rodrigues' rotation formula as , with . The transmittance of the resulting light thro
   `R_n (\pi/2)=\frac{1}{\sqrt2}I-i\frac{1}{\sqrt2} (\hat{n} \cdot \vec{\sigma} )`
81. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] The effect of a quarter-wave plate rotated by angle θ can be determined by Rodrigues' rotation formula as , with . The transmittance of the resulting light thro
   `\hat{n}=\hat{z}\cos{2\theta}+\hat{x} \sin{2\theta}`
82. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] :
   `\begin{align} T&= tr[R_n(\pi/2) \rho R_n (- \pi/2)|H\rangle\langle H|] \\ &= \frac{1}{2}\left[ 1 + a_y \sin{2\theta} + (\hat{n}\cdot \vec{a}) \cos{2\theta}\right] \\ &= \frac{1}{2}\left[ 1 + a_y \sin{2\theta} + (a_x \sin{2\theta} + a_z \cos{2\theta}) \cos{2\theta}\right] \\ &= \frac{1}{2}\left( 1 + a_y \sin{2\theta} +DOLP\times \frac{\cos{(4\theta-2\theta_0) }+\cos{(2\theta_0) }}{2 }\right) \end{align}`
83. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] The above expression is the theory basis of many polarimeters. For unpolarized light, T=1/2 is a constant. For purely circularly polarized light, T has a sinuso
   `\theta_0=\frac{\pi}{2}`
84. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] The above expression is the theory basis of many polarimeters. For unpolarized light, T=1/2 is a constant. For purely circularly polarized light, T has a sinuso
   `T=\frac{1- \cos{(4\theta)}}{4}`
85. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] Similarly, the effect of a half-wave plate rotated by angle θ is described by , which transforms the density matrix to:
   `R_n (\pi)=-i(\hat{n} \cdot \vec{\sigma} )`
86. [Stokes parameters / Relationship to Hermitian operators and quantum mixed states] :
   `\begin{align} R_n(\pi) \rho R_n (-\pi) &= \frac{1}{2}\left(I+\vec{a}\cdot[-\vec{\sigma}+2\hat{n} (\hat{n}\cdot\vec{\sigma} )]\right) \\ &= \frac{1}{2}\left[I- \vec{a} \cdot \vec{\sigma}+2(\hat{n}\cdot\vec{a} ) (\hat{n}\cdot\vec{\sigma} )\right] \end{align}`
87. [Jones calculus / Jones vector] :
   `\begin{pmatrix} E_x(t) \\ E_y(t) \\ 0\end{pmatrix} = \begin{pmatrix} E_{0x} e^{i(kz- \omega t+\phi_x)} \\ E_{0y} e^{i(kz- \omega t+\phi_y)} \\ 0\end{pmatrix} =\begin{pmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \\ 0\end{pmatrix}e^{i(kz- \omega t)}.`
88. [Jones calculus / Jones vector] :
   `\begin{pmatrix} E_{0x} e^{i\phi_x} \\ E_{0y} e^{i\phi_y} \end{pmatrix}.`
89. [Jones calculus / Jones vector] Note that all Jones vectors and matrices in this article employ the convention that the phase of the light wave is given by , a convention used by Eugene Hecht.
   `=e^{i\pi/2}`
90. [Jones calculus / Jones vector] Note that all Jones vectors and matrices in this article employ the convention that the phase of the light wave is given by , a convention used by Eugene Hecht.
   `\pi/2`
91. [Jones calculus / Jones vector] Note that all Jones vectors and matrices in this article employ the convention that the phase of the light wave is given by , a convention used by Eugene Hecht.
   `=e^{0}`
92. [Jones calculus / Jones matrices] 
   `\begin{pmatrix} \cos^2(\theta) & \cos(\theta)\sin(\theta) \\ \cos(\theta)\sin(\theta) & \sin^2(\theta) \end{pmatrix}`
93. [Jones calculus / Phase retarders] For example, if the fast axis of a quarter waveplate is horizontal, then the phase velocity along the horizontal direction is ahead of the vertical direction i.
   `\phi_y = \phi_x + \pi/2`
94. [Jones calculus / Phase retarders] Quarter-wave plate with fast axis vertical {{refn|The prefactor appears only if one defines the phase delays in a symmetric fashion; that is, . This is done in 
   `{\rm e}^{i\pi/4}`
95. [Jones calculus / Phase retarders] Quarter-wave plate with fast axis vertical {{refn|The prefactor appears only if one defines the phase delays in a symmetric fashion; that is, . This is done in 
   `\phi_x = -\phi_y = \pi/4`
96. [Jones calculus / Phase retarders] 
   `{\rm e}^{\frac{i\pi}{4}} \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}`
97. [Jones calculus / Phase retarders] 
   `{\rm e}^{-\frac{i\pi}{4}} \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}`
98. [Jones calculus / Phase retarders] 
   `{\rm e}^{-\frac{i\pi}{4}} \begin{pmatrix} \cos^2\theta + i\sin^2\theta & (1 - i)\sin\theta \cos\theta \\ (1 - i)\sin\theta \cos\theta & \sin^2\theta + i\cos^2\theta \end{pmatrix}`
99. [Jones calculus / Phase retarders] 
   `\begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}`
100. [Jones calculus / Phase retarders] 
   `{\rm e}^{-\frac{i\pi}{2}} \begin{pmatrix} \cos^2\theta - \sin^2\theta & 2 \cos\theta \sin\theta \\ 2 \cos\theta \sin\theta & \sin^2\theta - \cos^2\theta \end{pmatrix}`
101. [Jones calculus / Phase retarders] 
   `{\rm e}^{-\frac{i\eta}{2}} \begin{pmatrix} \cos^2\theta + {\rm e}^{i\eta} \sin^2\theta & \left(1 - {\rm e}^{i\eta}\right) \cos\theta \sin\theta \\ \left(1 - {\rm e}^{i\eta}\right) \cos\theta \sin\theta & \sin^2\theta + {\rm e}^{i\eta} \cos^2\theta \end{pmatrix}`
102. [Jones calculus / Phase retarders] 
   `{\rm e}^{-\frac{i\eta}{2}} \begin{pmatrix} \cos^2\theta + {\rm e}^{i\eta} \sin^2\theta & \left(1 - {\rm e}^{i\eta}\right) {\rm e}^{-i\phi} \cos\theta \sin\theta \\ \left(1 - {\rm e}^{i\eta}\right) {\rm e}^{i\phi} \cos\theta \sin\theta & \sin^2\theta + {\rm e}^{i\eta} \cos^2\theta \end{pmatrix}`
103. [Jones calculus / Phase retarders] :
   `\begin{align} &{\rm e}^{-\frac{i\eta}{2}} \begin{pmatrix} \cos^2\theta + {\rm e}^{i\eta} \sin^2\theta & \left(1 - {\rm e}^{i\eta}\right) {\rm e}^{-i\phi} \cos\theta \sin\theta \\ \left(1 - {\rm e}^{i\eta}\right) {\rm e}^{i\phi} \cos\theta \sin\theta & \sin^2\theta + {\rm e}^{i\eta} \cos^2\theta \end{pmatrix} \\ &= \begin{pmatrix} \cos(\eta/2)-i\sin(\eta/2)\cos(2\theta) & -\sin(\eta/2)\sin(\phi)\sin(2\theta) - i \sin(\eta/2)\cos(\phi)\sin(2\theta) \\ \sin(\eta/2)\sin(\phi)\sin(2\theta) - i \sin(\eta/2)\cos(\phi)\sin(2\theta) & \cos(\eta/2)+i\sin(\eta/2)\cos(2\theta) \end{pmatrix} \end{align}`
104. [Jones calculus / Phase retarders] :
   `\left\{ {\rm e}^{i\gamma}\begin{pmatrix} \alpha & -\overline{\beta} \\ \beta & \overline{\alpha} \end{pmatrix}: \ \ \alpha,\beta \in \mathbb{C},\ \ |\alpha|^2 + |\beta|^2 = 1,\ \ \gamma \in [0,2\pi] \right\}`
105. [Jones calculus / Phase retarders] Note that for linear retarders, = 0 and for circular retarders, = ± /2, = /4. In general for elliptical retarders, takes on values between - /2 and /2.
   `\pi`
106. [Jones calculus / Axially rotated elements] : where
   `R(\theta ) = \begin{pmatrix} \cos \theta & \sin \theta \\ -\sin \theta & \cos \theta \end{pmatrix}.`
107. [Jones calculus / Axially rotated elements] :
   `\theta_\text{t} - \theta_\text{r} + \theta_\text{t'} - \theta_\text{r'} = \pm \pi`
108. [Jones calculus / Arbitrarily rotated elements] :
   `R_{3D}(\theta)=\begin{bmatrix} \cos\alpha\cos\beta & \cos\alpha\sin\beta\sin\gamma - \sin\alpha\cos\gamma & \cos\alpha\sin\beta\cos\gamma + \sin\alpha\sin\gamma \\ \sin\alpha\cos\beta & \sin\alpha\sin\beta\sin\gamma + \cos\alpha\cos\gamma & \sin\alpha\sin\beta\cos\gamma - \cos\alpha\sin\gamma \\ -\sin\beta & \cos\beta\sin\gamma & \cos\beta\cos\gamma \\ \end{bmatrix}`
109. [Great-circle distance / Formulae] 
   `\Delta\sigma = {\arccos}\bigl(\sin\phi_1\sin\phi_2 + \cos\phi_1\cos\phi_2\cos\Delta\lambda\bigr).`
110. [Great-circle distance / Relation between central angle and chord length] 
   `\begin{align} \Delta\sigma &= 2\arcsin \tfrac12 \Delta\sigma_\text{c} ,\\ \Delta\sigma_\text{c} &= 2\sin \tfrac12 \Delta\sigma . \end{align}`
111. [Great-circle distance / Computational formulae] Historically, the use of this formula was simplified by the availability of tables for the haversine function defined by and .
   `\operatorname{hav} \theta = \sin^2 \tfrac12\theta`
112. [Great-circle distance / Computational formulae] Historically, the use of this formula was simplified by the availability of tables for the haversine function defined by and .
   `\operatorname{archav} x = 2 \arcsin \sqrt{x}`
113. [Great-circle distance / Computational formulae] 
   `\begin{align}\Delta\sigma_\text{c}&=2\sqrt{\sin^2 \tfrac12 \Delta\phi + \cos{\phi_1} \cos{\phi_2} \sin^2\tfrac12 \Delta\lambda} \\ &=2\sqrt{\left(\sin \tfrac12\Delta \lambda\, \cos\tfrac12(\phi_1+\phi_2) \right)^2 + \left(\cos \tfrac12 \Delta \lambda\, \sin \tfrac12 \Delta \phi \right)^2} . \end{align}`
114. [Great-circle distance / Computational formulae] 
   `\begin{align} \Delta\sigma = {\operatorname{atan2}} \Bigl( & {\textstyle \sqrt{\left( \cos\phi_2\sin\Delta\lambda\right)^2 + \left(\cos\phi_1\sin\phi_2 - \sin\phi_1\cos\phi_2\cos\Delta\lambda \right)^2}}, \\ &\quad {\sin\phi_1\sin\phi_2 + \cos\phi_1\cos\phi_2\cos\Delta\lambda} \Bigr), \end{align}`
115. [Great-circle distance / Vector version] 
   `\begin{align} \Delta\sigma &= \arccos \left(\mathbf n_1 \cdot \mathbf n_2\right) \\[5mu] &= \arcsin \left| \mathbf n_1 \times \mathbf n_2 \right| \\ &= \arctan \frac{\left| \mathbf n_1 \times \mathbf n_2 \right|}{\mathbf n_1 \cdot \mathbf n_2} \\ \end{align}`
116. [Great-circle distance / From chord length] 
   `\begin{align} \Delta{X} &= \cos\phi_2\cos\lambda_2 - \cos\phi_1\cos\lambda_1,\\[3mu] \Delta{Y} &= \cos\phi_2\sin\lambda_2 - \cos\phi_1\sin\lambda_1,\\[3mu] \Delta{Z} &= \sin\phi_2 - \sin\phi_1,\\[3mu] \Delta\sigma_\text{c} &= \sqrt{(\Delta{X}){}^2 + (\Delta{Y}){}^2 + (\Delta{Z}){}^2}. \end{align}`
117. [Solar zenith angle / Formula] 
   `\cos \theta_s = \sin \alpha_s = \sin \Phi \sin \delta + \cos \Phi \cos \delta \cos h`
118. [Solar zenith angle / Formula] 
   `\cos \theta_s = \sin \Phi \sin \delta + \cos \Phi \cos \delta = \cos(\Phi - \delta)`
119. [Solar zenith angle / Derivation of the formula using the subsolar point and vector analysis] 
   `\mathbf{S}=\cos\phi_{s}\cos\lambda_{s}{\mathbf i}+\cos\phi_{s}\sin\lambda_{s}{\mathbf j}+\sin\phi_{s}{\mathbf k},`
120. [Solar zenith angle / Derivation of the formula using the subsolar point and vector analysis] 
   `\mathbf{V}_{oz}=\cos\phi_{o}\cos\lambda_{o}{\mathbf i}+\cos\phi_{o}\sin\lambda_{o}{\mathbf j}+\sin\phi_{o}{\mathbf k}.`
121. [Solar zenith angle / Derivation of the formula using the subsolar point and vector analysis] 
   `\cos\theta_{s} = \mathbf{S}\cdot\mathbf{V}_{oz} = \sin\phi_{o}\sin\phi_{s} + \cos\phi_{o}\cos\phi_{s}\cos(\lambda_{s}-\lambda_{o}).`
122. [Solar zenith angle / Minimum and Maximum] At any given location on any given day, the solar zenith angle, , reaches its minimum, , at local solar noon when the hour angle , or , namely, , or . If , it i
   `\cos\theta_\text{min} = \cos(|\phi_{o}-\phi_{s}|)`
123. [Solar zenith angle / Minimum and Maximum] And at any given location on any given day, the solar zenith angle, , reaches its maximum, , at local midnight when the hour angle , or , namely, , or . If , it
   `\cos\theta_\text{max} = \cos(180^{\circ}-|\phi_{o}+\phi_{s}|)`
124. [Solar zenith angle / Sunrise/Sunset] 
   `\cos h_0 = -\tan \Phi \tan \delta.`
125. [Solar zenith angle / Albedo] 
   `\overline{\cos \theta_s} = \frac{\displaystyle \int_{-h_0}^{h_0} Q \cos \theta_s \, \text{d}h}{\displaystyle \int_{-h_0}^{h_0} Q \, \text{d}h}`
126. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] Standard gravitational parameter
   `b v_\infty^2 \cot \theta_\infty`
127. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] (External) Angle between asymptotes
   `2 \cos^{-1}(-1/e)`
128. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] (External) Angle between asymptotes
   `2\pi + 2 \tan^{-1}(b/a)`
129. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] Angle between asymptotes and the conjugate axis of the hyperbolic path of approach
   `2\theta_\infty - \pi`
130. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] Angle between asymptotes and the conjugate axis of the hyperbolic path of approach
   `2\sin^{-1}\bigg(\frac{1}{(1 + r_pv_\infty^2/\mu)}\bigg)`
131. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] Impact parameter (semi-minor axis)
   `-a \sqrt{e^2-1}`
132. [Hyperbolic trajectory / Parameters describing a hyperbolic trajectory] Semi-latus rectum
   `a (1-e^2)`
133. [Hyperbolic trajectory / Eccentricity and angle between approach and departure] : or
   `\theta{_\infty}=\cos^{-1}(-1/e)\,`
134. [Hyperbolic trajectory / Eccentricity and angle between approach and departure] : or
   `e=-1/\cos\theta{_\infty}\,`
135. [Hyperbolic trajectory / Impact parameter and the distance of closest approach {{anchor|Impact parameter|Closest approach}}] : where is the angle the smaller body is deflected from a straight line in its course.
   `\mu=b v_\infty^2 \tan \delta/2`
136. [Hyperbolic trajectory / Impact parameter and the distance of closest approach {{anchor|Impact parameter|Closest approach}}] : where is the angle the smaller body is deflected from a straight line in its course.
   `\delta = 2\theta_\infty - \pi`
137. [Hyperbolic trajectory / Position] :
   `r = \frac{\ell}{1 + e\cdot\cos\theta}`
138. [Hyperbolic trajectory / Position] : &nbsp; &nbsp; or &nbsp; &nbsp; &nbsp; &nbsp; or &nbsp;
   `\cosh{E} = {{\cos{\theta} + e} \over {1 + e \cdot \cos{\theta}}}`
139. [Hyperbolic trajectory / Position] : &nbsp; &nbsp; or &nbsp; &nbsp; &nbsp; &nbsp; or &nbsp;
   `\tan \frac{\theta}{2} = \sqrt{\frac{e+1}{e-1}} \cdot \tanh \frac{E}{2}`
140. [Hyperbolic trajectory / Position] : &nbsp; &nbsp; or &nbsp; &nbsp; &nbsp; &nbsp; or &nbsp;
   `\tanh \frac{E}{2} = \sqrt{\frac{e-1}{e+1}} \cdot \tan \frac{\theta}{2}`
141. [Hyperbolic trajectory / Position] :
   `M = e \sinh E - E`
142. [Hyperbolic trajectory / Flight path angle] :
   `\tan(\phi) = \frac{e\cdot\sin\theta}{1 + e\cdot \cos\theta}`
143. [Hyperbolic trajectory / Deflection with finite sphere of influence] :
   `\delta = 2\arcsin\left( \frac{\sqrt{1 - \frac{p_e}{R_\text{SOI}}} \sqrt{1 + \frac{p_e}{R_\text{SOI}} - \frac{2 \mu p_e}{v_{\infty}^2 R_\text{SOI}^2}}}{1 + \frac{v_{\infty}^2 p_e}{\mu} - \frac{2 p_e}{R_\text{SOI}}} \right)`
144. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\frac{v}{c}=\tanh(s),`
145. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\sqrt{1-\frac{v^2}{c^2}}=\operatorname{sech}(s).`
146. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\begin{align} E &= \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}} = m c^2 \cosh(s) \\ p &= \frac{mv}{\sqrt{1-\frac{v^2}{c^2}}}=m c \sinh(s) \end{align}`
147. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\begin{align} m_1 \cosh(s_1)+m_2 \cosh(s_2) &= m_1 \cosh(s_3)+m_2 \cosh(s_4) \\ m_1 \sinh(s_1)+m_2 \sinh(s_2) &= m_1 \sinh(s_3)+m_2 \sinh(s_4) \end{align}`
148. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `m_1 e^{s_1}+m_2 e^{s_2}=m_1 e^{s_3}+m_2 e^{s_4}`
149. [Elastic collision / Relativistic derivation using hyperbolic functions] subtract squares both sides equations "momentum" from "energy" and use the identity after simplifying we get:
   `\cosh^2(s)-\sinh^2(s)=1,`
150. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `2 m_1 m_2 (\cosh(s_1) \cosh(s_2)-\sinh(s_2) \sinh(s_1)) = 2 m_1 m_2 (\cosh(s_3) \cosh(s_4)-\sinh(s_4) \sinh(s_3))`
151. [Elastic collision / Relativistic derivation using hyperbolic functions] for non-zero mass, using the hyperbolic trigonometric identity we get:
   `\cosh(a-b)=\cosh(a)\cosh(b)-\sinh(b)\sinh(a),`
152. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\cosh(s_1-s_2) = \cosh(s_3-s_4)`
153. [Elastic collision / Relativistic derivation using hyperbolic functions] as functions is even we get two solutions:
   `\cosh(s)`
154. [Elastic collision / Relativistic derivation using hyperbolic functions] from the last equation, leading to a non-trivial solution, we solve and substitute into the dependent equation, we obtain and then we have:
   `e^{s_1}`
155. [Elastic collision / Relativistic derivation using hyperbolic functions] from the last equation, leading to a non-trivial solution, we solve and substitute into the dependent equation, we obtain and then we have:
   `e^{s_2},`
156. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\begin{align} e^{s_1} &= e^{s_4}{\frac{m_1 e^{s_3}+m_2 e^{s_4}} {m_1 e^{s_4}+m_2 e^{s_3}}} \\ e^{s_2} &= e^{s_3}{\frac{m_1 e^{s_3}+m_2 e^{s_4}} {m_1 e^{s_4}+m_2 e^{s_3}}} \end{align}`
157. [Elastic collision / Relativistic derivation using hyperbolic functions] 
   `\begin{align} v_1/c &= \tanh(s_1) = {\frac{e^{s_1}-e^{-s_1}} {e^{s_1}+e^{-s_1}}} \\ v_2/c &= \tanh(s_2) = {\frac{e^{s_2}-e^{-s_2}} {e^{s_2}+e^{-s_2}}} \end{align}`
158. [Elastic collision / Relativistic derivation using hyperbolic functions] and after long transformation, with substituting:
   `e^{s_3}=\sqrt{\frac{c+u_1} {c-u_1}}`
159. [Elastic collision / Relativistic derivation using hyperbolic functions] and after long transformation, with substituting:
   `e^{s_4}=\sqrt{\frac{c+u_2}{c-u_2}},`
160. [Elastic collision / Two-dimensional] 
   `\tan \theta_1=\frac{m_2 \sin \theta}{m_1+m_2 \cos \theta},\qquad \theta_2=\frac{{\pi}-{\theta}}{2}.`
161. [Elastic collision / Two-dimensional] 
   `\begin{align} v'_1 &= v_1\frac{\sqrt{m_1^2+m_2^2+2m_1m_2\cos \theta}}{m_1+m_2} \\ v'_2 &= v_1\frac{2m_1}{m_1+m_2}\sin \frac{\theta}{2}. \end{align}`
162. [Elastic collision / Two-dimensional collision with two moving objects] 
   `\begin{align} v'_{1x} &= \frac{v_{1}\cos(\theta_1-\varphi)(m_1-m_2)+2m_2v_{2}\cos(\theta_2-\varphi)}{m_1+m_2}\cos(\varphi)+v_{1}\sin(\theta_1-\varphi)\cos(\varphi + \tfrac{\pi}{2}) \\[0.8em] v'_{1y} &= \frac{v_{1}\cos(\theta_1-\varphi)(m_1-m_2)+2m_2v_{2}\cos(\theta_2-\varphi)}{m_1+m_2}\sin(\varphi)+v_{1}\sin(\theta_1-\varphi)\sin(\varphi + \tfrac{\pi}{2}), \end{align}`
163. [Elastic collision / Two-dimensional collision with two moving objects] where and are the scalar sizes of the two original speeds of the objects, and are their masses, and are their movement angles, that is, (meaning moving directly
   `v_{1x} = v_1\cos\theta_1,\; v_{1y}=v_1\sin\theta_1`
164. [Mercator projection / Mathematics] 
   `x = R( \lambda - \lambda_0), \qquad y = R\, {\ln}\bigl({\tan} \bigl(\tfrac14\pi + \tfrac12\varphi \bigr) \bigr),`
165. [Mercator projection / Mathematics] where is an arbitrary scale factor which determines the size of the resulting map, is the natural logarithm, and is the trigonometric tangent function.
   `tan`
166. [Mercator projection / Cylindrical projections] Since the cylinder is tangential to the globe at the equator, the scale factor between globe and cylinder is unity on the equator but nowhere else. In particula
   `''R''&nbsp;cos&nbsp;''φ''`
167. [Mercator projection / Cylindrical projections] Since the cylinder is tangential to the globe at the equator, the scale factor between globe and cylinder is unity on the equator but nowhere else. In particula
   `{{sfrac|1|cos ''φ''`
168. [Mercator projection / Integral of the secant] 
   `x'(\lambda) = R, \qquad y'(\varphi) = R\sec\varphi,`
169. [Mercator projection / Integral of the secant] 
   `x(\lambda) = \int_{\lambda_0}^\lambda R\, du, \qquad y(\varphi) = \int_0^\varphi R\sec v\, dv.`
170. [Mercator projection / Integral of the secant] 
   `x = R( \lambda - \lambda_0), \qquad y = R \operatorname{gd}^{-1}(\varphi) = R\, {\ln}\bigl({\tan} \bigl(\tfrac14\pi + \tfrac12\varphi \bigr) \bigr).`
171. [Mercator projection / Complex logarithm] 
   `\begin{align} M(\lambda, \varphi) &= {\log} \bigl( e^{\lambda i}\, {\tan}\bigl(\tfrac14\pi - \tfrac12\varphi\bigr) \bigr) \\[3mu] &= {\log} \bigl( {\tan}\bigl(\tfrac14\pi - \tfrac12\varphi\bigr) \bigr) + \lambda i. \end{align}`
172. [Mercator projection / Inverse transformations] 
   `\lambda = \lambda_0 + \frac{x}{R}, \qquad \varphi = \operatorname{gd}\left(\frac{y}{R}\right) = 2\tan^{-1}\left(\exp\left(\frac{y}{R}\right)\right) - \frac{\pi}{2} .`
173. [Mercator projection / Alternative expressions] 
   `\begin{align} y/R = \operatorname{gd}^{-1}(\varphi) &= \sinh^{-1} (\tan \varphi), \\[5mu] \varphi = \operatorname{gd}(y/R) &= {\tan^{-1}}\bigl({\sinh(y/R)} \bigr), \end{align}`
174. [Mercator projection / Alternative expressions] where is the hyperbolic sine function. An alternative expression, valid throughout the complex plane, is
   `sinh`
175. [Mercator projection / Alternative expressions] 
   `\begin{aligned} y/R = \operatorname{gd}^{-1} \varphi &= {2\tanh^{-1}}\bigl({\tan\tfrac12 \varphi} \bigr), \\[5mu] \varphi = \operatorname{gd}(y/R) &= {2\tan^{-1}}\bigl({\tanh\tfrac12 (y/R)} \bigr), \end{aligned}`
176. [Mercator projection / Alternative expressions] where is the hyperbolic tangent function.
   `tanh`
177. [Mercator projection / Truncation and aspect ratio] 
   `\varphi = \tan^{-1}\left[\sinh\left(\frac{y}{R}\right)\right] = \tan^{-1}\left[\sinh\pi\right] \approx \tan^{-1}\left[11.5487\right] \approx 85.05113^\circ.`
178. [Mercator projection / Small element geometry] The relations between and properties of the projection, such as the transformation of angles and the variation in scale, follow from the geometry of correspondi
   `''R''(cos&nbsp;''φ'')''δλ''`
179. [Mercator projection / Small element geometry] 
   `\tan\alpha \approx \frac{R\cos\varphi\,\delta\lambda}{R\,\delta\varphi}, \qquad\qquad \tan\beta=\frac{\delta x}{\delta y},`
180. [Mercator projection / Small element geometry] * parallel scale factor &nbsp;&nbsp;&nbsp;&nbsp;
   `\quad k(\varphi)\;=\;\frac{P'M'}{PM}\;=\;\frac{\delta x}{R\cos\varphi\,\delta\lambda},`
181. [Mercator projection / Small element geometry] 
   `\tan\beta = \frac{R\sec\varphi}{y'(\varphi)} \tan\alpha\,,\qquad k = \sec\varphi\,,\qquad h = \frac{y'(\varphi)}{R}.`
182. [Mercator projection / Formulae for distance] For a ruler measurement of a short line, with midpoint at latitude&nbsp; , where the scale factor is }}:
   `1=''k''&nbsp;=&nbsp;sec&nbsp;''φ''&nbsp;=&nbsp;{{sfrac|1|cos&nbsp;''φ''`
183. [Mercator projection / Formulae for distance] .&nbsp;&nbsp;&nbsp;(short lines)}}
   `1=True distance = rhumb distance ≅ ruler distance × cos&nbsp;''φ'' / RF`
184. [Mercator projection / On other parallels] &nbsp;&nbsp;&nbsp; (parallel).}}
   `1=Parallel distance = ruler distance × cos&nbsp;''φ'' / RF`
185. [Mercator projection / On other parallels] This is not the shortest distance between the chosen endpoints on the parallel because a parallel is not a great circle. The difference is small for short dista
   `(''a''&nbsp;cos&nbsp;''φ'')&nbsp;''λ''`
186. [Mercator projection / On other parallels] This is not the shortest distance between the chosen endpoints on the parallel because a parallel is not a great circle. The difference is small for short dista
   `2(''a''&nbsp;cos&nbsp;''φ'')&nbsp;sin&nbsp;{{sfrac|''λ''|2`
187. [Mercator projection / On other parallels] This is not the shortest distance between the chosen endpoints on the parallel because a parallel is not a great circle. The difference is small for short dista
   `2arcsin(cos&nbsp;''φ''&nbsp;sin&nbsp;{{sfrac|''λ''|2`
188. [Mercator projection / On other parallels] This is not the shortest distance between the chosen endpoints on the parallel because a parallel is not a great circle. The difference is small for short dista
   `2''a''&nbsp;arcsin(cos&nbsp;''φ''&nbsp;sin&nbsp;{{sfrac|''λ''|2`
189. [Mercator projection / On a meridian] 
   `m_{12} = a\left|\tan^{-1}\left[\sinh\left(\frac{y_1}{R}\right)\right] -\tan^{-1}\left[\sinh\left(\frac{y_2}{R}\right)\right]\right|,`
190. [Mercator projection / On a meridian] where may be calculated from the width of the map by }}. For example, on a map with the values of correspond to latitudes of and therefore the successive interv
   `1=''R''&nbsp;=&nbsp;{{sfrac|''W''|2''π''`
191. [Mercator projection / On a rhumb] A straight line on the Mercator map at angle to the meridians is a rhumb line. When }} or }} the rhumb corresponds to one of the parallels; only one, the equato
   `1=''α''&nbsp;=&nbsp;{{sfrac|''π''|2`
192. [Mercator projection / On a rhumb] A straight line on the Mercator map at angle to the meridians is a rhumb line. When }} or }} the rhumb corresponds to one of the parallels; only one, the equato
   `{{sfrac|3''π''|2`
193. [Mercator projection / On a rhumb] 
   `r_{12} = a\sec\alpha\,|\varphi_1 - \varphi_2| = a\,\sec\alpha\;\Delta\varphi.`
194. [Mercator projection / On a rhumb] 
   `r_{12} = a\sec\alpha\left|\tan^{-1}\sinh\left(\frac{y_1}{R}\right)-\tan^{-1}\sinh\left(\frac{y_2}{R}\right)\right|.`
195. [Mercator projection / Generalization to the ellipsoid] 
   `\begin{align} x &= R \left( \lambda - \lambda_0 \right) ,\\ y &= R \ln \left[\tan \left(\frac{\pi}{4} + \frac{\varphi}{2} \right) \left( \frac{1-e\sin\varphi}{1+e\sin\varphi}\right)^\frac{e}{2} \right] = R\left(\sinh^{-1}\left(\tan\varphi\right)-e\tanh^{-1}(e\sin\varphi)\right),\\ k &= \sec\varphi\sqrt{1-e^2\sin^2\varphi}. \end{align}`
196. [Coriolis force / Length scales and the Rossby number] The time, space, and velocity scales are important in determining the importance of the Coriolis force. Whether rotation is important in a system can be determi
   `f = 2 \omega \sin \varphi \`
197. [Coriolis force / Applied to the Earth] 
   `\omega \, v\ 2 \, \sin \phi`
198. [Coriolis force / Rotating sphere] 
   `\boldsymbol{ \Omega} = \omega \begin{pmatrix} 0 \\ \cos \varphi \\ \sin \varphi \end{pmatrix}\ , \mathbf{ v} = \begin{pmatrix} v_{\mathrm e} \\ v_{\mathrm n} \\ v_{\mathrm u} \end{pmatrix}\ ,`
199. [Coriolis force / Rotating sphere] 
   `\mathbf{a}_{\mathrm C } =-2\boldsymbol{\Omega} \times\mathbf{v}= 2\,\omega\, \begin{pmatrix} v_{\mathrm n} \sin \varphi-v_{\mathrm u} \cos \varphi \\ -v_{\mathrm e} \sin \varphi \\ v_{\mathrm e} \cos\varphi\end{pmatrix}\ .`
200. [Coriolis force / Rotating sphere] When considering atmospheric or oceanic dynamics, the vertical velocity is small, and the vertical component of the Coriolis acceleration ( ) is small compared 
   `v_e \cos\varphi`
201. [Coriolis force / Rotating sphere] where is called the Coriolis parameter.
   `f = 2 \omega \sin \varphi \,`
202. [Coriolis force / Inertial circles] where is the Coriolis parameter , introduced above (where is the latitude). The time taken for the mass to complete a full circle is therefore . The Coriolis pa
   `2 \Omega \sin \varphi`
203. [Coriolis force / Inertial circles] where is the Coriolis parameter , introduced above (where is the latitude). The time taken for the mass to complete a full circle is therefore . The Coriolis pa
   `2\pi/f`
204. [Coriolis force / Ballistic trajectories] 
   `A_\mathrm{X} = -2 \omega ( V_\mathrm{Y} \cos \theta_\mathrm{lat} \sin \phi_\mathrm{az} + V_\mathrm{Z} \sin \theta_\mathrm{lat} )`
205. [Coriolis force / Ballistic trajectories] 
   `A_\mathrm{Y} = 2 \omega ( V_\mathrm{X} \cos \theta_\mathrm{lat} \sin \phi_\mathrm{az} + V_\mathrm{Z} \cos \theta_\mathrm{lat} \cos \phi_\mathrm{az})`
206. [Coriolis force / Ballistic trajectories] 
   `A_\mathrm{Z} = 2 \omega ( V_\mathrm{X} \sin \theta_\mathrm{lat} - V_\mathrm{Y} \cos \theta_\mathrm{lat} \cos \phi_\mathrm{az})`
