# Using Puppet, install flask from pip3, Version must be 2.1.0


exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
