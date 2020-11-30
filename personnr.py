from random import randrange
from random import randint
from datetime import timedelta
from datetime import datetime

def random_date(start = datetime.strptime('1/1/1854', '%d/%m/%Y'), end = datetime.strptime('31/12/2039', '%d/%m/%Y')):
	return start + timedelta(days=randrange((end-start).days))

def random_individsifre(date):
	if datetime.strptime('1/1/1900', '%d/%m/%Y') <= date <= datetime.strptime('31/12/1999', '%d/%m/%Y'):
		return '{:03d}'.format(randint(0, 499))
	elif datetime.strptime('1/1/1854', '%d/%m/%Y') <= date <= datetime.strptime('31/12/1899', '%d/%m/%Y'):
		return '{:03d}'.format(randint(500, 749))
	else:
		return '{:03d}'.format(randint(500, 999))

def generate(date = random_date()):
	individsifre = random_individsifre(date)
	datestring = date.strftime('%d%m%y')
	d1 = int(datestring[0])
	d2 = int(datestring[1])
	m1 = int(datestring[2])
	m2 = int(datestring[3])
	y1 = int(datestring[4])
	y2 = int(datestring[5])
	i1 = int(individsifre[0])
	i2 = int(individsifre[1])
	i3 = int(individsifre[2])
	k1 = 11-((3*d1+7*d2+6*m1+m2+8*y1+9*y2+4*i1+5*i2+2*i3)%11) 
	if k1 == 10:
		return generate(date)
	if k1 == 11:
		k1 = 0
	k2 = 11-((5*d1+4*d2+3*m1+2*m2+7*y1+6*y2+5*i1+4*i2+3*i3+2*k1)%11)
	if k2 == 10:
		return generate(date)
	if k2 == 11:
		k2 = 0
	return '{}{}{}{}'.format(datestring,individsifre,k1,k2)	

print(generate())

