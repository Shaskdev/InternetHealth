import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker

time = []
download =[]
upload = []

with open('test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        time.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))
        
print(time, "/n", download, "/n", upload)


plt.figure(figsize=(30,30))
plt.plot(time, download, label='download', color='r')
plt.plot(time, upload, label='upload', color='b')
plt.xlabel('time')
plt.ylabel('speed in MB/s')
plt.title('Internet Speed')
plt.legend()
plt.savefig('test_graph.jpg', bbox_inches='tight')
