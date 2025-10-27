1.Which issues were the easiest to fix, and which were the hardest? Why?
Adding docstring to functions and modules and renaming functions to snake-case were the easiest and changing the eval function to act.literal_eval was the hardest


2.Did the static analysis tools report any false positives? If so, describe one example.
inventory_system.py:31:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
inventory_system.py:43:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
The static analysis tool pylint says to use a lazy evaluation function inside loggin instead of using an f string though this doesnt affect the quality of code


3.How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
Automation in CI pipeline could be done using GitHub,jenkins and github actions where we configure yaml and the static analysis tools start running automatically on pushing code into a repo or upon a pull request


4.What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes
.Improved readability as now all the purposes of the functions and modules are listed 
.Replacing the except blocks with specific exceptions helps us to handle them better and 
helps us to analyse errors or failures better
.Avoiding global parameters as it makes functions more readable and reusable
.eval() -replaced it with ast.literal_eval() eliminated potential code injection vulnerabilities flagged by Bandit 
Functions named according to PEP conventions using snake case standardised the module.