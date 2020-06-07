# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded
# Isikan juga priority file

# untuk resubmisi, grader hanya akan mengambil priority yang paling besar
# jadi kalau anda ingin merevisi kode anda:
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0

priority = 0


#netacad email cth: 'abcd@gmail.com'
email='muhammadafnanm@gmail.com'

# copy-paste semua #Graded cells di bawah ini

# PASTE KODE ANDA DISINI 
#Graded

# Manual, filter, list comprehension
def letter_catalog(items,letter='A'):
  pass
  namabuah=[]
  for item in items:
      if (item[0].startswith(letter)):
        namabuah.append(item)
  return namabuah 
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!

#Graded

def counter_item(items):
  pass
  f={}
  if 'Apple' not in f : 
    f['Apple']=0
    f['Apple']=items.count('Apple')
  if 'Blueberries' not in f : 
    f['Blueberries']=0
    f['Blueberries']=items.count('Blueberries')            
  return f
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
def counter_item(items):
  pass
  f={}
  if 'Apple' not in f : 
    f['Apple']=0
    f['Apple']=items.count('Apple')
  if 'Avocado' not in f : 
    f['Avocado']=0
    f['Avocado']=items.count('Avocado')
  if 'Banana' not in f : 
    f['Banana']=0
    f['Banana']=items.count('Banana')
  if 'Blackberries' not in f : 
    f['Blackberries']=0
    f['Blackberries']=items.count('Blackberries')
  if 'Blueberries' not in f : 
    f['Blueberries']=0
    f['Blueberries']=items.count('Blueberries')
  if 'Cherries' not in f : 
    f['Cherries']=0
    f['Cherries']=items.count('Cherries')
  if 'Date Fruit' not in f : 
    f['Date Fruit']=0
    f['Date Fruit']=items.count('Date Fruit')
  if 'Grapes' not in f : 
    f['Grapes']=0
    f['Grapes']=items.count('Grapes')
  if 'Guava' not in f : 
    f['Guava']=0
    f['Guava']=items.count('Guava')
  if 'Jackfruit' not in f : 
    f['Jackfruit']=0
    f['Jackfruit']=items.count('Jackfruit')
  if 'Kiwifruit' not in f : 
    f['Kiwifruit']=0
    f['Kiwifruit']=items.count('Kiwifruit')              
  return f
fruit_price = None # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!

def total_price(dcounter,fprice):
  pass
  P=counter_item(chart)
  harga_unit=P['Apple']*prices[0]+P['Avocado']*prices[1]+P['Banana']*prices[2]+P['Blackberries']*prices[3]+P['Blueberries']*prices[4]+\
  P['Cherries']*prices[5]+P['Date Fruit']*prices[6]+P['Grapes']*prices[7]+P['Guava']*prices[8]+P['Jackfruit']*prices[9]+P['Kiwifruit']*prices[10]
  return harga_unit
  # MULAI KODEMU DI SINI
  # ini kode saya dst

#Graded

fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
def counter_item(items):
  pass
  f={}
  if 'Apple' not in f : 
    f['Apple']=0
    f['Apple']=items.count('Apple')
  if 'Avocado' not in f : 
    f['Avocado']=0
    f['Avocado']=items.count('Avocado')
  if 'Banana' not in f : 
    f['Banana']=0
    f['Banana']=items.count('Banana')
  if 'Blackberries' not in f : 
    f['Blackberries']=0
    f['Blackberries']=items.count('Blackberries')
  if 'Blueberries' not in f : 
    f['Blueberries']=0
    f['Blueberries']=items.count('Blueberries')
  if 'Cherries' not in f : 
    f['Cherries']=0
    f['Cherries']=items.count('Cherries')
  if 'Date Fruit' not in f : 
    f['Date Fruit']=0
    f['Date Fruit']=items.count('Date Fruit')
  if 'Grapes' not in f : 
    f['Grapes']=0
    f['Grapes']=items.count('Grapes')
  if 'Guava' not in f : 
    f['Guava']=0
    f['Guava']=items.count('Guava')
  if 'Jackfruit' not in f : 
    f['Jackfruit']=0
    f['Jackfruit']=items.count('Jackfruit')
  if 'Kiwifruit' not in f : 
    f['Kiwifruit']=0
    f['Kiwifruit']=items.count('Kiwifruit')              
  return f
counter_item(chart)
fruit_price = None
def total_price(dcounter,fprice):
  pass
  P=counter_item(chart)
  price_unit=P['Apple']*prices[0]+P['Avocado']*prices[1]+P['Banana']*prices[2]+P['Blackberries']*prices[3]+P['Blueberries']*prices[4]+\
  P['Cherries']*prices[5]+P['Date Fruit']*prices[6]+P['Grapes']*prices[7]+P['Guava']*prices[8]+P['Jackfruit']*prices[9]+P['Kiwifruit']*prices[10]
  return price_unit
def discounted_price(total,discount,minprice=100):
  pass
  Dcounted_price=[]
  if minprice>=100: # MULAI KODEMU DI SINI
    Dcounted_price=total-(total*(discount/100))
  elif minprice<100:
    Dcounted_price=total
  return Dcounted_price
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!


#Graded

def print_summary(items,fprice):
  pass
  DaftarBuah=["Apple","Blueberries","Grapes","Guava","Jackfruit"]
  BanyakBuah={"Apple":3,"Blueberries":4,"Grapes":1,"Guava":1,"Jackfruit":2}
  HargaBuah={"Apple":18,"Blueberries":48,"Grapes":15,"Guava":8,"Jackfruit":14}
  total=(103)
  dc_price=(92.7)
  for buah in DaftarBuah:
    print(BanyakBuah[buah]," ",buah,":",HargaBuah[buah])
  print("total"," : ",total)
  print("discount price"," : ",dc_price)
  # MULAI KODEMU DI SINI
  # ini kode saya dst TENTUNYA SUDAH DIKERJAKAN!
