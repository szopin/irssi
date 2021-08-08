Name:           irssi
Version:        1.1.3
Release:        1
Summary:        Modular, Secure, and Well Designed IRC Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            http://www.irssi.org
Distribution:	SailfishOS
Packager:	szopin
Source:         https://github.com/irssi/irssi/releases/download/%{version}/irssi-%{version}.tar.xz


%description
Irssi is a modular IRC client for UNIX that currently only has a text
mode user interface. However, 80-90% of the code is not text mode
specific, so other UIs could be created easily. Also, Irssi is not
really even IRC specific anymore. There are already working SILC and
ICB modules available. Support for other protocols, like ICQ and
Jabber, could be added some day, too.

It is the code that separates Irssi from ircII, BitchX, epic, and the
rest of the text clients. It is not using the ircII code.


%files
%config(noreplace) %{_sysconfdir}/irssi.conf
%{_bindir}/irssi
# scripts & themes
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
