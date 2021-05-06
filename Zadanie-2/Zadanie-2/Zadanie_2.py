def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter the text: ")
if(is_palindrome(something)):
    print("Yes, it's a palindrome")
else:
    print("No, it's a palindrome")