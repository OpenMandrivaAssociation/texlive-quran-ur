Name:		texlive-quran-ur
Version:	68314
Release:	1
Summary:	Urdu translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quran-ur
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-ur.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-ur.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is prepared for typesetting some Urdu translations
of the Holy Quran. It adds eight Urdu translations to the quran
package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quran-ur
%doc %{_texmfdistdir}/doc/latex/quran-ur

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
