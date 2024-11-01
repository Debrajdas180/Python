import periodictable

Atomic_no = int(input("Enter Atomic No."))

element = periodictable.elements[Atomic_no]

print("Name:", element.name)
print("symbol:", element.symbol)
print("Atomic mass:", element.mass)
print("Density:", element.density)
