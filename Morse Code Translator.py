import tkinter
from tkinter import IntVar, END

# Define window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.geometry('500x350')
root.resizable (0 , 0)

# Define fonts colors
button_font = ('Cambri', 10)
root_color = "#EED5B7"
frame_color = "#FF7F24"
button_color = "#CD6600"
text_color = "#f8f8ff"
root.config(bg=root_color)

#Our Class 
class MorseCode:
  def __init__(self,input_text,language,output_text):

    self.input_text = input_text
    self.output_text = output_text
    self.language = language
    self.english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': ' ', '|': '|', "": ""}

    self.morse_to_english = dict([(value, key) for key, value in self.english_to_morse.items()])
      
  def encode(self,text):
    morse_code = ""
    # Remove any letters of symbols not in our dict keys
    for letter in text:
      if letter not in self.english_to_morse.keys():
        text = text.replace(letter, '')

    # Break up into individual words based on space " " and put into a list
    word_list = text.split(" ")

    # Turn each individual word in word_list into a list of letters
    for word in word_list:
      letters = list(word)
      # For each letter, get the morse code representation and append it to the string morse_code
      for letter in letters:
        morse_char = self.english_to_morse[letter]
        morse_code += morse_char
        # Seperate individual letters with a space
        morse_code += " "
      # Seperate individual words with a |
      morse_code += "|"

    output_text.insert("1.0", morse_code)

  def decode(self,text):
    english = ""
  
    # Remove any letters or symbols not in our dict keys
    for letter in text:
      if letter not in self.morse_to_english.keys():
        text = text.replace(letter, '')

    # Break up each word based on | and put into a list
    word_list = text.split("|")

    # Turn each word into a list of letters
    for word in word_list:
      letters = word.split(" ")
        # For each letter, get the English representation and add it to the string English
      for letter in letters:
        english_char = self.morse_to_english[letter]
        english += english_char
      # seperate individual words with a space
      english += " "

    output_text.insert("1.0", english)

  def convert(self):
    """Call the appropriate conversion function based off radio button values"""
    self.clearCon()
    text = input_text.get("1.0", END)
    text = text.lower()
    # English to morse code:
    if language.get() == 1:
      self.encode(text)
      
    elif language.get() == 2:
      self.decode(text)

  def clearCon(self):
    self.output_text.delete("1.0", END)
    
  def clear(self):
    """Clear both text fields"""
    self.input_text.delete("1.0", END)
    self.output_text.delete("1.0", END)

input_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16, 8))
output_frame.pack(padx=16, pady=(8, 16))

# Layout for the input frame
input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)



english_button = tkinter.Radiobutton(input_frame, text="     Morse To English          ", variable=language, value=2, font=button_font, bg=frame_color)
english_button.grid(row=1, column=0)

english_button = tkinter.Radiobutton(input_frame, text="     English To Morse          ", variable=language, value=1, font=button_font, bg=frame_color)
english_button.grid(row=0, column=0)

# Layout for the output frame
output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

# Calling the class 
M = MorseCode(input_text,language, output_text)

convert_button = tkinter.Button(output_frame, text="Translate", font=button_font, bg=button_color, command=M.convert)
clear_button = tkinter.Button(output_frame, text="Clear", font=button_font, bg=button_color, command=M.clear)
quit_button = tkinter.Button(output_frame, text="Exit", font=button_font, bg=button_color, command=root.destroy)
convert_button.grid(row=0, column=0, padx=10, ipadx=50)  # convert ipadx defines column width
clear_button.grid(row=2, column=0, padx=10, sticky="WE")
quit_button.grid(row=3, column=0, padx=10, sticky="WE")

# Run the root window's main loop
root.mainloop()

