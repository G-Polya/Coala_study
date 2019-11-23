print('BMI 계산기입니다.')
height = float(input('신장: '))
weight = float(input('몸무게: '))

BMI = (weight / (height ** 2)) * 10000

print('BMI: ', BMI)
