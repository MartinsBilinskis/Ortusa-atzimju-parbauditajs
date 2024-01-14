# Ortusa-atzimju-parbauditajs

## Programmas mērķis
Šīs programmas mērķis ir atsūtīt patieso vērējumi, ko esi saņēmis par pārbadījumu. Ortus atsūta e-pastu par to ka ir pievienota jauna atzīme, bet e-pastā nesaka, to cik patiesībā ir šī atzīme, tāpēc šī programma atsūta patieso vērtējumu.

## Uzstādes process
Pirms programmas palaišanas ir nepieciešams ierakstīt savējos kredenciāļus failā settings. Pie mainīgā "test_email" var uzstādīt e-pastu no kura sūtīs, lai pārbaudītu, vai programma strādā. G-mail parolei vajag radīt "app-password". Ir arī nepieciešams visus lielumus pierakstīt python sintaksē.



## Izmantotās bibliotēkas
### Selenium
Selenium tiek izmantots, lai varētu tikt iekšā ortusā un varētu nolasīt vērtējumu.

### smtplib
Ar smtplib nosūtam e-pastu paši uz savu e-pastu.

### email
Lai vieglāk varētu veidot e-pastu struktūru un tos izsūtītu.

### imaplib
Tiek izmantots, lai nolasītu e-pasta saturu.

### pytz
Ar pytz palīdzību tiek uzstādīta vienāda laika zona starp datoru, uz kura uzstādīta programma un ar saņemto e-pastu.

### time
Time tiek izmantots, lai varētu uzstādīt pauzi starp pārbaudes ciklu.


Pie settings neuzstādīt minutes rādītāju mazāk par 1 ārpus testēšanas nolūkiem, jo citādāk tiks atkārtoti nosūtīti vieni un tie paši e-pasti līdz minūtes beigām.
