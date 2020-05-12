# Usei as PTFs de Saxton & Rawls 2006 para estimar água no solo para FC e WP
# Theta = Th

# Unidades de Medida:
#   C, S, e OM em decimal volume/volume
#   Th em vol/vol (valores decimais)
#   Potencial matricial em KPa
#   Plant Av. Water (PAW) = Th33 - Th1500

# valores de teste com base nas figuras do artigo. No caso, seria um solo classificado como 'sandy loam'.
# Consultar tabela 3 do artigo para conferir valores encontrados pelo estudo. Quano não há OM acredito que o valor seja substituido por 1, mas preciso confirmar.
S = 0.63
C = 0.10            # Aqui vai ter que vir o input dos mapas e a Mat Org do modelo
OM = 0.015

#   Water soil content @ -33 kPa (Field Capacity)

def water_content_fieldcap(S, C, OM):
    global Th33
    Th33t = -0.251*S + 0.195*C + 0.011*OM + 0.006*(S*OM) - 0.027*(C*OM) + 0.452*(S*C) + 0.299
    Th33 = Th33t + (1.283 * pow(Th33t, 2) - (0.374 * Th33t) - 0.015)
    fc_result = Th33

    print('Water content at field capacity:')
    print(fc_result)

#   Water soil content @ 0 kPa (Saturated)

def water_content_saturated(S, C, OM):
    ThS_minus_33t = 0.278*S + 0.034*C + 0.022*OM - 0.018*(S*OM) - 0.027*(C*OM) - 0.584*(S*C) + 0.078
    ThS_minus_33 =  ThS_minus_33t + (0.6360*ThS_minus_33t - 0.107)

    ThS = Th33 + ThS_minus_33 - 0.097*S + 0.043
    s_result = ThS

    print('Water content in saturated soil:')
    print(s_result)

#   Water soil content @ -1500 kPa (Wilting Point)

def water_content_wpoint(S, C, OM):
    Th1500t = -0.024*S + 0.487*C + 0.006*OM + 0.005*(S*OM) - 0.013*(C*OM) + 0.068*(S*C) + 0.031
    Th1500 = Th1500t + (0.14 * Th1500t - 0.02)
    wp_result = Th1500

    print('Water content at wilting point:')
    print(wp_result)


if __name__ == '__main__':
    water_content_wpoint(S,C,OM)
    water_content_fieldcap(S,C,OM)
    water_content_saturated(S,C,OM)
