input_file_path = 'Original_data\\roadNet-CA.txt'  # Corrected file path
output_file_path = 'Filtered_data\\roadNet-CA_filtered.txt'


def filter_nodes(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            # Skip comments and empty lines
            if line.startswith('#') or line.strip() == '':
                continue

            # Split the line into node IDs
            node_ids = line.strip().split()

            # Check if both node IDs are below 50000
            if int(node_ids[0]) < 50000 and int(node_ids[1]) < 50000:
                outfile.write(line)


# Call the function to filter nodes
filter_nodes(input_file_path, output_file_path)
