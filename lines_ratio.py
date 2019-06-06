from agn import calculation


name = 'data/spec-1070-52591-0072.fits'
name = 'data/spec-1369-53089-0157.fits'
name = 'data/spec-1995-53415-0214.fits'
#name = 'data/spec-2128-53800-0577.fits'
z = 0.00420765
z = 0.00267364 #1369
z = 0.022513 #1995
#z = 0.0165055 #2128
#name = 'data/spec-1369-53089-0157.fits'

T, Ne = calculation(name,z=z)
