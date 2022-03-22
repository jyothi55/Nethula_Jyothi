user_input=input("Enter a Phrase")
text=user_input.split()
acrnym=""
for i in text:
  acrnym=acrnym+str(i[0]).upper()
print(acrnym)