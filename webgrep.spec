Summary:	The webgrep tool box consists of 7 utilities for the web-master
Summary(pl):	Webgrep jest zestawem 7 narzêdzi dla webmastera
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Name:		webgrep
Version:	2.9
Release:	1
License:	GPL
Source0:	http://www.linuxfocus.org/~guido.socher/%{name}-%{version}.tar.gz
Patch0:		%{name}-FHS.patch
URL:		http://www.linuxfocus.org/~guido.socher/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- taggrep is a program to grep for html tags. E.g search for meta tags
  or list the title of a number of web pages.
- lshtmlref is a nice utility to build tar archives from webpages and
  include all the necessary GIFs, textfiles etc..
- blnkcheck is an efficient web search utility that checks web-pages
  for broken links.
- httpcheck is a post processor for "blnkcheck -a" and can be used to
  check absolute links of protocol type http. It does the checks by
  sending HEAD requests to the webservers for the page in question.
- webfgrep is an efficient web search engine that works well for up to
  websites with up to 1Mb of html pages.
- srcgrep searches web-pages for <img ... src=...> or <body ...
  background=...> and displays the data contained in the tag in a nice
  readable format.
- hrefgrep is like srcgrep except that is searches for <a
  href=...>...</a> or an area tag of the from <area ... href=...>.
- htmlpp removes line breakes in html tags that contain one of
  href=,name=,background=,src= and compensate the removed newlines later
  on by adding them after the next newline outside a tag

%prep
%setup -q
%patch0 -p1

%build
%{__make} CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/webgrep

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__install} cgi-bin/* $RPM_BUILD_ROOT%{_datadir}/webgrep

gzip -9nf README webgrep-2.9.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/webgrep
