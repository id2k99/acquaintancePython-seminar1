in_day = int(input())    # Проезжает машина за один день км
total = int(input())     # Всего километров
# ost = total - total//in_day
# print((in_day + ost) // in_day) # Ищем за сколько дней проедем всего километров
print((in_day + total - 1) // in_day) # Ищем за сколько дней проедем всего километров