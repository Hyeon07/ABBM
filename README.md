# Approval Based Budgeting method
Understanding the proportional-greedy rule with the second satisfaction function and
coding the rule in python, running it on the selected dataset and reporting the outcomes set and its total utility.
# Procedure
1) The main data set is divided into two csv files namely "PROJECTSagt.csv" and "VOTESagt.csv". They hold information related to projects and votes respectively.
2) In the first 41 lines of the code The required datasets are separated and stored.
3) Two functions are created to abide by the allocated rules namely f() representing second satisfaction function and pgrule() representing the propotional-Greedy rule
4) while the budget of outcome set isn't greater than the allocated budget
   for every project voters utility is checked and the project with highest utility is added to the Outcome set.
5) This way the process is continued till Budget limit is reached.
6) The dictionary "util" contains the utility value of each project.
7) B contains Outcome set
8) The dictionary "voter_util" contains the total utility value to each voter.
# complexities 
I've tried running and checking the code by taking a few samples in the given large data set, I did get output for most of them.

