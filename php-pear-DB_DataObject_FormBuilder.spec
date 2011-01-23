%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	DB_DataObject_FormBuilder
Summary:	%{_pearname} - automatically build HTML_QuickForm object from a DB_DataObject derived class
Summary(pl.UTF-8):	%{_pearname} - automatyczne budowanie obiektu HTML_QuickForm pochodzącego z DB_DataObject
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3083ac45329c7c6d14877d00f8da2020
URL:		http://pear.php.net/package/DB_DataObject_FormBuilder/
BuildRequires:	php-pear-PEAR >= 1:1.4.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-8
Requires:	php-pear-DB_DataObject >= 1.8.5
Requires:	php-pear-HTML_QuickForm >= 3.2.4
Suggests:	php-pear-Date
Suggests:	php-pear-HTML_QuickForm_ElementGrid
Suggests:	php-pear-HTML_Table
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Date.*) pear(HTML/Table.*) pear(HTML/QuickForm/ElementGrid.*)

%description
DB_DataObject_FormBuilder will aid you in rapid application
development using the packages DB_DataObject and HTML_QuickForm. For
having quick but working prototype of your application, simply model
the database, run DataObject`s CreateTable script over it and write a
script that passes one of the resulting objects to the FormBuilder
class. The FormBuilder class will automatically generate a simple but
working HTML_QuickForm object that you can use to test your
application. It also provides a processing method that will
automatically detect if an insert() or update() command has to be
executed after the form has been submitted. If you have set
DataObject`s links.ini file correctly, it will also automatically
detect if a table field is a foreign key and will populate a selectbox
with the linked table`s entry. There are many optional parameteres
that you can place in DataObjects.ini or in properties of your derived
classes, that you can use to fine-tune the form generation, gradually
turning the prototypes into fully features forms and you can take
control of any stage at the process.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB_DataObject_FormBuilder pomaga w budowaniu aplikacji opartych na
klasach DB_DataObject oraz HTML_QuickForm. W celu uzyskania szybkiego,
lecz działającego prototypu aplikacji, wystarczy stworzyć model bazy,
uruchomić skrypt CreateTable i zapisać skrypt przekazujący jeden ze
zwróconych obiektów do klasy FormBuilder. Klasa ta automatycznie
wygeneruje prosty lecz działający obiekt HTML_QuickForm, który można
użyć do przetestowania aplikacji. Dostarcza także metod automatycznie
wykrywających czy komenda insert() lub update() musi być wykonana
przed wysłaniem formularza. Jeśli plik links.ini został poprawnie
skonfigurowany, DataObject automatycznie wykryje czy pole tabeli jest
kluczem obcym i rozpropaguje element formularza typu selectbox z
polami połączonej tabeli. Istnieje także wiele dodatkowych parametrów,
które można umieścić w pliku DataObjects.ini lub przekazać jako
parametr do klasy pochodnej, dzięki którym można usprawnić generowanie
formularza, stopniowo przekształcając prototypy w pełni konfigurowalne
formularze.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# packaging tools
rm .%{php_pear_dir}/data/DB_DataObject_FormBuilder/tools/fix0.9.0Files.php
rm .%{php_pear_dir}/data/DB_DataObject_FormBuilder/tools/fixPre1.52CVSFiles.php
rm .%{php_pear_dir}/package.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/DB/DataObject/FormBuilder.php
%{php_pear_dir}/DB/DataObject/FormBuilder
