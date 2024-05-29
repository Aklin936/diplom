f = open("surf.txt", "r", encoding="utf-8")

data = []
for line in f:
    data_line = line.split()
    for i in range(len(data_line)):
        data_line[i] = float(data_line[i])
    data.append(data_line)

h = data

f.close()

sum = 0
eta = 0.98
h_x = 3.5/len(data)
h_y = 10/len(line)
for line in data:
    for ch in line:
#        sum = sum + (0.6-ch)*0.666*(0.113333*0.151613)/ch
#        sum = sum + (h_x*h_y)/ch
        sum = sum + (h_x*h_y)*(0.6-ch)/ch

#sum = sum * (0.6-data[4][30])*(1-eta)/31.96 
sum = sum * (1-eta)/31.96 
print(sum)