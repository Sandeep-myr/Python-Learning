import datetime

x = datetime.datetime.now()

print(x)
print(x.strftime("%A"))
# // printing the perticular time we are using this thing

print("--------------------------------------------------------------------------------------------------------------------------------")

print(x.date)
print(x.day)
print(x.hour)
print(x.year)
print(x.dst)


#  create a date object

y = datetime.date(2022, 12, 25)
print(y)

print("--------------------------------------------------------------------------------------------------------------------------------")

# Weekday as locale's abbreviated name (e.g., Mon, Tue).
print(x.strftime("%a"))  # Example: Mon

# Weekday as locale's full name (e.g., Monday, Tuesday).
print(x.strftime("%A"))  # Example: Monday

# Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
print(x.strftime("%w"))  # Example: 1 (for Monday)

# Day of the month as a zero-padded decimal number (01, 02, ..., 31).
print(x.strftime("%d"))  # Example: 07

# Month as locale's abbreviated name (e.g., Jan, Feb).
print(x.strftime("%b"))  # Example: Jul

# Month as locale's full name (e.g., January, February).
print(x.strftime("%B"))  # Example: July

# Month as a zero-padded decimal number (01, 02, ..., 12).
print(x.strftime("%m"))  # Example: 07

# Year without century as a zero-padded decimal number (00, 01, ..., 99).
print(x.strftime("%y"))  # Example: 24

# Year with century as a decimal number.
print(x.strftime("%Y"))  # Example: 2024

# Hour (24-hour clock) as a zero-padded decimal number (00, 01, ..., 23).
print(x.strftime("%H"))  # Example: 13

# Hour (12-hour clock) as a zero-padded decimal number (01, 02, ..., 12).
print(x.strftime("%I"))  # Example: 01

# AM or PM.
print(x.strftime("%p"))  # Example: PM

# Minute as a zero-padded decimal number (00, 01, ..., 59).
print(x.strftime("%M"))  # Example: 45

# Second as a zero-padded decimal number (00, 01, ..., 59).
print(x.strftime("%S"))  # Example: 30

# Microsecond as a decimal number, zero-padded on the left (000000, 000001, ..., 999999).
print(x.strftime("%f"))  # Example: 123456

# UTC offset in the form +HHMM or -HHMM (empty string if the object is naive).
print(x.strftime("%z"))  # Example: +0000

# Time zone name (empty string if the object is naive).
print(x.strftime("%Z"))  # Example: UTC

# Day of the year as a zero-padded decimal number (001, 002, ..., 366).
print(x.strftime("%j"))  # Example: 189

# Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number (00, 01, ..., 53). All days in a new year preceding the first Sunday are considered to be in week 0.
print(x.strftime("%U"))  # Example: 27

# Week number of the year (Monday as the first day of the week) as a zero-padded decimal number (00, 01, ..., 53). All days in a new year preceding the first Monday are considered to be in week 0.
print(x.strftime("%W"))  # Example: 27

# Locale's appropriate date and time representation.
print(x.strftime("%c"))  # Example: Mon Jul 17 13:45:30 2024

# Century as a decimal number (00, 01, ..., 99).
print(x.strftime("%C"))  # Example: 20

# Locale's appropriate date representation.
print(x.strftime("%x"))  # Example: 07/17/24

# Locale's appropriate time representation.
print(x.strftime("%X"))  # Example: 13:45:30

# A literal '%' character.
print(x.strftime("%%"))  # Example: %

# ISO 8601 year with century as a decimal number.
print(x.strftime("%G"))  # Example: 2024

# ISO 8601 weekday as a decimal number, where 1 is Monday and 7 is Sunday.
print(x.strftime("%u"))  # Example: 1

# ISO 8601 week number of the year (Monday as the first day of the week) as a decimal number.
print(x.strftime("%V"))  # Example: 28
