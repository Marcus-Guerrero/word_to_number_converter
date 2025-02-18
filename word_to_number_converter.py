#Equivalent number values of the words
app_values= {"billion": 1000000000, "million": 1000000, "thousand": 1000, "hundred": 100, "ninety": 90, "eighty": 80,"seventy": 70,
             "sixty": 60, "fifty": 50, "forty": 40, "thirty": 30, "twenty": 20, "nineteen": 19, "eighteen": 18, "seventeen": 17,
             "sixteen": 16, "fifteen": 15, "fourteen": 14, "thirteen": 13, "twelve": 12, "eleven": 11, "ten": 10, "nine": 9, "eight": 8,
             "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2, "one": 1, "zero": 0}

#Converted values are placed inside a list
num_vals= []

#Counter values
hundred= 100
thousand= 1000
million= 1000000
#Place an input statement
word_val= input("Please enter a word that you want to convert into a number: ").lower()

#For splitting the values and storing inside a list
new_val_sep= word_val.split(" ")

#Conditions for locating and appending values
for val in new_val_sep:
    if val in app_values:
        converted_val= app_values.get(val)
        num_vals.append(converted_val)

print(num_vals) #For checking only

def converter (num_val):
    if len(num_vals) <=2: #thousands place
        if num_vals[-1]== 1000000:
            fin= million * num_vals[0]
        elif num_vals [-1] == 1000:
            fin=(num_vals [0] * num_vals[-1])
        elif num_vals [-1] == 100: #hundreds place
            fin=(num_vals [0] * num_vals[-1])
        else: #Tens place
            fin=(sum(num_vals))

    #Only applicable for 3 values
    elif len(num_vals) == 3:
        if num_vals[0] == 1: # One for first index
            if num_vals[1] == 100 and num_vals[2] == 1000000:  # For hundred million
                fin = million * hundred
            elif num_vals[1]==1000000:
                fin= million + num_vals[2]
            elif 1000 not in num_vals:
                fin= (sum(num_vals)-1)
            else:
                fin= hundred*thousand
        elif num_vals[0] != 1:
            if num_vals[1]==100 and num_vals[2]==1000000: #For hundred million
                fin= (million*hundred)*num_vals[0]
            elif num_vals [2]==1000000: #For ten millions place
                fin= million*(num_vals[0]+num_vals[1])
            elif num_vals[1]==1000000:
                fin= (million*num_vals[0])+num_vals[2]
            elif num_vals[1]== 100 and num_vals[2] == 1000:
                fin= num_vals[0]*hundred*thousand
            elif num_vals [1] != 1000 and num_vals[1] != 100: #for ten thousands place
                fin= thousand * (num_vals[0]+num_vals[1])
            elif num_vals[1] == 1000 and num_vals [0] >= 1 and num_vals [0] <=99: #for thousands place
                thousand_first= thousand+num_vals[2]
                fin= thousand_first + (thousand * (num_vals[0]-1))
            else: #for hundreds place
                fin= hundred * num_vals[0] + num_vals[2]

    #For more than 3 values
    elif len(num_vals) >3 and len(num_vals) <= 14:
        if 1000000 in num_vals:
            #For one million place value
            if num_vals[1]==1000000: #Millions place
                if len(num_vals)==11: #Complete set of values:
                    fin= million*num_vals[0] + (thousand*hundred)*num_vals[2] + (sum(num_vals[4:6])*thousand) + \
                    (hundred*num_vals[7]) + sum(num_vals[9:])
                else: #Incomplete set
                    fin= million*num_vals[0]
                    if num_vals[3]== 100 and 1000 in num_vals: #Applicable if hundred thousand is available
                        fin += (thousand*hundred)*num_vals[2]
                        if len(num_vals)>5:
                            if num_vals[4]!=1000 and sum(num_vals[4:])>=1000: #ten thousands/thousands place addition
                                if num_vals[5]!=1000:
                                    fin += sum(num_vals[4:6]) * thousand
                                    if sum(num_vals[6:])>=1100:
                                        fin += (hundred*num_vals[7])
                                    else:
                                        fin += sum(num_vals[7:])
                                else:
                                    fin += num_vals[4] * thousand
                                    if sum(num_vals[5:]) >= 1100 and len(num_vals) >= 9:
                                        fin += (hundred * num_vals[6]) + sum(num_vals[8:])
                                    elif sum(num_vals[5:]) >= 1100 and len(num_vals) == 8:
                                        fin += hundred * num_vals[6]
                                    else:
                                        fin += sum(num_vals[6:])
                            elif 1000>sum(num_vals[5:])>=100: # hundreds place
                                fin += num_vals[5]*hundred
                                if len(num_vals)>=8:
                                    fin += sum(num_vals[7:])
                            else: # tens and ones place
                                fin += sum(num_vals[5:])
                    elif 1000 in num_vals: #Application for the ten thousand/thousand place
                        if num_vals[3]!=1000:
                            fin += thousand*(sum(num_vals[2:4]))
                            if len(num_vals)>5:
                                if sum(num_vals[5:])>=100 and len(num_vals)>=8:
                                    fin += hundred*num_vals[5]+sum(num_vals[7:])
                                elif sum(num_vals[5:])>=100 and len(num_vals)==7:
                                    fin += hundred*num_vals[5]
                                else:
                                    fin += sum(num_vals[5:])
                        else:
                            fin += thousand*num_vals[2]
                            if len(num_vals)>4:
                                if sum(num_vals[4:])>=100 and len(num_vals)>=7:
                                    fin += hundred*num_vals[4]+sum(num_vals[6:])
                                elif sum(num_vals[4:])>=100 and len(num_vals)==6:
                                    fin += hundred*num_vals[4]
                                else:
                                    fin += sum(num_vals[4:])
                    else: #Application for hundreds/tens/ones
                        if sum(num_vals[2:])>=100 and len(num_vals)>=5:
                            fin += hundred*num_vals[2] + sum(num_vals[4:])
                        elif sum(num_vals[2:])>=100 and len(num_vals)==4:
                            fin += hundred*num_vals[2]
                        else:
                            fin += sum(num_vals[2:])

            # For two digits in the ten million value
            elif num_vals[1] != 1000000 and num_vals[1]!=100:
                if len(num_vals) == 12:  # Complete set of values:
                    fin = (million * sum(num_vals[0:2])) + (thousand * hundred) * num_vals[3] + (sum(num_vals[5:7]) * thousand) + \
                          (hundred * num_vals[8]) + sum(num_vals[10:])
                else:  # Incomplete set
                    fin = million * sum(num_vals[0:2])
                    if num_vals[4] == 100 and 1000 in num_vals:  # Applicable if hundred thousand is available
                        fin += (thousand * hundred) * num_vals[3]
                        if len(num_vals)>6:
                            if num_vals[5] != 1000 and sum(num_vals[5:]) >= 1000:  # ten thousands/thousands place addition
                                if num_vals[6]!= 1000:
                                    fin += sum(num_vals[5:7]) * thousand
                                    if len(num_vals)>8:
                                        if sum(num_vals[8:]) >= 100:
                                            fin += (hundred * num_vals[8])
                                        else:
                                            fin += sum(num_vals[8:])
                                else:
                                    fin += num_vals[5] * thousand
                                    if len(num_vals) > 7:
                                        if sum(num_vals[7:]) >= 100 and len(num_vals) >= 10:
                                            fin += (hundred * num_vals[7]) + sum(num_vals[8:])
                                        elif sum(num_vals[7:]) >= 100 and len(num_vals) == 9:
                                            fin += hundred * num_vals[7]
                                        else:
                                            fin += sum(num_vals[7:])
                            elif 1000> sum(num_vals[6:]) >= 100:  # hundreds place
                                fin += num_vals[6] * hundred
                                if len(num_vals) >= 9:
                                    fin += sum(num_vals[8:])
                            else:  # tens and ones place
                                fin += sum(num_vals[6:])
                    elif 1000 in num_vals:  # Application for the ten thousand/thousand place
                        if num_vals[4] != 1000:
                            fin += thousand * (sum(num_vals[3:5]))
                            if len(num_vals)>6:
                                if sum(num_vals[6:]) >= 100 and len(num_vals) >= 9:
                                    fin += hundred * num_vals[6] + sum(num_vals[8:])
                                elif sum(num_vals[6:]) >= 100 and len(num_vals) == 8:
                                    fin += hundred * num_vals[6]
                                else:
                                    fin += sum(num_vals[6:])
                        else:
                            fin += thousand * num_vals[3]
                            if len(num_vals)>5:
                                if sum(num_vals[5:]) >= 100 and len(num_vals) >= 8:
                                    fin += hundred * num_vals[5] + sum(num_vals[7:])
                                elif sum(num_vals[5:]) >= 100 and len(num_vals) == 7:
                                    fin += hundred * num_vals[5]
                                else:
                                    fin += sum(num_vals[5:])
                    else:  # Application for hundreds/tens/ones
                        if sum(num_vals[3:]) >= 100 and len(num_vals) >= 6:
                            fin += hundred * num_vals[3] + sum(num_vals[5:])
                        elif sum(num_vals[3:]) >= 100 and len(num_vals) == 5:
                            fin += hundred * num_vals[3]
                        else:
                            fin += sum(num_vals[3:])

            #For hundred million
            elif num_vals[1]== 100:
                if len(num_vals)== 14: #Complete set
                    fin= (hundred * million * num_vals[0]) + (million * sum(num_vals[2:4]) + (thousand * hundred
                          * num_vals[5]) + (sum(num_vals[7:9]) * thousand) + (hundred * num_vals[10]) +
                          sum(num_vals[12:]))
                else: #Incomplete set
                    fin = hundred * million * num_vals[0]
                    if num_vals[2]!= 1000000:
                        if num_vals[3]!=1000000:
                            fin += million * sum(num_vals[2:4])
                            if len(num_vals)>5:
                                if 1000 in num_vals:
                                    if num_vals[6]==100: # Applicable if hundred thousand is available
                                        fin += (thousand * hundred) * num_vals[5]
                                        if len(num_vals) > 7:
                                            if num_vals[7] != 1000 and sum(
                                                    num_vals[7:]) >= 1000:  # ten thousands/thousands place addition
                                                if num_vals[8] != 1000:
                                                    fin += sum(num_vals[7:9]) * thousand
                                                    if len(num_vals) > 10:
                                                        if sum(num_vals[10:]) >= 100:
                                                            fin += (hundred * num_vals[10])
                                                        else:
                                                            fin += sum(num_vals[10:])
                                                else:
                                                    fin += num_vals[7] * thousand
                                                    if len(num_vals) > 9:
                                                        if sum(num_vals[9:]) >= 100 and len(num_vals) >= 13:
                                                            fin += (hundred * num_vals[9]) + sum(num_vals[11:])
                                                        elif sum(num_vals[9:]) >= 100 and len(num_vals) == 12:
                                                            fin += hundred * num_vals[9]
                                                        else:
                                                            fin += sum(num_vals[9:])
                                            elif 1000 > sum(num_vals[8:]) >= 100:  # hundreds place
                                                fin += num_vals[8] * hundred
                                                if len(num_vals) >= 11:
                                                    fin += sum(num_vals[10:])
                                            else:  # tens and ones place
                                                fin += sum(num_vals[8:])
                                    else:  # Application for the ten thousand/thousand place
                                        if num_vals[6] != 1000:
                                            fin += thousand * (sum(num_vals[5:7]))
                                            if len(num_vals) > 8:
                                                if sum(num_vals[8:]) >= 100 and len(num_vals) >=11:
                                                    fin += hundred * num_vals[8] + sum(num_vals[10:])
                                                elif sum(num_vals[8:]) >= 100 and len(num_vals) == 10:
                                                    fin += hundred * num_vals[8]
                                                else:
                                                    fin += sum(num_vals[8:])
                                        else:
                                            fin += thousand * num_vals[5]
                                            if len(num_vals) > 7:
                                                if sum(num_vals[7:]) >= 100 and len(num_vals) >= 10:
                                                    fin += hundred * num_vals[7] + sum(num_vals[9:])
                                                elif sum(num_vals[7:]) >= 100 and len(num_vals) == 9:
                                                    fin += hundred * num_vals[7]
                                                else:
                                                    fin += sum(num_vals[7:])
                                else:  # Application for hundreds/tens/ones
                                    if sum(num_vals[5:]) >= 100 and len(num_vals) >= 8:
                                        fin += hundred * num_vals[5] + sum(num_vals[7:])
                                    elif sum(num_vals[5:]) >= 100 and len(num_vals) == 7:
                                        fin += hundred * num_vals[5]
                                    else:
                                        fin += sum(num_vals[5:])

                        elif num_vals[3]== 1000000:
                            fin += million * num_vals[2]
                            if len(num_vals) > 4:
                                if 1000 in num_vals:
                                    if num_vals[5] == 100:  # Applicable if hundred thousand is available
                                        fin += (thousand * hundred) * num_vals[4]
                                        if len(num_vals) > 6:
                                            if num_vals[6] != 1000 and sum(
                                                    num_vals[6:]) >= 1000:  # ten thousands/thousands place addition
                                                if num_vals[7] != 1000:
                                                    fin += sum(num_vals[6:8]) * thousand
                                                    if len(num_vals) > 9:
                                                        if sum(num_vals[9:]) >= 100:
                                                            fin += (hundred * num_vals[9])
                                                        else:
                                                            fin += sum(num_vals[9:])
                                                else:
                                                    fin += num_vals[6] * thousand
                                                    if len(num_vals) > 8:
                                                        if sum(num_vals[8:]) >= 100 and len(num_vals) >= 11:
                                                            fin += (hundred * num_vals[8]) + sum(num_vals[10:])
                                                        elif sum(num_vals[8:]) >= 100 and len(num_vals) == 10:
                                                            fin += hundred * num_vals[8]
                                                        else:
                                                            fin += sum(num_vals[8:])
                                            elif 1000 > sum(num_vals[7:]) >= 100:  # hundreds place
                                                fin += num_vals[7] * hundred
                                                if len(num_vals) >= 10:
                                                    fin += sum(num_vals[9:])
                                            else:  # tens and ones place
                                                fin += sum(num_vals[7:])
                                    else:  # Application for the ten thousand/thousand place
                                        if num_vals[5] != 1000:
                                            fin += thousand * (sum(num_vals[4:6]))
                                            if len(num_vals) > 7:
                                                if sum(num_vals[7:]) >= 100 and len(num_vals) >= 10:
                                                    fin += hundred * num_vals[7] + sum(num_vals[9:])
                                                elif sum(num_vals[7:]) >= 100 and len(num_vals) == 9:
                                                    fin += hundred * num_vals[7]
                                                else:
                                                    fin += sum(num_vals[7:])
                                        else:
                                            fin += thousand * num_vals[4]
                                            if len(num_vals) > 6:
                                                if sum(num_vals[6:]) >= 100 and len(num_vals) >= 9:
                                                    fin += hundred * num_vals[6] + sum(num_vals[8:])
                                                elif sum(num_vals[6:]) >= 100 and len(num_vals) == 8:
                                                    fin += hundred * num_vals[6]
                                                else:
                                                    fin += sum(num_vals[6:])
                                else:  # Application for hundreds/tens/ones
                                    if sum(num_vals[4:]) >= 100 and len(num_vals) >= 7:
                                        fin += hundred * num_vals[4] + sum(num_vals[6:])
                                    elif sum(num_vals[4:]) >= 100 and len(num_vals) == 6:
                                        fin += hundred * num_vals[4]
                                    else:
                                        fin += sum(num_vals[4:])

                    else:
                        if 1000 in num_vals:
                            if num_vals[4] == 100:  # Applicable if hundred thousand is available
                                fin += (thousand * hundred) * num_vals[3]
                                if len(num_vals) > 4:
                                    if num_vals[5] != 1000 and sum(
                                            num_vals[5:]) >= 1000:  # ten thousands/thousands place addition
                                        if num_vals[6] != 1000:
                                            fin += sum(num_vals[5:7]) * thousand
                                            if len(num_vals)>8:
                                                if sum(num_vals[8:]) >= 100 and len(num_vals) >= 11:
                                                    fin += (hundred * num_vals[8]) + sum(num_vals[10:])
                                                elif sum(num_vals[8:]) >= 100 and len(num_vals) == 10:
                                                    fin += hundred * num_vals[8]
                                                else:
                                                    fin += sum(num_vals[8:])
                                        else:
                                            fin += num_vals[5] * thousand
                                            if len(num_vals) > 7:
                                                if sum(num_vals[7:]) >= 100 and len(num_vals) >= 10:
                                                    fin += (hundred * num_vals[7]) + sum(num_vals[9:])
                                                elif sum(num_vals[7:]) >= 100 and len(num_vals) == 9:
                                                    fin += hundred * num_vals[7]
                                                else:
                                                    fin += sum(num_vals[7:])
                                    elif 1000 > sum(num_vals[6:]) >= 100:  # hundreds place
                                        fin += num_vals[6] * hundred
                                        if len(num_vals) >= 9:
                                            fin += sum(num_vals[8:])
                                    else:  # tens and ones place
                                        fin += sum(num_vals[6:])
                            else:  # Application for the ten thousand/thousand place
                                if num_vals[4] != 1000:
                                    fin += thousand * (sum(num_vals[3:5]))
                                    if len(num_vals) > 6:
                                        if sum(num_vals[6:]) >= 100 and len(num_vals) >= 9:
                                            fin += hundred * num_vals[6] + sum(num_vals[8:])
                                        elif sum(num_vals[6:]) >= 100 and len(num_vals) == 8:
                                            fin += hundred * num_vals[6]
                                        else:
                                            fin += sum(num_vals[6:])
                                else:
                                    fin += thousand * num_vals[3]
                                    if len(num_vals) > 5:
                                        if sum(num_vals[5:]) >= 100 and len(num_vals) >= 8:
                                            fin += hundred * num_vals[5] + sum(num_vals[7:])
                                        elif sum(num_vals[5:]) >= 100 and len(num_vals) == 7:
                                            fin += hundred * num_vals[5]
                                        else:
                                            fin += sum(num_vals[5:])
                        else:  # Application for hundreds/tens/ones
                            if sum(num_vals[3:]) >= 100 and len(num_vals) >= 6:
                                fin += hundred * num_vals[3] + sum(num_vals[5:])
                            elif sum(num_vals[3:]) >= 100 and len(num_vals) == 5:
                                fin += hundred * num_vals[3]
                            else:
                                fin += sum(num_vals[3:])

        # Hundreds thousands
        elif num_vals[1] == 100 and 1000 in num_vals:
            if len(num_vals)==9: #Hundred thousand complete set
                fin = ((thousand * hundred * num_vals[0]) + (thousand*(sum(num_vals[2:4]))) +
                       (hundred*num_vals[5]) + sum(num_vals[7:]))
            else: #Incomplete set
                fin = thousand * hundred * num_vals[0]
                if sum(num_vals[3:])>=1000: #Application for ten thousands/thousand place value
                    if num_vals[3]!=1000:
                        fin += thousand*sum(num_vals[2:4])
                        if sum(num_vals[5:])>=100 and len(num_val)>=8:
                            fin += hundred*num_vals[5] + sum(num_vals[7:])
                        elif sum(num_vals[5:])>=100 and len(num_val)==7:
                            fin += hundred * num_vals[5]
                        else:
                            fin += sum(num_vals[5:])
                    else:
                        fin += thousand*num_vals[2]
                        if sum(num_vals[4:])>=100 and len(num_val)>=7:
                            fin += hundred*num_vals[4] + sum(num_vals[6:])
                        elif sum(num_vals[4:])>=100 and len(num_val)==6:
                            fin += hundred * num_vals[4]
                        else:
                            fin += sum(num_vals[4:])
                else: #Application of hundreds/tens/ones
                    if sum(num_vals[3:])>=100 and len(num_vals)>=5:
                        fin += hundred * num_vals[3] + sum(num_vals[5:])
                    elif sum(num_vals[3:])>=100 and len(num_vals)==5:
                        fin += hundred * num_vals[3]
                    else:
                        fin += sum(num_vals[3:])

        #Ten thousands place value
        elif num_vals[1] >= 1 and num_val[1] <= 9:
            ten_thousand_first = thousand * (sum(num_vals[0:2]))
            if sum(num_vals[3:]) >= 100 and len(num_vals)>=6:
                fin = ten_thousand_first + (hundred * num_vals[3]) + sum(num_vals[5:])
            elif sum(num_vals[3:]) >= 100 and len(num_vals)==5:
                fin = ten_thousand_first + (hundred*num_vals[3])
            else:
                fin = ten_thousand_first + sum(num_vals[3:])

        # thousands place value
        elif 1000 in num_vals:
            if sum(num_vals[2:])>=100 and len(num_vals)>=5:
                fin= thousand*num_vals[0] + hundred*num_vals[2] + sum(num_vals[4:])
            elif sum(num_vals[2:])>=100 and len(num_vals)==4:
                fin= thousand*num_vals[0] + hundred*num_vals[2]
            else:
                fin=thousand * num_vals[0] + sum(num_vals[2:])

        # Hundreds place value
        else:
            fin= hundred*num_vals[0] + sum(num_vals[2:])
    return fin

print(converter(num_vals))