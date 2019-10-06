string1 = '브이넥 라이트 다운 베스트'
string2 = '    25,990원   '

# # 문자열 변환함수 : replace
# print(string1.replace('라이트', '헤비'))
# print(string1)
#
# string1 = string1.replace('라이트', '헤비')
# print(string1)

# 공백 제거 함수

print(string2)
print(string2.strip())
print(string2)

# string2 = string2.strip()
# string2 = string2.replace(',','')
# string2 = string2[:-1]
string2 = string2.strip().replace(',','')[:-1]

print(string2)

plusone = int(string2) + 1
print(plusone)