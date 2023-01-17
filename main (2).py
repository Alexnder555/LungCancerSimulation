import random
import numpy as np
seq_length = 20
dna = ''.join(np.random.choice(('C', 'G', 'T', 'A'), seq_length))

DNA = [x for x in dna]  
rna = []
rna2 = rna
count = 0
letters = ["A", "U", "C", "G"]

gen = 0



RNA = str.maketrans("GCTA", "CGAU")
for dna in DNA:
  rna.append(dna.translate(RNA))
#print('RNA Sequence:', rna)




option = ["Insertion", "Deletion", "Substitution", "none"]

insertion = 0
deletion = 0
substitution = 0



question = input("are you a smoker? ")
print('DNA Sequence:', DNA)

while count < 10:
  if question == "yes":
    mutation = random.choices(option, weights = [0.20, 0.20, 0.20, 0.40])
    if "Insertion" in mutation :
      lettersrandom = random.choices(letters)
      lettersrandom = lettersrandom[0]
      positionrandom = random.randint(1, len(rna))
      print("Insertion of", lettersrandom ,"at position", positionrandom)
      rna.insert(positionrandom, lettersrandom)
      count = count + 1
      insertion = insertion + 1
      gen = gen + 1
      print("Generation", gen, rna)
      print("DNA Sequence A")
    elif "Deletion" in mutation:
      #lettersrandom = random.choices(letters)
      #lettersrandom = lettersrandom[0]
      deleterandom = random.randint(1, len(rna))
      print('Deletion of', rna[deleterandom], "at position", deleterandom )
      del rna[deleterandom]
      count = count + 1
      deletion = deletion + 1
      gen = gen + 1
      print("Generation", gen, rna)
      print("DNA Sequence A")
    elif "Substitution" in mutation:
      lettersrandom = random.choices(letters)
      lettersrandom = lettersrandom[0]
      subrandom = random.randint(1, len(rna))
      pos = rna[subrandom]
      print('Substitution of', lettersrandom, "for", pos ,"at position", subrandom)
      rna[subrandom] = lettersrandom
      count = count + 1
      substitution = substitution + 1
      gen = gen + 1
      print("Generation", gen, rna)
      print("DNA Sequence A")
    elif "none" in mutation:
      count = count + 1
      gen = gen + 1
      print("Generation", gen, rna)
      print("DNA Sequence A")
  else:
      mutation = random.choices(option, weights = [0.1, 0.10, 0.10, 0.70])
      if "Insertion" in mutation :
        lettersrandom = random.choices(letters)
        lettersrandom = lettersrandom[0]
        positionrandom = random.randint(1, len(rna))
        print("Insertion of", lettersrandom ,"at position", positionrandom)
        rna.insert(positionrandom, lettersrandom)
        count = count + 1
        insertion = insertion + 1
        gen = gen + 1
        print("Generation", gen, rna)
        print("DNA Sequence B")
      elif "Deletion" in mutation:
        #lettersrandom = random.choices(letters)
        #lettersrandom = lettersrandom[0]
        deleterandom = random.randint(1, len(rna))
        print('Deletion of', rna[deleterandom], "at position", deleterandom )
        del rna[deleterandom]
        count = count + 1
        deletion = deletion + 1
        gen = gen + 1
        print("Generation", gen, rna)
        print("DNA Sequence B")
      elif "Substitution" in mutation:
        lettersrandom = random.choices(letters)
        lettersrandom = lettersrandom[0]
        subrandom = random.randint(1, len(rna))
        pos = rna[subrandom]
        print('Substitution of', lettersrandom, "for", pos ,"at position", subrandom)
        rna[subrandom] = lettersrandom
        count = count + 1
        substitution = substitution + 1
        gen = gen + 1
        print("Generation", gen, rna)
        print("DNA Sequence B")
      elif "none" in mutation:
        count = count + 1
        gen = gen + 1
        print("Generation", gen, rna)
        print("DNA Sequence B")

total = insertion + deletion + substitution


print("total Number of mutation:", total)
if total > 5:
  print('Outlook: Your lung tissue cells are mutating rapidly. You unfortunately have developed lung cancer.')
else:
  print('Outlook: You do not have lung cancer.')
print("Number of Insertions:", insertion)
print("Number of Deletion:", deletion)
print("Number of Substitutions:", substitution)

  