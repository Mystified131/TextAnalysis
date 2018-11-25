def text_processor(superman):
  setfin = []
  super = []
  wonder = {}
  super = superman.split()
  for x in range(len(super)):
    wonder[super[x]] = 1
 
  for elm in range(len(super)):
    if super[elm] not in setfin:
      setfin.append(super[elm])
    else:  
      wonder[super[elm]] += 1

  print("")
  print("how many:")
  replist2 = []
  totstr = ""
  for elm3 in wonder:
    repstr = str(wonder[elm3]/100) + ": " + elm3
    replist2.append(repstr)
  replist2.sort(reverse = True)
  for e in replist2:
    print(e)
    valstr = e[:4]
    vala = float(valstr)
    valb = vala * 100
    val = int(valb)
    for ex in range(val):
        astr = e[6:]
        totstr += astr + " "
  print("")
  print("reconstruct by word frequency:")    
  print(totstr)

inpi = input("Please enter a phrase made of letters or numbers: ")
inpi2 = inpi.lower()
inpi3 = ""
ctr = 0
for jar in inpi2:
  if inpi2[ctr].isalpha() or inpi2[ctr].isnumeric() or inpi2[ctr] == " ":
    inpi3 = inpi3 + jar
  ctr = ctr + 1

text_processor(inpi3)