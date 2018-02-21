from astropy.io import fits
import numpy as np

z, nz = np.genfromtxt("./data/nofz_mcal.txt", unpack=True)

primary = fits.PrimaryHDU()
a1 = np.array(z)
shift = a1[1] - a1[0]
a2 = a1 - shift
a3 = a1 + shift 
a4 = np.array(nz)
col1 = fits.Column(name='Z_LOW', format='D', array=a2)
col2 = fits.Column(name='Z_MID', format='D', array=a1)
col3 = fits.Column(name='Z_HIGH', format='D', array=a3)
col4 = fits.Column(name='BIN1', format='D', array=a4)

cols = fits.ColDefs([col1, col2, col3, col4])
hdu = fits.BinTableHDU.from_columns(cols, name = "NZ_SAMPLE")

hdu1 = fits.HDUList([primary, hdu])
hdu1.writeto('z_dist.fits')