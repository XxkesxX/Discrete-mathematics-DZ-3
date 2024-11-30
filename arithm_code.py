from math import ceil, log2, prod
from decimal import *


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class CharacterRange(Range):
    def __init__(self, char, start, end):
        super().__init__(start, end)
        self.char = char


def generate_char_ranges(freqs):
    char_ranges = {}
    current_start = Decimal('0')
    for char, prob in freqs.items():
        current_end = current_start + prob
        char_ranges[char] = CharacterRange(char, current_start, current_end)
        current_start = current_end
    return char_ranges


def compute_char_frequencies(encoded_word):
    length = len(encoded_word)
    freq_dict = {}
    for letter in encoded_word:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1
    for letter in freq_dict:
        freq_dict[letter] = Decimal(freq_dict[letter]) / Decimal(length)
    chance = sum(freq_dict.values())
    return dict(sorted(freq_dict.items(), key=lambda x: x[1]))


def encode_arithm(encoded_word):
    freqs = compute_char_frequencies(encoded_word)
    char_ranges = generate_char_ranges(freqs)
    print("\n\t\t\tИнтервалы начальные:")
    for char_range in char_ranges.values():
        print(f"{char_range.char}: {str(char_range.start).ljust(31, " ")} - {char_range.end}")

    print("\n\n\n\n\t\t\tИнтервалы конечные:")
    print("\n\t\tleft", "\t\t\t\tright")
    overall_range = Range(Decimal('0'), Decimal('1'))
    for step, char in enumerate(encoded_word):
        prev_start = overall_range.start
        prev_end = overall_range.end
        range_width = overall_range.end - overall_range.start
        overall_range = Range(
            overall_range.start + range_width * char_ranges[char].start,
            overall_range.start + range_width * char_ranges[char].end
        )
        print(f"{char}: [{str(overall_range.start).ljust(31, " ")}, {str(overall_range.end)})")

    final_start = overall_range.start
    final_end = overall_range.end
    diff = final_end - final_start
    bit_count = ceil(log2(float(1 / diff)))
    mult = 2 ** bit_count
    scaled_start = int(final_start * mult)
    scaled_end = int(final_end * mult)
    encoded_value = scaled_start
    binary_representation = bin(encoded_value)[2:].zfill(bit_count)
    print("\n\nЗакодированное слово(α) в двоичном виде:", binary_representation)
    return overall_range, bit_count, encoded_value, binary_representation




if __name__ == "__main__":
    encoded_word = "кесаеввладиславмаратович"
    encode_arithm(encoded_word)
