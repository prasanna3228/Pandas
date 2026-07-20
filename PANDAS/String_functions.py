import pandas as pd

df = pd.DataFrame({
    'name': ["prasanna", "praveen", "prashanth"],       
    'salary': [50000, 60000, 70000],
    'age': [20, 30, 40],
    'designation': ['developer', 'manager', 'analyst']
})

# String functions in pandas
# Convert to uppercase  
df['name'] = df['name'].str.upper()
print(df)
# Convert to lowercase
df['name'] = df['name'].str.lower()
print(df)
# Get the length of each string
df['name_length'] = df['name'].str.len()
print(df)
# Check if the string contains a specific substring
df['contains_pras'] = df['name'].str.contains('pras')
print(df)
# Replace a substring with another substring
df['name'] = df['name'].str.replace('pras', 'praveen')
print(df)
# Split the string into a list of substrings
df['name_split'] = df['name'].str.split(' ')
print(df)
# Get the first character of each string
df['first_char'] = df['name'].str[0]
print(df)
# Get the last character of each string
df['last_char'] = df['name'].str[-1]
print(df)
# Get the substring from index 1 to 3
df['substring'] = df['name'].str[1:4]
print(df)
# Check if the string starts with a specific substring
df['starts_with_p'] = df['name'].str.startswith('p')
print(df)
# Check if the string ends with a specific substring
df['ends_with_n'] = df['name'].str.endswith('n')
print(df)
# Get the number of occurrences of a specific substring
df['count_a'] = df['name'].str.count('a')
print(df)
# Get the index of the first occurrence of a specific substring
df['index_of_a'] = df['name'].str.find('a')
print(df)
# Get the index of the last occurrence of a specific substring
df['last_index_of_a'] = df['name'].str.rfind('a')
print(df)
# Get the string in reverse order
df['name_reversed'] = df['name'].str[::-1]
print(df)
# Get the string with leading and trailing whitespace removed
df['name_stripped'] = df['name'].str.strip()
print(df)
# Get the string with leading whitespace removed
df['name_lstrip'] = df['name'].str.lstrip()
print(df)
# Get the string with trailing whitespace removed
df['name_rstrip'] = df['name'].str.rstrip()
print(df)
# Get the string with all occurrences of a specific substring removed
df['name_removed_pras'] = df['name'].str.replace('pras', '')
print(df)
