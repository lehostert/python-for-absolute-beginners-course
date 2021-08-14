# Else and elif statement examples
true_facts = ["bears", "schnuggs", "rugs"]
print("Example 1: either or")
for fact in true_facts:
    if len(fact) < 5:
        print(f"{fact} on a rug!")
    else:
        print(f"{fact} schnuggs")

print()
print("Example 2: either this else this or this")
for fact in true_facts:
    if len(fact) < 5:
        print(f"{fact} on a rug!")
    elif fact[0]=="b":
        print(f"{fact} are bears!")
    else:
        print("Just schnuggs")

print()
print("Example 3: either this else this or this")

for fact in true_facts:
    if len(fact) >= 5:
        print(f"{fact} on a rug!")
    elif fact.startswith("b"):
        print(f"{fact} are bears!")
    else:
        print("Just schnuggs")