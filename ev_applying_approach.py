import glob
import csv

# Directory path containing CSV files
path = 'log/'

# Phrase to search for
datasets = ['ConfLongDemo_JSI', 'Healthy_Older_People', 'User_Identification_From_Walking']
methods = ['InCls:[UnCalibrated]_UQ:[Calibrated][Totall]']

for dataset in datasets:
    for method in methods:
        max_f1 = 0.0
        best_filename = ''
        best_row = ''

        # Loop through all CSV files in directory
        for filename in glob.glob(path + '*.csv'):
            # Open the CSV file
            with open(filename, 'r') as f:

                # Iterate over rows
                reader = csv.DictReader(f)
                for row in reader:

                    if dataset in row['dataset'] and method in row['prediction_method']:
                        if 'ENIR' in row['calibration']:
                            if float(row['MS_f1_mean']) > max_f1:
                                max_f1 = float(row['MS_f1_mean'])
                                best_filename = filename
                                best_row = row

        print(dataset, method, best_filename)
        # print("ECE", round(float(best_row['calibration_metric_ECE_mean']), 3), "($\pm$", round(float(best_row['calibration_metric_ECE_std']), 2), ")")
        # print("ACE", round(float(best_row['calibration_metric_ACE_mean']), 3), "($\pm$", round(float(best_row['calibration_metric_ACE_std']), 2), ")")
        # print("MCE", round(float(best_row['calibration_metric_MCE_mean']), 3), "($\pm$", round(float(best_row['calibration_metric_MCE_std']), 2), ")")
