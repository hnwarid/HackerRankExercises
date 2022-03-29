if __name__ == '__main__':
    s = input()

def check_string(string):
    methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    results = list()
    for method in methods:
        result = any(method(char) for char in string)
        results.append(str(result))
    return "\n".join(results)    

print(check_string(s))
