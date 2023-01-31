import sys

lines = open(sys.argv[-1]).readlines()

score = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
		 'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

def part1():

	tmp_score, tmp = 0, ''

	for line in lines:

		line = line.replace('\n','')	
		length = len(line)
		half = int(length/2)

		first = line[:half]
		second = line[half:]

		#print(f'{first}-{second}')

		for letter in first:
			if letter in second:
				tmp = letter
				tmp_score+=score[tmp]
				#print(f'>{tmp}')
				break
			else:
				pass

	print(tmp_score)

def part2():

	tmp_score, tmp = 0, ''

	length = len(lines)
	third = int(length/3)

	for i in range(third):

		_3mod0 = lines[3*i]
		_3mod1 = lines[3*i+1]
		_3mod2 = lines[3*i+2]
		
		for letter in _3mod0:
			if letter in _3mod1:
				tmp = letter
				if letter in _3mod2:
					tmp_score+=score[tmp]
					break

	print(tmp_score)

if __name__=='__main__':
	part2()