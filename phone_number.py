import re

# phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phone_num_regex.search('My number is 415-555-4242')
# print(f"Phone number found: {mo}")
# print(f"Phone number found: {mo.group()}")


# grouping with prentheses

# phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo = phone_num_regex.search('My number is 415-555-4242')

# print(mo.group())
# print(mo.group(0))
# print(mo.group(1))
# print(mo.group(2))

# area_code, man_number = mo.groups()
# print(area_code)
# print(man_number)

phone_num_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phone_num_regex.search('My number is (415) 555-4242')
print(mo.group(1))

