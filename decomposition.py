from CMD.source import *

file_name = r'./result/CDI_20230202203930_CMD_20230203114952_WfrProp_20230712095123_CMD_20230712100346_WfrProp_20230713055401.h5'
file_name = wfr_CMD_cal(file_name, method = 'np_svd', num = 1000)
h5_wfr_show(file_name, n = (3,4), num = 1000)

# file_name = r'./result/CDI_20230202203930_CMD_20230203114952_WfrProp_20230216185111.h5'
# file_name = wfr_CMD_cal(file_name, method = 'np_svd', num = 1000)
