# Sharing my SSH client configuration for working without typing a password.

file { '/home/ermac/.ssh/config':
  ensure  => present,
  content => "
    Host *
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  "
}
