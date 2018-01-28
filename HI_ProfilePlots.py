
"""
Some useful background here:

http://xxx.lanl.gov/abs/astro-ph/0005106



See
http://www.hs.uni-hamburg.de/DE/Ins/Per/Czesla/PyA/PyA/modelSuiteDoc/LyAProfile.html#example

class LyaTransmission(PyAstronomy.funcFit.onedfit.OneDFit)
    Lyman alpha transmission profile including Deuterium absorption

 ===== ============================= =====
 |  N     Hydrogen column density       /cm^2
 |  b     Doppler parameter             km/s
 |  Dfrac Deuterium fraction            --
 |  ===== ============================= =====

b = sqrt(2) * sigma

The Doppler parameter (corresponds to sqrt(2) times the velocity dispersion)
to model thermal line width [km/s]. The default is 10 km/s.

"""

from PyAstronomy import modelSuite as ms
import numpy as np
import matplotlib.pylab as plt
la = ms.LyaTransmission()
help(la)

print()
print(la.description())
print()

beta = 10.0
HIcolumndensity = 5e17

la["N"] = HIcolumndensity
la["b"] = beta
la["Dfrac"] = 1.5e-5


wvl = np.linspace(1213.,1218.,1000)
print('Wavelenghth range:', len(wvl), np.min(wvl), np.max(wvl))

print("Single transmission curve")

m = la.evaluate(wvl)

plt.title('HI Transmission: beta = ' + str(beta))
plt.xlabel('Wavelenght (Angstroms)')
plt.xlabel('Transmission')

plt.plot(wvl, m, 'b.-', label='HI: ' + str(HIcolumndensity))

plt.legend()
plt.savefig('Transmission_1.png')
plt.show()



# now look at the transmission as a funntion of beta and HI column density

print("unsaturated column density range")

wvl = np.linspace(1213,1218,1000)
Log10HIColumnDensity = np.linspace(10.0, 15.0, 11)
print('Log10(HI Column Density)[cgs]:', Log10HIColumnDensity)
HIColumnDensity = 10**Log10HIColumnDensity
print('HI Column Density [cgs]:', HIColumnDensity)


beta = 30.0
la["b"] = beta
for HI in HIColumnDensity:

    la["N"] = HI
    m = la.evaluate(wvl)

    plt.plot(wvl, m, 'b')

plt.plot(wvl, m, 'b', label='beta=' + str(beta))

print(np.min(wvl), np.max(wvl))
plt.title('HI Transmission (HI column density range (log10 = 10 - 15)')
plt.xlabel('Wavelenght (Angstroms)')
plt.ylabel('Transmission')

plt.legend()
plt.savefig('Transmission_2a.png')
plt.show()



print("unsaturated column density range: low beta")

Log10HIColumnDensity = np.linspace(10.0, 15.0, 11)
print('Log10(HI Column Density)[cgs]:', Log10HIColumnDensity)
HIColumnDensity = 10**Log10HIColumnDensity
print('HI Column Density [cgs]:', HIColumnDensity)


wvl = np.linspace(1213.,1218.,1000)
beta = 15.0
la["b"] = beta
for HI in HIColumnDensity:

    la["N"] = HI
    m = la.evaluate(wvl)

    plt.plot(wvl, m, 'b')

plt.plot(wvl, m, 'b', label='beta=' + str(beta))

print(np.min(wvl), np.max(wvl))
plt.title('HI Transmission (HI column density range (log10 = 10 - 15)')
plt.xlabel('Wavelenght (Angstroms)')
plt.ylabel('Transmission')

plt.legend()
plt.savefig('Transmission_2b.png')
plt.show()



print()
print('Full rnage inculding saturared opticall thick dample line profiles')
Log10HIColumnDensity = np.linspace(10.0, 22.0, 13)
print('Log10(HI Column Density)[cgs]:', Log10HIColumnDensity)
HIColumnDensity = 10**Log10HIColumnDensity
print('HI Column Density [cgs]:', HIColumnDensity)


wvl = np.linspace(1213.,1218.,1000)
beta = 30.0
la["b"] = beta
for HI in HIColumnDensity:

    la["N"] = HI
    m = la.evaluate(wvl)

    plt.plot(wvl, m, 'b')

plt.plot(wvl, m, 'b', label='beta=' + str(beta))

print(np.min(wvl), np.max(wvl))
plt.title('HI Transmission (HI column density range (log10 = 10 - 22)')
plt.xlabel('Wavelenght (Angstroms)')
plt.ylabel('Transmission')

plt.legend()
plt.savefig('Transmission_2c.png')
plt.show()



wvl = np.linspace(1215.67 - 50.0, 1215.67 + 50, 1000)
print(np.min(wvl), np.max(wvl), np.max(wvl), np.min(wvl))
beta = 30.0
la["b"] = beta
for HI in HIColumnDensity:

    la["N"] = HI
    m = la.evaluate(wvl)

    plt.plot(wvl, m, 'b')

# plot the label with call to the last plot in the loop
plt.plot(wvl, m, 'b', label='beta=' + str(beta))

print(np.min(wvl), np.max(wvl))
plt.title('HI Transmission (HI column density range (log10 = 10 - 22)')
plt.xlabel('Wavelenght (Angstroms)')
plt.ylabel('Transmission')

plt.xlim(1215.67 - 50.0, 1215.67 + 50.0)

plt.legend()
plt.savefig('Transmission_3.png')
plt.show()


betarange = np.linspace(5, 100, 21)
print(np.min(betarange), np.max(betarange), np.max(betarange),
      np.min(betarange))

HIcolumndensity = 1e20
la["N"] = HIcolumndensity
for beta in betarange:

    la["b"] = beta
    m = la.evaluate(wvl)

    plt.plot(wvl, m, 'b')

plt.plot(wvl, m, 'b', label='HI=' + str(HIcolumndensity))

print(np.min(wvl), np.max(wvl))
plt.title('HI Transmission (beta range 5 - 100 k/sec)')
plt.xlabel('Wavelenght (Angstroms)')
plt.ylabel('Transmission')

plt.xlim(1215.67 - 50.0, 1215.67 + 50.0)

plt.legend()
plt.savefig('Transmission_4.png')
plt.show()
