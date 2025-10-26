#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages
import os

# Directory where the cluster plots are saved
plot_directory = 'YOU/FILE/PATH'

pdf = PdfPages('PDF_With_Graphs.pdf')

# Number of plots per page
plots_per_page = 4
total_plots = 24 # Insert some number of your own interest

# Function definiting to create a page with multiple graphs
def create_plot_page(start_index, end_index):
    # Adjust the figure size for portrait orientation (width < height), figsize presented as inches
    fig, axs = plt.subplots(2, 2, figsize=(8, 12))  
    axs = axs.flatten()

    for i in range(start_index, end_index):
        ax = axs[i - start_index]
        
        # Loops through the directory to 
        plot_file = os.path.join(plot_directory, f"Graph_{i + 1}_Name.png")
        
        # Prints exact pathway that is being searched
        print(f"Looking for: {plot_file}")
        
        # Checking for graph.png is present
        if os.path.exists(plot_file):
            img = mpimg.imread(plot_file)
            ax.imshow(img)
            ax.axis('off')
        else:
            # Error handling
            print(f"Warning: File not found: {plot_file}")
            ax.text(0.5, 0.5, "File not found", ha='center', va='center', fontsize=12, color='red')

    # Layout adjustments
    plt.tight_layout()
    pdf.savefig(fig)
    plt.close(fig)  

# Looping through from graph_1.png to graph_24png
for i in range(0, total_plots, plots_per_page):
    create_plot_page(i, min(i + plots_per_page, total_plots))

pdf.close()
