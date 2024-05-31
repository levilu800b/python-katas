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


def decode(message_file):
    """
  Decodes a message from a .txt file with numbered words.

  Args:
      message_file (str): Path to the text file containing the encoded message.

  Returns:
      str: The decoded message.
  """
    # Initialize variables
    message = {}
    pyramid_order = []

    # Read the message file
    with open(message_file, 'r') as file:
        for line in file:
            # Split, handling potential extra spaces
            split_line = line.strip().split()
            if len(split_line) > 2:  # More than one word after split
                continue  # Skip lines with extra words
            elif len(split_line) < 2:  # No space or empty line
                continue
            number, word = split_line
            number = int(number)
            # Store word and track order
            message[number] = word
            pyramid_order.append(number)

    # Sort the order of numbers
    pyramid_order.sort()

    # Build the decoded message
    decoded_message = ""
    current_index = 0
    for level in range(1, len(pyramid_order) + 1):
      if current_index + level - 1 >= len(pyramid_order):  # Check for index out of range
        break  # Exit the loop if index is out of bounds
      decoded_message += message[pyramid_order[current_index + level - 1]] + " "
      current_index += level

    return decoded_message.strip()


# Example usage
decoded_message = decode(
    "/Users/levicharles/Documents/python-katas/Open Challenge/Decode message/encoded_message.txt")  # Replace "message.txt" with your actual file path
print(decoded_message)
