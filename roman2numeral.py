# Task 
"""
Create a RomanNumerals helper that can convert a roman numeral to and from an integer value. The class should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples:

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
"""

R2N = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


N2R= [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
]

class Roman2Numerals(object):
    """
    Roman2Numeral and Numeral2Roman converter
    """

    @staticmethod
    def numeral_to_roman(number):
        """
        This function converts numeral integer to ROMAN format.
        :param number: Numeric (Integer)
        :return: Roman format (String)
        """
        result = ''
        for i, (numeric, roman) in enumerate(TO_ROMAN):
            current = number//numeric
            if current:
                if str(number)[0] == '4':
                    result += roman + N2R[i - 1][1]
                    number -= numeric + N2R[i - 1][0]
                elif str(number)[0] == '9':
                    result += N2R[i + 1][1] + N2R[i - 1][1]
                    number -= N2R[i + 1][0] + N2R[i - 1][0]
                else:
                    result += roman*current
                    number -= numeric*current
        return result

    @staticmethod
    def roman_to_numeral(number):
        """
        This function converts ROMAN format string to Numeral integer.
        :param number: Roman format (String)
        :return: Numeral (Integer)
        """
        result = 0
        i = 0
        while i < len(number):
            current = FROM_ROMAN[number[i]]
            try:
                following = R2N[number[i+1]]

                if current >= following:
                    result += current
                else:
                    result += following - current
                    i += 1
            except IndexError:
                result += current
            finally:
                i += 1
        return result
