from Bio import Phylo
tree = Phylo.read('tree1.dnd', 'newick')
Phylo.draw(tree)