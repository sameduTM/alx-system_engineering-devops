# fix our stack to handle all requests

exec { 'replace nginx ulimit':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
  notify  => Exec['restart nginx'],
  require => Package['nginx'],
}

exec { 'restart nginx':
  command     => 'service nginx restart',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true,
}

package { 'nginx':
  ensure => installed,
}

