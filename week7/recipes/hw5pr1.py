

import os
import os.path
import shutil
import time


def count_txt_infilesind(L):
    '''find the txt files in each subfolder, show the subfolder name and how many txt files are in each folder.'''
    count = 0
    '''There are two loops, the first one is looking for all the directory and the second one is lookng for all 
    the txt files inside. '''
    for element in L:
        dirname, LoD, LoF = element
        print("dirname is", dirname)

        for f in LoF:
            if f[-3:] == 'txt':
                count +=1
        print('it has', count, 'txt files')
        time.sleep(0.5)

        count -= count

def count_txt_exercise(L):
    '''find all the txt files under the recipes folder, include subfolders and show one result. '''
    count = 0

    for element in L:
        d, LoD, LoF = element
        #print('++++++++',"dirname is", d,'++++++++')
        #print()

        for f in LoF:
            if f[-3:] == 'txt':
                count +=1

    return count


def count_jpg_exercise(L):
    '''find the jpg files in recipe folder'''
    count = 0

    for element in L:
        d, LoD, LoF = element
        #print('++++++++',"dirname is", d,'++++++++')
        #print()

        for f in LoF:
            if f[-3:] == 'jpg':
                count +=1

    return count


def count_cat_exercise(L):
    '''find the file name that has 'cat' '''
    count = 0

    for element in L:
        d, LoD, LoF = element
        #print('++++++++',"dirname is", d,'++++++++')
        #print()

        for f in LoF:
            if 'cat' in f :
                count +=1

    return count

def count_dog_exercise(L):
    '''find the file name that has 'dog' '''
    count = 0

    for element in L:
        d, LoD, LoF = element
        #print('++++++++',"dirname is", d,'++++++++')
        #print()

        for f in LoF:
            if 'dog' in f :
                count +=1

    return count



def readfile(name):
    '''read the content in the txt file and return it.'''
    f = open(name)
    txt = f.read()
    f.close()
    return  txt


def readsavoryorsweet(L):

    '''use the readfile function to read the content in the txt file, and loop for the key words.'''

    #count = 0
    savory = 0
    sweet = 0
    for element in L:
        dirname, LoD, LoF = element
        #print("dirname is", dirname)
        for file in LoF:
            if file[-3:] =='txt':
                #print(file)
                fullname = dirname + "/" + file
                '''if there is no dirname before the file, it's getting all the files in recipe folder  
                    however, if I want to run through the subfolders in the recipe folder, I have to give the full 
                    name. 
                    ./recipes 2004/recipe143.txt  -> Correct
                    recipe143.txt -> Wrong cuz there's no this file name in recipe folder. It's in recipes 2004'''
                #print(fullname)
                content = readfile(fullname)
                #print(content)

                if 'Savory Pie' in content:
                    savory += 1
                elif 'Sweet Pie' in content:
                    sweet += 1

    print('There are', savory, 'savory recipes in recipe files')
    time.sleep(0.5)
    print('There are', sweet, 'sweet recipes in recipe files')


def findingredient(L):
    '''look for the content in the txt file and split in to lines then split again to words.
        Then find the specific ingredient. '''
    kilo=0
    recipename = ''
    ingredient = ''
    for element in L:
        dirname, LoD, LoF = element
        #print("dirname is", dirname)
        for file in LoF:
            if file[-3:] =='txt':
                #print(file)
                fullname = dirname + "/" + file
                #print(fullname)
                content = readfile(fullname)
                #print(content)
                line = content.split('\n')   # read the file and split by the \n -> get each line separately.
                #print(line)
                for i in line:
                    if 'kilograms' in i :
                        food = i.split(' ')   # if kilograms is in the line, separate by space
                        weight = int(food[0]) # get the number of the kilo in that line
                        if weight > kilo:   # save the kilo for later use
                            kilo = weight   # find the max kilo
                            recipename = str(fullname) # find the max kilo filename
                            ingredient = str(i) #find the max kilo recipe
                        else:
                            continue

                        #kilo.append(int(weight[0])) # get the number in the list, and convert to integer and add to list
                    else:
                        continue
    #print(kilo)
    recipename = recipename.split('/')[-1].split('.')[0]
    ingredient = ingredient.split(' ')[-1]
    #print(recipename)
    #print(ingredient)
    #print(kilo)
    print('The', recipename.upper(), 'calls for the most kilograms of one ingredient' )
    time.sleep(0.5)
    print('The ingredient is', ingredient.upper(), 'and it calls for', kilo,'kilograms')
    time.sleep(0.5)
    print('Hmmm… an interesting recipe!')


