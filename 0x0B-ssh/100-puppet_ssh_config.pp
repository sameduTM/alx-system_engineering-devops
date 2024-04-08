# using Puppet to make changes to our configuration file.

<<<<<<< HEAD
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
=======
>>>>>>> 6960be626f63615a04449dc32d8b28443a2db863
file { '/etc/ssh/ssh_config':
        ensure  => present,
        content =>"
          # SSH client config
          host*
          IdentifyFile ~/.ssh/school
          PasswordAuthentication no
        ",
}
