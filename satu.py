total_belanja = int(input('Total belanja Almira: '))
ongkir = int(input('ongkir: '))
member = input('member premium (True/False): ') 
hari = input('Hari transaksi: ')

member = True if member == 'True' else False

if total_belanja >= 400000:
    promo_ongkir = 1.0
elif total_belanja >= 250000:
    promo_ongkir = 0.75
elif total_belanja >= 150000:
    promo_ongkir = 0.50
else:
    promo_ongkir = 0.0

bayar_ongkir = ongkir * (1-promo_ongkir)

if total_belanja >= 300000:
    cashback = 0.10
elif total_belanja >= 200000:
    cashback = 0.07
elif total_belanja >= 100000:
    cashback = 0.05
else:
    cashback = 0.0

if member:
    cashback += 0.03

if hari.lower() == 'sabtu':
    cashback += 0.03

if cashback > 0.15:
    cashback = 0.15

total_cashback = total_belanja * cashback
total_bayar = total_belanja + bayar_ongkir - total_cashback

print(f'\nPromo Ongkir: {promo_ongkir*100:.0f}%')
print(f'Ongkir: Rp{bayar_ongkir:,.0f}')
print(f'Cashback: {cashback*100:.0f}% = Rp{total_cashback:,.0f}')
print(f'Total Bayar: Rp{total_bayar:,.0f}')
