# Ortusa atzīmju pārbaudītājs

## Programmas mērķis
Šīs programmas mērķis ir atsūtīt patieso vērējumi, ko esi saņēmis par pārbadījumu. Ortus atsūta e-pastu par to ka ir pievienota jauna atzīme, bet e-pastā nesaka, to cik patiesībā ir šī atzīme, tāpēc šī programma atsūta patieso vērtējumu.

## Uzstādes process
Pirms programmas palaišanas ir nepieciešams ierakstīt savējos kredenciāļus failā settings. Pie mainīgā "test_email" var uzstādīt e-pastu no kura sūtīs, lai pārbaudītu, vai programma strādā. G-mail parolei vajag radīt "app-password". Ir arī nepieciešams visus lielumus pierakstīt python sintaksē. 

Tā kā programma strādā ar "Chrome" pārlūku to arī ir nepieciešams ieinstalēt, lai selenium strādātu.

Ir arī nepieciešams vai nu ortusā uzlikt ka vērtējumus sūta uz g-mail vai arī savs ortusa pasts (outlook) jauzstāda, lai tas automatiski pārsūta vēstules uz g-mail. Ja izvēlas pārsūtīt no outlook uz g-mail tad settingos vajag ierakstīt savu ortusa e-pasta adresi pie "test_email"

## Programmas lietošana
Pēc uzstādes, šī programma strādā fonā. Pēc norādītā perioda tā pieslēdzas e-pastam un pārbauda vai nav jauna ziņa no ortusa par atzīmi, ja ir tad tā neatverot jaunus logus iees ortusā un atsūtīts atpakaļ uz e-pastu vērtējumu. 

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
