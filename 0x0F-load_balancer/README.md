# 0x0F. Load Balancer

This repository contains the solutions to the tasks of the `0x0F. Load Balancer` project in the ALX System Engineering & DevOps curriculum. The project covers the basics of load balancing and using HAProxy to balance the load across multiple servers.

## Files

The repository contains the following files:

* `0-custom_http_response-header`: A configuration file that sets a custom HTTP response header on a server.
* `1-install_load_balancer`: A Bash script that installs and configures HAProxy on a server to balance the load across two Apache web servers.
* `2-puppet_custom_http_response-header.pp`: A Puppet manifest that sets a custom HTTP response header on a server using Puppet.
* `3-puppet_install_load_balancer.pp`: A Puppet manifest that installs and configures HAProxy on a server using Puppet to balance the load across two Apache web servers.

## Usage

To use any of the files in this repository, follow the instructions provided in the file's comments or the task instructions.

For example, to use the Bash script that installs and configures HAProxy on a server, execute the following command on the server:

```bash
$ ./1-install_load_balancer
```
