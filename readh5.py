import h5py as h5
import numpy as np
import matplotlib.pyplot as plt

# arEx_arrays_new = np.zeros((10000, 22500), dtype = np.complex128)
file_name = r'./result/CDI_180000e_10keV_20221208143134_CMD_20221209183615.h5'

with h5.File(file_name, 'r') as file:
    coh_fraction = np.array(file['coherent_fraction'])
    print(coh_fraction.shape)

# unused, coh_fraction_sqrt, coh_mode = np.linalg.svd(arEx_arrays_new, full_matrices = False)
coh_fraction = coh_fraction/np.sum(coh_fraction)
coh_fraction_sum = np.zeros((len(coh_fraction),2), dtype =np.float32)
coh_fraction_new = np.zeros((len(coh_fraction),2), dtype =np.float32)
coh_fraction_new[:,0] = np.array(range(len(coh_fraction)))
coh_fraction_new[:,1] = coh_fraction
coh_fraction_sum[:,0] = np.array(range(len(coh_fraction)))
coh_fraction_sum[0,1] = coh_fraction_new[0,1]
for i in range(1, len(coh_fraction)):
    coh_fraction_sum[i,1] = coh_fraction_sum[i-1,1] + coh_fraction_new[i,1]

plt.plot(coh_fraction_new[:,0],coh_fraction_new[:,1])
plt.show()
np.savetxt('coh_fraction_new.txt',coh_fraction_new)
