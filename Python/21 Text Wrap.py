import textwrap

def wrap(string, max_width):
    # silly me didn't notice the textwrap import...
	
    wrapped_strings = list()
    for i in range(0, len(string), max_width):
        wrapped_strings.append(string[i:i+max_width])
    return "\n".join(wrapped_strings)
	
	# another, more pythonic way is to use list comprehension
	# but using built-in library is the most pythonic way, which is:
	
    # wrapped_str = textwrap.fill(string, max_width)
    # return wrapped_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
