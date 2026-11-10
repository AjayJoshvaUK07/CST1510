from pathlib import Path
"""
RECORD CHECK  -  my version
===========================

Name  :Ajay Joshva
Lane  : Cyber 
Date  :10 th November

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Calculate difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records():
    records = []

    file_path = Path(__file__).parent / "records_sample.txt"
    with open(file_path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


records = load_records()


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

total_over = 0

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print(f'{record["label"]}: {status}')

    if status == "OVER LIMIT":
        total_over += 1

print(f"Total over limit: {total_over}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
