
"""

# **Satış Stratejisi için E-ticaret Veri Analizi**

**Amaç:**
Kmart, ABD'de önde gelen bir e-ticaret sitesidir ve yıllık satış inceleme toplantısının bir parçası
olarak, 2019'daki satış verilerinden elde edilen bilgilere dayanarak 2020 yılı satış stratejisine
karar vermeleri gerekir.Bu yüzden verilerin incelenip gerekli strateji belirlenecektir.

**Hedef:**
1. En iyi satış yapılan ay hangisidir? Ne kadar kazanılmıştır?
2. En çok satın alma yapan şehir hangisidir?
3. Görüntülü reklamcılık için en uygun zaman dilimine hangisidir?
4. En çok hangi ürünler sattı?
"""

import numpy as np
import pandas as pd

January = pd.read_csv("Sales_January_2019.csv")
February = pd.read_csv("Sales_February_2019.csv")
Marc = pd.read_csv("Sales_March_2019.csv")
April = pd.read_csv("Sales_April_2019.csv")
May = pd.read_csv("Sales_May_2019.csv")
June = pd.read_csv("Sales_June_2019.csv")
July = pd.read_csv("Sales_July_2019.csv")
August = pd.read_csv("Sales_August_2019.csv")
September = pd.read_csv("Sales_September_2019.csv")
October = pd.read_csv("Sales_October_2019.csv")
November = pd.read_csv("Sales_November_2019.csv")
December = pd.read_csv("Sales_December_2019.csv")

Month1 = pd.DataFrame(list(["january" for i  in range(len(January)) ]))
Month2 = pd.DataFrame(list(["February" for i  in range(len(February)) ]))
Month3 = pd.DataFrame(list(["Marc" for i  in range(len(Marc)) ]))
Month4 = pd.DataFrame(list(["April" for i  in range(len(April)) ]))
Month5 = pd.DataFrame(list(["May" for i  in range(len(May)) ]))
Month6 = pd.DataFrame(list(["June" for i  in range(len(June)) ]))
Month7 = pd.DataFrame(list(["July" for i  in range(len(July)) ]))
Month8 = pd.DataFrame(list(["August" for i  in range(len(August)) ]))
Month9 = pd.DataFrame(list(["September" for i  in range(len(September)) ]))
Month10 = pd.DataFrame(list(["October" for i  in range(len(October)) ]))
Month11 = pd.DataFrame(list(["November" for i  in range(len(November)) ]))
Month12 = pd.DataFrame(list(["December" for i  in range(len(December)) ]))

January["month"] = Month1
February["month"] = Month2
Marc["month"] = Month3
April["month"] = Month4
May["month"] = Month5
June["month"] = Month6
July["month"] = Month7
August["month"] = Month8
September["month"] = Month9
October["month"] = Month10
November["month"] = Month11
December["month"] = Month12

tumAylar = pd.concat([January,February,Marc,April,May,June,July,August,September,October,November,December])
tumAylar

newMonths = tumAylar.dropna()#boş değerleri sildim

newMonths = newMonths.sort_values("Quantity Ordered",ascending=False)#boş olmayan gereksiz değerleri bulmak için sıraladım.

newMonths = newMonths.reset_index()#silmek için değer reset index yaptım

for i in range(355):#355 e kadar olan gereksiz değerleri teker teker gezerek sildim.
    newMonths = newMonths.drop(index = i)
newMonths

newMonths = newMonths.reset_index()#son halini alması için tekrardan resetledim sıralanmış oldu.

newMonths

newMonths.drop(labels='level_0',axis=1,inplace=True)

newMonths['Quantity Ordered'] = newMonths['Quantity Ordered'].apply(pd.to_numeric, errors='coerce')#kolonlarda işlem yapabilmem için objeleri numerice çevirdik.
newMonths['Price Each'] = newMonths['Price Each'].apply(pd.to_numeric, errors='coerce')

newMonths.dtypes

newMonths.describe()

"""## **Hedefler**

# 1- En iyi satış yapılan ay hangisidir? Ne kadar kazanılmıştır?
"""

aylikToplam = newMonths.groupby("month").sum()

kazancHesapla= aylikToplam["Quantity Ordered"]*aylikToplam["Price Each"]
kazanc = pd.DataFrame(kazancHesapla,columns=["Kazanç Miktarı"]).sort_values("Kazanç Miktarı", ascending = False)

kazanc

kazanc.iloc[0].name

"""# 2- En çok satın alma yapan şehir hangisidir?"""

newMonths[["Bulvar","Sehir","Cadde"]]=newMonths["Purchase Address"].loc[newMonths["Purchase Address"].str.split(",").str.len()==3].str.split(",",expand=True)
newMonths.drop(labels=["Bulvar","Cadde"],axis=1,inplace=True)

ezFazlaSatınAlımYapanSehir = newMonths.groupby("Sehir").sum().sort_values("Quantity Ordered",ascending=False)
ezFazlaSatınAlımYapanSehir = pd.DataFrame(ezFazlaSatınAlımYapanSehir,columns=["Quantity Ordered"])
ezFazlaSatınAlımYapanSehir

ezFazlaSatınAlımYapanSehir.iloc[0]

"""# 3- Müşterilerin ürünleri satın alma olasılığını en üst düzeye çıkarmak için
#    görüntülü reklamcılık için en uygun zaman dilimine karar verin?
"""

newMonths[["Tarih","Zaman"]] = newMonths["Order Date"].loc[newMonths["Order Date"].str.split().str.len()==2].str.split(expand=True)

enUygunZamanDilimi = newMonths.groupby("Zaman").sum().sort_values("Quantity Ordered", ascending = False).head()
enUygunZamanDilimi

enUygunZamanDilimi.iloc[0].name

"""# 4- En çok hangi ürünler sattı?"""

enCokSatanUrun = newMonths.groupby("Product").sum().sort_values("Quantity Ordered", ascending = False)
enCokSatanUrun = pd.DataFrame(enCokSatanUrun, columns=["Quantity Ordered"])
enCokSatanUrun

enCokSatanUrun.iloc[0]

