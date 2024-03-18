# using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
        ensure  => present,
        content =>"
          # SSH client config
          host*
          IdentifyFile ~/.ssh/school
          PasswordAuthentication no
        ",
}
