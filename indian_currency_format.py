from decimal import Decimal

def indian_currency_format(number):
    # Convert input to Decimal (if not already)
    num = Decimal(str(number))  # always convert number to string first for precision

    # Convert Decimal to fixed-point string representation
    num_str = format(num, 'f')  # e.g. '123456.7890'

    # Now safe to do string operations
    if '.' in num_str:
        int_part, dec_part = num_str.split('.')
        dec_part = '.' + dec_part
    else:
        int_part = num_str
        dec_part = ''

    neg = ''
    if int_part.startswith('-'):
        neg = '-'
        int_part = int_part[1:]

    if len(int_part) <= 3:
        return neg + int_part + dec_part
    else:
        last_three = int_part[-3:]
        rest = int_part[:-3]
        rest_parts = []
        while len(rest) > 2:
            rest_parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            rest_parts.insert(0, rest)
        formatted_int = ','.join(rest_parts) + ',' + last_three
        return neg + formatted_int + dec_part

# Example usage
if __name__ == "__main__":
    print(indian_currency_format(123456.7891))          # 1,23,456.7891
    print(indian_currency_format(1234567890.12))        # 1,23,45,67,890.12
    print(indian_currency_format(-9876543.21))          # -98,76,543.21
