import pandas

morse_df = pandas.read_csv("morse.csv")
morse_dict = {row.letter: row.code for (index, row) in morse_df.iterrows()}


def generate_morse():
    word = input("Put in your word here: ").upper()
    try:
        output_list = [morse_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters and numbers please.")
        generate_morse()
    else:
        print(" ".join(output_list))


generate_morse()
