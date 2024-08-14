from odbAccess import *
from abaqusConstants import *
import os
import csv

# Enter the odb filepath
odbpath = 'insert_filename.odb'
odbname = os.path.splitext(os.path.basename(odbpath))[0]
odb = openOdb(path=odbpath)

# Create a CSV file for output
csv_file_path = '{}_output.csv'.format(odbname)

# Script setup
assembly = odb.rootAssembly
step1 = odb.steps['Heating']  # Step of interest

# Define the sets of elements - example elements given here
crit1 = ['2831', '2832', '2833', '2834', '2851', '2852', '2853', '2854', '2870', '2871', '2872', '2873', '2874', '2890', '2891', '2892', '2893', '2894', '2910', '2911', '2912', '2913', '2914', '2930', '2931', '2932', '2933', '2934', '2949', '2950', '2951', '2952', '2953', '2954', '2969', '2970', '2971', '2972', '2973', '2974', '2975', '2976', '2977', '2978', '2979', '2980', '2981', '2982', '2983', '2984', '2985', '2986', '2987', '2988', '2989', '2990', '2991', '2992', '2993', '2994', '2995', '2996', '2997', '2998', '2999', '3000', '3001', '3002', '3003', '3004', '3005', '3006', '3007', '3008', '3009', '3010', '3011', '3012', '3013', '3014', '3029', '3030', '3031', '3032', '3033', '3034', '3049', '3050', '3051', '3052', '3053', '3054', '3070', '3071', '3072', '3073', '3074', '3090', '3091', '3092', '3093', '3094', '3111', '3112', '3113', '3114', '3131', '3132', '3133', '3134']
crit2 = ['2831', '2832', '2833', '2834', '2851', '2852', '2853', '2854', '2870', '2871', '2872', '2873', '2874', '2890', '2891', '2892', '2893', '2894', '2910', '2911', '2912', '2913', '2914', '2930', '2931', '2932', '2933', '2934', '2949', '2950', '2951', '2952', '2953', '2954', '2969', '2970', '2971', '2972', '2973', '2974', '2988', '2989', '2990', '2991', '2992', '2993', '2994', '3008', '3009', '3010', '3011', '3012', '3013', '3014', '3029', '3030', '3031', '3032', '3033', '3034', '3049', '3050', '3051', '3052', '3053', '3054', '3070', '3071', '3072', '3073', '3074', '3090', '3091', '3092', '3093', '3094', '3111', '3112', '3113', '3114', '3131', '3132', '3133', '3134']
frames = list(range(38))

# Assuming you have a predefined list of output variables you want to extract  - example variables given here
output_variables = ['E11', 'E12', 'E13', 'E22', 'E23', 'E33', ' IE11', 'IE12', 'IE13', 'IE22', 'IE23', 'IE33','THE11', 'THE12', 'THE13', 'THE22', 'THE23', 'THE33', 'CEMAG', 'PEMAG']

# Open the CSV file for writing
with open(csv_file_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header to the CSV file
    header = ['Time', 'element'] + output_variables
    csvwriter.writerow(header)

    # Iterate through each element in crit1 and output time and output variables
    for elem_label in crit1:
        histregion = step1.historyRegions['Element TRACE-WIDE-1.{} Int Point 1'.format(elem_label)]
        E11_out = histregion.historyOutputs['E11']
        E12_out = histregion.historyOutputs['E12']
        E13_out = histregion.historyOutputs['E13']
        E22_out = histregion.historyOutputs['E22']
        E23_out = histregion.historyOutputs['E23']
        E33_out = histregion.historyOutputs['E33']
        IE11_out = histregion.historyOutputs['IE11']
        IE12_out = histregion.historyOutputs['IE12']
        IE13_out = histregion.historyOutputs['IE13']
        IE22_out = histregion.historyOutputs['IE22']
        IE23_out = histregion.historyOutputs['IE23']
        IE33_out = histregion.historyOutputs['IE33']
        THE11_out = histregion.historyOutputs['THE11']
        THE12_out = histregion.historyOutputs['THE12']
        THE13_out = histregion.historyOutputs['THE13']
        THE22_out = histregion.historyOutputs['THE22']
        THE23_out = histregion.historyOutputs['THE23']
        THE33_out = histregion.historyOutputs['THE33']
        CEMAG_out = histregion.historyOutputs['CEMAG']
        PEMAG_out = histregion.historyOutputs['PEMAG']
    
        for frame in frames:
            time = E11_out.data[frame][0]
            E11_data = E11_out.data[frame][1]
            E12_data = E12_out.data[frame][1]
            E13_data = E13_out.data[frame][1]
            E22_data = E22_out.data[frame][1]
            E23_data = E23_out.data[frame][1]
            E33_data = E33_out.data[frame][1]
            IE11_data = IE11_out.data[frame][1]
            IE12_data = IE12_out.data[frame][1]
            IE13_data = IE13_out.data[frame][1]
            IE22_data = IE22_out.data[frame][1]
            IE23_data = IE23_out.data[frame][1]
            IE33_data = IE33_out.data[frame][1]
            THE11_data = THE11_out.data[frame][1]
            THE12_data = THE12_out.data[frame][1]
            THE13_data = THE13_out.data[frame][1]
            THE22_data = THE22_out.data[frame][1]
            THE23_data = THE23_out.data[frame][1]
            THE33_data = THE33_out.data[frame][1]
            CEMAG_data = CEMAG_out.data[frame][1]
            PEMAG_data = PEMAG_out.data[frame][1]

            csvwriter.writerow([time, elem_label, E11_data, E12_data, E13_data, E22_data, E23_data, E33_data, IE11_data, IE12_data, IE13_data, IE22_data, IE23_data, IE33_data, THE11_data, THE12_data, THE13_data, THE22_data, THE23_data, THE33_data, CEMAG_data, PEMAG_data])
