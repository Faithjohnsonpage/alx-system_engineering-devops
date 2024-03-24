# Sharing my SSH client configuration for working without typing a password.

file { '~/.ssh/config':
  ensure  => present,
  content => "
    Host your_server_address
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  "
}
