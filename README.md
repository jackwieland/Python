1. **Backend_SQL_File_Processor.py:** Connects to a SQL database to run SQL scripts and manipulates the SQL script so a SQL comment is used as a row for column and the frequency counts are used in the second column. See my SQL repository.
2. **Backend_Multi_Python_Reader.py:** Loops over the Backend_SQL_File_Processor.py
3. **Switch_Case.py:**Creats a menu selection to pick a script to run choosing one of the Backend_Multi_Python_Reader.py scripts.
4. **CSV_Merger:**Merges multiple CSVs into one, dropping index 0 on the second CSV onwards.
5. **Normalisation_data_by_band_size.py:** Impliments a formula to normalise data using the equation: column_1 entries/column_2 entries * 1000000.
6. **bargraph.py**: Creates a bar graph with the option to make a single bar or a range of bars to a different colour.
7. **z_scores.py**: Runs the Z-score statistic.
8. **t_test_male_group_template.py:** Runs the paired two-tailed t-test between my male groups, abnormal category vs normal category for phenoptype. - **NOTE****** this refers to biological determination via chromosome karyotype.
9. **Female_Group_t_test_template.py:** compares my female groups by phenotype. - **NOTE****** this refers to biological determination via chromosome karyotype.
10. **File_Prep_template.py:** Finds the mean values for the data and puts these into a new CSV output with csv file production after each stage for validation checks after.
11. **File_prep_2_template.py:** Same method as File_Prep_template.py but, columns are from input file are grouped into categories.
12.  **chi_square.py**: Performs the chi-square test.
**Elbow_Method.py**: Performs the elbow method with silohuette scores to determine number of clusters for K-Means clustering.
**K-Means_Template.py**: Produces the K-means clustering graph.
