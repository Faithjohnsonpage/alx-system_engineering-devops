# Puppet script to create ssh config file

file { '/home/ermac/.ssh/config':
  ensure  => present,
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
  mode    => '0600',
  owner   => 'ermac',
  group   => 'ermac',
}
