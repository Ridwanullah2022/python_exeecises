s = "hello word"
to_be_found = "l"
for i in range(len(s)):

    if s[i] == to_be_found:
        print(f"{s[i]} was found at index {i}")
        break
else:
        print(f"Sorry I could not found '{to_be_found}")

