# revision 27044
# category Package
# catalog-ctan /macros/latex/contrib/ytableau
# catalog-date 2012-06-20 07:49:06 +0200
# catalog-license lppl1.2
# catalog-version 1.2
Name:		texlive-ytableau
Version:	1.2
Release:	1
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 813204
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757778
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719969
- texlive-ytableau
- texlive-ytableau
- texlive-ytableau

