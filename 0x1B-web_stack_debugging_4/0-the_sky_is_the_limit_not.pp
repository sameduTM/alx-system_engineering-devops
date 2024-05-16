# fix our stack to handle all requests
exec { 'extend nginx limit':
  command  => "sudo sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx reload",
}
