# -*- coding: utf-8 -*-

import random
list = []

for x in range(65, 91):
	a = str(chr(x))
	list.append(a)
	
for x in range(97, 123):
	a = str(chr(x))
	list.append(a)
	
for x in range(10):
	list.append(str(x))

for x in range(200):
	s = ''
	for x in range(16):
		a = random.choice(list)
		s = s + a
	print (s)