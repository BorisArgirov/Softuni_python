def palindrome_found(word):
    if word == word[::-1]:
        return word

given_words = input().split()
given_palindrome = input()

palindrome_list = [word for word in given_words if palindrome_found(word)]
palindrome_count = palindrome_list.count(given_palindrome)

print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")