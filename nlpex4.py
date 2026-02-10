from collections import Counter
from nltk.util import ngrams

text="""I like nlp.
      I like ml.
      I like python."""
tokens=text.split()
ug=Counter(tokens)
bg=Counter(ngrams(tokens,2))
tg=Counter(ngrams(tokens,3))

v=len(ug)
k=1

input=["I","like"]

nextwords=set(tokens)

scores={}

for word in nextwords:
	laplace=(bg[(input[1],word)]+1)/(ug[input[1]]+v)
      
      addk=(bg[(input[1],word)]+k)/(ug[input[1]]+k*v)
      
      
      if tg[(input[0],input[1],word)]>0:
            backoff=tg[(input[0],input[1],word)]/bg[(input[0],input[1])]
      elif bg[(input[1],word)]:
            backoff=bg[(input[1],word)]/ug[input[1]]
      else:
            backoff=ug[word]/sum(ug.values())

      i1,i2,i3=0.5,0.,0.2
                  
      if bg[(input[0],input[1])]>0:
                  tri=tg[(input[0],input[1],word)]/bg[(input[0],input[1])]
      else:
            tri=0
      if ug[input[1]]:
            bi=bg[(input[1],word)]/ug[input[1]]
      else:
            bi=0
      uni=ug[word]/sum(ug.values())
      
      interp=i1*tri+i2*bi+i3*uni
      
scores[word]=(laplace+addk+backoff+interp)/4
      
sugg=sorted(scores.items(),key=lambda x:x[1],reverse=True)[:3]
      
print("INPUT : ","".join(input))
print("next word sugg : ")
for w,p in sugg:
      print(w)
      
