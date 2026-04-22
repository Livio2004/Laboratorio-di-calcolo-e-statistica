import math
import numpy as np



def media(x): #MEDIA
    m = 0.0
    for i in x:
        m += i # += incrementa la variabile somma di i
    m /= len(x) # /= divide la variabile m per len(x)
    return m

def devst(x): #DEVIAZIONE STANDARD
  s = 0.0
  N = len(x)
  m = np.mean(x)
  for i in x:
    s = s + (i-m)**2 #attenzione: potevo usare +=

  v = math.sqrt(s/(N-1))
  return v


def erroreStandardMedia(x): #ERRORE STANDARD DELLA MEDIA
  N = len(x)
  e = np.std(x)/math.sqrt(N)
  return e
