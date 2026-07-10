%global tl_name ajl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX style for AJL
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/ajl.bst
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ajl.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Bibliographic style references in style of Australian Journal of
Linguistics.

