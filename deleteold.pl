#!/usr/bin/perl
use strict;
use warnings;

use File::Find;
use Time::Piece;
#use Data::Dumper;

#my $rootFolder=$ARGV[0];
my $rootFolder="/opt/wso2bam-2.2.0/tmp";
find(\&process, $rootFolder);
print "Last executed: ", localtime->strftime('%Y-%m-%d %H:%M:%S'), "\n";

sub process{
	my $lastaccessed=(stat($File::Find::name))[9];
	my $diffsecs=time()-$lastaccessed;
	#si no se ha accedido en más de 24h se borra
	if($diffsecs>86400){
		print "Deleted ".$File::Find::name."\n";
		unlink $File::Find::name;
	}

}
