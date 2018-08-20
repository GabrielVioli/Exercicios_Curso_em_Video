larg = float(input('Insira a largura da parede, em metros: '))
alt = float(input('Agora, insira a altura da parede, também em metros: '))
area = larg * alt
tinta = area / 2
print('A área da parede é {:.2f} m². Para pintar essa parede você precisará de {:.1f} litro(s) de tinta'. format(area, tinta))