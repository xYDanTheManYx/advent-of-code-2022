with open("input.txt") as f:
    datastream_buffer = f.read()


def start_of_packet_marker(distinct_characters: int) -> int:
    for index, character in enumerate(datastream_buffer):
        if len(set(datastream_buffer[index:index+distinct_characters])) == distinct_characters:
            break
    return index+distinct_characters


print("puzzle 1:", start_of_packet_marker(4))
print("puzzle 2:", start_of_packet_marker(14))
