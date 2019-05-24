import numpy as np
# Problem 2 (LLW tables)

sl_LLW = {
	'Misc' : [700, np.inf, np.inf], 
	'H-3' : [ 40, np.inf, np.inf],
	'Co-60' : [ 700, np.inf, np.inf ],
	'Ni-63' : [ 3.5, 70.0, 700.0 ],
	'Ni-63-A' : [35.0, 700.0, 7000.0 ],
	'Sr-90' : [0.04, 150.0, 7000.0 ],
	'Cs-137' : [1.0, 44.0, 4600.0]
}

ll_LLW = {
   'C-14' : 8,
   'C-14-A' : 80,
   'Ni-59-A' : 220,
   'Nb-94-A' : 0.2,
   'Tc-99' : 3.0,
   'Misc-Alpha' : 100.0,
   'Pu-241' : 3500.0,
   'Cm-242' : 20000.0
}

def search(a,b):
 try:
  k=a.index(b)
  return a[k] 
 except ValueError:
    return 'not found'

def SOF_class(isoAct, volume=1.0, wasteClass=0):
	SOF_SL = 0.0
	SOF_LL = 0.0
	
	for isotope in isoAct:
		if(isotope in sl_LLW):
			SOF_SL = SOF_SL + (isoAct[isotope]/volume)/sl_LLW[isotope][wasteClass]
		else:
			SOF_LL = SOF_LL + (isoAct[isotope]/volume)/ll_LLW[isotope]

	LLW_types = ['A','B','C','GTCC']
	LLW_string = 'Class {0:s}:\n'.format(LLW_types[wasteClass])
	
	if(SOF_SL > 0):
		LLW_string = LLW_string + \
			('Short-lived isotopes sum of fractions: {0:5.2f}\n').format(SOF_SL)
	if(SOF_LL > 0):
		LLW_string = LLW_string + \
		   ('Long-lived isotopes sum of fractions: {0:5.2f}\n').format(SOF_LL)
	print(LLW_string)
	
	if (SOF_SL > 1):
		wasteClass = SOF_class(isoAct, volume, (wasteClass+1))

	if (SOF_LL > 0.1):
		if (SOF_LL > 1):
			print(LLW_types[-1])
			return LLW_types[-1] #GTCC
		else:
			wasteClass = max(wasteClass,2)
	else:
		wasteClass = max(wasteClass,0)	
	return wasteClass

LLW_types = ['A','B','C','GTCC']
CI_TO_BQ = 3.7E10
	
LLW_1 = { 'H-3' : 30, 'Cs-137' : 50, 'Misc' : (450+300+5) }
LLW_2 = { 'Pu-241' : 4000, 'Misc-Alpha' : (450+700+650) }
LLW_5 = { 'C-14-A' : 1.665E12/CI_TO_BQ, 'Nb-94-A' : 5.55E9/CI_TO_BQ, 'Co-60' : 8.1E14/CI_TO_BQ}
print('LLW (part a): {0:s}\n***'.format(LLW_types[SOF_class(LLW_1)],1.0))
print('LLW (part b): {0:s}\n***'.format(LLW_types[SOF_class(LLW_2,100.0)])) # nCi / g
print('LLW (part e): {0:s}\n***'.format(LLW_types[SOF_class(LLW_5,10.0)]))

