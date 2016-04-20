f = open(~/GitHub/dayindata/,'output.txt')
while True:
    text = f.readline
    if 'timestamp format' in text: # add in timestamp string here to look for times
        print text
    elif 'emersons useful data' in text: # add in the strings for our useful txt
        print text
    elif 'stevens useful data' in text: # add in the strings for our useful txt
        print text
