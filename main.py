# Código do dev aqui

def list_comprehension_exercise_1():
    result = [i for i in range(11)]
    return result

list_comprehension_exercise_1()


def list_comprehension_exercise_2():
    result  = [i for i in range(22) if i % 2 == 0 or i % 3 == 0]
    return result

list_comprehension_exercise_2()


def list_comprehension_exercise_3():
    result = [i for i in range(-5, 32) if i % 2 != 0 and i % 5 != 0]
    return result

list_comprehension_exercise_3()


def list_comprehension_exercise_4():
    result = [i*i for i in range(11)]
    return result

list_comprehension_exercise_4()

sentence5 = 'O Rato Rui Gosta De QueiJo FresQuiNho'
def list_comprehension_exercise_5(sentence5):
    result = [letter for letter in sentence5 if letter.isupper()]
    return result

list_comprehension_exercise_5(sentence5)

sentence6 = 'o rato rui roeu a roupa do rei de roma'
def list_comprehension_exercise_6(sentence6):
    result = [word for word in sentence6.split(' ') if word[0] == 'r' and len(word) >= 4]    
    return result

list_comprehension_exercise_6(sentence6)


