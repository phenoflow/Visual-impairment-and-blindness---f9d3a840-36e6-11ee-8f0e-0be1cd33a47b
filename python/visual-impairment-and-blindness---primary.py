# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"8HlE.00","system":"readv2"},{"code":"9NlD.00","system":"readv2"},{"code":"F490.00","system":"readv2"},{"code":"F490z00","system":"readv2"},{"code":"F494.00","system":"readv2"},{"code":"F49z.00","system":"readv2"},{"code":"F49z000","system":"readv2"},{"code":"F4H7300","system":"readv2"},{"code":"FyuL.00","system":"readv2"},{"code":"SJ0z.11","system":"readv2"},{"code":"ZRhO.00","system":"readv2"},{"code":"100108","system":"med"},{"code":"100755","system":"med"},{"code":"100999","system":"med"},{"code":"101051","system":"med"},{"code":"101881","system":"med"},{"code":"10388","system":"med"},{"code":"103907","system":"med"},{"code":"104077","system":"med"},{"code":"104087","system":"med"},{"code":"104666","system":"med"},{"code":"104853","system":"med"},{"code":"105206","system":"med"},{"code":"105493","system":"med"},{"code":"105665","system":"med"},{"code":"105795","system":"med"},{"code":"106329","system":"med"},{"code":"107912","system":"med"},{"code":"10868","system":"med"},{"code":"110179","system":"med"},{"code":"1444","system":"med"},{"code":"15269","system":"med"},{"code":"18819","system":"med"},{"code":"1990","system":"med"},{"code":"20256","system":"med"},{"code":"20607","system":"med"},{"code":"23742","system":"med"},{"code":"25168","system":"med"},{"code":"25547","system":"med"},{"code":"25831","system":"med"},{"code":"2746","system":"med"},{"code":"29387","system":"med"},{"code":"32044","system":"med"},{"code":"32467","system":"med"},{"code":"3268","system":"med"},{"code":"32905","system":"med"},{"code":"33014","system":"med"},{"code":"33016","system":"med"},{"code":"33447","system":"med"},{"code":"37086","system":"med"},{"code":"37893","system":"med"},{"code":"38000","system":"med"},{"code":"3851","system":"med"},{"code":"3852","system":"med"},{"code":"38717","system":"med"},{"code":"3976","system":"med"},{"code":"40451","system":"med"},{"code":"42262","system":"med"},{"code":"44954","system":"med"},{"code":"47956","system":"med"},{"code":"50679","system":"med"},{"code":"510","system":"med"},{"code":"51274","system":"med"},{"code":"52227","system":"med"},{"code":"52630","system":"med"},{"code":"54513","system":"med"},{"code":"54962","system":"med"},{"code":"55108","system":"med"},{"code":"55436","system":"med"},{"code":"55844","system":"med"},{"code":"55846","system":"med"},{"code":"60043","system":"med"},{"code":"6020","system":"med"},{"code":"60401","system":"med"},{"code":"62657","system":"med"},{"code":"63045","system":"med"},{"code":"63928","system":"med"},{"code":"65144","system":"med"},{"code":"6661","system":"med"},{"code":"66731","system":"med"},{"code":"67126","system":"med"},{"code":"67594","system":"med"},{"code":"6768","system":"med"},{"code":"67765","system":"med"},{"code":"67872","system":"med"},{"code":"68386","system":"med"},{"code":"68391","system":"med"},{"code":"69998","system":"med"},{"code":"71319","system":"med"},{"code":"7203","system":"med"},{"code":"72411","system":"med"},{"code":"73224","system":"med"},{"code":"73508","system":"med"},{"code":"8367","system":"med"},{"code":"90766","system":"med"},{"code":"91521","system":"med"},{"code":"9645","system":"med"},{"code":"96455","system":"med"},{"code":"98226","system":"med"},{"code":"98637","system":"med"},{"code":"98672","system":"med"},{"code":"98935","system":"med"},{"code":"99165","system":"med"},{"code":"99166","system":"med"},{"code":"99191","system":"med"},{"code":"99504","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('visual-impairment-and-blindness-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["visual-impairment-and-blindness---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["visual-impairment-and-blindness---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["visual-impairment-and-blindness---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
