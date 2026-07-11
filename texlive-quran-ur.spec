%global tl_name quran-ur
%global tl_revision 74829

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.23
Release:	%{tl_revision}.1
Summary:	Urdu translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/quran-ur
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-ur.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-ur.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is prepared for typesetting some Urdu translations of the
Holy Quran. It adds eight Urdu translations to the quran package.

