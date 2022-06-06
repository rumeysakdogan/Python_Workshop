def isValid(s):
    bracket_map={"(":")", "[":"]", "{":"}"}
    opening_par =set(["(", "[", "{"])
    stack =[]
    for i in s:
        if i in opening_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

combination = input('Write a string that contains only `(`, `)`, `{`, `}`, `[` and `]`: ')
print(isValid(combination))
