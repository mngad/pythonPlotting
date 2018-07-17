import ternary
import numpy as np
import pandas as pd

### Scatter Plot

scale = 20
figure, tax = ternary.figure(scale=scale)

# Draw Boundary and Gridlines
#tax.boundary(linewidth=2.0)
tax.gridlines(color="blue", multiple=5)

# Set Axis labels and Title
fontsize = 20

tax.left_axis_label("Left label $\\alpha^2$", fontsize=fontsize)
tax.right_axis_label("Right label $\\beta^2$", fontsize=fontsize)
tax.bottom_axis_label("Bottom label $\\Gamma - \\Omega$", fontsize=fontsize)
df = pd.read_csv(
        'pc1_20.csv',
        header=0,
        sep=',')
p1 =[]
# Draw an arbitrary line, ternary will project the points for you
for index, row in df.iterrows():
    print (row["Stiffness Change"], row["Position"], row["SD"])
    p1.append([row["Stiffness Change"], row["Position"], row["SD"]])

print(p1)

ptest = ([10,10,10],[1,1,1])
tax.scatter(ptest, marker='s', color='green', linestyle=":")

tax.ticks(axis='lbr', multiple=5, linewidth=1)

tax.show()