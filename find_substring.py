def count_substring(string, sub_string):
    pos = 0
    cor_list = []

    for x in range(0,len(string)):
        
        res = (string.find(sub_string,pos,len(string)))
        #print("pos: {}  res :{}".format(pos,res))
        
        if res != -1 :
            if res not in cor_list:
                cor_list.append(res)
            pos += 1

    #print("cor_list : {}".format(cor_list))
        
    return len(cor_list)

print(count_substring("abcabcabc","abc"))