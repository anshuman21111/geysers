# Collation Folder
This folder was used to create the collation. The merge_data.py file was used to open the required geyser data files and take only the data between the two dates, and create a new csv file with only the data we required. The collation.py file is used to make a new csv file with each geyser's data in each column. Because the merge operation would take too long on a file this size, the method splits up the data and merges them one by one.

# netrd_methods Folder
This folder has the code used for the netrd methods. At the beginning of each file there is a data formatting step that puts the collation in a format that is readable by the netrd method. In this step we can manually change the time interval of the data and options of the specific netrd method we are using. This folder also includes a template for netrd methods. There is also a template for splitting up the data, running the netrd method on each piece, and taking the mean of all the values, called split_method_template.py.

# Scripts Folder
This folder has the script files we used to run on UMD's Deepthought2 cluster. The beginning of the file has the amount of the computer's resources we wanted to use when running the methods, and also messages to indicate which method had started.

# tigramite_methods Folder
This folder has the code for the tigramite methods that we ran. The parcorr/gpdc at the end of the files indicates the conditional independence tests we used in that specific method. To format the results of these methods into matrices, we had to manually copy the matrices from the output of the methods into a txt file, run results_processing.py on the file and write to a new file, and copy and paste that as an array to results_to_matrix.py.