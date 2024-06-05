# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0208010L0BBACAA","system":"bnf"},{"code":"0208010W0BCANAT","system":"bnf"},{"code":"0208010W0AAAKAK","system":"bnf"},{"code":"0208010L0BBAHAH","system":"bnf"},{"code":"0208010L0AAADAD","system":"bnf"},{"code":"0208010W0AAAFAF","system":"bnf"},{"code":"0208010L0AAAHAH","system":"bnf"},{"code":"0208010W0AAARAR","system":"bnf"},{"code":"0208010W0AAAIAI","system":"bnf"},{"code":"0208010W0BCAEAI","system":"bnf"},{"code":"0208010L0BBAFAF","system":"bnf"},{"code":"0208010L0AAAIAI","system":"bnf"},{"code":"0208010W0BCAJAN","system":"bnf"},{"code":"0208010W0BCAIAM","system":"bnf"},{"code":"0208010W0BCAHAL","system":"bnf"},{"code":"0208010W0AAAMAM","system":"bnf"},{"code":"0208010L0AAAGAG","system":"bnf"},{"code":"0208010L0AAAJAJ","system":"bnf"},{"code":"0208010W0BCAKAQ","system":"bnf"},{"code":"0208010L0BBAJAJ","system":"bnf"},{"code":"0208010L0BBAIAI","system":"bnf"},{"code":"0208010W0AAAJAJ","system":"bnf"},{"code":"0208010L0AAAKAK","system":"bnf"},{"code":"0208010W0BCAMAS","system":"bnf"},{"code":"0208010W0AAAQAQ","system":"bnf"},{"code":"0208010L0BBADAD","system":"bnf"},{"code":"0208010W0AAANAN","system":"bnf"},{"code":"0208010L0BBAGAG","system":"bnf"},{"code":"0208010W0AAALAL","system":"bnf"},{"code":"0208010L0BBAKAK","system":"bnf"},{"code":"0208010W0AAASAS","system":"bnf"},{"code":"0208010L0BBABAB","system":"bnf"},{"code":"0208010L0AAAFAF","system":"bnf"},{"code":"0208010L0AAACAC","system":"bnf"},{"code":"0208010W0AAATAT","system":"bnf"},{"code":"0208010L0AAABAB","system":"bnf"},{"code":"0208010W0BCAFAJ","system":"bnf"},{"code":"0208010L0AAAAAA","system":"bnf"},{"code":"0208010W0BCALAR","system":"bnf"},{"code":"0208010W0BCACAF","system":"bnf"},{"code":"0208010L0BBAAAC","system":"bnf"},{"code":"0208010W0BCAGAK","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('heparins-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["heparins-5000unit---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["heparins-5000unit---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["heparins-5000unit---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
