# TODO Найдите количество книг, которое можно разместить на дискете
n_k = 100
n_ctr = 50
n_sim = 25
bait = 4
mbait = 1.44
all = n_k * n_ctr * n_sim * bait
perevod_1 = mbait * 1024 * 1024
number_book = int(perevod_1 // all)
print("Количество книг, помещающихся на дискету:", number_book)
