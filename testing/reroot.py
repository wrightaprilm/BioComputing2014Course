import os
import dendropy

file_list = []
for file in os.listdir('.'):
    if file.startswith('ExaML_result'):
        file_list.append(file)
        print file_list
    if not os.path.exists('./rooted/'):
        os.makedirs('./rooted/')
    tree = dendropy.Tree()
    
for file in file_list:
    tree.read_from_path(file, 'newick')
    spe_node = tree.find_node_with_taxon_label("Sphenodon punctatus")
    outgroup_node = spe_node.parent_node
    tree.reroot_at_node(outgroup_node, update_splits=True)
    tree.write_to_path('./rooted/%s' % file, 'newick')
            


	
