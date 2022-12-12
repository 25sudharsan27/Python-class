import pickle
animalDict={"Cat":2,"Dog":7,"Lion":4,"Tiger":9,"Leopard":11,"Bear":8}
outfile=open("animals","wb")
pickle.dump(animalDict, outfile)

outfile.close()
fst=open("animals","rb")
data=pickle.load(fst)
print(data)