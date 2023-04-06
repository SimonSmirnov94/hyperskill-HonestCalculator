
msg_one = 'Enter an equation'
msg_two = 'Do you even know what numbers are? Stay focused!'
msg_three = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_four = 'Yeah... division by zero. Smart move...'
msg_five = 'Do you want to store the result? (y / n):'
msg_six = 'Do you want to continue calculations? (y / n):'

msg_seven = " ... lazy"
msg_eight = " ... very lazy"
msg_nine = " ... very, very lazy"
msg_ten = "You are"

msg_eleven = "Are you sure? It is only one digit! (y / n)"
msg_twelve = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_thirteen = "Last chance! Do you really want to embarrass yourself? (y / n)"

opearators = ['/', '*', '**', '+', '-', '%']
loop = True


memory = 0
result = 0

# -10 > v < 10 ; и интеджер 
# bool1: 0й и 2й  eq is_one_digit = msg + msg7
# bool2: или 0й, или 2й eq 1 = msg + msg8
# bool3: (0й или 2й eq 0) and (1й = '*', or '+', or '-')
# bool4: 

def check_message(digits):
    msg = ""

    if is_one_digit(digits[0]) and is_one_digit(digits[2]):
        msg = msg + msg_seven
    if (digits[0] == 1 or digits[2] == 1) and digits[1] == '*':
        msg = msg + msg_eight
    if (digits[0] == 0 or digits[2] == 0) and (digits[1] == '*' or digits[1] == '+' or digits[1] == '-'):
        msg = msg + msg_nine
    
    if msg != "":
        msg = msg_ten + msg

        print(msg)
    else:
        pass

def check_message_to_store():

    answer_loop = True
    final_result = True

    while answer_loop:

        answer = input(msg_eleven)

        if answer.lower() == 'y':
            answer = input(msg_twelve)
            if answer.lower() == 'y':
                answer = input(msg_thirteen)
                if answer.lower() == 'y':
                    final_result = True
                    answer_loop = False
                elif answer.lower() == 'n':
                    final_result = False
                    answer_loop = False
            elif answer.lower() == 'n':
                answer_loop = False
                final_result = False
        elif answer.lower() == 'n':
            answer_loop = False
            final_result = False

    return final_result




def is_one_digit(v):
    result = float(v).is_integer() and v > -10 and v < 10
    # result = v.is_integer() and v > -10 and v < 10

    if result:
        output = True
    else:
        output = False

    return output

def operation(op):
# функция операции калькулятора. Вывод результа кулькуляции + msg``

    global result
    global memory
    op_loop = True

    first_m = op[0].lower() == 'm'
    second_m = op[2].lower() == 'm'

    

    if first_m and not second_m:
         num_one = memory
         num_two = float(op[2])
    elif second_m and not first_m:
         num_two = memory
         num_one = float(op[0])
    elif second_m and first_m:  
        num_one = memory
        num_two = memory
    else:  
        num_one = float(op[0])
        num_two = float(op[2])

    
    if (op[1] == '/') and num_two == 0:
        result = msg_four
        op_loop = False

    elif op[1] == '/':
         result = num_one / num_two

    elif op[1] == '*':
         result = num_one * num_two

    elif op[1] == '**':
         result = num_one ** num_two

    elif op[1] == '+':
         result = num_one + num_two

    elif op[1] == '-':
         result = num_one - num_two
    
    elif op[1] == '%':
         result = num_one % num_two

    check_list = [num_one, op[1], num_two]

    check_message(check_list)
    print(result)
    return op_loop
    
def store_and_calculation(memory_input):
# заврешающий метод, в него входят два цикла: 1й сохранение в М 2й продолжить вычисления. Return - bool основного цикла

    loop_store = True
    loop_calculation = True
    main_loop = True
    global memory


    while loop_store:

        store_result = input(msg_five)

        

        if store_result.lower() == 'y':
            
            confirmation_to_store = True

            check_number = memory_input

            if is_one_digit(check_number):
                confirmation_to_store = check_message_to_store()
            
            if confirmation_to_store:
                memory =  memory_input
                loop_store = False
            else:
                loop_store = False
            
        elif store_result.lower() == 'n':
            loop_store = False

    


    while loop_calculation:
         calculation_result = input(msg_six)

         if calculation_result.lower() == 'y':
              main_loop = True
              loop_calculation = False

         elif calculation_result.lower() == 'n':
              main_loop = False
              loop_calculation = False

    return main_loop


while loop:
# основной цикл: try - обработка ошибок input + вызов завершающего метода

    print(msg_one)
    equation = input()
    elements = equation.split()
    is_error = True
    output = True

    try:
        m_type = (elements[2].lower() == 'm') or (elements[0].lower() == 'm')

        if m_type:
            pass
        else:
            check_one, check_two = float(elements[0]), float(elements[2])

    except (ValueError, IndexError):
        print(msg_two)
        is_error = False

    else:
        if (elements[1] in opearators) == False:
            print(msg_three)
            is_error = False
             
        else:
            output = operation(elements)

    if output and is_error:
        loop = store_and_calculation(result)

   
    

