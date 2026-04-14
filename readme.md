# Geography of the poetic formula "from A to B"

This repository contains data and code for the paper *Where Empires End: Geography of the poetic formula "from A to B"*.  
  
The dataset is derived from the [PoeTree corpora](https://versologie.cz/poetree/index). All analyses and visualizations were conducted in R and can be reproduced by running the scripts in numerical order. The rendered .md files contain the key outputs used in the paper. The `renv.lock` file records the R package versions used and enables environment restoration via `renv::restore()`.  
  
## Repository Structure
````
.
├── data/
│   ├── formulas_table.csv        # Main dataset of formulas
|   ├── loc_unique_tagged.csv     # Manually tagged location types
|   ├── locations.csv             # All locations found in PoeTree
|   ├── rivers_with_coords.csv    # Supplementary river data
│   └── wiki_df.csv               # Formulas' locations coords from Wikidata
├── models/                       # Saved model outputs (.Rds)
├── plots/                        # Figures used in the paper
├── scr/                          # Quarto (.qmd) notebooks and rendered .md                   
|   ├── 01_dist_analysis.qmd      # Descriptive statistics (distances & types)
|   ├── 02_compass_plots.qmd      # Compass visualisations
|   ├── 03_directions_plots.qmd   # Directions visualisations
|   └── 04_borders_model.qmd      # Statistical models
├── formulas_maps.Rproj           # R project
└── renv.lock                     # Dependency lockfile for reproducibility
````


## Abstract

The paper examines the imaginary geography of the poetic formula "from place\_a to place\_b"" across six European languages. Using georeferenced PoeTree corpora, we analyze the types, distances, and directions of these spans, which reflect a "soaring view" rooted in the ode tradition and sustained in 16th-19th century poetry. We show that the formula functions as a tool of political and cultural boundary-making: Romantic-era national literatures favour more local spaces, while imperial traditions combine local and global spans. Long-distance formulas tend to align along the East-West axis, being an important framework for global geographical imagery. We use statistical modelling to distinguish geographical symbolic "centers" and "borders" and show that centers are typically political entities and borders are natural features, pointing to a shared European geographical imagination.
  
  
### Citation
  
If you use this code or data, please cite:
- The paper: *Where Empires End: Geography of the Poetic Formula “From A to B”* (forthcoming)
- The repository (Zenodo): (forthcoming)