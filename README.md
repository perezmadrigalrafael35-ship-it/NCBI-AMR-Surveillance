# NCBI Antimicrobial Resistance (AMR) Surveillance Pipeline

## Overview
This repository contains a Python script designed for automated retrieval of antimicrobial resistance (AMR) gene sequences from the NCBI database. 

The script connects to the NCBI E-utilities API to fetch specific resistance genes (e.g., the `blaCTX-M-15` extended-spectrum beta-lactamase gene in *E. coli*) and saves the genomic FASTA sequence locally. 

## Use Case
This pipeline is a foundational tool for **bioinformatics and epidemiological surveillance**. It allows researchers to automate the downloading of resistance genes for downstream analysis, such as variant calling, phylogenetic analysis, or primer design.

## Technologies Used
* **Python 3**
* **Requests** (for API connection)
* **NCBI E-utilities**

## How to Run
1. Ensure you have Python installed.
2. Install the required library: `pip install requests`
3. Run the script: `python E.coli-fasta.py`
4. The script will generate a `.fasta` file containing the AMR gene sequence.
## Sequence Visualization
Below is the genetic map of the *blaCTX-M-15* resistance gene retrieved by the pipeline, visualized using VectorBee:
Genetic map of the blaCTX-M-15 extended-spectrum beta-lactamase gene, retrieved via the automated Python pipeline and visualized using VectorBee. This sequence confers resistance to third-generation cephalosporins in E. coli.
![AMR Gene Sequence Map](https://github.com/perezmadrigalrafael35-ship-it/NCBI-AMR-Surveillance/blob/main/plasmid_map.png.png)
