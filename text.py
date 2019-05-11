with open('log_files/201711133020.log','rb') as f:
    h = 0
    for line in f:
        date = f.readline()
        date = date[26:38]
   
        #date_str = str(date,encoding="uft8") 失败
        date_str = bytes.decode(date)
        #print(date_str)

        if date_str=='201711133020':
            h=h+1
            #print("called")

    print(h)