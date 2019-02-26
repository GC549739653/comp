min_temperature = 0
max_temperature = 300
step = 20
# \t: A tab
print('Celsius\tFahrenheit')
# We let celsius take the values
# - min_temperature
# - min_temperature + step
# - min_temperature + 2 * step
# - min_temperature + 3 * step
# ...
# up to the largest value smaller than max_temperature + step
for Celsius in range(min_temperature, max_temperature + step, step):
    fahrenheit = 9 * Celsius / 5 + 32
    # {:10d}:  celsius as a decimal number in a field of width 10
    # {:7.1f}: fahrenheit as a floating point number in a field of width 7
    #          with 1 digit after the decimal point
    print(f'{Celsius:7d}\t{fahrenheit:10.0f}')

# Output an empty line
print()