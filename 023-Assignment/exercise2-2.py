import datetime

idCards=["420821198411300017",\
"42082119680628004X",\
"422432197608280034",\
"420821196509095016",\
"441402196304056047",\
"420821196802056018",\
"420821199109136038",\
"420821196907246043",\
"441402196711030119",\
"42243219700222007X",\
"420821196302280513",\
"420821196401252323",\
"420821197403116020",\
"420821197208166030",\
"420821196610282318",\
"441402197805295552",\
"420821198211202359",\
"422432197207090045",\
"422432197101040517",\
"441402197601160515",\
"422432198107210526",\
"422432197009190096"]   

def get_nums_of_men_and_women(idCards):
    nums_men = nums_women = 0
    for id in idCards:
        if int(id[-2]) % 2 == 0:
            nums_women += 1
        else:
            nums_men += 1
    return nums_men, nums_women

def get_age(id):
    now = datetime.date.today()
    birthday = datetime.date(int(id[6:10]), int(id[10:12]), int(id[12:14]))
    age = (now - birthday).days
    return age

def sort_idCards(idCards):
    return sorted(idCards, key = lambda x : get_age(x))

def nums_areas(idCards):
    idCards = [id[:6] for id in idCards]
    return len(set(idCards))

def verification(idCards):
    error = []
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ver_dict = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6',7:'5', 8:'4', 9:'3', 10:'2'}
    for id in idCards:
        sum = 0
        verification_number = id[-1]
        id_int = [int(i) for i in id[:-1]]
        for i in range(len(id_int)):
            sum += factors[i] * id_int[i]
        remainder = sum % 11
        if ver_dict[remainder] != verification_number:
            id = id[:-1] + ver_dict[remainder]
            error.append(id)
    return error, idCards



nums_m, nums_w = get_nums_of_men_and_women(idCards)
error, idCards = verification(idCards)
# print('nums of men : {}\nnums of women : {}'.format(nums_m, nums_w))
# print('sorted idCards : ', sort_idCards(idCards))
# print('nums of areas : {}'.format(nums_areas(idCards)))
print('error : ', error)
print('idCards : ', idCards)