'''movies=['movie_1','movie_2',['movie_3','movie_4',['movie_5','movie_6']]]'''

def unzip(data,level=0):
    '''解串列+縮排函式'''
    for each_data in data:
        if type(each_data) == list:
            unzip(each_data,level+1)
        else:
            print(' '*level*3,end='')
            print(each_data)