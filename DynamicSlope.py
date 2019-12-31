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

if __name__ == '__main__':
	td_lag = 0
	k_rz = 0.069
	t_min = 5
	t_max = 30
	t_air = 20
	Rz_min = 10
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
