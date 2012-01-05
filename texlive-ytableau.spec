# revision 21264
# category Package
# catalog-ctan /macros/latex/contrib/ytableau
# catalog-date 2011-02-01 18:07:03 +0100
# catalog-license lppl1.2
# catalog-version 1.1
Name:		texlive-ytableau
Version:	1.1
Release:	2
Summary:	Many-featured Young tableaux and Young diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ytableau
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ytableau.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several functions for drawing Young
tableaux and Young diagrams, extending the young and youngtab
packages but providing lots more features. Skew and coloured
tableaux are easy, and keyval-syntax configuration is provided.

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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
