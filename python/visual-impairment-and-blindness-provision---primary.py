# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"1B75.00","system":"readv2"},{"code":"2BBr.00","system":"readv2"},{"code":"F49..00","system":"readv2"},{"code":"F49..11","system":"readv2"},{"code":"F491.00","system":"readv2"},{"code":"F492.00","system":"readv2"},{"code":"F492000","system":"readv2"},{"code":"F492300","system":"readv2"},{"code":"F492z00","system":"readv2"},{"code":"F495200","system":"readv2"},{"code":"F495300","system":"readv2"},{"code":"F495500","system":"readv2"},{"code":"F495600","system":"readv2"},{"code":"F495800","system":"readv2"},{"code":"F496200","system":"readv2"},{"code":"F496300","system":"readv2"},{"code":"F496500","system":"readv2"},{"code":"F496600","system":"readv2"},{"code":"Z96..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('visual-impairment-and-blindness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["visual-impairment-and-blindness-provision---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["visual-impairment-and-blindness-provision---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["visual-impairment-and-blindness-provision---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
