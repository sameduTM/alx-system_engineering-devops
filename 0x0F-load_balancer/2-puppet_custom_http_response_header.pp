# Puppet manifest to configure Nginx with a custom HTTP header

exec { 'update':
  provider => 'shell',
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

exec { 'add_header':
  provider    => 'shell',
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;
  \n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  require     => Package['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['add_header'],
}
