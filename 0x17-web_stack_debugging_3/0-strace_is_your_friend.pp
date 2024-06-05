#fixing server error 500

exec { 'wp-fix':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => ['/usr/bin/', '/bin', '/usr/local/bin/']
}
