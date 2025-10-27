1.Which issues were the easiest to fix, and which were the hardest? Why?
Adding docstring to functions and modules and renaming functions to snake-case were the easiest and changing the global variable was the hardest as the the variable was reference at various places and so many functions had to be rewritten by passing a parameter instead of using the global variable directly


2.Did the static analysis tools report any false positives? If so, describe one example.
inventory_system.py:31:4: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
inventory_system.py:43:8: W1203: Use lazy % formatting in logging functions (logging-fstring-interpolation)
The static analysis tool pylint says to use a lazy evaluation function inside logging instead of using an f string though this doesnt affect the quality of code


3.How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.

Automation in Continuous Integration (CI) pipelines enhances the software development process by ensuring that code is automatically built, tested, and analyzed whenever changes are made to a repository. Tools such as GitHub, Jenkins, and GitHub Actions support this automation through workflow configurations defined in YAML files or Jenkinsfiles.
When new code is pushed or a pull request is created, these workflows are triggered to perform tasks such as building the project, executing automated tests, and running static code analysis using tools like SonarQube, ESLint, or Pylint. The analysis results are then reported back to the repository, enabling to identify and address potential issues early in the development cycle.
Overall, this automation improves code quality, reduces integration errors, and promotes consistency and efficiency throughout the software development lifecycle.


4.What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes
.Improved readability as now all the purposes of the functions and modules are listed 
.Replacing the except blocks with specific exceptions helps us to handle them better and 
helps us to analyse errors or failures better
.Avoiding global parameters as it makes functions more readable and reusable
.eval() -replaced it with ast.literal_eval() eliminated potential code injection vulnerabilities flagged by Bandit 
Functions named according to PEP conventions using snake case standardised the module.