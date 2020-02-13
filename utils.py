# utils.py
# Math library


from scipy.integrate import quad

def fact(n):
	if n < 0:
		raise ValueError
	Result = 1
	for i in range(1, (n)):
		Result = Result * (i + 1)
	return Result

def roots(a, b, c):
	delta = (b ** 2) - 4 * (a * c)
	try:
		x1 = (-b + (delta ** (1/2))) / (2 * a)
		x2 = (-b - (delta ** (1/2))) / (2 * a)
	except:
		return ()
	if x1 == x2:
		return (x1)
	return (x1, x2)

def integrate(function, lower, upper):
	def f(x):
		return eval(function)
	Result2 = quad(f, lower, upper)
	Result = Result2[0]
	return Result
	

if __name__ == '__main__':
	print(fact(0))
	print(roots(1, 2, 2))
	print(integrate('2*x', -4, 2))
