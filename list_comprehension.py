# permutation combination of x,y,z list where sum of the x,y,z is not equal to n 
co_ord_x = [ele for ele in range(x+1)]
co_ord_y = [ele for ele in range(y+1)]
co_ord_z = [ele for ele in range(z+1)]
permut_xyz = [[x,y,z] for x in co_ord_x for y in co_ord_y for z in co_ord_z if sum([x,y,z]) != n]
print(permut_xyz)

# one line code:
permut_xyz = [[co_ord_x,co_ord_y,co_ord_z] for co_ord_x in range(x+1) for co_ord_y in range(y+1) for co_ord_z in range(z+1) if sum([co_ord_x,co_ord_y,co_ord_z]) != n]
print(permut_xyz)
