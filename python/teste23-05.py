import os

print ('Name of my terminal is:', os.ttyname(0))

f = open(os.ttyname(0))	# for reading                                                                               

print ('File object opened for reading from my terminal is:', f)

print ('Enter name of your favorite pet: ', end='',flush=True)

pet = f.readline()

f.close()

print ('Input from terminal was:', pet, end='')
print ('len(pet) =', len(pet))