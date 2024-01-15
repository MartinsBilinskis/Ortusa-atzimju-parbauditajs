# Ortusa atzīmju pārbaudītājs

## Programmas mērķis
Šīs programmas mērķis ir atsūtīt patieso vērējumi, ko esi saņēmis par pārbadījumu. Ortus atsūta e-pastu par to ka ir pievienota jauna atzīme, bet e-pastā nesaka, to cik patiesībā ir šī atzīme, tāpēc šī programma atsūta patieso vērtējumu.

![Problema](https://github.com/MartinsBilinskis/Ortusa-atzimju-parbauditajs/assets/144620146/e67643dc-3bfa-41d6-a3fc-df7f47d2a4eb)

## Uzstādes process
Pirms programmas palaišanas ir nepieciešams ierakstīt savējos kredenciāļus failā settings. Pie mainīgā "test_email" var uzstādīt e-pastu no kura sūtīs, lai pārbaudītu, vai programma strādā. G-mail parolei vajag radīt "app-password". Ir arī nepieciešams visus lielumus pierakstīt python sintaksē. 

Tā kā programma strādā ar "Chrome" pārlūku to arī ir nepieciešams ieinstalēt, lai selenium strādātu.

Ir arī nepieciešams vai nu ortusā uzlikt ka vērtējumus sūta uz g-mail vai arī savs ortusa pasts (outlook) jauzstāda, lai tas automatiski pārsūta vēstules uz g-mail. Ja izvēlas pārsūtīt no outlook uz g-mail tad settingos vajag ierakstīt savu ortusa e-pasta adresi pie "test_email"

## Programmas lietošana
Pēc uzstādes, šī programma strādā fonā. Pēc norādītā perioda tā pieslēdzas e-pastam un pārbauda vai nav jauna ziņa no ortusa par atzīmi, ja ir tad tā neatverot jaunus logus iees ortusā un atsūtīts atpakaļ uz e-pastu vērtējumu. 

## Video ar to kā programma strādā


https://github.com/MartinsBilinskis/Ortusa-atzimju-parbauditajs/assets/144620146/32463c15-7c6f-4b84-9b62-31f5d6c45f53


## Programmas darbības pamati
Programma uzņem laiku no sākšanas brīža. Tad ieiet e-pastā un pārbauda vai kopš uzņemtā laika nav ienākusi vēstule no noreply-estudijas@rtu.lv vai cita uzstādītā e-pasta. Ja nav, tad programma iziet no imap savienojuma un atkal piefiksē laiku. Tad gaida uzstādīto periodu. Ja ir ienākusi jauna vēstule, (vai vairākas) tad tiek atrasta saite, kurā ir rakstīts vērtējums. No sākuma tiek atvērts ortus chrome pārlūkā headless režīmā un programma ielogojas, pēc tam dodas uz atrasto saiti. Atrastajā saitē tiek nolasīts, gan vērtējums, gan priekšmeta nosaukums. Šis vērtējums pēc tam tiek nosūtīts uz g-mail adresi. Tēmas sadaļā tiek pierakstīts, kurā priekšmetā ir jauna atzīme, un galvenajā daļā ir norāda jauno atzīmi. Pēc vēstules izsūtīšanas programma iziet no chrome pārlūka, kā arī no imap un smtp savienojumiem. Uzņem atkal esošo laiku un gaida uzstādīto periodu. Pēc perioda viss atkārtojas, līdz programma tiek pārtraukta.

## Izmantotās bibliotēkas
### Selenium
Selenium tiek izmantots, lai varētu tikt iekšā ortusā un varētu nolasīt vērtējumu.

### smtplib
Ar smtplib nosūtam e-pastu paši uz savu e-pastu.

### email
Lai vieglāk varētu veidot izsūtāmus e-pastus.

### imaplib
Tiek izmantots, lai nolasītu e-pasta saturu.

### pytz
Ar pytz palīdzību tiek uzstādīta vienāda laika zona starp datoru, uz kura uzstādīta programma un ar saņemto e-pastu.

### time
Time tiek izmantots, lai varētu uzstādīt pauzi starp pārbaudes ciklu.
