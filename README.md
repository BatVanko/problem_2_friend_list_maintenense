# problem_2_friend_list_maintenense
Our player is having with his friend’s list and some guys are disappearing without reason , so he ask you  to create a program that will figure out what is going on and , in the end , will bring him a report.
On the first line you will receive all his friends separated by “, ”. On the next lines until the “Report” command you will receive some commands:
Input
•	The possible commands are:
o	"Blacklist {name}":  Change the given name to “Blacklist” 
And print {name} was blacklisted
o	"Error {index}":
If the index is valid and the username at the given index is not blacklisted or already lost due to an error, change it to “Lost” and print:{name} was lost due to an error.
o	"Change {index} {new name}"
If index is valid , change the current username with the new one and print : {current name} changed his username to {new name}.

o	"Report"
After you receite “Report” print on the console the count of blacklisted names , the count of lost names , and the friends list separated by a single space.
Output
•	The possible outputs are:
o	"{name} was blacklisted."
o	"{name} was not found."
o	"{name} was lost due to an error."
o	"{current name} changed his username to {new name}."
o	"Blacklisted names: {number of blacklisted names}"
o	"Lost names: {number of lost names}"

Examples
Input	Output
Mike, John, Eddie
Blacklist Mike
Error 0
Report	
Output
Mike was blacklisted.
Blacklisted names: 1 
Lost names: 0
Blacklisted John Eddie
