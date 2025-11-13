def is_armstrong_number(number):
    num_power = len(str(number))
    num_list_w_power = []
    for digit in str(number):
        num_list_w_power.append(int(digit) ** num_power)
    new_number = sum(num_list_w_power)
    if new_number ==number:
        return True
    return False