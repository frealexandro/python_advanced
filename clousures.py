

import string


def make_repeater_of(n):
    def repeater(string):
        assert type(string)== str , "solo puedes utilizar cadenas "
        return string * n
    return repeater





def run ():
    
    

    repeat_5 =  make_repeater_of(5)
    print (repeat_5(3))



if __name__=='__main__':
    run()