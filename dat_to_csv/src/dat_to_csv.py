import os
import csv
import numpy as np

def dat_to_csv(in_path_and_name):
    with open(in_path_and_name) as input_file:
        data_csv = []
        for line in input_file:
            newData = [i.strip() for i in line.split('|')]
            # newData = [i.strip('"') for i in line.split(',')]
            # add conditinionals here if necessary
            # if len(newData) == 6 and newData[3] and newData[4]:
            data_csv.append(newData)
        print("\nData converted!\n")
    return data_csv

def save_csv(out_path,out_filename,data):
    if ".csv" not in out_filename:
        out_filename = out_filename+".csv"
    with open(out_path+out_filename, 'w') as output_file:
        file_writer = csv.writer(output_file)
        file_writer.writerows(data)
        print("\nFile saved!\n")

def main():
    selection = "1"
    while selection != "2":
        selection = "1"
        print("*******_____Convert .dat to .csv_____*******")
        print("1. Convert")
        print("2. Quit")
        selection = str(input("Select an option (type a number, press enter):\n"))
        if selection == "1":
            in_path = "../files_to_convert/"
            change_in_path = str(input("Default input filepath is: "+in_path+"\nWould you like to change the input filepath?\nEnter 1 for yes, or 2 for no:\n"))
            if change_in_path == "1":
                in_path = str(raw_input("Enter filepath to .dat file to convert to .csv file:\n"))
            in_name = str(raw_input("Enter filename of .dat file to convert:\n"))
            if ".dat" not in in_name:
                in_name = in_name+".dat"
            in_path_and_name = in_path + in_name
            # in_filename = str()
            if os.path.exists(in_path_and_name) == False:
                print("Please try again. Some of the information you entered is incorrect.")
            else:
                converted_data = dat_to_csv(in_path_and_name)
                proceed = str(input("Would you like to save converted file in .csv format?\nEnter 1 for yes, or 2 for no:\n"))
                if proceed == "1":
                    out_path = "../converted_files/"
                    out_filename = str(raw_input("Enter desired filename:\n"))
                    change_out_path = str(input("Default output filepath is: "+out_path+"\nWould you like to change the output filepath?\nEnter 1 for yes, or 2 for no:\n"))
                    if change_out_path == "1":
                        new_out_path = str(raw_input("Enter new filepath relative to 'dat_to_csv.py':\n"))
                        save_csv(new_out_path,out_filename,converted_data)
                    else:
                        save_csv(out_path,out_filename,converted_data)
                else:
                    print("Okay. Going back.")
        elif selection == "2":
            print("\nSession Ended.\n")
        else:
            print("\nNot a valid choice.\n")

if __name__ == '__main__':
    main()
