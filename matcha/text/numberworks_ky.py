import math
import re

def maketail(san):
    last_two = san[-3:]
    kuyruktar = {
    u'өл ':u'үнчү', 
    u'ир ':u'инчи ', 
    u'ки ':u'нчи ', 
    u'үч ':u'үнчү ', 
    u'рт ':u'үнчү ', 
    u'еш ':u'инчи ', 
    u'ты ':u'нчы ', 
    u'ти ':u'нчи ', 
    u'из ':u'инчи ', 
    u'уз ':u'унчу ', 
    u'он ':u'унчу', 
    u'ма ':u'нчы ', 
    u'рк ':u'ынчы ', 
    u'үү ':u'нчү ', 
    u'ыш ':u'ынчы ', 
    u'иш ':u'инчи ', 
    u'ен ':u'инчи ', 
    u'үз ':u'үнчү ', 
    u'иң ':u'инчи ', 
    u'рд ':u'ынчы '}
    if last_two in kuyruktar:
        return "{}{}".format(san[:-1], kuyruktar[last_two])
    else:
        return san
        
def mingecheyin(san):
    birdikter = {"0":'', "1":u'бир ', "2":u'эки ', "3":u'үч ', "4":u'төрт ', "5":u'беш ', "6":u'алты ', "7":u'жети ', "8":u'сегиз ', "9":u'тогуз '}
    onduktar = {"1":u'он ', "2":u'жыйырма ', "3":u'отуз ', "4":u'кырк ', "5":u'элүү ', "6":u'алтымыш ', "7":u'жетимиш ', "8":u'сексен ', "9":u'токсон ', "0":'', }
    juz = ["жүз "]
    if len(san) == 3:
        if san[0] == "1":
            jazuu = juz[0]+onduktar[san[1]]+birdikter[san[2]]
            return jazuu
        if san[0] == "0":
            jazuu = onduktar[san[1]]+birdikter[san[2]]
            return jazuu
        else:
            jazuu = birdikter[san[0]]+juz[0]+onduktar[san[1]]+birdikter[san[2]]
            return jazuu
    if len(san) == 1:
        if san[0] == "0":
            jazuu = u'нөл '
            return jazuu
        else:
            jazuu = birdikter[san[0]]
            return jazuu
    if len(san) == 2:
        jazuu = onduktar[san[0]]+birdikter[san[1]]
        return jazuu

def readmynumber(n):
    if n==0:
        return u'нөл '
    number = "{}".format(n)    
    kanchanol = len(number)%3
    if kanchanol == 1:
        number = "00"+number
    elif kanchanol == 2:
        number = "0"+number
    else:
        number = number

    kanchaJuzbar =  math.ceil(int(len(number))/3.0)
    ranks = {"0":"","1":"миң ","2":"миллион ","3":"миллиард ","4":"триллион ","5":"квадриллион "}

    result = ""
    for i in range(int(kanchaJuzbar)):
        if number[-1*((i*3)+3)]+number[-1*((i*3)+2)]+number[-1*((i*3)+1)] == "000":
            result = result
        elif number[-1*((i*3)+3)]+number[-1*((i*3)+2)]+number[-1*((i*3)+1)] == "001" and len(number) == 6:
            result = ranks[str(i)] + result
        else:
            result = mingecheyin(number[-1*((i*3)+3)]+number[-1*((i*3)+2)]+number[-1*((i*3)+1)]) + ranks[str(i)] + result
    return result

def readmynumberindecimal(n):
    result = u'бүтүн '
    if int(n)<10:
        result += u'ондон '
    elif int(n)<100:
        result += u'жүздөн '
    elif int(n)<1000:
        result += u'миңден ' 
    else:
        result = u'чекит '
    result += readmynumber(n)
    return result

def readnumberintext(txt):
    newstr = ''.join((ch if ch in '0123456789.,-' else ' ') for ch in txt)
    listOfNumbers = []
    listOfFathers = []

    for i in newstr.split():
        if not bool(re.search(r'\d', i)):
            continue
        listOfFathers.append([i, ''])
        
    for k, val in enumerate(listOfFathers):
        tag = ''
        i = val[0]
        if '-' in i:
            if i[0]=='-':
                tag += 'minus'
                i = i[1:]
            if i[-1]=='-': 
                tag += 'tail'
                i = i[:-1]
            if '-' in i:
                multiplestring = i.split('-')
                for m in multiplestring:
                    listOfNumbers.append(['', m, 0.0, '', k, ''])
            else:
                listOfNumbers.append([tag, i, 0.0, '', k, ''])
        else:
            listOfNumbers.append(['', i,  0.0, '', k, ''])
    
    listOfNumbersFinal = []        
    for x, n in enumerate(listOfNumbers):
        
        i = listOfNumbers[x][1]
        i = i.replace(',','.')
        if '.' in i:
            if i.count('.')==1:
                multiplestring = i.split('.')
                if len(multiplestring[1])>0:
                    listOfNumbers[x][5] = multiplestring[1]
                listOfNumbers[x][2] = float(i)
                listOfNumbersFinal.append(listOfNumbers[x]) 
            else:
                father = listOfNumbers[x][4]
                multiplestring = i.split('.')
                for m in multiplestring:
                    b = ['', m, float(m), '', father, '']
                    listOfNumbersFinal.append(b)
        else:
            listOfNumbers[x][2] = float(i)
            listOfNumbersFinal.append(listOfNumbers[x]) 
    
    for i, n in enumerate(listOfNumbersFinal):
        father = n[4]
        numberintext = ''
        numberintext = readmynumber(int(n[2]))
        if len(n[5])>0:
            numberintext += readmynumberindecimal(n[5])
            
        if 'minus' in n[0]:
            numberintext = u'минус ' + numberintext
        if 'tail' in n[0]:
            numberintext = maketail(numberintext)
        listOfNumbersFinal[i][3] = numberintext
        listOfFathers[father][1] += numberintext
    return listOfFathers

def numberreader(text):
    arr = readnumberintext(text)
    newz = []
    newz_arr = dict()
    for d in arr:
        a = d[0]
        b = d[1]
        newz.append(a)
        newz_arr[a]=b
    newz.sort(key=len, reverse=True)
    for i in newz:
        if text==i:
            text=newz_arr[i]+"."
        else:
            text = text.replace(i," "+newz_arr[i])
    #print(text)
    return text
#numberreader('сф1д----а 3сд -9фу+6й4.3фң12-13кй444-сдфн-сдӨ,ӨӨ нфг4.4.6сфТ545.Тдг.көөҢҢ-4.2Ңөу3246.445-уүүүң.76ңңң....Ү -1-ҮҮ -,3-Ү')
#if __name__ == "__main__":
#    test_text = '1-март 1.345 саны'
#    result = numberreader(test_text)
#    print(result)
