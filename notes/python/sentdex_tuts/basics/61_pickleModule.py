# Pickle Module

'''
' Pickle is a serialisation and de-serialisation module, basically it converts
' python modules to byte stream and back again.
' In other languages it is known as flattening, serilisation, marshling, etc.
' but in python its called pickling.
'
' Pickling is used to store python objects. This means things like lists,
' dictionaries, class objects, and more.
'
' Another application of pickling is If you have a large dataset, for example,
' and you're loading that massive data set into memory every time you run the
' program, it may make a lot of sense to just pickle it, and then load that
' instead, because it will be far faster, again by 50 - 100x, sometimes far
' more depending on the size.
'
' ATTENTION: pickle has no security features so when reading pickled objects
' make sure you can trust the source as you might recieve malicious code in
' pickled objects, especially when dealing with web services.
'''

import pickle

'''
# example data
example_dict = {1:"6", 2:"2", 3:"f"}

# pickle output file
pickle_out = open("dict.pickle", 'wb')

# dump/write the pickle
pickle.dump(example_dict, # what you wanna dump
            pickle_out) # where to dump it

pickle_out.close()
'''

# Open pickle file
pickle_in = open("dict.pickle", "rb")

# Load in the pickle data
example_dict = pickle.load(pickle_in)

print(example_dict)
