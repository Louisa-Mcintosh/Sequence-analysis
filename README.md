Sequence Analysis Project

This project focuses on the sequence analysis of genetic data using bioinformatics tools and Python scripting. The workflow includes sequence alignment, visualisation, and analysis of DNA sequences.

Project Overview

This repository contains the code and files for performing sequence analysis on DNA sequences, using Clustal Omega for alignment and visualisation of phylogenetic trees. The analysis includes steps like sequence retrieval, multiple sequence alignment, and generating a guide tree.

Table of Contents

- Requirements
- Installation
- Usage
- Workflow
- Results
- License

Requirements

Before running the analysis, ensure that you have the following installed:

- Clustal Omega - for sequence alignment.
- Python 3 - for running Python scripts.
- Matplotlib - for visualising the phylogenetic tree.
- Biopython - for handling biological sequences in Python.
- OpenJDK- to run Java-based tools for tree visualization (if necessary).

You can install the required Python packages with:

```bash
pip install matplotlib biopython
```

Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Louisa-Mcintosh/Sequence-analysis.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd Sequence-analysis
   ```

3. Ensure all dependencies are installed (refer to the Requirements section).

Usage

 Step 1: Prepare the Sequence File

The first step is to make sure you have a valid sequence file in FASTA format, such as `sequences.fasta`. If you don't have a sequence file, you can generate or download one.

Step 2: Sequence Alignment with Clustal Omega

You can align your sequences using Clustal Omega. Here's how to run the alignment:

```bash
clustalo -i sequences.fasta -o aligned_output.fasta --outfmt=clustal
```

This will align the sequences in the `sequences.fasta` file and output the results in `aligned_output.fasta`.

Step 3: Generate Phylogenetic Tree

Once your sequences are aligned, you can generate a phylogenetic tree using the following Clustal Omega command:

```bash
clustalo -i sequences.fasta --guidetree-out=tree.dnd
```

This will output a Newick format guide tree (`tree.dnd`), which can be visualised.

Step 4: Visualising the Tree

You can visualise the generated tree using a Python script (e.g., `visualise_tree.py`). This script uses Matplotlib to render the tree into an image (`tree_visualisation.png`).

Run the following command:

```bash
python3 visualise_tree.py
```

This will create a visual representation of the phylogenetic tree as `tree_visualisation.png`.

Workflow

1. Data Preparation: Retrieve and prepare DNA sequence data in FASTA format.
2. Multiple Sequence Alignment: Use Clustal Omega to align sequences.
3. Guide Tree Generation: Generate a phylogenetic guide tree with Clustal Omega.
4. Tree Visualisation: Visualise the tree using a Python script and Matplotlib.

Results

- Aligned Sequences: The output of the sequence alignment is saved as `aligned_output.fasta` and `aligned_output.clustal`.
- Phylogenetic Tree: The guide tree is saved as `tree.dnd`, and the visual representation is stored as `tree_visualisation.png`.

License

This project is licensed under the MIT License - see the LICENSE file for details.





