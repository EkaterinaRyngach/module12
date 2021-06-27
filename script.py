money=float(input("Введите сумму"))
per_cent={'ТКБ':5.6,'СКБ':5.9,'ВТБ':4.28,'СБЕР':4.0}
print(per_cent)
deposit=[round(money*per_cent['ТКБ']/100),round(money*per_cent['СКБ']/100),round(money*per_cent['ВТБ']/100),round(money*per_cent['СБЕР']/100)]
print(deposit)
deposit.sort(reverse=True)
print(deposit)
print("Максимальная сумма, котору вы можете зарботать - %d" %(deposit[0]))