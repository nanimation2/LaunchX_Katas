fact = 'The Moon has no atmosphere.'
two_facts =""
two_facts= fact + 'No sound can be heard on the Moon.'
print(two_facts)

moon_fact= 'The "near side" is the part of the Moon that faces the Earth'
moon_visible_surface = """We only see about 60% of the Moon's surface, this is known as the "near side"."""
print (moon_visible_surface)

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
multiline_two = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline_two)

'temperatures and facts about the moon'.title()
heading = 'temperatures and facts about the moon'
heading.title()
print(heading)

temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures .split('\n'))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

print(temperatures.find('Mars'))

mars_temperature = 'The highest temperature on Mars is about 30 C'
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

        
'-60'.startswith('-')

