colA = int(input('Grunnfarge:\n'))
colB = int(input('Målfarge:\n'))
rationB = float(input('Andel målfarge:\n'))

colA_R = colA // 1000000
colA_G = (colA // 1000) % 1000
colA_B = colA % 1000

colB_R = colB // 1000000
colB_G = (colB // 1000) % 1000
colB_B = colB % 1000

colC_R = (1-rationB) * colA_R + rationB * colB_R
colC_G = (1-rationB) * colA_G + rationB * colB_G
colC_B = (1-rationB) * colA_B + rationB * colB_B

colC_R = round(colC_R)
colC_G = round(colC_G)
colC_B = round(colC_B)

colC = colC_R * 1000000 + colC_G * 1000 + colC_B

print(colC)