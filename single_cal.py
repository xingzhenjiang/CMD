#-----------------------------------------------------------------------------#
# ©1995-2004 Xing Zhenjiang
#-----------------------------------------------------------------------------#

__authors__  = "Xing Zhenjiang"
__date__     = "date : 18.10.2022"
__version__  = "0.1"


"""
configure: The process of source construction.
"""

#-----------------------------------------------------------------------------#
# library

from CMD.source import *
import time

#-----------------------------------------------------------------------------#
# parameters

param_electron_RMS = {
        '_Iavg':                0.3,                # average current [A]
        '_e':                   3.0,                # energy [GeV]
        '_sig_e':               0.618e-03,          # RMS energy spread
        '_sig_x':               26.51e-06,          # horizontal RMS size [m]
        '_sig_x_pr':            3.36e-06,           # horizontal RMS divergence [rad]
        '_m_xx_pr':             0,                  # <(x-<x>)(x'-<x'>)> [m]
        '_sig_y':               4.941e-06,           # vertical RMS size [m]
        '_sig_y_pr':            1.803e-06,            # vertical RMS divergence [rad]
        '_m_yy_pr':             0                   # <(y-<y>)(y'-<y'>)> [m]
        }


param_undulator = {
        '_n':                   1,                  # harmonic number of magnetic field(Generally,the value is set to 1)
        '_h_or_v':              'v',                # magnetic field plane horzontal ('h') or vertical ('v')
        '_B':                   0,                  # magnetic field amplitude [T] (efficient if>0)
        '_K':                   0,             # K value (efficient if>0)
        '_n_harmonic':           5,                   # harmonic number of energy ((efficient if>0))  priority:_B>_K>_n_harmonic
        '_ph':                  0,                   # initial phase [rad]
        '_s':                   -1,                  # symmetry vs longitudinal position 1 - symmetric (B ~ cos(2*Pi*n*z/per + ph)) , -1 - anti-symmetric (B ~ sin(2*Pi*n*z/per + ph))
        '_a':                   1.0,                 # coefficient for transverse depenednce B*cosh(2*Pi*n*a*y/per)*cos(2*Pi*n*z/per + ph)
        "_per":                 0.02,               # period length [m]
        "_nPer":                225.0,              # number of periods (will be rounded to integer)
        }

para_calc_mesh = {
        '_eStart':               10000.0,             # initial value of photon energy (/time)
        '_eFin':                 10000.0,             # final value of photon energy (/time)
        '_ne':                   1,                   # number of points vs photon energy (/time)
        "_xStart":              -0.00045,            # initial value of horizontal position (/angle)
        "_xFin":                0.00045,             # final value of horizontal position (/angle)
        "_nx":                  150,                # number of points vs horizontal position (/angle)
        "_yStart":              -0.00045,            # initial value of vertical position (/angle)
        "_yFin":                0.00045,             # final value of vertical position (/angle)
        "_ny":                  150,                # number of points vs vertical position (/angle)
        "_zStart":              29.0,           # longitudinal position
        }

#-----------------------------------------------------------------------------#

_e_beam, _mag, _mesh = source_param_parse(param_electron_RMS, param_undulator, para_calc_mesh)
single_intensity_cal(_e_beam, _mag, _mesh, arPrecParSR = [1, 0.01, 0.0, 0.0, 50000, 1, 0.0])
single_part_traj_cal(_e_beam, _mag, arPrecParSR = [1,1,1,1,1,1,1,50000])

param_undulator = {
        '_n':                   1,                  # harmonic number of magnetic field(Generally,the value is set to 1)
        '_h_or_v':              'v',                # magnetic field plane horzontal ('h') or vertical ('v')
        '_B':                   0,                  # magnetic field amplitude [T] (efficient if>0)
        '_K':                   0,             # K value (efficient if>0)
        '_n_harmonic':           5,                   # harmonic number of energy ((efficient if>0))  priority:_B>_K>_n_harmonic
        '_ph':                  0,                   # initial phase [rad]
        '_s':                   -1,                  # symmetry vs longitudinal position 1 - symmetric (B ~ cos(2*Pi*n*z/per + ph)) , -1 - anti-symmetric (B ~ sin(2*Pi*n*z/per + ph))
        '_a':                   1.0,                 # coefficient for transverse depenednce B*cosh(2*Pi*n*a*y/per)*cos(2*Pi*n*z/per + ph)
        "_per":                 0.02,               # period length [m]
        "_nPer":                225.0,              # number of periods (will be rounded to integer)
        }

para_calc_mesh = {
        '_eStart':               10000.0,             # initial value of photon energy (/time)
        '_eFin':                 10000.0,             # final value of photon energy (/time)
        '_ne':                   1,                   # number of points vs photon energy (/time)
        "_xStart":              -0.00065625,            # initial value of horizontal position (/angle)
        "_xFin":                0.00065625,             # final value of horizontal position (/angle)
        "_nx":                  150,                # number of points vs horizontal position (/angle)
        "_yStart":              -0.00065625,            # initial value of vertical position (/angle)
        "_yFin":                0.00065625,             # final value of vertical position (/angle)
        "_ny":                  150,                # number of points vs vertical position (/angle)
        "_zStart":              35.0,           # longitudinal position
        }
_e_beam, _mag, _mesh = source_param_parse(param_electron_RMS, param_undulator, para_calc_mesh)
power_cal(_e_beam, _mag, _mesh, arPrecParSR = [1.0, 1, 0.0, 0.0, 50000])


mag_cal(_mag, [5000,5000,12000,0.005,0.005,6], arPrecParSR = [0,0,0,1])
# print(file_name)
# file_name = wfr_CMD_cal(file_name)
#-----------------------------------------------------------------------------#

# optBL = optBL_generate()
