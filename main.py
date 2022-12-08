import os
import pandas as pd
import _ctypes
dow = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
timeblocks = []
timesecond = []
timethird = []
timefourth = []
timefifth = []
timesixth = []
days = []
bothtimes = []

buildingprep = []
furtherprep = []
bnr = []
both = []
last = []
building = []
roomnum = []
laststep =[]
cleanroomnum = []
cleanbuildings = []

subjectblocks = []
subjectspre = []
subjects = []


firstsort = []
split2 = []


classblocks = []
secondsort = []
thirdsort = []
classnames = []


count = 0
filelist = os.listdir("htmlfiles")
for i in filelist:
    with open('htmlfiles/1.html', 'r') as file:  # r to open file in READ mode
        html_as_string = file.read()
        splitlist = html_as_string.split('<tr')
        for i in splitlist:
            if 'data-id' in i:
                firstsort.append(i)
        for i in firstsort:
            split2 += i.split('<td')
        for i in split2: 
            if 'section-details-link' in i:
                classblocks.append(i)
            elif 'meetingTime' in i:
                timeblocks.append(i)
            elif 'subjectDescription' in i:
                subjectblocks.append(i)
        for i in classblocks:
            secondsort += i.split('>')
        for i in secondsort:
            if '/a' in i:
                thirdsort.append(i)
        for i in thirdsort:
            classnames.append(i[:-3])
        for i in subjectblocks:
            subjectspre += i.split('>')
        for i in subjectspre:
            if "</td" in i:
                subjects.append(i[:-4])
        for i in timeblocks:
            timesecond += i.split('>')
        for i in timesecond:
            if '''"meetingTime"''' in i:
                timethird.append(i[142:])
                buildingprep.append(i[178:])
            
        for i in timethird:
            timefifth += i.split('SMTWTFS')
        for i in timefifth:
            timesixth += i.split('Type')
        for i in timesixth:
            if 'Class' not in i:
                timefourth.append(i)
        for i in timefourth:
            if '-' in i:
                bothtimes.append(i)
            else:
                days.append(i)
        for i in buildingprep:
            furtherprep += i.split('Building:')
            
        for i in furtherprep:
            
            bnr += i.split('Start')
            
        for i in bnr:
            
            if 'Date' not in i:
                both.append(i)
        for i in both:
            last += i.split(' R')
        for i in last:
            if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' in i:
                roomnum.append
            if 'oom' in i:
                roomnum.append(i)
            else:
                building.append(i)
        for i in roomnum:
            laststep += i.split(' ')
        for i in laststep:
            if 'oom' not in i:
                cleanroomnum.append(i)
        for i in building:
            if 'ype:' in i:
                building.remove(i)

        
dfcolumns = ['Hall Name', 'Room Number', 'Class Subject', 'Class Name', 'Days of Week', 'Time']
dataset = list(zip(building,cleanroomnum,subjects,classnames,days,bothtimes))
bigdf = pd.DataFrame(dataset,columns=dfcolumns)
print(bigdf)


# print(days)
# print(bothtimes)
# print(subjects)
# print(classnames) 
# print(len(building))
# print(cleanroomnum)




    


    # print(thirdsort)
    # print(len(thirdsort))
    