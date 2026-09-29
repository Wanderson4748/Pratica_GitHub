velocidade = input("Você está dirigindo na rodovia, deseja andar a qual velocidade? Detalhe, tem um radar a 2 quilometros, pode digitar: ") # Velocidade Atual do Carro
velocidade = int(velocidade)
local_carro = 109 # Local em que o carro está na estrada

RADAR_2 = 85 # Velocidade máxima do radar 2
LOCAL_RADAR_2 = 110 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_2 = velocidade > RADAR_2
carro_passou_radar_2 = local_carro >= (LOCAL_RADAR_2 - RADAR_RANGE)
local_carro <= (LOCAL_RADAR_2 + RADAR_RANGE)
carro_multado_radar_2 = carro_passou_radar_2 and vel_carro_pass_radar_2

if carro_multado_radar_2:
    print("Velocidade do carro passou do radar 2")
    print("Carro multado em radar 2")
else:
    print("Você passou dentro da velocidade correta no radar!")