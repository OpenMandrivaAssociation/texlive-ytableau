# revision 21264
# category Package
# catalog-ctan /macros/latex/contrib/ytableau
# catalog-date 2011-02-01 18:07:03 +0100
# catalog-license lppl1.2
# catalog-version 1.1
Name:		texlive-ytableau
Version:	1.1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides several functions for drawing Young
tableaux and Young diagrams, extending the young and youngtab
packages but providing lots more features. Skew and coloured
tableaux are easy, and keyval-syntax configuration is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ytableau/ytableau.sty
%doc %{_texmfdistdir}/doc/latex/ytableau/README
%doc %{_texmfdistdir}/doc/latex/ytableau/ytableau.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ytableau/ytableau.dtx
%doc %{_texmfdistdir}/source/latex/ytableau/ytableau.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
