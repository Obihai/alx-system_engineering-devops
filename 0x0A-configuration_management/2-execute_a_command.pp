# This manifest kills a process named "killmenow" using the pkill command
exec { 'killmenow':
  command => 'pkill killmenow',
}

