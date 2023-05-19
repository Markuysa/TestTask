# operations is a list of allowed operations
operations = ['','+','-']
# this function calculates the indexes
# of operations that will be inserted
# between the numbers in the row
def calculate_indexes(length):
    base = len(operations)
    result_indexes = ''
    while length > 0:
        # calc a new position
        result_indexes = str(length % base) + result_indexes
        # decrease the length
        length //= base
    return result_indexes

# create expression function
# forms the result expression that will be
# tested for equality to 200 later
def create_expression(k):
    # calculating the operations indexes
    indexes_list = list(calculate_indexes(k))
    operation_positions = [''] * 9
    for i in range(1, 10):
        temp = i - 1
        # * -1 to get the number in desc order from the beginning
        i *= (-1)
        # if the condition is true => take the operation corresponding to index i
        if temp < len(indexes_list):
            element = int(indexes_list[i])
            operation_positions[i] = operations[element]
        # otherwise => set the operation ''
        else:
            operation_positions[i] = ''
    # form the expression
    result_expression = ''
    for i in range(9):
        result_expression += f'{9-i}{operation_positions[i]}'
    result_expression += '0'
    return result_expression

# this algo works with n ** 9 complexity ( where n is the number of operations )
# calculate_result function calcs the whole permutations and outputs the correct ones
def calculate_result():
    results_dictionary = {}
    for i in range(len(operations)**9):
        expression = create_expression(i)
        # eval calculates the expression
        result = eval(expression)
        # if the result number is in result dictionary => add the expression to the list
        if result in results_dictionary:
            results_dictionary[result].append(expression)
        # otherwise => set the expression to the list
        else:
            results_dictionary[result] = [expression]
    if RESULT_NUMBER in results_dictionary:
        return results_dictionary[RESULT_NUMBER]
    else:
        return None

if __name__ == '__main__':
    global RESULT_NUMBER
    RESULT_NUMBER = 300
    print('\n'.join(calculate_result()))
