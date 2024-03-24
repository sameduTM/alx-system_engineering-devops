# using Puppet to make changes to our configuration file. 

file { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
  ensure => present,
}

file { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  ensure => present,
}

# Ensure the ssh_config file exists
file { '/etc/ssh/ssh_config':
  ensure => file,
}
