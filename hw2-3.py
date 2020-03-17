
#######----1

# gunler = {"gun1":"pazartesi",
#           "gun2":"sali",
#           "gun3":"carsamba",
#           "gun4":"persembe",
#           "gun5":"cuma",
#           "gun6":"cumartesi",
#           "gun7":"pazar"}
#
# index = input("silmek istediginiz gunu yaziniz:")
# index_list= list(index)
#
# for i in index_list:
#     if i == "1":
#         del gunler["gun1"]
#     elif i == "2":
#         del gunler["gun2"]
#     elif i == "3":
#         del gunler["gun3"]
#     elif i == "4":
#         del gunler["gun4"]
#     elif i == "5":
#         del gunler["gun5"]
#     elif i == "6":
#         del gunler["gun6"]
#     elif i == "7":
#         del gunler["gun7"]
# print(*gunler.values())

############---2

aylar = [{"ocak":31},{"şubat":28},{"mart":31},{"nisan":30},{"mayıs":31},
         {"haziran":30},{"temmuz":31},{"ağustos":31},{"eylül":30},
         {"ekim":31},{"kasım":30},{"aralık":31}]

##########---3 (sanırım yanlış oldu sorunun ne demek istediğini anlayamadım)
new_aylar = []
for i in range(len(aylar)):
    new_aylar.append(aylar[i])
print(new_aylar)

##########----4
kış = []
ilkbahar = []
yaz = []
sonbahar = []

for i in aylar:
    if i == {'ocak': 31}:
        kış.append(i)
    if i == {'şubat': 28}:
        kış.append(i)
    if i == {'mart': 31}:
        ilkbahar.append(i)
    if i == {'nisan': 30}:
        ilkbahar.append(i)
    if i == {'mayıs': 31}:
        ilkbahar.append(i)
    if i == {'haziran': 30}:
        yaz.append(i)
    if i == {'temmuz': 31}:
        yaz.append(i)
    if i == {'ağustos': 31}:
        yaz.append(i)
    if i == {'eylül': 30}:
        sonbahar.append(i)
    if i == {'ekim': 31}:
        sonbahar.append(i)
    if i == {'kasım': 30}:
        sonbahar.append(i)
    if i == {'aralık': 31}:
        kış.append(i)
total = 0


for sub in yaz:
    for key in sub:
        total = total + sub[key]
print("yaz ayında",total,"gün vardır")











