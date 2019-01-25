def testaddition(a,b):
	c=a+b
	return c

def testDivision(a,b):
	c=0
	try:
		c=a/b
	except NameError:
		print("La variable numerateur ou denominateur n'a pas été définie.")
	except TypeError:
		print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
	except ZeroDivisionError:
		print("La variable denominateur est égale à 0.")
	return c

def testsoustraction(a,b):
	c=a-b
	return c


def testmultiplication(a,b):
	c=a*b
	return c

a=testaddition(1,2)
print(a)

b=testDivision(4,1)
print(b)

c=testsoustraction(4,1)
print(c)

d=testmultiplication(1,2)
print(d)
