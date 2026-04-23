for baris in range(5):
    for kolom in range(5):
        if baris == 2 or kolom == 2:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

for baris in range(5):
    for kolom in range(5):
        if baris == 0 or baris == 4 or kolom == 0 or kolom == 4:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()