# Using Puppet to install flask from pip3

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'python3-pip':
  ensure  => 'installed',
  require => Exec['apt-get update']
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}

