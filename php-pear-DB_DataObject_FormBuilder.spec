%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       DataObject_FormBuilder
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class to automatically build HTML_QuickForm object from a DB_DataObject derived class
Summary(pl):	%{_pearname} - klasa do automatycznego budowania obiektu HTML_QuickForm pochodz�cego z DB_DataObject
Name:		php-pear-%{_pearname}
Version:	0.8.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	17a34041fa7a1830dc721ea7a01f723c
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} will aid you in rapid application development using the
packages DB_DataObject and HTML_QuickForm. For having quick but working
prototype of your application, simply model the database, run
DataObject`s CreateTable script over it and write a script that passes
one of the resulting objects to the FormBuilder class. The FormBuilder
class will automatically generate a simple but working HTML_QuickForm
object that you can use to test your application. It also provides a
processing method that will automatically detect if an insert() or
update() command has to be executed after the form has been submitted.
If you have set DataObject`s links.ini file correctly, it will also
automatically detect if a table field is a foreign key and will populate
a selectbox with the linked table`s entry. There are many optional
parameteres that you can place in DataObjects.ini or in properties of
your derived classes, that you can use to fine-tune the form generation,
gradually turning the prototypes into fully features forms and you can
take control of any stage at the process.

This class has in PEAR status: %{_status}.

%description -l pl
%{_pearname} pomaga w budowaniu aplikacji opartych na klasach
DB_DataObject oraz HTML_QuickForm. W celu uzyskania szybkiego, lecz
dzia�aj�cego prototypu aplikacji, po prostu stw�rz model bazy, uruchom
skrypt CreateTable i zapisz skrypt przekazuj�cy jeden ze zwr�conych
obiekt�w do klasy FormBuilder. Klasa ta automatycznie wygeneruje prosty
lecz dzia�aj�cy obiekt HTML_QuickForm, kt�ry mo�esz u�y� aby
przetestwoa� aplikacji. Dostarcza tak�e metod automatycznie
wykrywyaj�cych czy komenda insert() lub update() musi by� wykonana przed
wys�aniem formularza. Je�li plik links.ini zosta� poprawnie
skonfigurowany, DataObject automatycznie wykryje czy pole tabeli jest
kluczem obcym i rozpropaguje element formularza typu selectbox z polami
po��czonej tabeli. Istnieje tak�e wiele dodatkowych parametr�w kt�re
mo�esz umie�ci� w pliku DataObjects.ini lub przekaza� jako parametr do
klasy pochodnej, dzi�ki kt�rym mo�esz usprawni� generowanie formularza,
stopniowo przekszta�caj�c prototypy w pe�ni konfigurowywalne formularze.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
