from pylab import *

def sin_waves(data,times):
	f = fft(data)
	N = len(data)
	am = real(f[:(N/2)+1])
	bm = imag(f[:(N/2)+1])

	allsin = [bm[i] * sin(times*i) for i in range(len(bm))]
	allcos = [am[i] * cos(times*i) for i in range(len(am))]

	return allsin + allcos

def drawall(a):
	t = arange(0,pi*2,0.001)
	waves = sin_waves(a,t)
	figure()
	for x in waves:
		plot(x)

	figure()

	sumwaves = sum(waves,axis=0)
	plot(sumwaves)

data = [1,0,0,1,0,0,1]
plot(data)
drawall(data)

show()