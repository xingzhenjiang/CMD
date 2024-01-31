mpiexec -n 41 python source_calculation.py
mpiexec -n 41 python propagation.py
python wfr_show.py
python decomposition.py
mpiexec -n 41 python ptycho_data_generate.py
python single_cal.py
