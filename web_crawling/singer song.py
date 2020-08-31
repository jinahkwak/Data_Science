f= open("test.csv","w")

singer= ["박정현","임창정","BTS","아이유"]
song= ["꿈에","소주한잔","쩔어","에잇"]

for i in range(len(singer)):
    f.write(singer[i]+','+song[i]+"\n")

f.close()