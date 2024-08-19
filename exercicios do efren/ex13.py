t_viagem = int(input())
vm_viagem = int(input())

consumo_gasosa_km_l = 12

dist_percorrida_km = t_viagem * vm_viagem

l_gasosa = dist_percorrida_km / consumo_gasosa_km_l


print(f'{l_gasosa:.3f}')