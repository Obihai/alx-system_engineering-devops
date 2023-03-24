# 0x0A. Configuration management
This repository contains Puppet manifests for three different tasks: creating a file, installing a package, and executing a command.


# Requirements
## General ##
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
* Your Puppet manifests must run without error
* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
* Your Puppet manifests files must end with the extension .pp

# Tasks
## 1. Creating a file ##
The manifest for creating a file is located in the `0-create_A_file.pp` file. This manifest uses Puppet's `file` resource type to create a file at `/tmp/school` with the following properties:

* File permission is 0744
* File owner is www-data
* File group is www-data
* File contains I love Puppet

To apply this manifest, run the following command:

```
sudo puppet apply 0-create_A_file.pp
```

## 2. Installing a package ##
The manifest for installing a package is located in the `1-install_a_package.pp` file. This manifest uses Puppet's package resource type to install Flask from pip3 with the version `2.1.0`.

To apply this manifest, run the following command:

```
sudo puppet apply 1-install_a_package.pp
```

## 3. Executing a command ##
The manifest for executing a command is located in the `2-execute_a_command.pp` file. This manifest uses Puppet's `exec` resource type to kill a process named killmenow using the `pkill` command.

To apply this manifest, run the following command:

```
sudo puppet apply 2-execute_a_command.pp
```
Please note that it's important to use caution and verify that the command you're running is safe and expected, especially when using the `exec` resource type.

