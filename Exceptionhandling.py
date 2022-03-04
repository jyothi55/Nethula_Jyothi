s="cherry"
t=3
try:
    print(t+s)
except Exception as e:
    print(e)
finally:
    print("thi is final")