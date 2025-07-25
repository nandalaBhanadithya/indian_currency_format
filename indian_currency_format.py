def indian_currency_format(number):
    # Split integer and decimal parts
    num_str = str(number)
    if '.' in num_str:
        int_part, dec_part = num_str.split('.')
        dec_part = '.' + dec_part
    else:
        int_part = num_str
        dec_part = ''
        
    # If negative, handle separately
    neg = ''
    if int_part.startswith('-'):
        neg = '-'
        int_part = int_part[1:]

    # If integer part is less than 4 digits, return as is
    if len(int_part) <= 3:
        return neg + int_part + dec_part
    else:
        # First three digits from the right
        last_three = int_part[-3:]
        rest = int_part[:-3]
        # Now add commas after every two digits in the rest part
        rest_parts = []
        while len(rest) > 2:
            rest_parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            rest_parts.insert(0, rest)
        formatted_int = ','.join(rest_parts) + ',' + last_three
        return neg + formatted_int + dec_part

# Example usage
print(indian_currency_format(123456.7891))          # 1,23,456.7891
print(indian_currency_format(1234567890.12))        # 1,23,45,67,890.12
print(indian_currency_format(-9876543.21))          # -98,76,543.21
