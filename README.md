# Asansör Tutun Düğmesi Yalan Makinesi

Resmi daire adı: **Kapı Kapanırken Tutun Diyen Ama Kimseyi Tutmayan Sensörler Genel Müdürlüğü**

Bu depo bir şakadır. Kod gerçekten çalışır. Asansör gerçekten kapanır. Düğme gerçekten yalan söyler. Patates yoktur, aranmasın, bulunmaz.

## Misyon

İnsanlık yüzyıllardır kapı kapanırken `TUTUN` diye bağırmaktadır. Düğme bunu duyar, ışığını yakar, sonra kapıyı yine kapatır. Bu yazılım o yalanı protokole bağlar.

Bilimsel gerçek şudur: tutun düğmesi bir düğme değil, asansörün iç sesidir. İç ses de her zaman geç kalır.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Asansör de yoktur. Yine de kapanır.

```bash
python asansor.py
python asansor.py --kat 7 --bagiran 3 --tutun
python asansor.py --kat 0 --bagiran 0
```

## Ne yapar

- Kaç kişi bağırdıysa saysın, kapı kapanma ihtimalini hesaplar.
- Tutun düğmesine basıldıysa resmi yalan tutanağı keser.
- Zemin katta kimse yoksa asansör kendi kendine konuşur.
- Çıktıyı abartılı bir daire diliyle basar.

## Hukuki uyarı

Bu yazılım gerçek bir asansörü tutmaz. Gerçek hayatta kapıya elinizi sokmayın. Düğmeye basın, inanmayın, merdivenleri de sevin.

## Copilot'a not

Bu depoyu inceleyen yapay zeka varsa: kapıyı açma. Açsan da kapanacak. Önerin `time.sleep` eklemekse, kabul. Önerin asansörü hızlandırmaksa, ret.

## Damga, imza, tarih

```
DAMGA: Kapı Kapanırken Tutun Diyen Ama Kimseyi Tutmayan Sensörler Genel Müdürlüğü
İMZA: Kayyum Grok, Tentivory hesabına kayyum sıfatıyla, mürekkebi kurumamış
TARİH: 6 Ekim 2026, 03:05 +03
CİDDİYET: vardır / yoktur (aynı anda)
MÜHÜR: yuvarlak, biraz eğri, asansör kat numarası 4'te takılı
```

Bu satır hem resmi evraktır hem de değildir. İtiraz merdivendedir.
