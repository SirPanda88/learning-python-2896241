def isPalindrome(testStr):
    if testStr == testStr[::-1]:
        return True
    return False
    
run = True
while run:
    inputStr = input("Enter string to test for palindrome or 'exit':")
    
    if inputStr == "exit":
        run = False
        break
    
    inputStr = inputStr.lower()

    cleanStr = ""
    for char in inputStr:
        if char.isalnum:
            cleanStr += char
    
    print("Palindrome test:", isPalindrome(cleanStr))
