import sys 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import plotly.express as px
import time as tm
def main () :
	x_coord = np.linspace(0,2*np.pi, 10000)
	y_coord1 = np.sin(x_coord)
	y_coord2 = np.cos(x_coord)
	fig1 = px.line(x = x_coord, y = y_coord1, color = 'red', title= 'Comparing trigonometric functions')
	fig1.add_scatter(x = x_coord, y = y_coord2)
	
	fig1.show()



if __name__ == "__main__":
  main ()
