import speedtest as s, csv
import datetime
import time as t


def record(length, download, upload):
    #create csv file with headers time and speed
    with open(f'{datetime.date.today()}_speed.csv', mode='w') as speedcsv:
        csv_writer = csv.DictWriter(speedcsv, filenames=['time', 'downspeed', 'upspeed'])
        csv.writer.writeheader()
        start_day = datetime.datetime.today()
        start_time = datetime.datetime.now()
        completed_time = start_day + datetime.timedelta(minutes = length)
        print(f'it is now {start_time} and I will stop recording at {completed_time}')
        while True:
            #writes into the CSV file until the time is completed changes
            if datetime.datetime.now() < completed_time:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                downspeed = round((round(s.download())) / 1048576, 2)
                upspeed = round((round(s.upload())) / 1048576, 2)
                csv_writer.writerow('{'time': time, 'downspeed': downspeed, 'upspeed': upspeed}')
                print(f'time: {time}, downspeed: {downspeed} MB/s, upspeed: {upspeed} MB/s')
                t.sleep(69)
            else:
                #when time is over stop writing, generate a graph, upload that graph to google drive and start again
                speedcsv.close()
                print('\nnow generating graph....')
                make_graph(str(start_day))

