%include	/usr/lib/rpm/macros.perl
Summary:	The webgrep tool box consists of 7 utilities for the web-master
Summary(pl):	Webgrep jest zestawem 7 narzêdzi dla webmastera
Name:		webgrep
Version:	2.12
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://main.linuxfocus.org/~guido.socher/%{name}-%{version}.tar.gz
# Source0-md5:	c15b7f37b9cae5942172f593bc5fc218
Patch0:		%{name}-FHS.patch
URL:		http://www.linuxfocus.org/~guido.socher/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Webgrep is a set of different check and search utilities for the
web-master:
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
  on by adding them after the next newline outside a tag.

%description -l pl
Webgrep jest zestawem prostych narzêdzi dla webmastera:
- taggrep jest programem wyszukuj±cym znaczniki html, np. znaczniki
  meta albo tytu³y stron.
- lshtmlref buduje archiwa tar ze stron webowych, do³±czaj±c wszystkie
  obrazki, pliki tekstowe itd...
- blnkcheck jest wydajnym narzêdziem sprawdzaj±cym czy wszystkie linki
  w tre¶ci strony s± wa¿ne
- httpcheck jest post procesorem polecenia "blnkcheck -a" i mo¿e byæ
  u¿yty do sprawdzenia czy linki absolutne s± wa¿ne.
- webfgrep jest wydajn± przeszukiwark± sieci WWW
- srcgrep wyszukuje w tek¶cie strony znaczników <img ... src=...> albo
  <body ... background=...>
- hrefgrep dzia³a jak srcgrep tylko ¿e szuka znaczników <a
  href=...></a> albo <area ... href=...>.
- htmlpp usuwa znaki koñca linii w znacznikach html zawieraj±cych
  cz³on href=,name=,background=,src= i dodaje usuniêty znak w linii
  nastêpuj±cej po znaczniku.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/webgrep

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

install cgi-bin/* $RPM_BUILD_ROOT%{_datadir}/webgrep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/webgrep
