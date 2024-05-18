# Puppet manifest to configure Nginx with a custom HTTP header

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is enabled and running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}

# Create the custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => template('custom_header/custom_header.conf.erb'),
  require => Package['nginx'],
}

# Create the directory for the custom template if it doesn't exist
file { '/etc/puppetlabs/code/environments/production/modules/custom_header/templates':
  ensure => directory,
}

# Create the custom template
file { '/etc/puppetlabs/code/environments/production/modules/custom_header/templates/custom_header.conf.erb':
  ensure  => file,
  content => "# Custom Nginx configuration to add a custom header
server {
    listen 80;
    server_name _;

    location / {
        add_header X-Served-By <%= @hostname %>;
    }
}
",
  require => File['/etc/puppetlabs/code/environments/production/modules/custom_header/templates'],
}

# Obtain the hostname and pass it to the template
$hostname = $facts['networking']['hostname']
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => template('custom_header/custom_header.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
  with    => { 'hostname' => $hostname },
}
