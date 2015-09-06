import uuid

def create_code(num=200):
    result = []
    no = 0
    while no < num:
        temp = str(uuid.uuid1()).replace('-','')
        if not temp in result:
            result.append(temp)
            no +=1
    return result
if __name__ == '__main__':
    print len(create_code())


    
