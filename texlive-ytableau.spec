Name:		texlive-ytableau
Version:	59580
Release:	2
Summary:	Many-featured Young tableaux and Young diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ytableau
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several functions for drawing Young
tableaux and Young diagrams, extending the young and youngtab
packages but providing lots more features. Skew and coloured
tableaux are easy, and pgfkeys-enabled options are provided
both at package load and configurably.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ytableau/ytableau.sty
%doc %{_texmfdistdir}/doc/latex/ytableau/README
%doc %{_texmfdistdir}/doc/latex/ytableau/ytableau.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ytableau/ytableau.dtx
%doc %{_texmfdistdir}/source/latex/ytableau/ytableau.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
