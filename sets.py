#union sets 
my_set1 = {3,4,5}
my_set2 = {5,6,7}
my_set3 = my_set1 | my_set2
print(my_set3)


#interseccion

my_set1 = {3,4,5}
my_set2 = {5,6,7}
my_set3 = my_set1 & my_set2
print(my_set3)

#diferencia 
my_set1 ={3,4,5}
my_set2 ={5,6,7}
my_set3 = my_set1 - my_set2
print(my_set3)
my_set3 = my_set2 - my_set1
print(my_set3)

#diferencia simetrica
my_set1 ={3,4,5}
my_set2 ={5,6,7}
my_set3 = my_set1  ^ my_set2
print(my_set3)

def del_duplicates(random_list):
    return list(set(random_list))


def main():
    random_list = [ 11, 55, 2, 2, 55]
    print(del_duplicates(random_list))


if __name__ == '__main__':
    main()
