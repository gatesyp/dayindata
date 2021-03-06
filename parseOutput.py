import csv

# emersons test is fully functaionl

# open the csv file
with open('speedtest-laptop-ouput-21-23.csv', 'wb') as csvfile:
# create a dictionary which will hold each rows values
    row = {'time': 0, 'latency': 0, 'download': 0, 'upload' : 0}
# format the csv file
    datawriter = csv.DictWriter(csvfile, row.keys())
    datawriter.writeheader()
# read  the output file and fill up my dict
    for text in open('goodOutputanothertry.txt', 'r'):
        if 'Current time: ' in text: # get the time
            text = text[-9:]
            print text
            row['time'] = text
        if 'Hosted ' in text: # get the latency
            text = text[-10:] 
            print text
            row['latency'] = text
        elif 'Download: ' in text:  # get the download speed
            text = text[10:15]
            print text
            row['download'] = text
# one row is filled after getting the upload. then write the dict to csv file as one row
        elif 'Upload: ' in text: # get the upload speed
            text = text[8:13]
            print text
            row['upload'] = text
            # add row to csv file
            datawriter.writerow(row)
# end of loop. now go back to top and make a new row entry


# ---------- Stevens Code not functional yet
with open('arptest-laptop-output-21-22.csv', 'wb') as csvfile:
# create a dictionary which will hold each rows values
    row = {'hosts_total': 0, 'hosts_responded': 0, 'time' : 0}
# format the csv file
    datawriter = csv.DictWriter(csvfile, row.keys())
    datawriter.writeheader()
# read  the output file and fill up my dict
    for text in open('laptop-uarh-arpscan-20-21.txt', 'r'):
        if 'Current time: ' in text: # get the time
            text = text[-9:]
	    row['time'] = text
        if 'Ending arp-scan' in text: # get how many hosts are connected 
		all_hosts = text[23:28]
            	text = text[-15:-10]
		print text
		print all_hosts
	    	row['hosts_responded'] = text
	    	row['hosts_total'] = all_hosts 
		datawriter.writerow(row)
