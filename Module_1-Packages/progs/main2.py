from sys import path

path.append("..\\packages")

# imports from the extra dir
import extra.iota as iota

# imports from the good dir
import extra.good.alpha as alpha
import extra.good.beta as beta

# imports from the best dir
import extra.good.best.sigma as sigma
import extra.good.best.tau as tau

# imports from the ugly dir
import extra.ugly.omega as omega
import extra.ugly.psi as psi

print(iota.funI())

print(alpha.funA())
print(beta.funB())

print(sigma.funS())
print(tau.funT())

print(omega.funO())
print(psi.funP())
