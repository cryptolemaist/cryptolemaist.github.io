p = 139285
q = 13859057

def half_to_send(halfk):
    return (p**halfk)%q

def half_to_one(halfk,halfk2):
    return (halfk2**halfk)%q

def unipadding(t):
    outp = []
    for j in t:
        j = j[2:]
        le = len(j)
        if le<=7:
            outp.append("0"+"0"*(7-le)+j)
        elif le<=11:
            outp.append("110"+"0"*(11-le)+j[:-7+le]+"10"+j[-7+le:])
        elif le<=16:
            outp.append("1110"+"0"*(16-le)+j[:-12+le]+"10"+j[-12+le:le-6]+"10"+j[le-6:])
        else:
            outp.append("11110"+"0"*(21-le)+j[:-17+le]+"10"+j[-17+le:le-11]+"10"+j[le-11:])
    return "".join(outp)

def uniunpadding(t):
    t = list(t)
    outp = []
    while True:
        if len(t)<8:
            break
        if t[0] == "0":
            b = "".join(t[1:8])
            outp.append(int("0b"+b,2))
            del t[:8]
        elif t[2] == "0":
            b = "".join(t[3:8]+t[10:16])
            outp.append(int("0b"+b,2))
            del t[:16]
        elif t[3] == "0":
            b = "".join(t[4:8]+t[10:16]+t[18:24])
            outp.append(int("0b"+b,2))
            del t[:24]
        else:
            b = "".join(t[5:8]+t[10:16]+t[18:24]+t[26:32])
            outp.append(int("0b"+b,2))
            del t[:32]
    return outp

def encode_d(t,k):
    outp = []
    t = map(ord,t)
    t = list(map(bin,t))
    t = unipadding(t)
    k = bin(k)[2:]
    while len(t)>len(k):
        k += k
    for i in range(len(t)):
        if t[i]==k[i]:
            outp.append("0")
        else:
            outp.append("1")
    return "".join(outp)

def decode_d(t,k):
    outp = []
    k = bin(k)[2:]
    while len(t)>len(k):
        k += k
    for i in range(len(t)):
        if t[i]==k[i]:
            outp.append("0")
        else:
            outp.append("1")
    t = "".join(outp)
    t = uniunpadding(t)
    outp = []
    for j in t:
        outp.append(chr(int(j)))
    return "".join(outp)

input_text0 = Element("input_text0")
output_text0 = Element("output_text0")

def sendkeyinout(*args):
    output_text0.element.innerText = half_to_send(int(input_text0.value))
    input_text0.clear()
    
input_text1 = Element("input_text1")
output_text1 = Element("output_text1")
input_text2 = Element("input_text2")

def keyinout(*args):
    output_text1.element.innerText = half_to_one(int(input_text1.value),int(input_text2.value))
    input_text1.clear()
    input_text2.clear()

input_text3 = Element("input_text3")
output_text2 = Element("output_text2")
input_text4 = Element("input_text4")

def eninout(*args):
    output_text2.element.innerText = encode_d(int(input_text3.value),int(input_text4.value))
    if output_text2.element.innerText.replace(" ","")=="":
        output_text2.element.innerText="..."
    input_text3.clear()
    input_text4.clear()
    
input_text5 = Element("input_text5")
output_text3 = Element("output_text3")
input_text6 = Element("input_text6")

def eninout(*args):
    output_text3.element.innerText = encode_d(int(input_text5.value),int(input_text6.value))
    if output_text3.element.innerText.replace(" ","")=="":
        output_text3.element.innerText="..."
    input_text5.clear()
    input_text6.clear()
