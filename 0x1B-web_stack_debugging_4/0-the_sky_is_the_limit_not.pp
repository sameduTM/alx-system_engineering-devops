# simulate HTTP requests to a web server

# increase ULIMIT of default file
exec { 'nginx-fix';
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
} ->

exec { 'restart-nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
