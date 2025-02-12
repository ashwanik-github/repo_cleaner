# repo_cleaner 

This repository contains the source code for the [repo_cleaner] hosted on the (https://github.com/ashwanik-github/repo_cleaner).


## Problem Statement

Build a utility “repoCleaner” to clean stale github repos and branches and host the utility on personal Github account


### Functional requirements:

1. repoCleaner should read the list of repository from a file “masterRepoList.txt”. For the scope of this exercise,
candidate can populate the “masterRepoList.txt”  with forks on candidate’s github account for below repos:
    - https://github.com/github/docs
    - https://github.com/github/gh-ost
    - https://github.com/github/dmca
    - https://github.com/github/DPG-guidance
2.  For each repository, repoCleaner to identify all branches in the repository, and build a summary view containing
information on
    - Total branches in the repo
    - Total branches with latest commit which are older than a user defined time window(TW) from current datetime
 (Note. For scope of this exercise, candidate can assume the value of TW = 1 year)
3. For all branches in a repo which are older than an year, repoCleaner to take user consent to delete the branches at
per repo level
    - User should be able to select all, some, or none of the stale branches from the list provided to be deleted
    - User should not be able to specify a branch which is not stale for deletion via repoCleaner
4. repoCleaner to delete identified branches approved by user
5. As a final step, repoCleaner creates an executive summary which contains information on branches deleted in current
run. In case If all branches in project are stale, repoCleaner to add recommendation for deletion of the repository.

### Notes

1. Expected time commitment from candidate for assignment: 2-4 hours
2. Candidates to host the code on Github on their personal account publicly, and share the repo with recruitment
coordinator when done in no later than 3 business days after sharing by the recruiter.
3. Candidates to make reasonable assumptions to proceed wherever they feel and document them in README file in the repo.

### Program Execution
1. To run the program first install python3 on your system.
2. It is recommended to run it on the Vscode first however it is also CLI compatible.
3. Import all the dependencies as suggested prior the initial runtime.
4. You also need to generate the Github token (classic) which will allow you to grant permissions to delete etc.
5. export the GITHUB_TOKEN generated earlier to your bash/zsh/system variable.
6. Fill the masterRepoList.txt with any repo that you want for now we will strict to the list suggested.
7. Run the program using - python repo_cleaner.py
8. It will scan the repos and suggest the branches or repos to be deleted using y/n 
9. Provide y for yes to delete and n for not to delete.
10. At the result for the program is stored in the summary file repo_cleaner_summary.json