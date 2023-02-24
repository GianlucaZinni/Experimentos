import re

file = open('duracion.txt', encoding="utf8")
count = 0
list_info = []
list_rating = []

for line in file:
    count += 1
    
    words = line.split()

    if len(words) == 0:
        continue
    
    if words[-1] == "*Relleno":
        
        words = words[0:2]
        words.append("Relleno")
        words[0] = re.sub("(\.)", "", words[0])
        words[0] = int(words[0])
        list_info.append(words)
    
    elif words[-1] == "Recopilatorio":
        words = words[0:2]
        words.append("Recopilatorio")
        words[0] = re.sub("(\.)", "", words[0])
        words[0] = int(words[0])
        list_info.append(words)
        
    else:
        filter1 = re.search("[0-9]", words[0])
        
        if filter1 is not None:
            
            digits = len(words[0])
            
            if "-" in words[0]:
                continue
            else:
                if "*Mixto," in words:
                    episode = words[0]
                    time = words[1]
                    mixto = ' '.join(words[2:])
                    words.clear()
                    words.append(episode); words.append(time); words.append(mixto)
                    words[0] = re.sub("(\.)", "", words[0])
                    words[0] = int(words[0])
                    list_info.append(words)
                
                else:
                    words[0] = re.sub("(\.)", "", words[0])
                    words[0] = int(words[0])
                    list_info.append(words[0:2])

            # if count == 2:
            #     break

# for item in list_info:
    
#     print(item[0])

file1 = open('onepiece_episode_ratings.txt', encoding="utf8")

for line in file1:
    
    line = line.split(" ~ ")
    filter = line[1].strip().replace('\n', '')
    line[1] = filter
    
    list_rating.append(line)

for i in range(len(list_info)):
    
    for j in range(len(list_rating)):
        
        if int(list_info[i][0]) == int(list_rating[j][0]):
            
            rating = list_rating[j][1]
            
            list_info[i].append(rating)

# for item in list_info:
#     print(item)
    
    
            
def is_numeric(some_string):
    try:
        float(some_string)
        return True
    except ValueError:
        return False

file = open('onepiece_data.txt', "w+")
for item in list_info:
    if len(item) == 2:
        file.write("Episodio: " + str(item[0]) + " ~ " + str(item[1]) + "\n")
        
    elif len(item) == 3:
        
        if item[2] == "Relleno" or item[2] == "Recopilatorio":
                file.write("Episodio: " + str(item[0]) + " ~ " + str(item[1]) + " ~ " + str(item[2]) + "\n")
            
        elif is_numeric(item[2]):        
            file.write("Episodio: " + str(item[0]) + " ~ " + str(item[1]) + " ~ Rating: " + str(item[2]) + "\n")
            
        else:
            file.write("Episodio: " + str(item[0]) + " ~ " + str(item[1]) + " ~ " + str(item[2]) + "\n")

    else:
        file.write("Episodio: " + str(item[0]) + " ~ " + str(item[1]) + " ~ " + str(item[2]) + " ~ Rating: " + str(item[3]) + "\n")

            

file.close()