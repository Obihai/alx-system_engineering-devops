# Install Flask version 2.1.0 from pip3 using Puppet
package { 'flask':
  ensure => '2.1.0',
}
