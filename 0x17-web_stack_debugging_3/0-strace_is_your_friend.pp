#  Using strace, find out why Apache is returning a 500 error. Fix it and then automate it using Puppet

exec {'fix Apache Error':
    command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => shell,
}
