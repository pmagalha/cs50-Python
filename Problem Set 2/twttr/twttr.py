vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def main():
    prompt = input.("")
    shorten(prompt)
    print (prompt)

def shorten(prompt):
    newstr = prompt
    for c in prompt:
        if c in vowels:
            newstr = newstr.replace(c , "")
    return (newstr.lower())

if __name__ == "__main__":
    main()
