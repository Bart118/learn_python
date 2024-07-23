#learn to store more complex data in binary files

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ['Claussen', 'Heinz', 'Vlassic']

f = open("pickles.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('\nUnpicking lists.')
f = open('pickles.dat', 'rb')
variety  = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print('\nshelving lists.')
s = shelve.open('pickles2.dat')

s['variety'] = ['sweet', 'hot', 'dill']
s['shape'] = ['whole', 'spear', 'chip']
s['brand'] = ['claussen', 'heinz', 'vlassic']

s.sync()  #make sure data is written

print('\nretrieving lists from a shelved file:')
print('brand -', s['brand'])
print('shape -', s['shape'])
print('variety -', s['variety'])

s.close()

input("\nPress the enter key to exit")
