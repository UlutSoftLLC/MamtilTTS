""" from https://github.com/keithito/tacotron

Defines the set of symbols used in text input to the model.
"""
# _pad = "_"
# _punctuation = ';:,.!?¡¿—…"«»“” '
# _letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# _letters_ipa = (
#     "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
# )



# kyr

_pad        = '_'
_punctuation = '!\'(),.:;?!¡¿—…"«»“” '
_special = '-'
_letters = 'абвгдеёжзийклмнңоөпрстуүфхцчшщьыъэюя'

# Export all symbols:
# symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters)

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_special)
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)


# Special symbol ids
SPACE_ID = symbols.index(" ")
