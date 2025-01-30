import os
import numpy as np
import matplotlib.pyplot as plt
from shadePy import Colors

GREEN, RED, BRIGHT_GREY, YELLOW, RESET = (
    Colors.GREEN, Colors.RED, Colors.BRIGHTGREY,
    Colors.YELLOW, Colors.RESET
)

BIP39_LIST = './utils/wordsBIP39.txt'

def load_bip39_list():
    try:
        with open(BIP39_LIST, "r", encoding="utf-8") as f:
            bip39_list = [line.strip() for line in f if line.strip()]
        return bip39_list
    except FileNotFoundError:
        print(f"{RED}ERROR: The file '{BIP39_LIST}' could not be found.{RESET}")
        return []
    except Exception as e:
        print(f"{RED}ERROR: Error while loading the BIP39 list : {e}{RESET}")
        return []

def words_to_indices(phrase, bip39_list):
    words = phrase.split()
    indices = []
    
    for i, word in enumerate(words):
        try:
            index = bip39_list.index(word) + 1
            indices.append(index)
        except ValueError:
            print(f"{RED}ERROR The word '{word}' at position {i+1} (index {i}) is not in the BIP39 list.")
            return []  
    
    return indices

def encode_base2048(indices):
    base = 2048
    unique_value = 0
    for i, index in enumerate(reversed(indices)):
        unique_value += (index - 1) * (base ** i)
    return unique_value

def decode_base2048(unique_value, n_indices):
    base = 2048
    indices = []
    for _ in range(n_indices):
        indices.append(unique_value % base + 1)
        unique_value //= base
    return list(reversed(indices))

def generate_number_mapping(combined_value):
    value_str = str(combined_value)
    mapping = [int(c) for c in value_str]
    return mapping

def draw_sigil(number_mapping, filename, combined_value, add_name=False):
    ax = plt.subplots()[1]
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 10) if add_name else ax.set_ylim(0, 10)

    point_positions = [
        (5, 9), (7, 8), (8.5, 6), (8.5, 4), (7, 2),
        (5, 1), (3, 2), (1.5, 4), (1.5, 6), (3, 8)
    ]
    
    line_connections = []
    drawn_connections = set() 
    
    for i in range(len(number_mapping) - 1):
        part_start = number_mapping[i]
        part_end = number_mapping[i + 1]
        
        if part_start == part_end:
            x1, y1 = point_positions[part_start]
            if i > 0:
                x0, y0 = point_positions[number_mapping[i - 1]]
                dx = x1 - x0
                dy = y1 - y0
                length = np.sqrt(dx**2 + dy**2)
                if length != 0:
                    dx /= length
                    dy /= length
                offset = 0.4
                x, y = x1 + dx * offset, y1 + dy * offset
            else:
                x, y = x1 + 0.5, y1 + 0.5  
            plt.scatter(x, y, color='#FF9900', s=15) 
            continue
        
        connection = (part_start, part_end)
        reverse_connection = (part_end, part_start)

        thickness = 2 if (connection in drawn_connections or reverse_connection in drawn_connections) else 1
        
        drawn_connections.add(connection)
        drawn_connections.add(reverse_connection)
        
        line_connections.append((point_positions[part_start], point_positions[part_end], thickness))

    start_point = point_positions[number_mapping[0]]
    plt.scatter(start_point[0], start_point[1], color='#FF9900', s=40) 

    for start, end, thickness in line_connections:
        plt.plot([start[0], end[0]], [start[1], end[1]], color='black', linewidth=thickness) 

    last_start, last_end, last_thickness = line_connections[-1]
    dx = last_end[0] - last_start[0]
    dy = last_end[1] - last_start[1]
    length = np.sqrt(dx**2 + dy**2)
    if length != 0:
        dx /= length
        dy /= length
    perpendicular_dx = -dy * 0.5
    perpendicular_dy = dx * 0.5
    plt.plot([last_end[0] - perpendicular_dx/2, last_end[0] + perpendicular_dx/2], 
             [last_end[1] - perpendicular_dy/2, last_end[1] + perpendicular_dy/2], 
             color='#FF9900', linewidth=last_thickness + 1) 

    if add_name and combined_value:
        ax.text(5, -1, str(combined_value), fontsize=12, ha='center', va='center', color='black')

    ax.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=False)
    plt.close()

def main():
    print(f"\n{BRIGHT_GREY}1.{RESET} Create a Sigil")
    print(f"{BRIGHT_GREY}2.{RESET} Retrieve the mnemonic phrase from a combined value\n")
    choice = input(f"{BRIGHT_GREY}Choose an option (1 or 2) : {RESET}")

    bip39_list = load_bip39_list()

    if choice == "1":
        mnemonic_phrase = input(f"{BRIGHT_GREY}Enter your mnemonic phrase (separate words by spaces) : {RESET}")
        indices = words_to_indices(mnemonic_phrase, bip39_list)
        print(f"{BRIGHT_GREY}\nIndices :{RESET} {indices}")
        if not indices:
            print(f"{RED}ERROR: Error in phrase conversion{RESET}")
            return

        combined_value = encode_base2048(indices)
        print(f"{BRIGHT_GREY}Encoded combined value :{RESET} {combined_value}")

        number_mapping = generate_number_mapping(combined_value)
        print(f"{BRIGHT_GREY}Number Mapping for the sigil :{RESET} {number_mapping}")

        sigil_folder = "sigils"
        os.makedirs(sigil_folder, exist_ok=True)
        filename = os.path.join(sigil_folder, 'sigil2.png')
        draw_sigil(number_mapping, filename, combined_value)
        print(f"{GREEN}Sigil saved as {filename[-10:]}{RESET}")

    elif choice == "2":
        combined_value = int(input(f"\n{BRIGHT_GREY}Enter the encoded combined value :{RESET} "))
        n_indices = int(input(f"{BRIGHT_GREY}Enter the number of indices to reconstruct the phrase :{RESET} "))
        reconstructed_indices = decode_base2048(combined_value, n_indices)
        print(f"{BRIGHT_GREY}Reconstructed indices :{RESET} {reconstructed_indices}")

        bip39_list = load_bip39_list()
        reconstructed_mnemonic = " ".join([bip39_list[i - 1] for i in reconstructed_indices])
        print(f"{BRIGHT_GREY}Reconstructed mnemonic phrase :{RESET} {reconstructed_mnemonic}")
    
    else:
        print(f"{RED}ERROR: Invalid choice.{RESET}")

if __name__ == "__main__":
    main()
