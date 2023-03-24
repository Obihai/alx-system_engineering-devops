# This manifest kills a process named "killmenow" using the pkill command
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
