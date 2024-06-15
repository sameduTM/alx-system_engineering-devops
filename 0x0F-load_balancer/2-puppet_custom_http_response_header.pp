# puppet_custom_http_response_header.pp

node default {

  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running and enabled at boot
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/nginx.conf'],
  }

  # Ensure the hostname is available as a fact
  Facter.add('hostname') do
    setcode do
      Facter::Core::Execution.exec('hostname')
    end
  end

  # Configure Nginx to include the custom HTTP header
  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx/nginx.conf.erb'),
    notify  => Service['nginx'],
  }

  # Create a template for nginx.conf with the custom header
  file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/nginx.conf.erb':
    ensure  => file,
    content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;
        root /var/www/html;

        location / {
            try_files \$uri \$uri/ =404;
            add_header X-Served-By <%= @hostname %>;
        }
    }
}
",
    notify  => Service['nginx'],
  }

}
