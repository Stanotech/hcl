# Trapped water between piles

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
volume = 0

for i in range(len(heights)):
    L_max = heights[i]
    P_max = heights[i]
    print(f"wartosc pozycji={heights[i]}")
    for j in range(i, len(heights)):
        if heights[j] > P_max:            
            P_max = heights[j]
        print(f"Pmax={P_max}")
    for j in range(i, 0, -1):
        if heights[j] > L_max:
            L_max = heights[j]
        print(f"Lmax={L_max}")
    
    print (min(L_max, P_max) - heights[i])
    volume += min(L_max, P_max) - heights[i]

print(volume)
