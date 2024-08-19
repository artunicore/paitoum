VELOCIDADE_DA_LUZ=299792458 #m/s
VELOCIDADE_DO_SOM=343 #m/s

t = float(input('tempo(s):'))
dl = (t * VELOCIDADE_DA_LUZ) / 1000 #km

ds = (t*VELOCIDADE_DO_SOM) / 1000 

print(f'distacia perccorrida pela é {dl} km\n a distacia percorrida na veloxidade do som é {ds} km')
