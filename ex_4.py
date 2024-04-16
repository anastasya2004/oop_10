class RomanNumber:
    """
    This class represents a Roman number converter that can convert Roman numerals to decimal numbers.
    """
    def __init__(self, value):
        """
        Initialize the RomanNumber object with the given value if it is a valid Roman numeral.
        """
        if self.is_roman(value):
            self.rom_value = value
        else:
            print('Ошибка')
            self.rom_value = None

    def decimal_number(self):
        """
        Convert the Roman numeral to a decimal number.
        """
        all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        dec = 0
        rom = self.rom_value
        for i, r in all_roman:
            while rom.startswith(r):
                dec += i
                rom = rom[len(r):]
        return dec
    
    @staticmethod
    def is_roman(value):
        """
        Check if the given value is a valid Roman numeral.
        """
        roman_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for letter in value:
            if letter not in roman_num:
                return False
            if value.count("I") > 3:
                return False
        if not isinstance(value, str):
            return False
        
        return True
    
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
        