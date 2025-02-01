# with open('example.txt', 'a+') as file:
#     while True:
#         content = input("Enter something to write to the file: or type -1 to Exit: ")
#         if content == '-1':
#             break
#         file.write(content + " ")
        
#     file.seek(0)
#     print(file.read())

# reading a file line by line
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# creating a csv file

# with open('example.txt','w+') as file:
#     content = list(map(str,input("Enter the keys and values separated by spaces:").split()))
#     while content:
#         for i in range(len(content)):
#             if ',' in content[i]:
#                 content[i] = f'"{content[i]}"'
                
#         file.write(','.join(content)+"\n")
                
#         content = list(map(str,input("Enter the keys and values separated by spaces:").split())) 



# with open('example.txt','r') as file:
     
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)

import csv


with open('example.txt', 'w+', newline='') as file:  # Use 'w+' mode
    writer = csv.writer(file)
    
    while True:
        content = input("Enter the keys and values separated by spaces: ").split()
        
        if not content:  # Stop if input is empty or contains only spaces
            break
        
        # Enclose fields with commas in double quotes
        for i in range(len(content)):
            if ',' in content[i]:
                content[i] = f'"{content[i]}"'

        writer.writerow(content)  # Write content correctly

    file.seek(0)  # Move the file pointer back to the beginning
    
    # Read and print file contents
    reader = csv.reader(file)
    for line in reader:
        print(line)  # Print each row in the file

    



