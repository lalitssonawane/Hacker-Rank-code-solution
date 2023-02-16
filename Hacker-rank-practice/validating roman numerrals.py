#You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.



regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'    # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))