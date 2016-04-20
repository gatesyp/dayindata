f = open('outputTest.txt', 'r')
while True:
    text = f.readline
    #if 'timestamp format' in text: # add in timestamp string here to look for times
    #    print text
    if 'Download: ' in text: 
        text = text.replace(test[10:15])
        print text
    elif 'Upload: ' in text: 
        text = text.replace(test[8:13])
        print text
    elif 'Hosted by: ' in text: 
        text = text.replace(test[:]) # look up how to get last 5 characters of string
        print text
    elif 'stevens useful data' in text: # add in the strings for our useful txt
        print text
