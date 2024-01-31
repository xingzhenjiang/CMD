from CMD.source import *
from CMD.optics.optics_KB2_part2 import optBL_generate



optBL = optBL_generate
file_name = r'./result/CDI_20230202203930_CMD_20230203114952_WfrProp_20230712095123_CMD_20230712100346.h5'
file_name = wfr_propagate(file_name, optBL_generate, n_wfr_arrays=100, n_vibration=10)
# h5_wfr_show(file_name, n = (2,3), num = 1000)
