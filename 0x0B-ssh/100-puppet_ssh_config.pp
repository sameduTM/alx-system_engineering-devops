# using Puppet to make changes to our configuration file. 

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
  ensure => present,
  require => File['/etc/ssh/ssh_config'],
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  ensure => present,
  require => File['/etc/ssh/ssh_config'],
}

# Ensure the ssh_config file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
}
