from Bio import Phylo
import matplotlib.pyplot as plt

#load the tree from the Newick format file
tree = Phylo.read("tree.dnd", "newick")

# Draw the tree
Phylo.draw(tree)

# Save the tree

plt.savefig("tree_visualisation.png")

# Display the tree
plt.show()
