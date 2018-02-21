import numpy as np
import healpy as hp
import astropy.io.fits as pf
import astropy.stats as stat

kappa = pf.open('y1a1_spt_mcal_6_kE.fits')[1].data['kE']
jkid = pf.open('y1a1_spt_mcal_6_mask_jk.fits')[1].data['jk']

ids = []
for i in range(len(jkid)):
    wo_num = []
    for j in range(len(jkid)):
        if jkid[j] != i:
            wo_num.append(kappa[j])
    ids.append(wo_num)

print(ids)

