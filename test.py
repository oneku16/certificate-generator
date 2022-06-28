from certificate import Certificate
from names import get_full_name
from random import randint as rd, choice as c

names = [get_full_name() for i in range(20)]
certificates = [rd(10000,99999) for i in range(20)]
organization = [c(["University of Cental Asia", "NATO", "QWEQWE wqe weq wqe weqeq"]) for i in range(20)]
results = [rd(50, 100) for i in range(20)]

# for i in range(20):
#     Certificate(names[i], certificates[i], organization[i], results[i]).draw_text()

Certificate("Vladimit Putin", 1945, "Kremls", 100).draw_text()




