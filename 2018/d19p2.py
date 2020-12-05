JUMP TO 18
R3 = 1                  # MAIN LOOP STARTS HERE
R2 = 1
R1 = R2 * R3
SET R1 IF R1 == R5
JUMP BY R1
JUMP TO 9
R0 = R0 + R3
R2 = R2 + 1
SET R1 IF R2 > R5
JUMP BY R1
JUMP TO 4
R3 = R3 + 1
SET R1 IF R3 > R5
JUMP BY R1
JUMP TO 3
STOP

R5 = R5 + 2             # ONLY EXECUTED ONCE AT THE BEGINNING
R5 = R5 * R5
R5 = R4 * R5
R5 = R5 * 11
R1 = R1 + 4
R1 = R1 * R4
R1 = R1 + 15
R5 = R5 + R1
JUMP BY R0              # VALUE IS 0 (i.e. next instruction) FOR PART 1, VALUE IS 1 (i.e., skip next jump) FOR PART 2
JUMP TO 2               # FOR PART 1, INITIALIZATION ENDS HERE; THIS INITIALIZES TO [0, 103, 0, 0, 25, 939]
setr 4 2 1              # EXTRA INITIALIZATION FOR PART 2
mulr 1 4 1
addr 4 1 1
mulr 4 1 1
muli 1 14 1
mulr 1 4 1
addr 5 1 5
R0 = 0
JUMP TO 2               # FOR PART 2, THIS INITIALIZES TO [0, 10550400, 0, 0, 34, 10551339] <= KEY NUMBER IS 10551339


=============================
| PRELIMINARY TRANSFORMATION
=============================

R3 = 1                  # MAIN LOOP STARTS HERE
R2 = 1
R1 = R2 * R3
IF R1 == R5:                
    R0 = R0 + R3
R2 = R2 + 1
IF R2 <= R5:                  
    JUMP TO 46
R3 = R3 + 1
IF R3 <= R5:
    JUMP TO 45
                        # PROGRAM STOPS WHEN IT REACHES THIS POINT


======================
| FUNCTIONALITY
======================

# RENAMING AS FOLLOWS:
#   R0 = RESULT
#   R1 = TEMPPRODUCT
#   R2 = FACTOR2
#   R3 = FACTOR1
#   R5 = N

FOR FACTOR1 IN [1, N]:      
    FOR FACTOR2 IN [1, N]:
        TEMPPRODUCT = FACTOR1 * FACTOR2
        IF TEMPPRODUCT == N:                
            RESULT += FACTOR2

# I.E., THIS PROGRAM SUMS THE DIVISORS OF THE INPUT N
# FOR PART 2, THIS INITIALIZES TO [0, 10550400, 0, 0, 34, 10551339] => N IS 10551339, FOR WHICH SUM OF DIVISORS IS 16137576
                        