PROCESS:
=====================
1. Create Random R
random_Rgenerator.py creates 1M(approximately) of random data in chunks of 100+2 records each
This program is an user interactive and request basic information from user such as:
    1. Asks for file name
    2. Min random value
    3. Max random value
    4. Number of records per row

Output: It creates/update file as answered in (1).

Logic:
=========
Program exection stats at main.py
1. Boiler plate function 'distinct' which takes command line arguments such as file_name,number_of_blocks, each block sie and algorithm it should opt for de-duplication.
2. After accepting values, it performs basic validations on given arguments
3. Further this function creates an instance for DDuplicate Class
4. Dduplicate class's object calls 'open' method, which takes file_name as input and create read_buffer and write buffers ( This step is common for both the methods)
5. On successful execution, it invokes 'Getnext' method of Dduplicate object which takes algorithm as an input
    5.1 Getnext reads algorithm type
    5.2 creates btree and hashtree objects and provides read_buffers as input until evapurated.
    5.3 On successful exection of 5.2 it invokes close methods which takes input as distinct records of above algorithms
6. Close methods writes files with respective results.

Sample Outputs
==========
jonve02mac115:src JONVE02$ python random_Rgenerator.py
Enter destination file name : records.txt
Enter Minimum number of range : 0
Etner Maximum number of range : 99
No of records for row  : 3
Random R generated on records.txt


De-duplicate records with btree tables
jonve02mac115:src JONVE02$python main.py records.txt 4 3 btree
Writing results to output_btree.txt

De-duplicate records with hash tables
jonve02mac115:src JONVE02$ time python main.py records.txt 4 3 hash
Writing results to output_hash.txt
