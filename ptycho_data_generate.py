from CMD.source import *
# from optics import *

sample_para = {
        'd_sd':                 10,         # sample to detector
        'xrange':               15e-6,
        'yrange':               15e-6,
        'upsampling_rate':      1,
        'range_enlarge_rate':   1
}

scanning_para = {
        'scanning_mode':        'z',
        'n_xscan':              10,
        'n_yscan':              10,
        'probe_size':           10e-6,
        'xstep_length':         1e-6,
        'ystep_length':         1e-6,
        'drift':                0
        }

beamstop_para = {
        'diameter':             -4e-3
        }

detector_para = {
        'type':                 'HPC',       # HPC/CCD/CMOS, HPC(Hybrid Photon Counting)
        'pixel_size':           75e-6,
        'n_pixel':              2048,
        'maximum_frame_rate':   100,       # (Hz)
        'maximum_count_rate':   1e7777777,       # (ph/s/pixel)
        'image_bit_depth':      32,          # (bits)
        'dark_noise':           0,
        'read_noise':           0,
        'poisson_noise':        0,
        'x_shift':              0,
        'y_shift':              0,
        'binning':              1,
        'efficiency':           0.108,
        'exposure_time':        0.1,      # (s)
        'frame_rate':           1         # (Hz)
        }


# optBL = optBL_generate()
file_name = r'./result/CDI_20230202203930_CMD_20230203114952_WfrProp_20230221174159_CMD_20230222094322.h5'
file_name = ptycho_diffration_generate(file_name, sample = 'sample1', sample_para = sample_para, detector_para = detector_para, scanning_para = scanning_para, beamstop_para = beamstop_para, n_wfr_arrays=20)
