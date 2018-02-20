from cosmosis.datablock import option_section, names
from scipy.interpolate import interp1d
import numpy as np
import csv

mypipe = "moment"
cosmosis_dir = "output/"

def setup(options):
    #load in data/make up test data
    # fake_theta = np.linspace(0, 2*np.pi*(1./360), num=100)
    # fake_moment = []
    # for ft in fake_theta:
    #     fake_moment.append(2*ft)
    # err = 1

    section = "momentlike"
    data_dir = options[section, "data_dir"]
    data_name = options[section, "data_name"]
    filename = data_dir+data_name
    theta, moment, err = np.genfromtxt(filename, unpack=True)

    #the return defines config parameter for execute
    #return fake_theta, fake_moment, err
    return theta, moment, err

def execute(block,config):
    theta, moment, err = config
    like_name = names.likelihoods
    #pull in real data with config

    #theoretically computed
    theta_theo = block[mypipe, "theta"]
    moment_theo = block[mypipe, "moment"]

    with open('moments/theo.csv', 'w') as f:
        writer = csv.writer(f, delimiter = " ")
        writer.writerows(zip(theta_theo, moment_theo))

    #compute chi-sq
    #chi = (moment - moment_theo(theta))/err
    chi = (moment - moment_theo)/err

    dof = 2
    chi_sq = chi**2
    red_chi_sq = chi_sq.sum()/(chi.size-dof)

    likeli = -0.5*chi_sq.sum()

    print "\t\t\t red_chi_sq", "{:10.1f}".format(red_chi_sq), 
    print "   likelihood {:10.1f} ".format(likeli)
    #put chi-sq in block
    block[like_name, "MOMENTLIKE_LIKE"] = likeli
    return 0 

def cleanup(config):
    return 0



