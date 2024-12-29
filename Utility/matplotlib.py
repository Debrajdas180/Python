import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#Marker -----
plt.plot(xpoints, ypoints, 'o') #this code will execute to data pointing using circle dot, below attachd few other symbols
# 'o' 	Circle 	
# '*' 	Star 	
# '.' 	Point 	
# ',' 	Pixel 	
# 'x' 	X 	
# 'X' 	X (filled) 	
# '+' 	Plus 	
# 'P' 	Plus (filled) 	
# 's' 	Square 	
# 'D' 	Diamond 	
# 'd' 	Diamond (thin) 	
# 'p' 	Pentagon 	
# 'H' 	Hexagon 	
# 'h' 	Hexagon 	
# 'v' 	Triangle Down 	
# '^' 	Triangle Up 	
# '<' 	Triangle Left 	
# '>' 	Triangle Right 	
# '1' 	Tri Down 	
# '2' 	Tri Up 	
# '3' 	Tri Left 	
# '4' 	Tri Right 	
# '|' 	Vline 	
# '_' 	Hline

   
plt.plot(ypoints, 'o:r')   #marker|line|color

#Line reference--
# '-' 	Solid line 	
# ':' 	Dotted line 	
# '--' 	Dashed line 	
# '-.' 	Dashed/dotted line

#Color reference--
# 'r' 	Red 	
# 'g' 	Green 	
# 'b' 	Blue 	
# 'c' 	Cyan 	
# 'm' 	Magenta 	
# 'y' 	Yellow 	
# 'k' 	Black 	
# 'w' 	White 	

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r') # ms = marker size , mec = marker border color , mfc = marker frame color
plt.xlabel("Average Pulse") # printing the label in x axix
plt.ylabel("Calorie Burnage") # printing the label in y axix
plt.title("Sports Watch Data") # printing the tittle of the data 


font1 = {'family':'serif','color':'blue','size':20} # defining a font dictionary 
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1) # To print the tittle in different font
plt.xlabel("Average Pulse", fontdict = font2) # To print the label in different font
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.title("Sports Watch Data", loc = 'left') # for plot tittle in left side 

plt.grid() # for show up the grid

plt.grid(axis = 'y') # will show the grid in y axis only 

plt.grid(axis = 'x') # will show the grid in x axix only 

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) #will show the grid in green color dashed form with width of 0.5

#Subplot:
# plt.subplot(1, 2, 1) the figure has 1 row, 2 columns, and this plot is the first plot. 
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)