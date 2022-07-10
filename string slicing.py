text = "X-DSPAM-Confidence:    0.8475"
numb = text.find(':')
bol = text[numb+1:]
rslt = float(bol)
print(rslt)
