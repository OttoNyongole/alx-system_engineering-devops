# Create the ~/.ssh/config with puppet
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '~/.ssh/config',
  content => 'Host *
     HostName 100.25.194.59
     User ubuntu
     IdentityFile ~/.ssh/school',
  mode    => '7000',
}
