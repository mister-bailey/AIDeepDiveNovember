import fun_file

print("Imported functions:")
help(fun_file.convert_to_string)
help(fun_file.overlap)
help(fun_file.make_pancakes)

s = fun_file.convert_to_string(33) + fun_file.convert_to_string(type(33))
print(s)

overlap1 = fun_file.overlap([2,3,5,1,2,7,5],[9,0,2,'yes',7])
print(overlap1)

overlap2 = fun_file.overlap([1,2,4,1,8],['yes',0,7,'no'])
print(overlap2)

print(fun_file.make_pancakes(overlap1))

try:
    print(fun_file.make_pancakes(overlap2))
except Exception as e:
    print(e)

try:
    print(fun_file.make_pancakes((1,2,3)))
except Exception as e:
    print(e)