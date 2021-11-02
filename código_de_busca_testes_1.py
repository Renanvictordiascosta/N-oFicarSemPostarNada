import re

numeros = """(98)0000-0000
(55)90000-0000
(77)90000-0000
(87)0000-0000
"""
print(re.findall("\(\d{2}\)\d{4,5}-\d{4}", numeros))

CEPs = """56094-676
65045-236
68904-076
65034-886
"""
print(re.findall("\d{5}-\d{3}", CEPs))

URLs = """https://www.quicolindo.com.br
https://www.coloquialissimamente.com.br
https://www.20comer70correr.com.br
https://www.paulobrificado.com.br
"""
print(re.findall("\w+://\w+\.\w+\.\w+5\.\w+", URLs))