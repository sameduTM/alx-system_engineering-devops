# Using Puppet, create a manifest that kills a process named killmenow.


exec { 'terminate_killmenow_processes':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  provider    => 'shell',
  onlyif      => "pgrep -f killmenow",
}
