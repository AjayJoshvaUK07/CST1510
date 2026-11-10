"""
RECORD CHECK  -  my version
===========================

Name  : Ajay Joshva
Lane  :  Cyber 
Date  :10 November

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label  = input("Enter label: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = second - first
if second != 0:
    percent = (first / second) * 100
else:
    percent = None


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign
print(f"Label      : {label}")
print(f"First      : {first:>10.2f}")
print(f"Second     : {second:>10.2f}")
print(f"Difference : {difference:+.2f}")
if percent is not None:
     print(f"Percent    : {percent:.2f}%")
else:
     print("percent.     : Cannot calculate (total is zero)")    

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
