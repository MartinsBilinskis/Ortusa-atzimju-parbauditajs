# Ortusa-atzimju-parbauditajs

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
