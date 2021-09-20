package Solution;

use 5.030;
use strict;
use warnings;
use Exporter qw(import);

our @EXPORT_OK = qw(multiply);

sub multiply {
    my $a = shift;
    my $b = shift;
    return $a * $b;
}

1;