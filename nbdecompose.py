import json

def decompose_nb_stages_with_header(file_name, markdown_header='STAGE'):
    with open(file_name, mode = 'r', encoding='utf-8') as f:
        combined_nb = json.load(f)
    metadata = combined_nb['metadata']
    first_stage = combined_nb['cells'][0]
    decomposed_nb_file_name = first_stage['source'][0][3:] + '.ipynb'
    nb['cells'] = [first_stage]
    nb['metadata'] = metadata
    nb['nbformat']= 4
    nb['nbformat_minor']= 2
    for cell in combined_nb['cells'][1:]:
        if cell['cell_type'] == 'markdown' and cell['source'][0].startswith(f'## {markdown_header}'):
            with open(decomposed_nb_file_name, mode = 'w', encoding='utf-8') as f:
                print(decomposed_nb_file_name)
                json.dump(nb, f)
            ## initail nb stage
            decomposed_nb_file_name = cell['source'][0][3:] + '.ipynb'
            nb['cells'] = [cell]
        else:
            nb['cells'].extend([cell])
    with open(decomposed_nb_file_name, mode = 'w', encoding='utf-8') as f:
                json.dump(nb, f)
    print(decomposed_nb_file_name)