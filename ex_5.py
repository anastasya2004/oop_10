class RomanNumber:
    """
    This class represents a Roman number converter that can convert Roman numerals to decimal numbers and vice versa.
    """
    all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def __init__(self, value):
        """
        Initialize the RomanNumber object with the given value if it is a valid Roman numeral or integer.
        """
        if self.is_roman(value):
            self.rom_value = value
            self.int_value = None
        elif self.is_int(value):
            self.rom_value = None
            self.int_value = value
        else:
            print('Ошибка')
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Convert the Roman numeral to a decimal number.
        """
        dec = 0
        rom = self.rom_value
        for i, r in RomanNumber.all_roman:
            while rom.startswith(r):
                dec += i
                rom = rom[len(r):]
        return dec
    
    def roman_number(self):
        """
        Convert the integer to a Roman numeral.
        """
        roman = ''
        num = self.int_value
        while num > 0:
            for i, r in RomanNumber.all_roman:
                while num >= i:
                    roman += r
                    num -= i
        return roman

    @staticmethod
    def is_roman(value):
        """
        Check if the given value is a valid Roman numeral.
        """
        roman_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for letter in str(value):
            if letter not in roman_num:
                return False
            if value.count("I") > 3:
                return False
        if not isinstance(value, str):
            return False
        
        return True
        
    @staticmethod
    def is_int(value):
        """
        Check if the given value is a valid integer within the range of Roman numerals.
        """
        if type(value) == int and 0 < value < 4000:
            return True
        else:
            return False
        
    def __str__(self):
        """
        Return the Roman numeral as a string.
        """
        return str(self.rom_value)

    def __repr__(self):
        """
        Return the representation of the RomanNumber object as a string.
        """
        return self.__str__()