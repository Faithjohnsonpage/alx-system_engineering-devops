# Sharing my SSH client configuration for working without typing a password
# using Puppet.

file_line { 'Turn off passwd auth':
  path    => '/home/ermac/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^#*PasswordAuthentication',
}

file_line { 'Declare identity file':
  path    => '/home/ermac/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#*IdentityFile',
}