def highestdegree(L):
    '''Same as the previous function, divide to line and fine the word in the lines
        because of the position of the degree is the same, it's easy to use index to find it.'''
    temp = 0
    recipename = ''
    ingredient = ''

    for element in L:
        dirname, LoD, LoF = element
        #print("dirname is", dirname)
        for file in LoF:
            if file[-3:] =='txt':
                #print(file)
                fullname = dirname + "/" + file
                #print(fullname)
                content = readfile(fullname)
                #print(content)
                line = content.split('\n')   # read the file and split by the \n -> get each line separately.
                #print(line)
                for i in line:
                    if 'minutes' in i :
                        F = i.split(' ')   # if kilograms is in the line, separate by space
                        degree = int(F[2]) # get the number of the kilo in that line
                        if degree > temp:   # save the kilo for later use
                            temp = degree   # find the max kilo
                        else:
                            continue

                        #kilo.append(int(weight[0])) # get the number in the list, and convert to integer and add to list
                    else:
                        continue
    print('In all recipes, the highest degree is', temp,'degrees')


def longesttime(L):
    '''Same as previous function, look up the time instead of temp'''
    duration = 0
    recipename = ''
    ingredient = ''

    for element in L:
        dirname, LoD, LoF = element
        #print("dirname is", dirname)
        for file in LoF:
            if file[-3:] =='txt':
                #print(file)
                fullname = dirname + "/" + file
                #print(fullname)
                content = readfile(fullname)
                #print(content)
                line = content.split('\n')   # read the file and split by the \n -> get each line separately.
                #print(line)
                for i in line:
                    if 'minutes' in i :
                        timespent = i.split(' ')   # if kilograms is in the line, separate by space
                        minute = int(timespent[-2]) # get the number of the kilo in that line
                        if minute > duration:   # save the kilo for later use
                            duration = minute   # find the max kilo
                        else:
                            continue

                        #kilo.append(int(weight[0])) # get the number in the list, and convert to integer and add to list
                    else:
                        continue
    print('In all recipes, the longest baking time is', duration,'minutes')


def longestrecipe(L):
    '''split the file by lines and find the longest line in the recipe.'''
    countline = 0
    recipename = ''

    for element in L:
        dirname, LoD, LoF = element
        # print("dirname is", dirname)
        for file in LoF:
            if file[-3:] == 'txt':
                # print(file)
                fullname = dirname + "/" + file
                # print(fullname)
                content = readfile(fullname)
                #print(content)
                line = content.split('\n')  # read the file and split by the \n -> get each line separately.
                # print(line)
                if len(line) > countline:
                    countline = len(line)
                    recipename = str(fullname)
                else:
                    continue

    folder = recipename.split('/')[1]
    file = recipename.split('/')[2]

    print ('The', file.upper(), 'in folder', folder.upper(), 'is the longest recipe.')
    time.sleep(0.5)
    print('It has', countline, 'lines.')




if True:
    time.sleep(0.5)
    """ run functions/code here... """
    L = list(os.walk("."))
    print()
    print('For the txt files in subfolder')
    time.sleep(1.0)
    num_txt_subfiles = count_txt_infilesind(L)
    num_txt_files = count_txt_exercise(L)
    num_jpg_files = count_jpg_exercise(L)
    num_cat_files = count_cat_exercise(L)
    num_dog_files = count_dog_exercise(L)
    print()
    print('For the files in recipes')
    time.sleep(1.0)
    print("There are", num_txt_files, "txt files.")
    time.sleep(0.5)
    print("There are", num_jpg_files, "jpg files.")
    time.sleep(0.5)
    print("There are", num_cat_files, "files has cat in the file name.")
    time.sleep(0.5)
    print("There are", num_dog_files, "files has dog in the file name.")
    print('!!!')
    print()
    time.sleep(1.0)
    print('For the recipe type:')
    readsavoryorsweet(L)
    print()
    time.sleep(1.0)
    print('Here are three more questions:')
    print('Question A: What is the highest temperature in all recipes?')
    time.sleep(0.5)
    highestdegree(L)
    time.sleep(1.0)
    print('Question B: What is the longest baking time in all recipes?')
    time.sleep(0.5)
    longesttime(L)
    time.sleep(1.0)
    print('Question C: Which one is the longest recipe in all recipes?')
    time.sleep(0.5)
    longestrecipe(L)
    print()
    time.sleep(1.0)
    print('Here is the extra point question:')
    time.sleep(0.5)
    print('For the most kilograms of one ingredient')
    time.sleep(0.5)
    findingredient(L)


