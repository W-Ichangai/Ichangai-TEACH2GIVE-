"""Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.
"""
def capitalize_words():
  """
  This function prompts the user for input, capitalizes the first letter of each word, and returns the result string.
  """

  # Prompt the user for input.
  text = input("Enter a string: ")

  # Split the string into words.
  words = text.split()

  # Capitalize the first letter of each word.
  capitalized_words = [word.capitalize() for word in words]

  # Join the capitalized words back into a string.
  return " ".join(capitalized_words)

# Call the function to get the capitalized text.
capitalized_text = capitalize_words()
print(capitalized_text)
