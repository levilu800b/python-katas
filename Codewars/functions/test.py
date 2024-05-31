# # Part 3 - Coding Exercise: Decoding a Message from a Text File
# # In this exercise, you will develop a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string.

# # Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

# # Your function must be able to process an input file with the following format:

# # 3 love
# # 6 computers
# # 2 dogs
# # 4 cats
# # 1 I
# # 5 you
# # In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:

# #   1
# #  2 3
# # 4 5 6
# # The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

# # 1: I
# # 3: love
# # 6: computers
# # and your function should return the string "I love computers".

# # Solution
# # Here is a possible solution for the exercise:

# def decode(message_file):
#     with open(message_file, 'r') as file:
#         lines = file.readlines()
#         decoded_message = []
#         for i in range(1, len(lines) + 1):
#             decoded_message.append(lines[i - 1].split()[1])
#         return ' '.join(decoded_message)
    
# # You can test the function with the following code:

# print(decode('message.txt')) # "I love computers"


def decode(message_file):
    # Step 1: Read the file
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Step 2: Parse the contents into a dictionary
    number_word_map = {}
    for line in lines:
        number, word = line.strip().split()
        number_word_map[int(number)] = word
    
    # Step 3: Determine the positions of the pyramid lines
    pyramid_end_positions = []
    current_line_end = 1
    while current_line_end in number_word_map:
        pyramid_end_positions.append(current_line_end)
        current_line_end += len(pyramid_end_positions) + 1
    
    # Step 4: Extract the words at the end of each pyramid line
    decoded_message = [number_word_map[pos] for pos in pyramid_end_positions]
    
    # Step 5: Return the decoded message as a string
    return ' '.join(decoded_message)

# Example usage
message_file = 'functions/encoded_message.txt'  # Make sure to replace with your actual file path
decoded_message = decode(message_file)
print(decoded_message)
