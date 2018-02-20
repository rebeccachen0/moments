from cosmosis.datablock import option_section, names
from scipy.interpolate import interp1d
import numpy as np
import moment as m

mypipe = "moment"


def setup(options):
	section = option_section
	return 0

def execute(block, config):
	ell = block["shear_cl", "ell"]
	C_ell = block["shear_cl", "bin_1_1"]
	theta, moment = m.moment(ell, C_ell)
	block[mypipe, "theta"] = theta
	block[mypipe, "moment"] = moment
	return 0


def cleanup(config):
    return 0