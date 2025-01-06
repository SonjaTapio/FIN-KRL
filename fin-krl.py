import streamlit as st

finnish_file = "output_fin.txt"
karelian_file = "output_krl.txt"

# Read the files
with open(finnish_file, 'r', encoding='utf-8') as fin_file, open(karelian_file, 'r', encoding='utf-8') as kar_file:
    finnish_words = [line.strip() for line in fin_file]
    karelian_words = [line.strip() for line in kar_file]

# Create the dictionary
verb_dictionary = dict(zip(finnish_words, karelian_words))

# Streamlit app
def main():
    st.image("fin-krl-logo.png", width=700)
    # Input field for Finnish word
    finnish_word = st.text_input("Enter a Finnish verb:")

    # Translation logic
    if finnish_word:
        karelian_translation = verb_dictionary.get(finnish_word.strip())
        if karelian_translation:
            st.success(f"{karelian_translation}")
        else:
            st.error(f"'{finnish_word}' does not exist in the dictionary. Try another verb.")

if __name__ == "__main__":
    main()
