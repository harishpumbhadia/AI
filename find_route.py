import sys
class node:
	def __init__(self,name,source):
		self.name=name
		self.route=source; 
		self.distance=0
	def update(self,parent,cost):  
		self.route=parent.route+","+self.name 
		self.distance=parent.distance+cost 
if(len(sys.argv)==4): 
	filename=sys.argv[1]
	source=sys.argv[2]
	destination=sys.argv[3]
	f=open(filename,"r")
	city_list=f.readlines()
	city_list.pop()
	table={}
	
	for i in city_list:
		a=i.split()
		
		if(a[0] in table.keys()):
			 table[a[0]][0].append(a[1])
			 table[a[0]][1].append(int(a[2]))
		else:
			 table[a[0]]=[[],[]]
			 table[a[0]][0].append(a[1])
			 table[a[0]][1].append(int(a[2]))
		if(a[1] in table.keys()):
			 table[a[1]][0].append(a[0])
			 table[a[1]][1].append(int(a[2]))
		else:
			 table[a[1]]=[[],[]]
			 table[a[1]][0].append(a[0])
			 table[a[1]][1].append(int(a[2]))
	print(table)
	fringe=[]
	startnode=node(source,source)
	closed=[]
	fringe.append([startnode,0])
	ne=0
	ng=1
	while True:
		
		if(len(fringe)==0):
			print("\n")
			print("nodes expanded:",ne)
			print("nodes generated:",ng)
			print("distance:infinity")
			print("route:")
			print("none")
			break
		else:
			f=fringe.pop(0)
			front=f[0]  
			if(front.name==destination):
				ne=ne+1
				print("\n")
				print("nodes expanded:",ne)
				print("nodes generated:",ng)
				
				route=front.route;
				c=route.split(',');
				
				tot_dist=0
				for i in range(0,len(c)-1):
                                        tot_dist=tot_dist+table[c[i]][1][table[c[i]][0].index(c[i+1])]
				print("distance:",str(tot_dist)+" km")
	
				print("route:")
				for i in range(0,len(c)-1):
					print(c[i]+" to "+c[i+1]+", "+str(table[c[i]][1][table[c[i]][0].index(c[i+1])])+" km")
				break
                                
			if(front.name not in closed):
				closed.append(front.name)
				ne=ne+1
				city=table[front.name][0]
				distance=table[front.name][1]
				for i in range(0,len(city)):
					ng=ng+1
					new_node=node(city[i],source)
					new_node.update(front,distance[i])
					fringe.append([new_node,new_node.distance])
					fringe.sort(key = lambda fringe: fringe[1])
			else:
				ne=ne+1
elif(len(sys.argv)==5): 
	filename=sys.argv[1]
	source=sys.argv[2]
	destination=sys.argv[3]
	hname=sys.argv[4]
	f=open(filename,"r")
	city_list=f.readlines()
	city_list.pop()
	f2=open(hname,"r")
	hlist=f2.readlines()
	hlist.pop()
	table={}
	heuristic={}
	
	for i in hlist:
		x=i.split()
		heuristic[x[0]]=int(x[1]) 
	for i in city_list:
		x=i.split()
		if(x[0] in table.keys()):
			 table[x[0]][0].append(x[1])
			 table[x[0]][1].append(float(x[2]))
		else:
			 table[x[0]]=[[],[]]
			 table[x[0]][0].append(x[1])
			 table[x[0]][1].append(float(x[2]))
		if(x[1] in table.keys()):
			 table[x[1]][0].append(x[0])
			 table[x[1]][1].append(float(x[2]))
		else:
			 table[x[1]]=[[],[]]
			 table[x[1]][0].append(x[0])
			 table[x[1]][1].append(float(x[2])) 
	fringe=[]
	startnode=node(source,source)  
	fringe.append([startnode,0+heuristic[source]])
	closed=[]
	ne=0
	ng=1
	while True:
		
		if(len(fringe)==0):
			print("\n")
			print("nodes expanded:",ne)
			print("nodes generated:",ng)
			print("distance:infinity")
			print("route:")
			print("none")
			break
		else:
			f=fringe.pop(0)
			front=f[0]  
			if(front.name==destination):
				ne=ne+1
				print("\n")
				print("nodes expanded:",ne)
				print("nodes generated:",ng)
				
				route=front.route;
				c=route.split(',');
				
				tot_dist=0
				for i in range(0,len(c)-1):
                                        tot_dist=tot_dist+table[c[i]][1][table[c[i]][0].index(c[i+1])]
				print("distance:",str(tot_dist)+" km")
				print("route:")         
				for i in range(0,len(c)-1):
					print(c[i]+" to "+c[i+1]+", "+str(table[c[i]][1][table[c[i]][0].index(c[i+1])])+" km") 
				break
			if(front.name not in closed):
				closed.append(front.name)
				ne=ne+1
				city=table[front.name][0]
				distance=table[front.name][1]
				for i in range(0,len(city)):
					ng=ng+1
					new_node=node(city[i],source)
					new_node.update(front,distance[i])
					fringe.append([new_node,new_node.distance+heuristic[city[i]]])
					fringe.sort(key = lambda fringe: fringe[1])
			else:
				ne=ne+1
