import os 
def Lr(td,td_lag,k_rz,t_min,t_max,Rz_min,Rz_max):
	if td <= td_lag:
		return Rz_min
	elif td > td_lag:
		return (td - td_lag) * k_rz + Rz_min
	elif ((td - td_lag) * k_rz + Rz_min) > Rz_max:
		return Rz_max

def td(t_min, t_max, t_air):
	if t_min >= t_air:
		return 0
	elif t_air > t_min and t_air < t_max:
		return t_air - t_min
	elif t_air >= t_max:
		return t_max - t_min

def Lnrd(zr, R0, R1, R2, R3):
	return R0 + R1 * zr + R2 * zr * zr + R3 * zr * zr * zr

def ET_c(kcb, ke, et0):
	return (kcb + ke) * et0

def S(h, h1, h2, h3, h4, T_pot, lr, lnrd):
	def gamma(h, h1, h2, h3, h4):
		if h >= h1 or h < h4:
			return 0
		elif h >= h2 and h < h1:
			return (h - h1) / (h2 - h1)
		elif h >= h3 and h < h2:
			return 1
		elif h >= h4 and h < h3:
			return (h - h4) / (h3 - h4)
	
	temp = gamma(h, h1, h2, h3, h4)
	return temp * (T_pot / lr) * lnrd


if __name__ == '__main__':
	td_lag = 0
	k_rz = 0.069
	t_min = 5
	t_max = 30
	t_air = 20
	Rz_min = 100
	Rz_max = 100
	R0 = 2.21
	R1 = -3.72
	R2 = 3.46
	R3 = -1.87
	zr = 0.5
	a = Lnrd(zr, R0, R1, R2, R3)
	td = td(t_min, t_max, t_air)
	c = Lr(td,td_lag,k_rz,t_min,t_max,Rz_min,Rz_max)
	print (a)
	print (td)
	print (c)
