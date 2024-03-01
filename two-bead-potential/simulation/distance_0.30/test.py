import os

# Output file to save collected field E values
 
folder_path = './'
     
log_file = os.path.join(folder_path, 'sim.log')
 
with open(log_file, 'r') as log:
    lines = log.readlines()
    for i, line in enumerate(lines):
        if line.startswith('         step         time         temp        tot E        kin E        pot E      field E '):
            print('-----------------')
            field_E_line = lines[i+1]
            field_E_value = float(field_E_line.split()[6])
            # Write the field E value to the output file
            print(field_E_value)
            break

