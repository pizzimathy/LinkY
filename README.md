# LinkY

LinkY allows people creating command line interfaces to test their commands and packages
easily. The program creates globally installed symlinks for specified packages and
commands so that you can test your package structures, specify your commands, and run tests.

### configuration
Consider a sample directory structure:

    proj/
        |__ main_package/
        |   |__ index.py
        |   |__ ...
        |
        |__ setup.py
        |__ README.md
        |__ LICENSE.md
        
To configure LinkY, we add a `linky.json` file in the project's root directory:

    proj/
        |__ main_package/
        |   |__ index.py
        |   |__ ...
        |
        |__ setup.py
        |__ README.md
        |__ LICENSE.md
        |__ linky.json
        
Then, we can write in the configurations:
        
    linky.json
    
    {
        "name": "main_package",
        "bin": {
            "any_command" : "index.py"
        }
    }
    
LinkY will identify the main package and retrieve the specified entry point file.

### usage
`$ linky link` or `$linky -l` wires up an executable file and globally installs your package. In our example, running
`$ any_command` will run the specified entry point file.

`$ linky unlink` or `$ linky -u` uninstalls the your package and disables the specified command.

### notes
- unlinking does not delete your package or files
- `linky.json` will be overwritten to save package and command locations, but the data you entered will remain intact