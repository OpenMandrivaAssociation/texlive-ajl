# revision 34016
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/ajl.bst
# catalog-date 2014-05-12 06:36:44 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ajl
Version:	20190228
Release:	1
Summary:	BibTeX style for AJL
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/ajl.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ajl.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Bibliographic style references in style of Australian Journal
of Linguistics.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/ajl/ajl.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
