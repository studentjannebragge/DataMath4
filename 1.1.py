import sympy as sp

# Määritellään muuttujat ja funktio
x, y = sp.symbols('x y')
T = x**2 * sp.exp(-y)

# Lasketaan gradientti, joka näyttää suurimman kasvunopeuden suunnan
grad_T = [sp.diff(T, var) for var in (x, y)]

# Piste, jossa gradientti lasketaan
point = {x: 2, y: 1}
grad_T_at_point = [component.evalf(subs=point) for component in grad_T]

# Gradientin suuruus (muutosnopeus suurimman kasvun suunnassa)
magnitude = sp.sqrt(sum(component**2 for component in grad_T)).evalf(subs=point)

print(f' gradiaani pisteessa: {grad_T_at_point}, \nMagnituri (muutosnopeus): {magnitude}')
