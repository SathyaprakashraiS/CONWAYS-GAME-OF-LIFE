import random

def checksurround(z,x,c):
	revive=0
	alive=0
	if(z==0):
		revive=0
		if(x==0 and c!=width-1):
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				revive+=1
			if(gen1[x+1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				revive+=1
			if(gen1[x+1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				revive+=1
			if(gen1[x+1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				revive+=1
		if(x==0 and c==width-1):
			#print("here1")
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				revive+=1
			if(gen1[x+1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				revive+=1
		if(x==height-1 and c!=width-1):
			#print("here2")
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				revive+=1
			if(gen1[x-1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				revive+=1
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				revive+=1
			if(gen1[x-1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				revive+=1
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				revive+=1
		if(x==height-1 and c==width-1):
			#print("here3")
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				revive+=1
			if(gen1[x-1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				revive+=1
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				revive+=1
		if(x!=0 and x!=height-1 and c!=0 and c!=width-1):
			#print("here4")
			if(gen1[x-1][c]==1):
				#print("1")
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				revive+=1
			if(gen1[x-1][c+1]==1):
				#print("2")
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				revive+=1
			if(gen1[x][c+1]==1):
				#print("3")
				#print("in 3 value",gen1[x-1][c+1])
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				revive+=1
			if(gen1[x+1][c]==1):
				#print("4")
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				revive+=1
			if(gen1[x+1][c+1]==1):
				#print("5")
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				revive+=1
			if(gen1[x-1][c-1]==1):
				#print("6")
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				revive+=1
			if(gen1[x][c-1]==1):
				#print("7")
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				revive+=1
			if(gen1[x+1][c-1]==1):
				#print("8")
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				revive+=1
		if(x!=0 and c==0 and x!=height-1):
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				revive+=1
			if(gen1[x-1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				revive+=1
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				revive+=1
			if(gen1[x+1][c]==1):
				print("value:",z,"i:",x,"j:",c,x+1,c)
				revive+=1
			if(gen1[x+1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				revive+=1
		if(revive>=3):
			return 1
		else:
			return 0
	if(z==1):
		alive=0
		if(x==0 and c!=width-1):
			print("here0",x,c)
			#print("here5")
			if(gen1[x][c+1]==1):
				print("checked")
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				alive+=1
			if(gen1[x+1][c]==1):
				print("checked")
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				alive+=1
			if(gen1[x+1][c+1]==1):
				print("checked")
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				alive+=1
			if(gen1[x+1][c-1]==1):
				print("checked")
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				alive+=1
			if(gen1[x][c-1]==1):
				print("checked")
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				alive+=1
		if(x==0 and c==width-1):
			print("here1",x,c)
			#print("here6")
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				alive+=1
			if(gen1[x+1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				alive+=1
		if(x==height-1 and c!=width-1):
			print("here2",x,c)
			#print("here7")
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				alive+=1
			if(gen1[x-1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				alive+=1
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				alive+=1
			if(gen1[x-1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				alive+=1
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				alive+=1
		if(x==height-1 and c==width-1):
			print("here3",x,c)
			#print("here8")
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				alive+=1
			if(gen1[x-1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				alive+=1
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				alive+=1
		if(x!=0 and x!=height-1 and c!=0 and c!=width-1):
			print("here4",x,c)
			#print("here9")
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				alive+=1
			if(gen1[x-1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				alive+=1
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				alive+=1
			if(gen1[x+1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				alive+=1
			if(gen1[x+1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				alive+=1
			if(gen1[x-1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c-1)
				alive+=1
			if(gen1[x][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c-1)
				alive+=1
			if(gen1[x+1][c-1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				alive+=1
		if(x!=0 and c==0 and x!=height-1):
			if(gen1[x-1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c)
				alive+=1
			if(gen1[x-1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x-1,c+1)
				alive+=1
			if(gen1[x][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x,c+1)
				alive+=1
			if(gen1[x+1][c]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c)
				alive+=1
			if(gen1[x+1][c+1]==1):
				#print("value:",z,"i:",x,"j:",c,x+1,c+1)
				alive+=1
		if(alive>=2):
			return 1
		else:
			return 0

def display(ngen,height,width):
	for i in range(height):
		for j in range(width):
			print(ngen[i][j],end="")
		print(" ")
def display2(gen1,height,width):
	for i in range(height):
		for j in range(width):
			print(gen1[i][j],end="")
		print(" ")
def randomiser(gen1,height,width):
	for i in range(height):
		for j in range(width):
			v=random.randint(0,11)
			if(v>8):
				gen1[i][j]=1
			else:
				gen1[i][j]=0
	return gen1

#height=random.randint(5,10)
#width=random.randint(5,10)
height=8
width=6
print(height,width)
#gen1=[[0 for y in range(width) ]for x in range(height)]
#ngen=[[0 for y in range(width) ]for x in range(height)]
#display(gen1,height,width)

#gen1=randomiser(gen1,height,width)

gen1=[
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,1,1,1,0],
[0,0,1,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
]
ngen=[
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
]
generation=0
print("GENERATION:",generation)
display(gen1,height,width)
while(generation!=11):
	for i in range(height):
		for j in range(width):
			print("CHECKING",i,j)
			res=checksurround(gen1[i][j],i,j)
			'''
			if(generation==0 or generation==1):
				print("calling",gen1[i][j],i,j,"height:",height,"width:",width)
				print("CURRENT GEN")
				display2(gen1,height,width)
				print("UPDATED GEN")
				display(ngen,height,width)
			'''
			#display2(gen1,height,width)
			if(res==1):
				#print("alive")
				#print("old:",ngen[i][j])
				ngen[i][j]=1
				#print("new:",ngen[i][j])
				#display(ngen,height,width)
			if(res==0):
				#print("killed")
				#print("old:",ngen[i][j])
				ngen[i][j]=0
				#print("new:",ngen[i][j])
	'''
	print("GEN1")
	display2(gen1,height,width)
	'''
	gen1=ngen
	ngen=[
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
]
	#ngen=[[0 for y in range(width) ]for x in range(height)]
	generation+=1
	print("GENERATION:",generation)
	#if(generation==0 or generation==1):
	display(gen1,height,width)
#display(ngen,height,width)
