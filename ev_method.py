import glob
import csv

# Directory path containing CSV files
path = 'log/'

# Phrase to search for
# 'ConfLongDemo_JSI', 'Healthy_Older_People', 'User_Identification_From_Walking',
datasets = ['Dataset#2', 'UCI-HAR-Dataset']
# 'HistogramBinning', 'IsotonicRegression', 'BBQ', 'LogisticCalibration', 'TemperatureScaling',
#            'BetaCalibration'
methods = ['ENIR']

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

                    if dataset in row['dataset'] and method in row['calibration']:
                        if 'InCls:[UnCalibrated]_UQ:[Calibrated][Totall]' in row['prediction_method']:
                            if float(row['MS_f1_mean']) > max_f1:
                                max_f1 = float(row['MS_f1_mean'])
                                best_filename = filename
                                best_row = row

        print(dataset, method, best_filename)
        print("f1", round(float(best_row['MS_f1_mean']) * 100, 2), "($\pm$", round(float(best_row['MS_f1_std']), 2),
              ")")
        print("esl", round(float(best_row['MS_esl_mean']), 4), "($\pm$", round(float(best_row['MS_esl_std']), 3), ")")
        print("ll", round(float(best_row['MS_ll_mean']), 4), "($\pm$", round(float(best_row['MS_ll_std']), 3), ")")

        print("recall", round(float(best_row['MS_recall_mean']) * 100, 2), "($\pm$",
              round(float(best_row['MS_recall_std']), 2), ")")
        print("precision", round(float(best_row['MS_precision_mean']) * 100, 2), "($\pm$",
              round(float(best_row['MS_precision_std']), 2), ")")
        print("accuracy", round(float(best_row['MS_accuracy_mean']) * 100, 2), "($\pm$",
              round(float(best_row['MS_accuracy_std']), 2), ")")
