a = 60
b = 13
 #bitwise and
and_result = a&b
print(f"bitwise and : {a} & {b} = {and_result} (binary: {bin(and_result)})")

#or result
or_result = a | b
print(f"binary or : {a} | {b}  = {or_result} (binary: {bin(or_result)}")

#xor
xor_result = a^b
print(F"binary xor {a} ^ {b} = {xor_result} (binary :{bin(xor_result)})")

#bitwise not
not_result = ~a
print(F"binary not ~{a} = {not_result} binary- {bin(not_result)}")

#bitwise left shift
left_shift_result = a << 2
print(F"left shift {a} << 2  = {left_shift_result} (bin- {bin(left_shift_result)})")

#right shift