# ECOR 1042 Lab 3 - Template


# Update
__author__ = "Arsal Awan"
__student_number__ = "101305046"
__team__ = "T040"

#==========================================#
# Place your machine_cache_list function after this line


def machine_cache_list(filename: str, cache: int) -> dict:
    """
    Take information from 
    """
    final_list = []
    infile = open(filename, "r")
    fileline = set()
    for line in infile:
        fileline = line.split(",")
        if fileline[5] != "CACH":
            if int(fileline[5]) >= cache:
                cache_list = ({v: fileline[0], m: fileline[1],
                               myct: int(fileline[2]), mmin: int(fileline[3]),
                               mmax: int(fileline[4]), prp: int(fileline[6]), erp: int(fileline[7]), })
                final_list.append(cache_list)
        else:
            v = fileline[0].lower()
            m = fileline[1].lower()
            myct = fileline[2]
            mmin = fileline[3]
            mmax = fileline[4]
            prp = fileline[6]
            erp = fileline[7].strip().replace("\n", "")
    return final_list

# Do not include a main script



