counter = 1000
KMS = 100.00
name = "Mahesh"

print (counter)
print (KMS)
print (name)

print (name[2:4])
print ("Hi" + " " + name)

lstMr = ['1', 2, 3.4, 'wer']

print (lstMr)

tpl = {'asd', '1', 1, 4.5,0}
print (tpl)
print(lstMr[2])

d = {4:400, 7:567
}

d [1] = 100
d [2] = 'two'
d [3] = "threeeee"
d ['one'] = 86.4
d ["hunder"] = 1000000

print(d["hunder"])

print (d["hunder"] + 100 + lstMr[2])

if (d["hunder"] > 100) :
    print ("> 100")
if( d["hunder"] > 1000 and d['one']!=86.4 ):
    print ("> 1000")
else:
    print("In else")
    i = 0
    while d["hunder"] < 1000005:
        print("non ", d["hunder"], i)
        d["hunder"]=d["hunder"]+1
        print("Counter ", i) 
        i=(i+1)

import random

print ("Random samples..............")
print (random.choice(['1', 2, 3.4, 'wer']))
#print (random.choice({'asd', '1', 1, 4.5,0}))
#print ("rndm ", random.choice(d))
print (random.choice(['1', 2, 3.4, 'wer']))

print (lstMr)
lstMr[2] = 1500
print (lstMr)

print (d)

print ("Something : ", d[1], " later: ", d[2], " length: ", type(d))

print ("Something : ", d[1], " later: ", d[2], " length: ", type(d))

print ("Done till Dictionary in TutorialsPoint")