# A Puppet manifest to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

file_line { 'replace_line':
  ensure => present,
  path   => $file_to_edit,
  line   => 'define("DB_PASSWORD", "php");',
  match  => '^define\("DB_PASSWORD", "phpp"\);',
}
