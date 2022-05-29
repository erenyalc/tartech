from pathlib import Path
from turtle import width
import streamlit as st
from PIL import Image
import os
import sys
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form
import keras
from keras.preprocessing.image import *
from keras.applications.vgg19 import preprocess_input
from keras.models import Model , load_model
from tensorflow import *
import re
import base64


def button_two():
  st.header('TAHMİNLE')
  st.markdown('''
            Tahminlemenin daha doğru sonuç vermesi için;
            * Fotoğrafların iyi bir kalitede, anlaşılır olması gerekmektedir.
            * Bir fotoğrafta birden fazla yaprak gözükmesi önerilmez.
            * Yaprak fotoğraflarında arka plan olabildiğince sade olmalıdır. Başka bitkilerin gözükmesi tahminlemeyi bozabilmektedir.
            * Yaprağın olabildiğince açık ve net görünmesi gerekmektedir.
            Örnek olarak:
''')
  col1, col2, col3 = st.columns(3)
  with col1:
    st.image('orn1.jpg', width= 200)
  with col2:
    st.image('orn4.jpg', width=200)
  with col3:
    st.image('orn3.jpg', width=200)
            
  st.markdown('Aşağıdaki ‘Browse Files’ butonuna basıp fotoğraf yükleyerek tahminlemeyi başlatabilirsiniz.')
  image_file = st.file_uploader("Lütfen fotoğraf yükleyiniz:")
  try:
    with open(os.path.join("fileDir",image_file.name),"wb") as f:
        f.write((image_file).getbuffer())
  except AttributeError:
      st.write(' ')

  def load_image(image_file):
      
    imge = Image.open(image_file)
    return imge
    
  
  col1, col2, col3, col4 = st.columns(4)

  with col1:
    st.write("")
  with col2:
    try:
        st.image(load_image(image_file),width=370)
    except AttributeError:
      st.write(' ')
        
  with col3:
    st.write("")
  with col4:
      st.write('')
  

  #train_datagen = ImageDataGenerator(zoom_range = 0.5, shear_range = 0.3, horizontal_flip = True, preprocessing_function= preprocess_input)
  #val_datagen = ImageDataGenerator(preprocessing_function= preprocess_input)
  #train = train_datagen.flow_from_directory(directory = r"C:\Users\Erenyalc\bitpro\New Plant Diseases Dataset(Augmented)\New Plant Diseases Dataset(Augmented)\train", target_size= (256,256), batch_size= 32)
  #ref = dict(zip(list(train.class_indices.values()) , list(train.class_indices.keys())))
  ref = {0: 'Apple___Apple_scab', 1: 'Apple___Black_rot', 2: 'Apple___Cedar_apple_rust', 3: 'Apple___healthy', 4: 'Blueberry___healthy', 5: 'Cherry_(including_sour)___Powdery_mildew', 6: 'Cherry_(including_sour)___healthy', 7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 8: 'Corn_(maize)___Common_rust_', 9: 'Corn_(maize)___Northern_Leaf_Blight', 10: 'Corn_(maize)___healthy', 11: 'Grape___Black_rot', 12: 'Grape___Esca_(Black_Measles)', 13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 14: 'Grape___healthy', 15: 'Orange___Haunglongbing_(Citrus_greening)', 16: 'Peach___Bacterial_spot', 17: 'Peach___healthy', 18: 'Pepper,_bell___Bacterial_spot', 19: 'Pepper,_bell___healthy', 20: 'Potato___Early_blight', 21: 'Potato___Late_blight', 22: 'Potato___healthy', 23: 'Raspberry___healthy', 24: 'Soybean___healthy', 25: 'Squash___Powdery_mildew', 26: 'Strawberry___Leaf_scorch', 27: 'Strawberry___healthy', 28: 'Tomato___Bacterial_spot', 29: 'Tomato___Early_blight', 30: 'Tomato___Late_blight', 31: 'Tomato___Leaf_Mold', 32: 'Tomato___Septoria_leaf_spot', 33: 'Tomato___Spider_mites Two-spotted_spider_mite', 34: 'Tomato___Target_Spot', 35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 36: 'Tomato___Tomato_mosaic_virus', 37: 'Tomato___healthy'}
  model = load_model('https://github.com/erenyalc/tartech/blob/main/kod/model_d1.h5')
  try:
    imge = "https://github.com/erenyalc/tartech/tree/main/kod/fileDir/ {}".format(image_file.name)
  except AttributeError:
      st.write(' ')
  def prediction(imge):
      img = load_img(imge, target_size=(256, 256))
      i = img_to_array(img)
      im = preprocess_input(i)
      img = np.expand_dims(im, axis=0)
      pred = np.argmax(model.predict(img))
      # print(f'tahmin: {ref[pred]}')
      ctrl = ref[pred]
      #st.write(ctrl)
      if ctrl == 'Apple___Apple_scab':
          st.header('Elma - Kara Leke')
          col1, col2 = st.columns(2)
          with col1:
                st.image('e.karaleke2.jpg', width=350)
          with col2:
                st.image('e.karaleke1.jpg', width=369)
          st.subheader('Nedir?')
          st.markdown('Elma kara leke hastalığı, temelde bir mantar hastalığıdır. Hastalığın belirtileri ağacın yaprak, meyve ve sürgünlerinde görülür. Yaprağın üst ve alt yüzeyinde oluşan lekeler başlangıçta yağlımsı görünümdedir, giderek zeytin rengini alır ve daha sonra kahverengileşir.')
          st.markdown('Lekeler kadifemsi yapıdadır ve bu kısımdaki dokular zamanla ölür, üzerinde çatlaklar ve delikler oluşur. Ağır hastalıklı yapraklar erkenden sarararak dökülürler. Meyvelerdeki lekeler yeşilimtırak olup zamanla kahverengine dönüşür. Küçük lekeler zamanla birleşirler ve bu kısımlarda meyvenin gelişmesi durduğu için şekilsiz meyveler oluşur.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1 - Kültürel Önlemler
                        * Sonbaharda yere dökülmüş yaprakları temizlemek, yakmak
                        * Sıracalı dallar budanmalı
                        * Ağaçlar, yapraklardaki nemin daha hızlı kuruyabilmesi için hava akımına izin verecek şekilde taçlandırılmalı ve uygun aralıklar ile dikilmelidir.
                        2 - Kimyasal Tedavi
                        * İlaçlama: Çiçek gözleri kabardığında (dal sıracası bulunan yerlerde ise 3-5 gün önce yapılır)
                        * İlaçlama: Pembe çiçek tomurcuğu döneminde (çiçekler ayrı ayrı görüldüğünde)
                        * İlaçlama: Çiçek taç yaprakları %70-80 oranında döküldüğünde
                        * Ve diğer ilaçlamalar: Hastalığın ilerlemesi le paralel olarak ve mantarın etki süresi dikkate alınarak.
                        """)
      if ctrl == 'Apple___Black_rot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('e.siyahcurukluk2.jpg', width=350)
          with col2:
                st.image('e.siyahcurukluk1.jpg', width=390)
          st.header('Elma - Siyah Çürüklük')
          st.subheader('Nedir?')
          st.markdown('Elmada siyah çürüklük, Alternata fungal etmeni neden olmaktadır. Etmen, bitkinin zayıflamış veya ölmüş dokularında küçük yara izleri olarak yaşayabilmektedir.')
          st.markdown('Yaygın olarak her yerde bulunabilmektedir. Hastalığın gelişimi nemli ortam ve 26-28°C sıcaklıkta olmakla birlikte, 0°C’de dahi gelişme gösterebilmektedir. 8-10 gün içinde belirtiler ortaya çıkmaktadır. Hastalık çoğunlukla hasat öncesi ve sonrası meyve çürümelerine neden olur. İlk belirtiler, elmanın çiçek çukuru etrafında veya orta kısmında önceleri renk açılması şeklinde gerçekleşir. Daha sonra bu kısımlarda yassı ve kenarları belirgin şekilde çökük, kahverenginden siyah renge dönüşen lekeler gözlenir. Hastalıklı kısımdan kesit alındığında bu lekelerin altında meyve etinden çekirdeğe doğru derinlemesine ilerleyen çürümekte olan bölgeler görülür.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Meyvelerin elle toplanmasında dikkatli olunmalı, toplama ve paketleme esnasında meyveler ezilmemelidir.
                        * Depolama atmosferi ve sıcaklığı uygun olmalı, meyvenin muhafazası optimum şartlarda olmalıdır.
                        * Toplama yapılacak olan kasa veya sepetin yüzeyi uygun bir dezenfektan ile temizlenmeli veya meyve kasalara konmadan önce buhardan geçirilmelidir.
                        2- Kimyasal Tedavi
                        * 1. İlaçlama: Meyve Tatlanma başlangıcında
                        * 2. İlaçlama: İlacın etki süresi ve hasat süresine dikkat edilerek yapılacak ilaçlamalar. Genellikle Trifloxystrobin etken maddelli ilaçlar kullanılabilir.
                        """)
      if ctrl == 'Apple___Cedar_apple_rust':
            
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.pasakarı2.jpg')
            with col2:
                st.image('e.pasakarı1.jpg')
            st.header('Elma - Pas Akarı')
            st.subheader('Nedir?')
            st.markdown('Pas Akarı canlısı, iğ şeklinde, sarımsı kahverenginde ve uzunluğu 0.16-0.18 mm’dir. İki çift bacaklı ve gözle görülemeyecek kadar küçüktür.')
            st.markdown('Kışı ergin dişi döneminde, gevşek yapılı ağaç kabukları altında, tomurcuklara yakın yarık ve çatlaklarda, sürgünlerde, tomurcuk pulları altında gruplar halinde geçirir. Tomurcukların patlamasıyla ortaya çıkan zararlı, gelişmekte olan çiçekler ve yaprak dokusu üzerinde beslenmek amacıyla, ayrılan çiçek tomurcuklarına saldırır ve aynı zamanda kabarmakta olan odun gözlerine de geçerler. Mayısta ortaya çıkan erkek ve yazlık dişi bireyler çiftleştikten sonra, dişiler yumurtalarını çiçek tomurcukları ile odun gözlerinin yeşil aksamı üzerine bırakırlar. Çiftleşmeleri ilkbahar ve yaz süresince devam eder ve döller birbirine karışır.')
            st.subheader("Pas Akarının Zararlı Olduğu Bitkiler")
            st.markdown('Öncelikle elmada yaygın olarak bulunur. Armutta da zarara neden olabilir.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Pas Akarı Zarar Şekli')
                st.markdown("""
                        * Zararlı, yaprakların alt yüzünde keçeye benzer düzensiz şekli bozukluğuna neden olur, yaprakların alt yüzü donuk ve solgun, benekli bir görünüm alır.
                        * Akar ile yoğun olarak bulaşık yapraklar gümüşi bir renk alır ve daha sonra pas rengine veya kahverengine dönebilir.
                        * Şiddetli zarar görmiş yapraklar zamanla kuruyup büzülür, ağacın sürgün gelişimi zayıflar
                        * Bazen de zararlı, meyvelerde paslanma meydana getirerek, meyvenin pazar değerinin düşmesine neden olabilir.""")
            with col2:
                st.image('e.pas3.jpg')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Biyolojik Mücadele
                        * Doğal düşmanların korunması ve etkinliklerinin arttırılması için diğer zararlılarla mücadelede kimyasal mücadeleye alternatif metotlara öncelik verilmeli, eğer kimyasal mücadele gerekiyorsa, doğal düşmanlara yan etkisi en az olan bitki koruma ürünleri tercih edilmelidir.
                        2-	Kimyasal Tedavi
                        * Elma Pas Akarları’nın mücadelesine karar vermek için çiçeklenme öncesi ve çiçeklenme sonrası kontroller gereklidir. Mayısta 100 yaprakta yapılan sayımlarda yaprak başına ortalama 300-400 akar, ağustos ve eylül aylarında ise yaprak başına ortalama 700- 1000 akar bulunursa ilaçlama yapılır. Sayımlar, hazirandan başlayarak sürgünlerin uçtan itibaren 1/3’lük kısmındaki yapraklarda akar fırçalama aleti ile yapılır. Genellikle Acrinathrin 22,5 g/l+ Abamectin 12,6 g/l etken maddeli ürünler tercih edilmelidir.
                        """)
            st.subheader("Detaylı bilgi için: [tarimorman.gov](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/524)")
            st.subheader("Detaylı bilgi için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/elma-pasakari)")

      if ctrl == 'Apple___healthy':
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.sag2.jpg')
            with col2:
                st.image('e.sag1.jpg')
            st.header('Elma - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Elma ağaçları, serin ve ılıman iklimde yetiştirilmeye uygundur. Bu ağaçlar bol ışıklı ve güneşli ortamları sever.
                        * Nemli ve geçirgen topraklarda kolaylıkla büyüyebilirler. Ülkemizde pek çok yerde çeşitli elma ağaçları bulunur.
                        * Elmanın içeriğinde bulunan vitamin ve mineraller sayesinde hem kozmetik, hem ilaç sektöründe sıkça kullanılıyor.
                        * Elma ağaçları üretimine göre bodur, sarmaşık ve sarkıcı olmak üzere farklı çeşitlerde yetiştirilir.
                        * Elma ağaçları, aşılama, çelik ve kök sürgünleri ile üretilir.""")
            st.subheader('Elma Ağacı Ne Zaman Dikilir?')
            st.markdown('Aşılı kök elma ağacı fidanları, yaprak dökümü ile birlikte genellikle Kasım ayının 1. ya da 2 haftasından itibaren rakıma, bölgeye ve iklim şartlarına göre Nisan sonuna kadar ekilebilir. ')
            st.subheader('Nasıl Yetiştirilir ve Budanır?')
            st.markdown('Elma dünyanın her bölgesinde yetişen ve yaygın olarak ulaşılabilen bir meyvedir. Dünyada yaklaşık 7500 farklı elma çeşidi bulunur. Elmaların sağlıklı şekilde büyümeleri için uygun sıcaklığa ve toprağa sahip olması önem taşır. Elma bitkisinin 7 derece altında 1000 saat kadar bir soğuklanma süresine sahip olması, meyve üretimini artırır ve hızlandırır.')
            st.markdown('Fazla soğuğa gelmeyen elma bitkileri, 20 - 26 derece arası sıcaklıklarda ideal olarak yetişir. Elmanın olgunluk döneminde yağış olaylarının gerçekleşmesi meyve sağlığını olumsuz etkiler. Her çeşit toprakta yetişebilen elma, fazla rüzgarı ve sert hava koşullarını sevmez. Ticari elma yetiştiriciliğinde toprağın yabani otlardan temizlenmesi, havalandırılması ve gübrelenmesi ile birlikte uygun sıcaklık ve güneş ışığının bulunması elmaların sağlıklı ve bol olmasını sağlar.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Tohumdan Elma Yetiştirme Tekniği')
                st.markdown("""
                        * Olgun elma tohumlarını toplayın. 
                        * Bu toplanan tohumları kağıt havlu gibi nemlendirilmiş bir yatak içine koyun
                        * Daha sonra, nemli peçeteleri plastik bir torba içerisinde, uyuşukluklarını kırmak için yaklaşık 30 ila 50 gün boyunca buzdolabı içerisinde bekletin.
                        * Buzdolabından çıkardığınız tohumları toprağa ekin
                        * Elma filizleri göründüğünde, saksınızı güneşli ve açık alana taşıyın, böylece daha hızlı büyüyebilirler
                        * Elma bitkisinin iyi gelişimi için düzenli olarak sulayın. 
                        """)
            with col2:
                st.image('e.sag3.jpg', width=300)
            st.subheader('Nerede Yetiştirilir')
            st.markdown("Batı Asya kökenli olan elma, tarihçede Asya'dan Akdeniz'e ve Batı Avrupa'ya yayılmıştır. Ilıman iklim koşullarının olduğu her ülkede yetişebilen elma, -30 dereceye kadar soğuklara dayanabilir. Dünyada muz üretiminden sonra ikinci sıra gelen elma, her ekonomik seviyede olan bir meyvedir. Bu nedenle herkesin kolayca ulaşabileceği bir meyvedir.")
            
            st.subheader("Detaylı bilgi için: [Hürriyet](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")
            st.subheader("Detaylı bilgi için: [Çiçek Bakım Evi](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")
            st.subheader("Detaylı bilgi için: [Sakarya Üniversitesi](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")
          
      if ctrl == 'Blueberry___healthy':
          col1, col2 = st.columns(2)
          with col1:
              st.image('y.sag1.jpg', width=350)
          with col2:
              st.image('y.sag2.jpg', width=390)
          st.header('Yabanmersini - Sağlıklı')
          st.subheader('Özellikleri')
          st.markdown("""
                        * Ülkemizde yaban mersininin dört farklı türü görülüyor.
                        * Sonbahar sonunda veya ilkbahar başında 30-40 cm derinliğinde çukurlara dikilen ekinlerin kökleri ince olduğu için dikim sonrası kuru bırakılmaması önem arz ediyor. Bitki dikildikten sonra etrafına 10-15 cm kalınlığında malç seriliyor. Yaban mersini yetiştiriciliğinin 1 sene kadar öncesinde toprağın hazırlanması öneriliyor.
                        * pH değeri dengelenmesi için dikimden 6 ay kadar önce kükürt uygulamasının tamamlanması gerekiyor. Dikim sırasında sıra üzerinde 1.0-1.5 metre, sıra arasında 1.5-3.0m mesafe bırakılıyor. """)
          st.subheader('Hangi mevsimde ne zaman yetiştirilir?')
          st.markdown('Yaban mersini çeşidine bağlı olarak 4 ile 12 hafta arasında olgunlaşıyor. Genellikte yaz ortasından sonra, yaz sonunda hasada başlanıyor.')
          st.subheader('Kaç günde bir sulanır?')
          st.markdown('Mavi yemişlerin olgunlaşma mevsimi uzun olduğu için hasat süresi boyunca 10 günlük aralıkla 2-3 kez sulama yapılıyor. Sulama için hem damla sulama hem de yağmurlama sulama kullanılabiliyor.')
          st.subheader("Detaylı bilgi için: [yabanmersini.org](https://www.yabanmersini.org/yabanmersini-yetistiriciligi.html)")

      if ctrl == 'Cherry_(including_sour)___healthy':
            col1, col2 = st.columns(2)
            with col1:
                st.image('k.sag1.jpg', width=350)
            with col2:
                st.image('k.sag2.jpg', width=390)
            st.header('Kiraz, Vişne - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Kiraz ve vişne ağaçları 4 yaşında iken budama işlemi yapılır. Budama aletinin iyice temizlenmesine dikkat edilmelidir. Makasın keskin olmaması gerekmektedir. Ağacın ömrünü tamamladığında zaman kök budaması yapılarak, gençleştirme yapılır ve  ağaç yenilenir.
                        * Budama sonrası mutlaka ilaçlama yapılmalıdır.
                        * Toprak analizi yapıldıktan sonra gübreleme işlemi yapılır. Mart ayında hayvan gübresi ile yapılan  ağaçların gübrelenmesi işlemi ile gerekli vitaminler sağlanır. Şubat ayında komposit gübre yapılır.
                        * Her yıl bahar aylarında toprağın havalandırma işlemi yapılır. Çiçekler açmadan önce çapa ile çapalanması önemli bir noktadır. Sonbahar geldiğinde de hasat sonrasında havalandırma yapılır.
                        * Hasat zamanı önemlidir. Meyve toplama aşamasında yapraklara ve dallara zarar verilmemesi gerekir. Özellikle göz kısmının koparılmaması önemlidir.
            """)
            st.subheader('Nasıl Yetiştirilir?')
            st.markdown('Kiraz ağaçları kış aylarında belirli bir süre dinlenmeyi, çiçeklenmeyi ve hasadı seven bir meyve ağacıdır. Üretimi en erken olabileceği gibi çok geç zamana kadar yayılan bir yetiştirme zamanına sahip bir ağaçtır.')
            st.markdown('Kiraz genelde çok düşük ve fazla yüksek sıcakları sevmez. Kiraz ağacı soğukların -20 ve -25 derece altında olduğu bölgelerde yetiştirme yapılmamalıdır. Donlar ağaçlara zarar vermektedir.')
            st.subheader('Kaç günde bir sulanır?')
            st.markdown('Düzenli bir şekilde yılda 600 mm üzerinde yağış olan bölgelerde kiraz ağacının sulanmasına ihtiyaç yoktur. Fakat 600 mm altında yağış alan bir yerde ise yaz aylarında 2-3 defa sulanması yeterlidir. Tabii ki bozuk olmayan topraklar da bu sulama sistemi geçerlidir. Topraklar bozuldukça, su tutmadığı için daha fazla su istemektedir ve masrafları da artmaktadır.')
            st.subheader("Detaylı bilgi için: [cicekal](https://www.cicekal.net/blog/kiraz-agaci-bakimi/)")

          
      if ctrl == 'Cherry_(including_sour)___Powdery_mildew':
          col1, col2 = st.columns(2)
          with col1:
                st.image('vk.küllenme1.jpg', width=350)
          with col2:
                st.image('vk.küllenme2.jpg', width=370)
          st.header('Kiraz, Vişne - Küllenme')
          st.subheader('Nedir?')
          st.markdown('Halk arasında basıra adıyla da anılan bir mantar hastalığıdır. Nemli ortamlarda daha sık rastlanan hastalık, yağmurdan, çiğden sonra hızlı yayılma özelliği gösterilmektedir. Alt yapraklardan ilerleyerek kısa sürede tüm ekini saran külleme, taze yaprak ve sürgünleri de etkisi altına alabilmektedir. Yapraklarda un serpilmiş gibi puslu ve tozlu bir görünüm yaratılır. Beyazlayan yapraklarda öbek öbek kümelenme görülmektedir.  Lekelenme artarak yaprağın ve ekinin tüm yüzeyini kaplayabilir.  Canlı bitki hücrelerinden beslenen mantarlar, yaşayan bir mahsül bulamadığında hayatta kalamıyor, müdahale edilmediğinde canlı bitkinin her yerini sarmaktadır. Bulaşıcı bir hastalıktır.')
          st.markdown('Farklı bitki türlerinde sık sık görülen külleme hastalığı, halk arasında basıra adıyla da anılıyor. Nemli ortamlarda daha sık rastlanan hastalık, yağmurdan, çiğden sonra hızlı yayılma özelliği gösteriyor. Alt yapraklardan ilerleyerek kısa sürede tüm ekini saran külleme, taze yaprak ve sürgünleri de etkisi altına alabiliyor. Yapraklarda un serpilmiş gibi puslu ve tozlu bir görünüm yaratıyor. Beyazlayan yapraklarda öbek öbek kümelenme görülüyor.  Lekelenme artarak yaprağın ve ekinin tüm yüzeyini kaplayabiliyor. Hastalığa zamanında müdahale etmek, hasarın en aza indirilmesinde önemli rol oynuyor. Mantar kaynaklı olan külleme, görülür görülmez mücadeleye başlanıyor. ')
          st.markdown('Belirti olarak; çiçek açmama görülür, yaprak ve meyve dökümü göze çarpar, zayıflama ve dökülme gerçekleşir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bahçelerin bakımlı tutulması gerekmektedir.
                        * Budama yapılması, fazla dalların çıkarılması ağacın yapraklarının güneş ve hava almasını sağlayarak yayılımı azaltıyor.
                        * Yılda iki kez dip sürgünlerin alınması gerekiyor.
                        * Yabancı ot temizliği önem taşıyor.
                        * Dökülen enfekte yaprakların tırpanla toplanması, yakılarak imha edilmesi önerilir.
                        2-	Kimyasal Tedavi
                        * Hastalık görüldüğü tarihten itibaren 10 günde bir ilaçlama uygulanmalıdır.
                        * Hastalığın üst taraflara ilerlediği durumda, bayrak yaprağa bulaşın önlenmesi için yeşil aksamın ilaçlanmasına başlanıyor. İlaçlar, önerilen dozlarda yaprak alt ve yüzlerini kaplayacak şekilde uygulanıyor. Genellikle peptisit etkili ilaçlar kullanılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [tarfin](https://tarfin.com/blog/kulleme-hastaligi-nedir-nasil-mucadele-edilir)")
     
      if ctrl == 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('m.yapraklekesi1.jpg', width=350)
          with col2:
                st.image('m.yapraklekesi2.jpg', width=370)
          st.header('Mısır - Cercospora (Yaprak Lekesi Hastalığı)')
          st.subheader('Nedir?')
          st.markdown('Hastalığın etmeni Cercospora beticola mantarıdır. Mantarın zararı pancar yapraklarının sürekli lekelenip ölmesi ve bitkinin yeni yapraklar sürmesi şeklindedir. Sonuçta bitkilerin kök büyümesi ve şeker biriktirmesi önemli ölçüde geriler. Hastalığın başlangıcı ve gelişmesi, o yılın sıcaklık ve yağış ortalamaları ile direkt olarak ilintilidir. Hastalık genellikle bölgelerin rakımına göre değişmekle birlikte Haziran başı ile Temmuz ortasında bitkinin ilk olarak yaşlı yaprakları üzerinde görülmeye başlar.')
          st.markdown('İlerleyen dönemlerde sıcaklık ve rutubetin artmasıyla birlikte yaprak üzerindeki lekeler aniden artarak yüzeyin tamamını kaplar. Lekeyle kaplanan yapraklar peyderpey kuruyup ölür. Ağır bulaşıklık durumunda yaprakların çoğu ölür ve bu durumda bitki yeni yapraklar sürmek zorunda kalır. Bu taze yapraklar da sürekli olarak hastalığa yakalanıp ölür ve bitkinin şeker kaybetmesine sebebiyet verir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Çok kısa aralarla mısır üretiminden kaçınılmalıdır
                        * Silo yerlerinde, bu mantarlara depo görevi yapan bitki artıkları bırakılmamalıdır.
                        * Yaprak hastalıklarına toleranslı çeşitler ekilmelidir (Özellikle Cercospora görülen bölgelerde)
                        2-	Kimyasal Tedavi
                        * Bölgelere göre değişmekle beraber, 1-3 ilaçlama gerekebilir. Her ilaçlamada farklı etkili maddeli fungisitlerin kullanılması ve sezon içinde ilaçlamaların geç dönemde yapılmaması çok önemlidir.
                        """)
          st.subheader("Detaylı bilgi için: [tarfin](https://tarfin.com/blog/kulleme-hastaligi-nedir-nasil-mucadele-edilir)")
      if ctrl == 'Corn_(maize)___Common_rust_':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.yaprakpası1.jpg')
            with col2:
                st.image('m.yaprakpası2.jpg')
            st.header('Mısır - Paslanma')
            st.subheader('Nedir?')
            st.markdown('Mısır bitkisinde üç önemli yaprak pası yaygın olarak görülmektedir. Bunlar Adi Pas, Polysora Pası ve Tropik Pas’tır. Bunlar bitkilerin tepe püskülü çıkmasına yakın bir dönemde çok belirgin olarak görülür. Adi Pas (P. sorghi) yaprakların her iki yüzünde tozlu bir görünüme sahip küçük kahverengi püsçüller meydana getirir. Daha sonra epidermis yırtılır ve bitki olgunlaştığında bu püsçüller siyahlaşır.')
            st.markdown('Polysora spp’nin meydana getirdiği püsçüller adi pasta meydana gelene göre daha açık renkli ve daha yuvarlaktır. Bitkiler olgunlaştıkça püsçüllerin renkleri daha koyulaşır. Bu pas türünde de püsçüller yaprağın her iki yüzünde meydana gelir. Epidermisin yırtılması ise adi pasta olduğundan daha geç olur.')
            st.markdown('Tropikal pasın püskülleri yuvarlak ile oval arasında değişen şekillerde ve küçük yapılı olup, epidermisin altında meydana gelir. Püskülün ortası beyazdan sarıya kadar değişen renkler alabilir. Ayrıca bir de delik görülür. Püskül bazen kararır fakat ortası açık renkliliğini korur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bahçelerin bakımlı tutulması gerekmektedir.
                        * Budama yapılması, fazla dalların çıkarılması ağacın yapraklarının güneş ve hava almasını sağlayarak yayılımı azaltıyor.
                        * Yılda iki kez dip sürgünlerin alınması gerekiyor.
                        * Yabancı ot temizliği önem taşıyor.
                        * Dökülen enfekte yaprakların tırpanla toplanması, yakılarak imha edilmesi önerilir.
                        2-	Kimyasal Tedavi
                        * Hastalık görüldüğü tarihten itibaren 10 günde bir ilaçlama uygulanmalıdır.
                        * Hastalığın üst taraflara ilerlediği durumda, bayrak yaprağa bulaşın önlenmesi için yeşil aksamın ilaçlanmasına başlanıyor. İlaçlar, önerilen dozlarda yaprak alt ve yüzlerini kaplayacak şekilde uygulanıyor. Genellikle peptisit etkili ilaçlar kullanılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [cropscience](https://www.cropscience.bayer.com.tr/turkiye/tarim-haberleri/misir-hastaliklari.html)")
            st.subheader("Detaylı bilgi için: [dergipark](https://dergipark.org.tr/download/article-file/40861)")

      if ctrl == 'Corn_(maize)___healthy':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.sag1.jpg', width=350)
            with col2:
                st.image('m.sag2.jpg', width=390)
            st.header('Mısır - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Toprak havasızlığı mısır yetiştiriciliğinde sorun oluşturuyor. 
                        * Besince zengin, pH’sı 5 ile 8 arasında değişen verimli topraklarda rahatlıkla mısır dikimi yapılabiliyor. 
                        * Çimlenme sıcaklığı 8 ile 10 derece arasında hesaplanıyor. Yüksek sıcaklıklarda (18-20) tohumların çimlenmesi ve çıkışı daha hızlı oluyor. Uygun büyüme sıcaklığı ise 20 ile 30 derece arasını gösteriyor. 
                        * Mısır üretimi için nemli bir tohum yatağı önem taşıyor. İyi bir tohum yatağı hazırlamak için toprak önce pulluk ile 8-10 cm, sonra sonbaharda 18-20 cm derinlikte, iki kez sürülüyor. 
                        """)
            st.subheader('Nasıl Yetiştirilir?')
            st.markdown('Toprakta bol su isteyen mısır, özellikle sapa kalkma ve çiçeklenme dönemlerinde çok su tüketiyor. Eğer doğal yağışlarla su karşılanmıyorsa sulama suyu ile destek verilmesi gerekiyor.  Susuz mısır üretimi, çok yağış alan bölgelerde nadiren yapılabiliyor. Ülkemizde susuz tanelik mısır yetiştiriciliği Karadeniz’de gerçekleştiriliyor. Topraktaki faydalı su oranı %50’nin altına düştüğünde tarlanın sulanması gerekiyor. Mısır yetiştiriciliği sırasında en az 4 kez sulama yapılıyor. İlk sulama, birinci ara çapası sonrası, ekin boyu 10-15 cm’ye geldiğinde yapılıyor. İkinci sulama boğaz doldurmanın ardından, üçüncü sulama tepe püskülü çıkmadan 4-5 gün önce, dördüncü sulama ise süt olum devresinde gerçekleştiriliyor. ')
            st.subheader("Detaylı bilgi için: [tarfin](https://tarfin.com/blog/misir-yetistiriciligi-nasil-yapilir)")

      if ctrl == 'Corn_(maize)___Northern_Leaf_Blight':
          col1, col2 = st.columns(2)
          with col1:
                st.image('m.yaprakyanıklığı1.jpg', width=350)
          with col2:
                st.image('m.yaprakyanıklığı2.jpg', width=370)
          st.header('Mısır - Yaprak Yanıklığı')
          st.subheader('Nedir?')
          st.markdown('Yaprak yanıklığı, yaprak, kın, koçan yaprağı, koçan sapı ve koçanda bulunabilir. Belirtiler hastalığın ilk evrelerinde baklava dilimini andıran küçük lekeler iken hastalık ilerledikçe bu lekeler büyür ve boyutları 2-3 cm’ye kadar ulaşabilir. Etmen ayrıca fide döneminde kök çürüklüğü ve solgunluğa da neden olabilir. Hastalık ılıman (20-32°C) ve nemli bölgelerde görülmektedir. 18-27°C ve nemli havalar hastalık gelişimini teşvik ederken kuru havalar ise engeller. Etmen kışı mısır artıkları veya mısır tanelerinde miselyum ve spor olarak geçirir.')
          st.markdown('Bitkilerin hastalığa duyarlı devresi olan tozlanma döneminde ağır enfeksiyonlar meydana getirir. Hastalık bu dönemden önce ortaya çıkmışsa %50’ye varan verim kayıplarına sebep olabilir.')
          st.markdown('Hastalığa karşı tercih edilen dayanıklı çeşitler, uygulanan ekim nöbeti, tarladaki hastalıklı bitki artıklarının temizliği, toprak analizi sonucu ve gübre kullanımı gibi birçok kültürel mücadele bulunmaktadır. Gerekli durumlarda kimyasal mücadele önerilebilir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalığa dayanıklı çeşitler ekilmeli
                        * Ekim nöbeti uygulanmalı
                        * Gerekli dönemlerde gübreleme yapılmalı
                        * Hastalıklı bitkiler temizlenmeli
                        2-	Kimyasal Tedavi
                        * Bu hastalığa karşı pek fazla kimyasal mücadele uygulanmamaktadır. Fakat kimyasal savaşta pyraclostrrobin, epoxiconazole+ pyraclostrrobin ve , epoxiconazole + carbendazim önerilebilir.
                        """)
          st.subheader("Detaylı bilgi için: [dergipark](https://dergipark.org.tr/download/article-file/40861)")
      if ctrl == 'Grape___Black_rot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('u.karaçürüklük1.jpg', width=350)
          with col2:
                st.image('u.karaçürüklük2.jpg', width=370)
          st.header('Üzüm - Kara Çürüklük')
          st.subheader('Nedir?')
          st.markdown('Üzüm kara çürüklüğü , sıcak ve nemli havalarda üzüm asmalarına saldıran temelde bir mantar hastalığıdır. Hastalık bitkinin sürgünler, yaprak ve meyve saplarına da yansır.')
          st.markdown('Hastalık döngüsü kışlayan yapılarla başlar. İlkbahar yağmurları, kışlayan yapılarda bulunan larvalaşmış mantarları serbest bırakır ve bu sporlar rüzgar ve yağmur sıçramasıyla yapraklara, çiçeklere ve genç meyvelere bulaşmak üzere yayılır. Yerdeki bazı mumyalarda, tomurcukların kırılmasından yaklaşık iki ila üç hafta sonra başlayan ve çiçeklenmenin başlamasından bir ila iki hafta sonra olgunlaşabilir. Nem varlığında, bu mantarlar yavaş yavaş filizlenir, 36 ila 48 saat sürer, ancak sonunda genç yapraklara ve meyve saplarına nüfuz eder. Enfeksiyonlar 8 ila 25 gün sonra görünür hale gelir.')
          st.markdown('Meyvenin enfeksiyonu, hastalığın en ciddi aşamasıdır ve önemli ekonomik kayıplara neden olabilir. Enfekteli meyveler önce açık renkli veya çikolata kahverengisi görünür; kuş gözü gibi çok yuvarlak görünen bir yeri olacak. Bu nokta büyüyecek ve daha fazla meyve salkımına ve daha fazla bitkiye bulaşacaktır.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Üzümün yetiştirileceği bölge için doğru üzüm çeşidinin seçilmesidir. Üzüm çeşitleri, hastalık kara çürüklüğü hastalığındaki farklılıklar da dahil olmak üzere, hastalıklara duyarlılıkları bakımından farklılık gösterir. Bazı çeşitler daha az hassastır, diğerleri ise doğru çevre koşulları oluştuğunda hastalığa daha yatkındır.
                        * Uygun bir budama tekniği, hastalıkları sınırlamak için başka bir kültürel kontrol yöntemidir. Her asmayı uyku döneminde her yıl budayın. Bu hareketsiz budama, dengeli budama terimini sağlamak için yoğun bir şekilde araştırılmıştır.
                        2-	Kimyasal Tedavi
                        * Kimyasal uygulamaları uygulamak için mantar ilacı etiketine bakın. Uygulama nedeniyle mantar ilacının kaymasını ve verimsizliklerini önlemek için koşulların püskürtmek için en uygun olduğundan emin olun. Mantar ilacı kurallarına uyulmalıdır. Hem normal hem de organik yetiştiriciler için çok çeşitli kimyasallar mevcuttur. Ticari olarak maliyetli olabilir.
                        """)
          st.subheader("Detaylı bilgi için: [tarfin](http://www.tarimkutuphanesi.com/baglarda_kav_(esca)_hastaligi_00727.html#:~:text=Kav%20hastal%C4%B1%C4%9F%C4%B1%20asman%C4%B1n%20tamamen%20kurumas%C4%B1na,yapraktaki%20ve%20odun%20dokusundaki%20belirtisi.)")
      if ctrl == 'Grape___Esca_(Black_Measles)':
          col1, col2 = st.columns(2)
          with col1:
                st.image('u.kav1.jpg', width=350)
          with col2:
                st.image('u.kav2.jpg', width=370)
          st.header('Üzüm - Kav')
          st.subheader('Nedir?')
          st.markdown('Asmaları yara yerlerinden enfekte ederek, bitki dokusunda enine ve boyuna yayılır. Miselyum gelişmesi yavaş olduğundan enfeksiyon sonrası belirtilerin ortaya çıkması uzun yıllar alabilmektedir. Hastalık asmanın odun kısmını tahrip eder. Bunun sonucunda yeşil akşamda solgunluğa, gelişme geriliğine hatta bitkinin ölümüne yol açar.')
          st.markdown('Yaşlı yapraklarda damar aralarında önce dış kısımlarda oluşur, daha sonra bu alanlar kurur ve beyaz çeşitlerde sarımsı, renkli çeşitlerde kızıl kahverengiye dönüşür. Daha genç yapraklar şeffaflaşır, salkım silker, yapraklarla birlikte kuruyarak dalında asılı kalır. Hastalıklı asmaların gövde ve kalın dalları enine kesildiğinde, açık renkli yumuşak dokulu hastalıklı kısmın koyu renkli sert dokulu bir kuşakla çevrilmiş olduğu görülür.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Çok yaşlı, verimden düşmüş hastalıklı dal ve yapraklar sökülerek artıkları yakılmalıdır.
                        * Hastalıklı ağaçlar en son budanmalı ve budama aletleri %10’luk sodyum hipoklorit ile dezenfekte edilmelidir. 
                        2-	Kimyasal Tedavi
                        * Bu hastalığa karşı pek fazla kimyasal mücadele uygulanmamaktadır. Fakat kimyasal savaşta pyraclostrrobin tipi ilaçlar kullanılabilmektedir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/baglarda_kav_(esca)_hastaligi_00727.html#:~:text=Kav%20hastal%C4%B1%C4%9F%C4%B1%20asman%C4%B1n%20tamamen%20kurumas%C4%B1na,yapraktaki%20ve%20odun%20dokusundaki%20belirtisi.)")

      if ctrl == 'Grape___healthy':
            col1, col2 = st.columns(2)
            with col1:
                st.image('u.sag1.jpg', width=350)
            with col2:
                st.image('u.sag2.jpg', width=390)
            st.header('Üzüm - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Üzüm bağlarında mutlaka, kış budaması yapılmalıdır. Budama amatör kişiler tarafından değil işinin uzmanı kişiler tarafından doğru bir şekilde yapılmalıdır.
                        * Bağlarda toprak işlemesi, sonbahar ve ilkbahar aylarında yapılmalı ve bağlarda yabani otların büyümesine engel olunmalıdır.
                        * Bağlarda gübreleme yapılmalıdır. Gübreleme, için mutlaka toprak analizi yapılmalı ve bu doğrultuda toprağın ihtiyaç duyduğu vitamin ve mineral takviyesi yapılmalıdır.
                        * Üzüm bağlarında sulama için su kontrolleri sağlayan cihazlar kullanıldığı takdirde toprağın suya ihtiyaç duyduğu anlarda toprak sulaması yapılmalıdır.
                        * Üzüm  bağlarında yaz budaması için doğru ay belirlenmeli ve budama yapılmalıdır.
                        * Bağlarda hastalıklara karşı ve böceklere karşı ilaçlama yapılmalıdır. Bunun için böcek cinsi tespit edilmelidir.                        """)
            st.subheader('Üzüm bağlarına kükürt ne zaman atılır?')
            st.markdown('Birçok meyve yetiştiriciliğinde olduğu gibi kükürt, üzüm bağları içinde oldukça gerekli bir vitamindir. Kükürt eksikliği ise şu şekilde anlaşılır; toprakta kireçlenme, besin değerinin düşmesi, enerji düşüklüğü yaşandığı zaman, protein eksikliğinde ve aminoasit yetersizliğinde, bitkide herhangi bir hastalık tespit  edildiğinde,  tuz oranının yükseldiği zaman ve buna bağlı etmenlerin arttığı dönemlerde üzüm bağlarına kükürt takviyesi yapılmalıdır. Kükürt, üzüm bağları için ilkbahar aylarının başlarında uygulaması yapılmalıdır. Toprağın kükürte ihtiyaç duyup duymadığı ise toprak analizleri soncunda meydana çıkar.')
            st.subheader("Detaylı bilgi için: [link](https://www.cicekal.net/blog/uzum-agaci-bakimi-nasil-yapilir/)")

      if ctrl == 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
          col1, col2 = st.columns(2)
          with col1:
                st.image('u.yaprakyanıklığı1.jpg', width= 500)
          with col2:
                st.image('u.yaprakyanıklığı2.jpg')
          st.header('Üzüm - Yaprak Yanıklığı')
          st.subheader('Nedir?')
          st.markdown('Bakteriyel bir hastalıktır. Birçoğu önemsiz belirtiler gösteren veya hiçbir belirti göstermeyen pek çok konukçuya sahiptir. Gün geçtikçe daha fazla konukçu bitki türleri keşfedilmektedir.')
          st.markdown('Bakteriler; köklerde, damarlarda, gövdelerde, yapraklarda yaşar. Bitki buna, damarlarında tutkal benzeri bir madde olan zamk ve tiloz oluşturarak cevap verir. Bakteriler damarları tıkayarak bitkinin solmasına neden olur. Böcekler sayesinde bitkiden bitkiye aktarılabilir. Yaprakların birincil enfeksiyonu yaprak yanıklığına yol açar. Yeşil yaprağın bir kısmı aniden ölür ve kahverengiye döner; bu sırada bitişik doku sararır veya kızarır. Bu desikasyon yayılır ve yaprağın tamamı büzüşüp düşebilir. Enfekte gövdelerde düzensiz olgunlaşma ve kahverengi ve yeşil doku lekeleri görülür. İzleyen sezonlarda, bu enfekte bitkilerin gelişmesi yavaşlar ve bodur klorotik sürgünler oluştururlar. Enfeksiyon kronik hale geldiğinde, yapraklar damarlar arasında sararmalar ile bozulmaya başlar ve sürgünlerin boğum araları kısalır. Etkilenen asmalar sonunda ölür. Bu, genç asmalarda yaşlılardan daha hızlı gerçekleşir. Hassas çeşitlerde (2-3 yıl içinde) beş yıldan fazla yaşayabilen daha toleranslı çeşitlerde olduğundan daha hızlı olur.')
          st.subheader('Zarar Belirtileri')
          st.markdown('Yaprakların birincil enfeksiyonu yaprak yanıklığına yol açar. Yeşil yaprağın bir kısmı aniden ölür ve kahverengiye döner; bu sırada bitişik doku sararır veya kızarır. Bu desikasyon yayılır ve yaprağın tamamı büzüşüp düşebilir. Enfekte gövdelerde düzensiz olgunlaşma ve kahverengi ve yeşil doku lekeleri görülür. İzleyen sezonlarda, bu enfekte bitkilerin gelişmesi yavaşlar ve bodur klorotik sürgünler oluştururlar. Enfeksiyon kronik hale geldiğinde, yapraklar damarlar arasında sararmalar ile bozulmaya başlar ve sürgünlerin boğum araları kısalır. Etkilenen asmalar sonunda ölür. Bu, genç asmalarda yaşlılardan daha hızlı gerçekleşir. Hassas çeşitlerde (2-3 yıl içinde) beş yıldan fazla yaşayabilen daha toleranslı çeşitlerde olduğundan daha hızlı olur.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Tüm dikim ve aşı materyali hastalıkla bulaşık olmayana alanlarda temin edilir.
                        * Budama ve diğer işlemlerde ekipmanlar temizlenmeli ve dezenfekte edilmelidir.
                        * Tamamen ölmüş veya enfekte olmuş bitkiler sökülmeli yayılımı engellenmelidir.
                        * Yağmurlama sulamadan kaçınılmalıdır.
                        2-	Kimyasal Tedavi
                        * Bordo bulamacı spreyi veya fiks bakır spreyi ile budamadan sonra ve periyodik olarak yapraklar yarı büyüklüğünü alıncaya kadar ilaçlama yapılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [Çiçek Al](https://www.cicekal.net/blog/uzum-agaci-bakimi-nasil-yapilir/)")
      if ctrl == 'Orange___Haunglongbing_(Citrus_greening)':
          col1, col2 = st.columns(2)
          with col1:
                st.image('p.turunçgil1.jpg', width=350)
          with col2:
                st.image('p.turunçgil2.jpg', width=370)
          st.header('Portakal - Trunçgil Yeşillenme')
          st.subheader('Nedir?')
          st.markdown('Hastalık anaca bakmaksızın portakal, mandarin ve greyfurtlarda oldukça etkilidir. Bunun yanında limon, kaba limon hastalıktan etkilenmektedir.')
          st.markdown('Belirtileri; hastalık aşırı derecede meyve dökümü görülmektedir. Meyveler olgunluğa erişmesine rağmen yeşil olarak görülmektedir. Ortadan kesildiğinde, küçük, koyu abortif çekirdekler gözlenebilir. Meyve eksenindeki demetler renksizdir. Meyve, özellikle portakal, alacalı bir görüntü alır ve eğer kabuğa bir parmakla bastırılırsa, bastırılan bölgede gümüşi bir alan oluşabilmektedir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bitkilerin vasküler sisteminde etkili bir bakteri hastalığıdır. Ağaç bir kez hastalandığında herhangi bir tedavisi yoktur. Hastalığın birincil konukçusu turunçgillerdir.
                        * Budama ve diğer işlemlerde ekipmanlar temizlenmeli ve dezenfekte edilmelidir.
                        * Tamamen ölmüş veya enfekte olmuş bitkiler sökülmeli yayılımı engellenmelidir.
                        2-	Kimyasal Tedavi
                        * Özellikle bahar sürgünlerinin korunması gerekmektedir. Çünkü en fazla artış bu dönemde görülür.
                        * İlaçlamanın zamanlaması da önemlidir. Bu nedenle sarı yapışkan tuzak uygulaması ilaçlama zamanını belirlemek açısından önemlidir.
                        * Yayılım engellenemezse karantinaya almak gerekebilmektedir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/baglarda_kav_(esca)_hastaligi_00727.html#:~:text=Kav%20hastal%C4%B1%C4%9F%C4%B1%20asman%C4%B1n%20tamamen%20kurumas%C4%B1na,yapraktaki%20ve%20odun%20dokusundaki%20belirtisi.)")

      if ctrl == 'Peach___Bacterial_spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('ş.bakteriyel1.jpg', width=350)
          with col2:
                st.image('ş.bakteriyel2.jpg', width=370)
          st.header('Şeftali - Bakteriyel Leke')
          st.subheader('Nedir?')
          st.markdown('Hastalığın gelişmesi için uygun olan koşullar ilik ve orta derecede sıcaklıklar, sik ve hafif geçen yağmurlu havalar, ağır çiğ ve az şiddetli rüzgârlı hava koşullarıdır. Belirtilen hava koşullarının tamamı ya da birazının hakim olduğu sezonlarda, şiddetli enfeksiyonlar her zaman beklenmelidir. Yine hava koşulları uygun olduğunda, bakteriyel enfeksiyon tomurcukların açılmasından hasat zamanına kadar olabilir. Şiddetli yağan yağmurlardan sonra yeni enfeksiyonlar her zaman çıkabilir, böyle koşullarda hastalık genellikle ağaçların bir tarafında daha yaygın olarak görülmektedir.')
          st.markdown('Hastalık meyve ağaçlarının yeşil aksam, ince dallar ve meyvelerinde görülmektedir. Bazı yetiştiriciler hastalığı genellikle bakteriyel etmeninin yapraklarda neden olduğu saçma deliği belirtisinden karakterize eder ve tanımlarlar. Hastalık belirtisi yapraklarda ilk önce, küçük, açık yeşil ya da beyazımsı renkte ve lekeyi çevreleyen dokudan kesin olarak ayrılmıştır. Bu lekeler çoğunlukla yeşil akşamların uçlarında daha yoğun görülmektedir. Şiddetli olarak enfektelenen yapraklar sarıya döner ve daha dökülürler. Duyarlı çeşitlerde, yapraklarda oluşan bir kaç lezyon yaprakların dökülmesine neden olabilir. Yaz baslarında da ağır yaprak dökülmeleri meyvelerin büyüklüğünü azaltır ve ağaçları zayıflatır.')
          st.markdown('Meyve belirtileri başlangıçta meyvenin yüzeyinde küçük, yuvarlak kahverengi lekeler olarak görülür. daha sora ise bu lekelerde çökme ve lekelerin etrafında ise çatlamalar meydana gelir. Bu tür lekeler meyvelerin görünümünü büyük ölçüde bozmasına rağmen, meyvenin yenilebilir özelliği bozmamaktadır. Yalnız meyvelerde meydana gelen çatlamalar, çürüklük mikroorganizmaların girişine müsaade ettiği için zararlanmalara neden olurlar. Geç sezonlarda görülen lekeler genellikle yüzeyseldir ve meyvelerde sadece benekleneme görüntülerin oluşmasını sağlar.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Kanserli dokuları barındıran ince dal ve sürgünler budanmalı ve imha edilmeli.
                        * Hastalık etmenine karsı dayanıklı kültüvarlar meyve bahçelerinin tesisinde tercih edilmelidir. 
                        * Canlı ve gür gelişen meyve ağaçları bakımsız ve yetersiz beslenen meyve ağaçlarına göre daha dayanıklıdır. Bundan dolayı, gübreleme, budama, sulama ve diğer bakim isleri zamanında ve dikkatli bir şekilde yapılmalıdır.
                        2-	Kimyasal Tedavi
                        * Kimyasal ilaçlama özellikle hasattan sonra yapılmalı ve kanserli dokuların oluşmasına böylelikle izin verilmez. Tomurcuklar patlamadan önce yapılacak bir ilaçlamada hastalığın etkili bir şekilde kontrolü için gereklidir. Bu ilaçlamayı takiben diğer ilaçlamalar hastalığın ortaya çıkmasına uygun ortamlar hakim olursa yapılabilir. Tarım ilacı olarak bakırlı preparatlar tavsiye edilmektedir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/baglarda_kav_(esca)_hastaligi_00727.html#:~:text=Kav%20hastal%C4%B1%C4%9F%C4%B1%20asman%C4%B1n%20tamamen%20kurumas%C4%B1na,yapraktaki%20ve%20odun%20dokusundaki%20belirtisi.)")

      if ctrl == 'Peach___healthy':
          
            col1, col2 = st.columns(2)
            with col1:
                st.image('ş.sag2.jpg', width=350)
            with col2:
                st.image('ş.sag1.jpg', width=360)
            st.header('Şeftali - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Şeftali ağacının toprağı çok önemlidir. Toprağın derinliği yüksek ve drenajı sağlanabilen toprak türünde olması gerekmektedir. Ph derecesi 6,5 olan toprak türü, şeftali ağacı için olması gereken ölçüttür.
                        * Şeftali ağacı bakımı konusunda bilgi sahibi olmak ve bu tür meyve veren ağaçların tozlaşma yoluyla meyve verebildiğinin bilinmesi gerekmektedir. Şeftali ağacı kendi kendine tozlaşma sağlamaktadır.
                        * Şeftali ağacının etrafı derin şekilde kazılarak, köklerine kadar suyu çekmesi sağlanmalıdır. İlk fide halindeyken bu yöntemin uygulanması, ağacın uzun vadede sağlıklı olması için önemlidir.
                        * Şeftali ağacından iyi verim almak için, ağacın budamasının düzenli olarak yapılması gereklidir. Budama yapılarak, ağacın gövde ve kök kısımlarında denge sağlanarak, kırılması önlenir.
                        * Meyve veren ağaçların gübrelemesinin, düzenli olarak yapılması gerekmektedir. Kaliteli meyve üretimi için toprağın ihtiyacı olan azot ve mineraller, gübre ile desteklenmelidir.
                        * Şeftali ağacı dikilen toprağınızın iyi sürülmüş ve derinliğinin iyi ayarlanmış olması çok önemlidir.
            """)
            st.subheader('Şeftali Ağaçlarında İlaçlama')
            st.markdown('Şeftali ağacı ilaçlamada, ağacın hastalığına göre ve mevsime göre ilaçlama yapılmalıdır. Eğer ağacın bütün yaprakları dökülmüş ve ağır hastalık varsa, ağaç kökünden sökülmeli ve yakılmalıdır. İlaçlama ağaçların kış uykusunda olduğu dönemde yapılırsa, ağaç daha verimli olacaktır. Şeftali ağacının yapraklarında delikler ve tomurcuklarında hasarlar oluşmuşsa, bu hastalıklı bölgeler budanmalıdır. Daha sonra ağacın toprağının gübresi ve suyu verilerek, ağacın toprağının havalandırılması sağlanmalıdır. Böylece ağaç hastalıktan korunmuş olacaktır. Şeftali ağacının çiçeklenme zamanları, ağaçta böceklenmeler oluşur. Gündüz vakitlerinde ağaç silkelenerek, böceklerin ağaçtan uzaklaştırılması sağlanmalıdır. Şeftali ağacında, çiçeklenme sonunda da ağaca zarar veren türlerden ağacı kurtarmak için, ilaçlama yapılma zamanlarına dikkat edilmesi gerekmektedir. Topraktaki eksiklikten kaynaklı hastalık oluşumu varsa, toprağın gübresinin düzenli olarak verilmesi gerekmektedir.')
            st.subheader("Detaylı bilgi için: [cicekal](https://www.cicekal.net/blog/seftali-agaci-bakimi-puf-noktalari-nelerdir/#:~:text=Sulamas%C4%B1%20iyi%20yap%C4%B1lan%20%C5%9Feftali%20a%C4%9Fac%C4%B1n%C4%B1n,defada%20bol%20su%20ile%20sulanmal%C4%B1d%C4%B1r.)")

      if ctrl == 'Pepper,_bell___Bacterial_spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('b.bakteriyel1.jpg', width=350)
          with col2:
                st.image('b.bakteriyel2.jpg', width=370)
          st.header('Biber - Bakteriyel Leke')
          st.subheader('Nedir?')
          st.markdown('Hastalıktan dolayı kayıplar hem tohum yataklarında hem de üretim alanlarında görülebilir. Eğer bitkiler tohum yataklarında bulaştı ise, hastalık belirtileri bitkiler tarla ya da sera gibi yetiştirme yerlerine şaşırtıldıktan sonraki 6 hafta içerisinde görülmeye baslar ve hemen hemen tüm bitkilerde ortaya çıkabilir. Erken dönemlerde etkilenen bitkilerde genellikle bodurluk belirtisi görülürken, geç ya da şaşırtıldıktan sonra enfetelenen bitkilerde erken yaprak dökümleri görülmektedir. Bu yaprak dökümünden sonra meyveler de de belirtiler görülür ve aşırı yaprak dökümü nedeniyle de bitkiler güneş yanığı gibi sekonder zararlanmalara maruz kalabilir. Bakteriyel etmen hastalıklı bitkilerin sayesinde aylarca tohum yataklarında ve tohum üzerinde canlılığını muhafaza edebilir. Bakteriyel etmen, tarlada bırakılmış bitkilerin kök ve gövdelerinde, yabancı otlar üzerinde canlılığını korur ve diğer sezona bakteriler taşınmaktadır. Toprakta ise uzun süre canlılığını muhafaza edemeyebilir. İlk bulaşma tohum, bulaşık şaşırtılmış fide, yabancı otlar ve bulaşık bitki ve toprak ile olabilir.')
          st.markdown("Yaprak belirtileri ilk önce küçük suyla ıslanmış alanlar olarak yaprakların alt tarafında görülmeye baslar. Bu lekeler birkaç mm' ye kadar genişler, koyu kahverengiye döner ve hafifçe kabarmaktadır. Yaprak üst yüzeyinde, lekelerin etrafı kahverengi bir hale le kuşatılır. Böyle küçük belirtiler çökerek ölmekte ve nekrotik alanlar yaprak üzerinde oluşur ve bu lekelerin büyük bir kısmi yaprak neminin toplandığı yaprak kenarları ve uçlarında oluşmaktadır. Sonunda yapraklar sararır ve düşer, böyle bitkilerde güneş yanıklığından etkilen meyvelerin sayısında artış görülür. Meyve üzerinde ise pazara değerini azalmış, kabarık ve uyuz halini almış lekeler seklinde kendini gösterir.")
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıktan ari tohum ve fidelerin kullanımı.
                        * Sera ve tohum yataklarında hastalıktan ari toprak, su ve alet ekipmanı kullanılmalı.
                        * 2-3 yıl gibi ürün rotasyonu yapılmalı.
                        * Aşırı sulamadan kaçınılmalı nem oluşumu engellenmeli. Ayrıca nemli koşullarda ve bitkiler ıslak iken çalışmaktan kaçınılmalı.
                        * Hastalıklı fideler hemen yetiştirme ortamlarından uzaklaştırılmalı ve imha edilmeli.
                        2-	Kimyasal Tedavi
                        * Tohum yataklarında Bakir ile karıştırılmış Streptomycin antibiyotiği (200 PPM) 5 gün aralıklara ile kullanılabilir. Fakat pratikte pahalıya gelebilir onun için pek tavsiye edilmiyor. Bakirli preparatlar bitkilerde koruyucu olarak ve yayilmasini engellemek için kullanılabilir. Ayrıca bakirli preparatlar maneb ya da macozeb ile birlikte kullanılarak ilaçların etkinliği artırılabilir ve diğer fungal etmenlere karşı da koruyucu bir etki yapabilir. Genellikle bakteriyel etmenler ile mücadele zor, onun için kültürel önlemlere ve temiz çalışmaya oldukça fazla dikkat edilmelidir.
                        """)
          st.subheader("Detaylı bilgi için: [cicekal](https://www.cicekal.net/blog/seftali-agaci-bakimi-puf-noktalari-nelerdir/#:~:text=Sulamas%C4%B1%20iyi%20yap%C4%B1lan%20%C5%9Feftali%20a%C4%9Fac%C4%B1n%C4%B1n,defada%20bol%20su%20ile%20sulanmal%C4%B1d%C4%B1r.)")

      if ctrl == 'Pepper,_bell___healthy':
          
            col1, col2 = st.columns(2)
            with col1:
                st.image('b.sag2.jpg')
            with col2:
                st.image('b.sag1.jpg')
            st.header('Biber - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Biber ılık ve sıcak iklim meyvesidir.Soğuklardan çok etkilenir. Yetiştirme devrelerinde sıfırın altında 2-3 dereceye düştüğünde tamamen ölür.
                        * Biber bitkisinde hava sıcaklığı 15 derecenin altında 32 derecenin üzerine çıktığında alınan verim düşmektedir.
                        * Biberlerde iyi bir gelişme ve yüksek verim oldukça derin, geçirgen, su tutma kabiliyeti yerinde, besin ve organik maddece zengin bahçelerde yetiştirilir.
                        * Erken verim alma maksadıyla yapılan yetiştirmelerde takviye edilmiş kumlu topraklar ve özellikle kumlu-tınlı toprak üzerinde durulmalıdır. Bol mahsul almak için kumlu-killi topraklar tercih edilmelidir.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Ekim Nöbeti: Biber ekim nöbetine girebilecek bitkiler pamuk, buğday ve buğdaygillerdir. En iyi ekim nöbeti; buğday+ikinci ürün+biber olarak belirlenmiştir.
                        * Toprak Hazırlığı: Sonbaharda pullukla derin sürüm yapılır. İlkbaharda ise diskardo çekildikten sonra hafif bir tapan çekilir.
                        * Dikim: Dikim esnasında fideler çapa ile açılan yeterli büyüklükteki çukura olduğu gibi yerleştirilir ve çukurun boş kısımları toprakla doldurulan hafifçe bastırılır.
                        * Sulama: Biber sulamasına dikimden 10-15 gün sonra başlanmalı, ilk meyve görülünceye kadar sulamalardan kaçınılmalıdır. İlk meyveyi gördükten sonra haftalık aralıklarla sulamalara devam edilmeli.
                        """)
            st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/biber_yetistiriciligi_00026.html)")

          
      if ctrl == 'Potato___Early_blight':
          col1, col2 = st.columns(2)
          with col1:
                st.image('p.yanık1.jpg', width=350)
          with col2:
                st.image('p.yanık2.jpg', width=370)
          st.header('Patates - Erken Yanıklık')
          st.subheader('Nedir?')
          st.markdown('Yaprak, sap ve meyvede gayri muntazam küçük kahverengi lekeler halinde başlar. Lekeler iç içe daireler şeklinde 1–2 cm büyürler. Yapraklarda çoğu kez sarı bir çerçeve ile çevrili kahverengi daire biçiminde lekeler oluşur. Yaprak lekeleri kendine has koyu renkli halkalara sahiptir. Yaprak lekeleri ilk önce yaşlı yapraklarda görülür ve bitkinin üst yapraklarına doğru ilerlemeye başlar. Hastalığın şiddetli olması halinde bütün yapraklar kururlar. ')
          st.markdown('Çiçek ve meyve sapları hastalığa yakalanırlarsa dökülürler, meyvelerde genellikle sapın tutunduğu kısımda koyu renkli çökük, çoğu zamanda sınırlanmış lekeler oluşur. Hastalık için uygun gelişme koşulları 28–30 °C’dir.')
          st.markdown('Hastalığı oluşturan mantar tarafından neden olunan erken yaprak yanıklığı hastalığı, tarlada ürünlere ve depoda yumru kalitesi üzerine önemli bir risk oluşturmaktadır. Bu risk tarla ve depoda oluşabilecek ürün zayiatları göz önüne alınırsa, mücadele edilmediği takdirde oldukça ciddi ekonomik kayıplara sebep olabilir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Küresel Önlemler
                        * Temiz tohum ve temiz fide kullanılmalıdır.
                        * Aşırı sulamadan kaçınılmalıdır.
                        * Fidelik toprağı dezenfekte edilmelidir.
                        * Fidelikler ve seralar sık sık havalandırılmalıdır.
                        * Çiğ oluşumundan kaçınmak için havalandırma iyi olmalı ve bitkilerin üzerinde serbest su oluşumu engellenmeli. Bunun için nemli ve bulutlu havalarda sulamadan kaçınılmalı.
                        * Hastalık görülen yerlerde patlıcan ve patatesle rotasyona girilmemelidir.
                        2-	Kimyasal Tedavi
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır
                        * Bitkinin tüm yüzeyi ilaçlanmalı, ilaçlama serin ve rüzgarsız zamanlarda 7–10 gün arayla yapılmalıdır.
                        * Kimyasal mücadelede kullanılan pek çok pestisitin yanı sıra Syngenta firmasının ruhsatlamış olduğu Revus Pro içerdiği 250 g/l mandipropamid ve 250 g/l difenoconazole ile Patates mildiyösü mücadelesinin yanı sıra Patates erken yaprak yanıklığı hastalığına karşı da üstün etki ve performans gösterir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım orman](https://kayseri.tarimorman.gov.tr/Belgeler/SOL%20MEN%C3%9C%20BELGELER%C4%B0/Z%C4%B0RAA%C4%B0%20M%C3%9CCADELE/Sebze%20Hastal%C4%B1klar%C4%B1/patates_mildiyosu_hastaligi.pdf)")

      if ctrl == 'Potato___healthy':
            col1, col2 = st.columns(2)
            with col1:
                st.image('p.sag1.jpg')
            with col2:
                st.image('p.sag2.jpg')
            st.header('Patates- Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Patates, fazla bakım isteyen bir bitkidir. Çıkıştan önce düzeltilmiş tırmık çekmek faydalıdır. Hem toprak kaymak tabakası bağladıysa kırılmış, hem de çıkmaya başlayan yabancı otlar örtülmüş olur.
                        * 3-4 yapraklı olunca yüzeye ve dikkatli bir şekilde ilk çapa yapılır. Bu çapa ile toprak kabartılır, yabancı otlar öldürülür ve nemin korunması sağlanır. Bundan sonra 20'şer gün arayla her çapa ile birlikte doldurma işlemi yapılır.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Gübreleme: Genellikle çiftlik gübresi kullanılır. Dekara 1.5-2 ton, eğer toprak çok fakir ise 2.5-3 ton çiftlik gübresi verilirse verim artar. Bu miktardan fazlası nişasta miktarını ve lezzeti olumsuz etkiler.
                        """)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                        * Hasat: Patateste hasat zamanının geldiği yaprak ve sapların sararıp kuruduğu, yumruların normal büyüklüğünü alarak bitkiden kolayca ayrıldığı ve kabuğun kalınlaşıp sertleştiğinden anlaşılır.Yumrunun kesiti ıslak değil, koyu bir görüntüdedir.
                        Patates hasadında çok dikkatli olmak gerekir. Yumrular kesilip zedelenmemeli, toprakta yumru bırakılmamalıdır. Söküm sırasında toprak yaş olmamalıdır. Hasattan sonra yumrular ıslak ise gölgede kurutulur. Hasta, çürük, berelenmiş ve kabuğun soyulmuş olanları ayıklanır. Sonra iri ve küçük boy olmak üzere sınıflandırılarak file çuvallara doldurulur.
                        """)
            with col2:
                st.image('p.arac.jpg')  
            st.markdown("""
                        * Sulama: Bitkinin su ihtiyacı alt yapraklardaki solma ve sararmayla kendini belli eder. Topraktaki nem dikkate alınarak ilk sulama, yumrular fındık büyüklüğüne geldiğinde yapılmalıdır. Hafif topraklarda 15-18, ağır 22-25 gün arayla yetiştirme süresince 2-4 sulama yapılır.')
                        En yaygın sulama yöntemi, karık ile sulamadır. İki karık arası mesafe kumlu topraklarda 60-65cm, ağır topraklarda 70-80cm'dir.
                        Patatesin enfazla suya ihtiyaç duyduğu evre, çiçeklenmeden 20 gün önce başlayan ve yumru yapmaya başladığı zamana kadar geçen evredir.
                        Sulama yeterli ve düzenli yapılmadığı taktirde, başta verim kaybı olmak üzere, memeli ve çatlak yumrular, yumru içinde kararmalar ve boşluklar ortaya çıkar.
                        * Depolama: Patates fazla miktarda su ihtiva eden bir ürün olduğundan iyi ibr şekilde depolanmazsa çok zarara uğrar. Yumrular çürür, pörsür, filiz verir ve değerlerini kaybeder.
                        Yumrular en iyi şekilde; olgun zedlenmemiş ve temiz olarak 3-40C sıcaklık, %85-90 nisbi nemde ve solunum sonucu meydana gelen karbondioksit, su ve ısıyı uzaklaştırıp oksijen sağlamak için havalandırma tertibatı iyi olan özel koruma depolarında saklanabilir. Depolamada yığın yüksekliği, yemeklik patateslerde 3-4 metre olabilir. Tokumluk patateslerde ise en fazla 1 metre olmaktadır.
                        """)
            st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/patates_yetistiriciligi_00005.html#:~:text=Patates%20bitkilerinde%20su%20ihtiyac%C4%B1%20alt,s%C3%BCresince%202%2D4%20sulama%20yap%C4%B1l%C4%B1r)")
            st.subheader("Detaylı bilgi için: [lezzet](https://www.lezzet.com.tr/lezzetten-haberler/patates-ne-zaman-ekilir)")

          
      if ctrl == 'Potato___Late_blight':
          col1, col2 = st.columns(2)
          with col1:
                st.image('p.gyanık1.jpg', width=350)
          with col2:
                st.image('p.gyanık2.jpg', width=370)
          st.header('Patates - Geç Yanıklık')
          st.subheader('Nedir?')
          st.markdown('Temelde bir mantar hastalığıdır. Uygun koşullar altında hayat döngüsü bulaştığı bitki yaprağının altında yaklaşık beş gün içinde tamamlanır. Sıcaklığın düştüğü ve nem seviyesinin yükseldiği akşam saatlerinde en az iki gün boyunca sporlar oluşur. Yağmur ve/veya sulama ile bu sporlar topraktaki yeni bitkilere bulaşır. Aynı zamanda rüzgarla da komşu bitkilere taşınabilir. Bulaştıktan sonra kolayca fark edilemez. Bu yüzden kültürel yöntemlerle hastalıkla mücadele etmek neredeyse imkânsızdır.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıklı bitkiler, yumrular imha edilir. Tarlada kalan bitki artıkları temizlenir. Sertifikalı yumrular veya tohumlar kullanılır. Yabancı otlarla mücadele edilir. Hastalığın yayılmasını önlemek için uygun sulama sistemi kurulmalıdır, nemli havalarda sulama yapılmamalıdır. Nem oranın yüksek olması salgın oluşmasına neden olur. Ancak hastalık görülmeye başlandıktan sonra kültürel yöntemlerle mücadele salgını önlemekte başarılı değildir.
                        2-	Kimyasal Tedavi
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır
                        * Bitkinin tüm yüzeyi ilaçlanmalı, ilaçlama serin ve rüzgarsız zamanlarda 7–10 gün arayla yapılmalıdır.
                        * Kimyasal mücadelede kullanılan pek çok pestisitin yanı sıra Syngenta firmasının ruhsatlamış olduğu Revus Pro içerdiği 250 g/l mandipropamid ve 250 g/l difenoconazole ile Patates mildiyösü mücadelesinin yanı sıra Patates erken yaprak yanıklığı hastalığına karşı da üstün etki ve performans gösterir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/patates_yetistiriciligi_00005.html#:~:text=Patates%20bitkilerinde%20su%20ihtiyac%C4%B1%20alt,s%C3%BCresince%202%2D4%20sulama%20yap%C4%B1l%C4%B1r)")
          st.subheader("Detaylı bilgi için: [lezzet](https://www.lezzet.com.tr/lezzetten-haberler/patates-ne-zaman-ekilir)")

      if ctrl == 'Raspberry___healthy':
          
            col1, col2 = st.columns(2)
            with col1:
                st.image('a.sag1.jpg')
            with col2:
                st.image('a.sag2.jpg', width=390)
            st.header('Ahududu - Sağlıklı')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Ahududu bakımında en önemli unsurlardan birisi topraktır. Ahududu toprağında özellikle yabani otlar ile mücadele çok önemlidir. İlk dönemlerden başlanarak hasat zamanına kadar ahududu bakımı için sürekli toprak işlenmelidir. Daha sonra ahududu bakımında gübreleme işlemi önemlidir. Ahududu bakımında gübreleme için ticari tarım gübreleri ve özel çiftlik gübreleri verilerek ahududunun fiziksel yapısının ve bitkinin besin değerlerinin yükseltilmesi çok önemlidir.
                        * Ahududu toprağının da su tutma kapasitesinin artırılması da ahududu bakımı için çok önemlidir. Ahududu bakımı sırasında bitkiye verilen azotlu gübreye azami özen gösterilmelidir. Çünkü verilen azot miktarı iyi ayarlanamaz ise ahududu meyvesinin yumuşaması ve özelliğini kaybederek pazar değerinin düşmesine sebep olmaktadır. Ahududu bakımında bitkiden daha verimli meyve alınması için en doğru gübreleme sıravari yada ocak usulü gübreleme şekilleri olmaktadır.
                        * Ahududu bakımında toprak tahlilleri de her yıl düzenli bir şekilde yapılması gereklidir. Ahududu bakımında sulama işlemi ise genellikle sulamada ahududu hasat zamanına yakın bir zamanda çok daha fazla sulanması gereken bir bitkidir.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Dikim budaması: Ahududu dikiminden hemen sonra en fazla 30 cm yükseklikte budanmalıdır. Ahududu budamada ilk bahar aylarında bakılarak 3-4 adet kuvvetli olan kollar bırakılarak diğer filizler kesilmelidir. Ahududu gövdesinde budama yapılırken bırakılan kuvvetli dallar arası da en az 25 cm olmalıdır.
                        * Kış budaması: Ahududu kış budamasında hasat zamanı geçtikten hemen sonra sonbahar aylarına doğru kuruyan dallar dipten kesilerek temizlenmelidir. Kök kısmından yetişen filizlerin önü açılmalıdır. Ahududu kış budaması için en uygun zaman ise sonbahar ayları yada ilk bahar başlangıcında olmaktadır.
                        * Yaz budaması: Ahududu bakımında yaz budaması bitki tepeleri kesilerek aşırı derecede fazla olan dalların budanması gerekmektedir. Fakat çok aşırı sıcaklarda bu işlemin yapılması bitki için çok zararlıdır. Ahududu bakımında zayıf ve yere yakın kollar budanmalıdır. Ahududu meyvelerinin kuvvetlendirilmesi için fazla kollar gövdeden temizlenmelidir. İri meyve alınması ancak kuvvetlendirilmiş dallardan alınacağı unutulmamalıdır.
                        * Gençleştirme budaması: Son olarak ahududu bakımında gençleştirme budaması olarak bitki artık yaşlandığından kök kısımlarında zayıflama görülür. Bu durumda ahududu bitkisinin kalitesi düşerek verimsizleşir. Bu durumu önlemek için ahududu en az 6 yıl aralıklar ile toprak altında bulunan köke ulaşarak kesilmesi ve bitkinin gençleştirilmesi önemlidir. Yaşlı kökler bitkiden ayrılarak akabinde bol miktarda çiftlik gübresi ve bunun yanı sıra ticari gübre verilerek ahududunun güçlenmesi ve ömrünün uzaması sağlanır.
                        """)
            st.subheader("Detaylı bilgi için: [ahududu.gen](https://www.ahududu.gen.tr/ahududu-bakimi.html)")

          
      if ctrl == 'Soybean___healthy':
          
            col1, col2 = st.columns(2)
            with col1:
                st.image('s.sag2.jpg')
            with col2:
                st.image('s.ssag3.png')
            st.header('Soya Fasulyesi - Sağlıklı')
            st.subheader('Nasıl- Nerede Yetiştirilir')
            st.markdown("""
                        * Soya fasulyesi, farklı iklim etkilerine uyum sağlayabildiği için dünyanın farklı bölgelerinde yetiştirilir. Buna göre soya ekiminden elde edilebilecek en iyi verim Mayıs ve Eylül ayları arasında kabul edilmektedir. Yetiştirilme için optimum ortam sıcaklığı 25 derecedir. Ancak 18 ile 40 derece arasındaki tüm sıcaklıklarda yetiştirilmesi mümkündür. Bu aralık dışında kalan düşük ve yüksek sıcaklıklar soya fasulyesinin gelişimi üzerinde negatif etki yaratmaktadır.
                        * Soya fasulyesinin toprak isteği de oldukça geniş bir yelpazeye sahiptir. Buna göre aşırı kumlu topraklar dışındaki tüm bölgelerde ekim yapmak ve verim elde etmek mümkündür.
                        * Soya fasulyesi, iklim ve toprak açısından pek seçici değildir. Bu bakımdan dünyanın çok farklı bölümlerinde soya fasulyesi yetiştiriciliği yapmak mümkündür. Ancak üretimin %85 gibi büyük bir kısmı Adana ve Osmaniye tarafından karşılanmaktadır.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Ekim nöbeti: Soya üst üste aynı tarlaya ekilmemelidir. Çünkü hem verimi düşer, hem de hastalık ve zararlar çoğalır.
                        * Gübreleme: Kombine mibrezle yapılan ekimlerde azotlu gübrenin tamamı, toprak sathına serpildikten sonra, fosforlu gübre ve tohum mibrezle banda verilmelidir.
                        * Sulama: Soya yetiştirme süresi boyunca en az 2 defa sulanmalıdır. Bunlardan birincisi bitkiler 20-25 cm boylandığında, diğeri de çiçeklenme öncesi sulanmadır. Eğer bir su verilecekse mutlaka çiçeklenme öncesi verilmelidir. Sulamadan önce toprak nemi önceden kontrol ediilmelidir.
                        * Hasat: Hasat zamanı baklalar çeşide göre kirli sarı veya esmerimsi bir renk alır. Hasat için alt baklalar kontrol edilmelidir. Taneler sertleşir ve dişle zor kırılır. Yaprakların sararıp dökülmesinden 4-6 gün sonra hasada başlayıp kısa sürede bitirmek gerekir.
                        """)
            st.subheader("Detaylı bilgi için: [tarım orman araştırma](https://arastirma.tarimorman.gov.tr/cukurovataem/Belgeler/Yeti%C5%9Ftiricilik/soya-yetistiriciligi_1.pdf)")

          
      if ctrl == 'Squash___Powdery_mildew':
          col1, col2 = st.columns(2)
          with col1:
                st.image('k.kül1.jpg', width=350)
          with col2:
                st.image('k.kül2.jpg', width=370)
          st.header('Kabak - Küllenme')
          st.subheader('Nedir?')
          st.markdown('Hastalık bitkilerin önce yaşlı yapraklarında görülür, daha sonra genç yapraklara da geçer. Öncelikle yaprağın üst yüzeyinde parça parça, nispeten yuvarlak lekeler belirir, sonradan bu lekeler birleşerek yaprağın her iki yüzeyini, yaprak sapını ve gövdeyi kaplar. Lekeler ilk zamanlarda beyaz renkte toz tabakası gibi görünür, zaman ilerledikçe esmerleşir. Yapraklar kuruyup dökülür ve bitkide gelişme durur. Bunun sonucu olarak da ürün kaybı meydana gelir. Hastalık için en uygun sıcaklık 27 C’dir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hasattan sonra hastalıklı bitki artıkları toplanarak yakılmalıdır.
                        2-	Kimyasal Mücadele
                        * İlk hastalık belirtileri görüldüğünde ilaçlamaya başlanmalıdır.
                        * İlaçlama havanın serin ve sakin olduğu zamanlarda bitkinin her tarafının ilaçla kaplanması şeklinde olmalıdır.
                        * Yağıştan sonra ve fazla çiğ bulunduğunda toz kükürt uygulaması yapılmamalıdır, çünkü çıkabilecek güneş nedeni ile yanıklar meydana gelebilir.
                        * Genellikle günlük sıcaklık ortalaması 27 derecenin üstünde ve orantılı nemin de %50’nin altına düştüğü zamanlarda ilaçlamaya ara verilmeli, şartlar değiştiğinde ise ilaçlamaya devam edilmelidir.
                        """)
          st.subheader("Detaylı bilgi için: [growveg](https://www.growveg.com/plant-diseases/us-and-canada/squash-powdery-mildew/)")
      if ctrl == 'Strawberry___healthy':
            
            col1, col2 = st.columns(2)
            with col1:
                st.image('ç.sag1.jpg', width=350)
            with col2:
                st.image('ç.sag2.jpg', width=370)
            st.header('Çilek - Sağlıklı')
            st.subheader('Çilek Yetiştiriciliği')
            st.markdown("""
                        * Çilek meyvesi gerçek bir meyve olmayıp yenen kısmı 40-60 kadar pistilin birleştiği çiçek tablasıdır. Çilek yüzeysel kök yapan otsu bir bitkidir.Kökler iyi drene edillmiş(süzek)topraklarda  60-70 cm' ye kadar iner.Ağır topraklarda ise kökler yatay büyür.
                        * Çilek yaprakları 2/5 düzeninde spiral olarak dizilmiştir.İlkbaharda havalar ısınınca patlayan embriyonik yapraklar 2-3 hafta sonra tam büyüklüğe erişir.Her yaprağın 1-3 ay ömrü vardır. Kollar (stolonlar)yaz boyunca  yeni yaprakların koltuklarındaki tomurcuklarından oluşarak gelişirler. Çilekte çiçekler salkım şeklindedir.Buna değişmiş gövdede denilebilir. Çilekte iyi tozlanma gereklidir. Tozlanmadan sonra meyve genelde 30-35 günde olgunlaşır.
                        * Çilek -10 oC ‘ye kadar yetiştirilebilir. Daha soğuk bölgelerde bitkilerin saman ,kuru  yaprak gibi materyalle örtülerekdondan korunması gerekir. Çilek yetiştiriciliği için en uygun toprak ; süzek, kumlu-tınlı  ve hafif topraklardır. Kireci fazla topraklar çilek için uygun değildir. Toprak  PH’ sı 7.0 - 7.5  olan topraklarda önemli bir problem yaratmamaktadır.
                        * Toprak derin işlendikten sonra dekara 3-4 ton çiftlik gübresi atılmalıdır. Ayrıca dekara 30-35 kg kompoze gübre verilmelidir.
                        * Büyük arazilerde  karık pulluğu ile, küçük alanlarda ise  elle 60-70 cm genişliğinde, 20-30 cm yüksekliğinde masuralar açılarak toprak dikime hazır hale getirilir. Çilek yetiştiriciliğinde ilkbahar dikimi, kış dikimi, yaz dikimi, sonbahar dikimi olmak üzere 4 dikim zamanı vardır.
""")
            st.subheader('Yetiştirme Tekniği Ve Dikim Zamanları')
            st.markdown("""
                        * Çilek -10C‘ ye kadar yetiştirilebilir. Daha soğuk bölgelerde bitkilerin saman ,kuru  yaprak gibi materyalle örtülerekdondan korunması gerekir. Çilek yetiştiriciliği için en uygun toprak ; süzek, kumlu-tınlı  ve hafif topraklardır. Kireci fazla topraklar çilek için uygun değildir. Toprak  PH’ sı 7.0 - 7.5  olan topraklarda önemli bir problem yaratmamaktadır.
                        * Çilek , toprak kökenli mantarsal hastalıklara karşı duyarlı olduğu için dikim yapılacağı toprağın bu hastalıklardan ve nematod yönünden temiz olması gerekir. Bunun için bir önceki mevsimde buğday, arpa gibi tahıl ekilmiş araziler tercih edilmelidir. Böyle topraklar bulunmadığı taktirde toprak metilbromit, vapam, kloropikrin gibi ilaçlarla fümige edilmelidir.
                        * İlkbahar Dikimi: Kışları soğuk geçen bölgelerde genellikle  Nisan ayında yapılan bir dikimdir. Bu dikimde frigo fideler veya fidelikte Ocak - Şubat  aylarında sökülmeyip bekletilen fideler  kullanılır. Bu fideler Mayıs ve Haziran aylarında az miktarda çiçek açarak meyve verirler. Bunların esas ürünü 1 yıl sonraki Haziran ayındadır. Bu bitkilerin 1 yıl boyunca su ,besin maddesi ihtiyaçları  karşılanmalı ve hastalık ve zarlılardan korunmalıdır.
                        * Kış Dikimi: Kışları ılık  geçen yerlerde yapılır. Dekara yaklaşık 8000 adet bitki dikilir. Dikimler fidelikten sökülen yavru bitkilerle yapılır. Akdeniz  Bölgesinde kış dikimi için en uygun zaman Ekim 15 - Kasım 15 arasıdır. Ilkbaharda açıkta Mart ortasından itibaren ürün alınmaya başlanır .Ayrıca alçak ve yüksek tüneller altında çilek yetiştiriciliği yapılırsa, ,açıkta yetiştiriciliğe göre yaklaşık 15- 30 günlük erkencilik sağlanır.
                        * Yaz Dikimi: Frigo bitkilerde yapılır. Bu dikim sisteminde verim kış dikimine göre 2-3 kat daha fazladır. Ancak ürün kış dikimine göre biraz geç kalmaktadır. Akdeniz Bölgesinde yaz dikimi için en uygun zaman Temmuz 15 - Ağustos 15 arasıdır.-20 OC ‘den çıkartılan frigo fideler  bir gece suda bırakılır. Sonra dikim yapılır. Fideler sıra üzeri ve sıra arası 30 x 32 cm olarak dikilir. Yazın sulama büyük problem teşkil eder. Dekara yaklaşık 6200 adet bitki dikilmektedir. Bütün yaz ve sonbahar aylarında büyümelerine devam eden bitkiler giderek kuvvetlenmekte ve kışa 5-10 gövdeli olarak girmektedirler.
                        * Sonbahar Dikimi: Fideler serin ve nemli havalarda dikilmelidir. Fide açılan çukurlara tam kök boğazı seviyesinde dikilir. Dikimden önce kök (8-10 cm kalacak şekilde ) ,taç tuvaleti (2-3 genç yaprak kalacak şekilde)yapılarak bitkilerin tutma oranı arttırılır. Dikimden sonra cansuyu verilir. Yaz dikiminde bitkiler 15 gün ,günde en az 3 defa olmak üzere çok iyi sulanmalıdır. Yaz dikiminde dikimden 6-8 gün sonra açan çiçekler koparılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/cilek_yetistiriciligi_-_1_00296.html)")
          
      if ctrl == 'Strawberry___Leaf_scorch':
          col1, col2 = st.columns(2)
          with col1:
                st.image('ç.yapraky1.jpg', width=350)
          with col2:
                st.image('ç.yapraky2.jpg', width=370)
          st.header('Çilek - Yaprak Yanıklığı')
          st.subheader('Nedir?')
          st.markdown('Kavrulmuş çilek yapraklarına, çilek ekimlerinin yapraklarını etkileyen bir mantar enfeksiyonu neden olur. Yaprak kavrulmuş çilekler, ilk önce yaprakların üst kısmında oluşan küçük morumsu lekelerin gelişmesiyle sorun belirtileri gösterebilir. Zamanla, lekeler büyümeye ve kararmaya devam edecektir. Şiddetli vakalarda, koyu lekeler çilek bitkisinin yapraklarının tüm kısımlarını kaplayabilir ve bunların tamamen kurumasına ve bitkiden düşmesine neden olabilir. Enfekte olmuş bitkilerin yaprakları estetik olarak hoş olmasa da bu mantarın varlığının çilek mahsulünün kalitesini etkilemesi nadiren olur.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * İyi drene edilmiş topraklarda çilek yetiştirilmeli.
                        * Bitkiler arasında iyi bir hava sirkülasyonu sağlanmalı, dayanıklı çeşitler kullanılmalı.
                        * Sağlıklı üretim materyali kullanılmalı
                        * Kış sürecinde bitki üzerinde kalan enfekteli yaşlı yapraklar, hastalığın inokulum kaynağının azaltılmasına yardımcı olması bakımından, ilkbahar büyüme dönemi başlamadan önce tarlandan uzaklaştırılmalıdır.
                        2-	Kimyasal Mücadele
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır.
                        * Yağıştan sonra ve fazla çiğ bulunduğunda toz kükürt uygulaması yapılmamalıdır, çünkü çıkabilecek güneş nedeni ile yanıklar meydana gelebilir.
                        * Genellikle günlük sıcaklık ortalaması 27 derecenin üstünde ve orantılı nemin de %50’nin altına düştüğü zamanlarda ilaçlamaya ara verilmeli, şartlar değiştiğinde ise ilaçlamaya devam edilmelidir.
                        """)
          st.subheader("Detaylı bilgi için: [tarım orman.gov](https://www.tarimorman.gov.tr/GKGM/Belgeler/Uretici_Bilgi_Kosesi/Dokumanlar/cilek.pdf)")

      if ctrl == 'Tomato___Bacterial_spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.bakteriyel1.jpg', width=350)
          with col2:
                st.image('d.bakteriyel2.jpg', width=370)
          st.header('Domates - Bakteriyel Leke')
          st.subheader('Nedir?')
          st.markdown('Hastalık etmeni bakteri olup, optimum gelişme sıcaklığı 29°C ‘dir. Etmen bir yıl veya daha uzun süre tohum üzerinde veya içinde canlılığını sürdürebilir. Ancak konukçu bitki kalıntısı olmadan toprakta yaşayamaz. Seradaki hava hareketleri, su damlacıkları, yüksek basınçlı ilaçlamalar ve ıslak bitkilere temas edilmesi hastalığın yayılmasını teşvik etmektedir. Bakteri bitkideki doğal açıklıklardan veya herhangi bir nedenle bitkide açılan yaralardan giriş yapmaktadır. Uzun süreli yüksek orantılı nem ve 20-35°C sıcaklık koşulları hastalık gelişimini teşvik ederken 16°C’ den düşük gece sıcaklıkları hastalık gelişimini baskılamaktadır. Domateste yaprak, gövde ve meyve üzerinde bakteriyel leke hastalığının belirtileri görülür.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Üretimde sertifikalı tohum ve fideler kullanılmalıdır.
                        * Hastalığın görüldüğü̈ üretim alanlarında domates ve biber dışındaki bitkilerle en az 2 yıl süre ile ekim nöbeti uygulanmalıdır.
                        * Üretim sezonu sonunda tüm bitki artıkları sökülerek imha edilmelidir.
                        * Dengeli bir gübreleme programı uygulanmalı, özellikle meyve bağlama döneminden önce aşırı gübrelemeden kaçınılmalıdır.
                        * Bitkilerin ıslak olduğu zamanlarda serada çalışılmamalıdır.
                        * Seralarda havalandırmaya özen gösterilmeli ve aşırı nem birikimi önlenmelidir.
                        2-	Kimyasal Mücadele
                        * Yeşil akşam ilaçlamaları fidelikte veya serada hastalık görülür görülmez, fide döneminde haftada bir, serada ise 8-10 gün ara ile 2-3 uygulama yapılmalıdır. Hastalığın seyrine göre uygulama sayısı arttırılabilir Fide ve sera döneminde yapılacak olan yeşil akşam ilaçlamaları kaplama olarak yapılmalıdır.
                        * Özellikle örtü̈ altı üretiminde ilaçsız alan kalmamasına özen gösterilmeli ve bitki yüzeyinde ıslaklık söz konusu ise bitkilerin yüzeyi kuruduktan sonra ilaçlama yapılmalıdır.
                        * Etkili madde olarak Bakır oksiklorid (300-400 g) kullanılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [tarım orman.gov](https://www.tarimorman.gov.tr/GKGM/Belgeler/Uretici_Bilgi_Kosesi/Dokumanlar/cilek.pdf)")

      if ctrl == 'Tomato___Early_blight':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.eyanık1.jpg', width=350)
          with col2:
                st.image('d.eyanık2.jpg', width=370)
          st.header('Domates - Erken Yanıklık')
          st.subheader('Nedir?')
          st.markdown('Hastalığa konukçu bitkilerin her evresinde rastlanabilir. Hastalık, fide döneminde kök çürüklüğü veya kök boğazı yanıklığı yapar. Sonraki dönemlerde ise yaprak, gövde ve meyvelerde lekeler halinde görülür. Bu lekeler önce küçük, düzensiz ve esmerdir. Sonra iç içe halkalar halinde 1-2 cm kadar büyürler ve koyu gri renk alırlar. Hastalığın şiddetine göre bütün yapraklar kuruyup dökülebilir. Çiçek ve meyve sapları hastalığa yakalanırsa dökülürler. Meyvelerde genellikle sapın tutunduğu kısımda koyu renkli çökük, çoğunlukla sınırlanmış lekeler meydana gelir. Hastalık kısa zamanda bitkiyi öldürmesi nedeniyle önemlidir.')
          st.markdown('Etmenin konukçuları domates, patlıcan ve patatestir. Hastalık 6-34oC arası sıcaklıkta gelişebilmektedir; ancak optimum gelişme sıcaklığı 28-30oC arasıdır. Görece nemin yüksek olduğu koşullar hastalığın gelişimini teşvik eder.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Sertifikalı tohum veya sağlıklı fide kullanılmalıdır.
                        * Fidelikler ve seralar sık sık havalandırılmalıdır.
                        * Aşırı sulamadan kaçınılmalıdır.
                        * Hasattan sonra hastalıklı bitki artıkları imha edilmelidir.
                        2-	Kimyasal Mücadele
                        * Fidelikte veya tarlada ilaçlamaya ilk lekeler görülür görülmez başlanmalıdır. İklim koşulları hastalık gelişimi için uygun olduğunda ilacın etki süresine bağlı olarak ilaçlama tekrarlamalıdır.
                        * Erken yaprak yanıklığının mücadelesinde Activus® kullanılabilmektedir.
                        * Bir sezonda maksimum 3 kez Activus® kullanılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [syngenta.com](https://www.syngenta.com.tr/blog/murat-kadioglu/domateste-erken-yaniklik-alternaria-solani#:~:text=Alternaria%20solani%20ya%C5%9Fam%C4%B1n%C4%B1%20topraktaki%20bitki,ve%20k%C3%B6k%20bo%C4%9Faz%C4%B1%20yan%C4%B1kl%C4%B1%C4%9F%C4%B1%20yapar.)")

      if ctrl == 'Tomato___healthy':
            st.header('')
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.sag3.png')
            with col2:
                st.image('d.sag2.jpg')
            st.header('Domates- Sağlıklı')
            st.subheader('Domates Yetiştiriciliği')
            st.markdown("""
                        * Sıcaklık: Domates, sıcak ve ılıman iklim sebzesidir. Gündüz 17-26˚C, gece ise 14-18˚C'dir. Sıcaklık -2°C'ye düşerse, bitki tamamen zarar görür. 10˚C'nin altında ve 30˚C'nin üzerinde tozlanma ve döllenmede problemler ortaya çıkmakta, meyve bağlayamamaktadır.
                        * Toprak: Derin, geçirgen ve su tutma özelliği iyi, humus ve besin maddelerince zengin tınlı toprakları sever. Toprak pH’sı 5-7 (hafif asidik) arasında, tuzsuz-az tuzlu (2,3 mS’dan az) toprakları sever. Kazık kök derine inebildiğinden toprak derin sürülmelidir. Gerektiğinde pulluk tabanı kırılmalıdır.
                        * Çapalama: Dikimden 10-15 gün sonra kesekler varsa kırılmalı, fide boğazı gevşekse doldurulmalıdır. Dikimi takiben 25-30 gün sonra ikinci çapa yapılır. Yabancı ot mücadelesi ve toprak neminin muhafazası için 3. ve 4. çapa yapılmalıdır. 
                        * Hasat: Domatesler, açık alanda fide dikiminden hasada kadar 60-80 günlük bir zamanda hasat olgunluğuna gelir. Pazara uzaklık durumuna göre değişik olgunluk devrelerinde hasat edilir. Hasat, havanın kuru ve serin olduğu zamanlarda yapılmalıdır. Meyve avuç içine alınarak, sapı etrafında hafifçe döndürülmek suretiyle zedelenmeden koparılmalıdır.
                        * Tek dallı olarak büyümesini istediğimiz bitkinin şeklini korumuş oluruz. Koltukların alınma devresi 5-15 cm boya eriştikleri zamandır. Erken koparıldıklarında yeniden çıkma ihtimalleri varken, büyük koparıldıklarında hem boşa besin maddesi tüketmiş olurlar hem de bitkide açılacak yara yüzeyi artmış olacaktır.
""")
            st.subheader('Domates ektikten sonra bakım nasıl yapılmaktadır?')
            st.markdown("""
                        Derin sürümle hazır olan toprak, sonbaharda 3-4 ton/da ahır gübresi alır. İlkbaharda ise karık hazırlığından önce taban gübresi alır. Fosforlu gübrenin tamamı gider. Diğerlerin üçte biri taban gübresi olarak gider. Geriye kalan gübreler ise bitkilerim üzerinde meyve görülmeye başladığı zaman verilmelidir. Meyveler fındık büyüklüğüne geldiğinde 10 ila 15 gün arayla 2-3 kez 100 lt suya 400-600 gr olacak şekilde yapılan magnezyum uygulanmaları ve verilen yaprak gübresi meyve kalitesini arttırmaya yönelik olumlu etki etmektedir.
                        """)
            st.markdown("""İlkbahar geç donlarının tehlikesi kalktığında, toprak ve hava sıcaklığı 12-15°C yi bulduğu zaman fide dikimi gerçekleştirilmektedir. Tarlaya dikim esnasında çiçek atmış ya da meyve tutmuş domates fideleri dikilmemelidir. Buna benzer fidelerin verimleri düşük, boyları bodur ve gelişmeleri yavaş olmaktadır.  Güneş altında bekletilmeyen fideler, akşama doğru dikilmelidir. 15-20 cm boyuna gelen fideler genelde dikime hazır hale gelmişlerdir. Dikimde can suyu yeterli miktarda olur. Can suyu ile birlikte, kök ve kök boğazı hastalıklarına karşı gereken ilaçlamalar gerçekleşir. Sıra arası ve üzeri mesafeler domatesin çeşidine göre değişmektedir.
                        
                        """)
            st.subheader('Seralarda Havalandırma İşleminin Önemi')
            st.markdown('Örtü altı domates yetiştiriciliğinde en önemli kültürel işlemlerin biri de yetiştirme ortamın havalandırılması işlemidir. Güneşli bir günde dış ortam soğuk olsa bile örtü altı koşulları bitki için optimum iklim koşullarının üstüne çıkabilir.')
            st.markdown('Örtü altı koşullarında hava oransal nemimin % 60-90 arasında olması istenir. Hava oransal nemi optimum koşullardan aşağı düşerse verim ve kalite kayıplarına sebep olur. Üstüne çıkarsa hastalık ve zararlı yoğunluğu artar. Erken sonbahar veya geç ilkbahar da havalandırma ile ortam sıcaklıkları yeterli düzeye düşmeyebilir.Bu dönemlerde gölgeleme materyalleri ile sera gölgelendirilmeli ve ortam sıcaklıkları düşmesi sağlanmalıdır.')
            st.image('d.st.jpg')
            st.subheader("Detaylı bilgi için: [Tarım Orman](https://adana.tarimorman.gov.tr/Belgeler/SUBELER/bitkisel_uretim_ve_bitki_sagligi_sube_mudurlugu/sebze_yetistiriciligi_ve_mucadelesi/Domates.pdf)")
            st.subheader("Detaylı bilgi için: [Milliyet](https://www.milliyet.com.tr/pembenar/domates-ektikten-sonra-bakimi-nasil-yapilir-domates-fidesi-bakimi-nasil-yapilmalidir-6517133)")

          
      if ctrl == 'Tomato___Late_blight':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.gyanık1.jpg', width=350)
          with col2:
                st.image('d.gyanık2.jpg', width=370)
          st.header('Domates - Geç Yanıklık')
          st.subheader('Nedir?')
          st.markdown('Bölgelere göre ilkbahar ve yaz başlagıcında hastalık belirtileri patates bitkilerinde görülmeye başlar. Hastalık etmeni toprakta ve ölü bitki artıklarında canlılığını uzun süre koruyamaz, fakat dayanıklı üreme organı olan oosporları muhafaza edilebilir. Bir alanda epideminin (salgın) başlaması için mikroorganizma patates yumrularında kışı geçirmekte ya da tohumluk patates veya şaşırtılacak domates fideleri ile yeni bir alana tekrar girmelidir veyahutta canlı sporlar yağmurla veya sulama suyu ile taşınmalıdır. Serin, yağışlı havalar (16 - 27 °C) hastalığın gelişmesi için uygun iken, kuru ve sıcak havalar hastalığın gelişmesini engelleyebilir.')
          st.markdown('Enfektelenmiş gövde dokuları hastalık etmenini kuru ve sıcak havalardan korur ve uygun koşullarda hastalık buralardan tekrar gelişir ve büyük epidemilere yol açabilir. Yağmurlu, sisli ve çiğ oluşumu yüksek olan yerlerde hastalık sık olarak karşımıza çıkar. Enfekteli dokular üzerinde fungal etmenin sporları (sporongia) oluşur. Yağmur ya da sulama suları sporları sağlıklı bitkilere taşır ve sporongialar ıslak yaprak ve gövdeleri direkt yada stomalardan infekte ederler. Serin ve nemli koşullarda, sporongia hareketli olan zoosporları da üretebilir ve bu sporlarda bitkileri direkt olarak enfekte edebilir. Fungal etmen yaprak ve gövde de hızla kolonize olur ve infektelen bölge hastalık ilerken nekrotik olur.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Yaprak ve gövdeler kontrol edilerek koyu lekeli bitkiler şaşırtılmamalı.
                        * Bitki artıkları uzaklaştırşmalı ve yok edilmelidir.
                        * Sulama esnasında yaprakların ıslanmamalı, özellikle geç ve akşam sulamalarından kaçınılmalı.
                        2-	Kimyasal Mücadele
                        * İlaçlamalar düzenli aralıklarla yapılmalı, özellikle hastalığın görüldüğü bölgelerde hastalık belirtileri ortaya çıkmadan önce, bitkiler koruyucu ilaçlar ile ilaçlanmalıdır.
                        * Kullanılan ilaçlar arasında; Azoxystrobin SC 250 g/l, Bakır Oksiklorid WP 50%, Folpet WP 50% vardır.
                        """)
          st.subheader("Detaylı bilgi için: [syngenta.com](https://www.syngenta.com.tr/blog/murat-kadioglu/domateste-erken-yaniklik-alternaria-solani#:~:text=Alternaria%20solani%20ya%C5%9Fam%C4%B1n%C4%B1%20topraktaki%20bitki,ve%20k%C3%B6k%20bo%C4%9Faz%C4%B1%20yan%C4%B1kl%C4%B1%C4%9F%C4%B1%20yapar.)")

      if ctrl == 'Tomato___Leaf_Mold':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.küllenme1.jpg', width=350)
          with col2:
                st.image('d.küllenme2.jpg', width=370)
          st.header('Domates - Küllenme')
          st.subheader('Nedir?')
          st.markdown('Hastalık, bitki dokusunun içinde ve dışında gelişir. Kışı yapraklar üzerinde; ılıman bölgelerde yeşilliğini muhafaza eden bitki dokularında geçirir. Hastalığın ilk belirtileri domatesin yapraklarında görülen yuvarlakça beyaz küçük lekeler halindedir. Bu küçük lekeler, zamanla birleşerek bütün yaprak ayasını, yaprak sapını ve gövdesini kaplar; mevsim ilerledikçe rengi beyazdan kül rengine döner. Hastalığın ilerlemesi ile yapraklar pörsür, aşağıya doğru sarkar ve kurumalar meydana gelir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıklı bitki artıkları toplanıp imha edilmelidir.
                        2-	Kimyasal Mücadele
                        * İlaçlamalar tarla ve serada ilk hastalık belirtileri görüldüğünde yapılmalıdır.
                        * Domates küllemesinde Activus ürünleri kullanılabilmektedir.
                        * Bir sezonda en fazla 3 kez kullanılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [agro](https://www.agro.basf.com.tr/tr/Bilgi-Bankas%C4%B1/Hastal%C4%B1k-Zararl%C4%B1-Yabanc%C4%B1-Ot-Bilgi-Bankas%C4%B1/Fungal-Hastal%C4%B1klar/B%C3%BCy%C3%BCme-noktas%C4%B1-yaprak-sap-hastal%C4%B1klar%C4%B1/K%C3%BClleme-(Leveillula-Taurica)/#:~:text=Hastal%C4%B1%C4%9F%C4%B1n%20ilk%20belirtileri%20domatesin%20yapraklar%C4%B1nda,rengi%20beyazdan%20k%C3%BCl%20rengine%20d%C3%B6ner.)")
          st.subheader("Detaylı bilgi için: [tarım orman](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/1266?csrt=6516937016701123893)")

      if ctrl == 'Tomato___Septoria_leaf_spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.sept1.jpg', width=350)
          with col2:
                st.image('d.sept2.png', width=370)
          st.header('Domates - Septoria Yaprak Lekesi')
          st.subheader('Nedir?')
          st.markdown('Esas olarak yapraklarda meydana gelmekle beraber gövdede yaprak ve çiçek sapında da görülmektedir. Yapraklarda küçük sarımsı alanlar şeklinde başlar daha sonra gri veya kahverengiye döner. Lekelerin büyüklüğü hassas çeşitlerde 2.5 cm çapa kadar ulaşır ve yuvarlak şekildedirler. Lekeler üzerinde inokulasyondan 10 gün sonra siyah renkte piknidler gelişir. Piknidiosporları rüzgarla çevreye yayılarak hastalığı başlatır. Hastalık yaşlı yapraklardan genç yapraklara doğru gelişen yaprak dökümüne neden olmaktadır.')
          st.markdown('Hastalığın eşeyli dönemi yoktur. Hastalık etmeni tohumda, tarladaki hastalıklı bitki artıklarında, enfekteli çok yıllık yabancı otlarda canlılığını sürdürür. Enfeksiyonun gerçekleşmesi için nisabi nemin 48 saat süreyle % 100 düzeyinde olması gerekmektedir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Temiz tohum kullanılmalıdır. Hastalığın görülmediği bölgelerde tohum üretimi yapılmalıdır.
                        * Hastalık bazı yabancı otlarda da kışladığı için tarlada iyi bir yabancı ot mücadelesi yapılmalıdır.
                        2-	Kimyasal Mücadele
                        * Kimyasal mücadelesinde Mancozeb ve Chlorotholonil ile 7-10 günlük aralıklarla ilaçlama yapılmalıdır.
                        """)
          st.subheader("Detaylı bilgi için: [sorhocam](https://www.sorhocam.com/konu.asp?sid=4157&domates-septoria-yaprak-lekesi-hastaligi.html)")
          st.subheader("Detaylı bilgi için: [tarım orman](https://kayseri.tarimorman.gov.tr/Belgeler/SOL%20MEN%C3%9C%20BELGELER%C4%B0/Z%C4%B0RAA%C4%B0%20M%C3%9CCADELE/Sebze%20Hastal%C4%B1klar%C4%B1/sebzelerde_septoria_leke_hastaligi.pdf)")

      if ctrl == 'Tomato___Spider_mites Two-spotted_spider_mite':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.kırmızı1.jpg', width=350)
          with col2:
                st.image('d.kırmızı2.jpg', width=370)
          st.header('Domates - İki Noktalı Kırmızı Örümcek Isırığı')
          st.subheader('Nedir?')
          st.markdown('İki noktalı kırmızı örümcek, tüm dünyada birçok mahsulde görülebilen bir zararlıdır. Küçük boyutlarına rağmen, çok hızlı üreyebildiklerinden dolayı çok hızlı biçimde son derece büyük zarara neden olabilirler.')
          st.markdown('Yumurtalar özellikle yaprakların alt kısmında görülür. Gövdeleri oval şekilli olup arka ucu yuvarlaktır. Turuncu, açık sarı veya açık yeşilden koyu yeşil, kırmızı, kahverengi veya neredeyse siyaha kadar çok çeşitli renklerde olabilirler. Genellikle bitki öz suyundan beslenerek bitkiye zarar verir.')
          st.markdown('Domateste yaprak yüzeyinin %30’luk bir kısmını yiyerek mahsülün tamamen kaybedilmesine neden olabilir.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler 
                        * Seraya temiz fideler dikilmeli
                        * Hasattan sonra bitki artıkları tarla ve seradan uzaklaştırılmalı
                        * Ot çapasına önem verilmeli
                        * Gereğinden fazla azotlu gübreler kullanılmamalı
                        * Toprak işlemesi yapılarak kırmızı örümceklerin kışladıkları bitki artıkları toprağa gömülmelidir.
                        2-	Kimyasal Mücadele
                        * Küçük yapraklı sebzelerde yaprak başına 3 adet, büyük yapraklı sebzelerde 5 adet canlı Kırmızı örümcek bulunduğunda ilaçlama yapılır.
                        * Bakanlıkça önerilen ruhsatlı zirai mücadele ilaçlarından biri kullanılır.
                        """)
          st.subheader("Detaylı bilgi için: [sorhocam](https://www.sorhocam.com/konu.asp?sid=4157&domates-septoria-yaprak-lekesi-hastaligi.html)")
          st.subheader("Detaylı bilgi için: [tarım orman](https://kayseri.tarimorman.gov.tr/Belgeler/SOL%20MEN%C3%9C%20BELGELER%C4%B0/Z%C4%B0RAA%C4%B0%20M%C3%9CCADELE/Sebze%20Hastal%C4%B1klar%C4%B1/sebzelerde_septoria_leke_hastaligi.pdf)")

      if ctrl == 'Tomato___Target_Spot':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.hedef1.jpg', width=350)
          with col2:
                st.image('d.hedef2.jpg', width=370)
          st.header('Domates - Hedef Nokta')
          st.subheader('Nedir?')
          st.markdown('Hastalık domatesin diğer mantar hastalıklarına benzediğinden, domates meyvesindeki hedef noktanın erken aşamalarda tanınması zordur. Bununla birlikte, hastalıklı domatesler olgunlaşıp yeşilden kırmızıya döndükçe, meyve, merkezde hedef benzeri halkalar ve kadifemsi siyah, mantar lezyonları olan dairesel noktalar gösterir. Domates olgunlaştıkça "hedefler" çekirdeksiz hale gelir ve büyür. Domates meyvesindeki hedef noktayı kontrol etmek zordur, çünkü toprakta bitki artıklarında hayatta kalan sporlar mevsimden mevsime taşınır.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Büyüme mevsiminin sonunda eski bitki kalıntılarını çıkarın; aksi takdirde sporlar, bir sonraki büyüme mevsiminde artıklardan yeni ekilen domateslere geçecek ve böylece hastalık yeniden başlayacaktır.
                        * Mahsulleri değiştirin ve geçtiğimiz yıl başta patlıcan, biber, patates veya tabii ki domates olmak üzere hastalığa yatkın diğer bitkilerin bulunduğu alanlara domates dikmeyin.
                        * Sabahları domates bitkilerini sulayın, böylece yaprakların kuruması için zamanınız olur. Yaprakları kuru tutmak için bitkinin tabanında su veya bir sağanak hortumu veya damlama sistemi kullanın.
                        2-	Kimyasal Mücadele
                        * Mantar spreyini de önleyici tedbir olarak mevsimin başlarında veya hastalık fark edilir edilmez uygulayabilirsiniz.
                        """)
          st.subheader("Detaylı bilgi için: [gardenjornal](https://tr.gardenjornal.com/10369834-target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes)")
          st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

      if ctrl == 'Tomato___Tomato_mosaic_virus':
          col1, col2 = st.columns(2)
          with col1:
                st.image('d.mozaik1.jpg', width=350)
          with col2:
                st.image('d.mozaik2.jpg', width=370) 
          st.header('Domates - Mozaik Virüsü')
          st.subheader('Nedir?')
          st.markdown('Etmen; hastalıklı bitki artıklarında, yabancı otlarda, bulaşık topraklarda, sigara ve tütün kalıntılarında yaşamını sürdürebilir. Konukçularından ve bunların artıklarından mekanik olarak temasla, boğaz doldurma, koltuk ve uç alma gibi bakım işlemleri sırasında yayılma gösterir. Bulaşık domates bitkilerinde en yaygın belirti tipi; yapraklarda açık yeşil veya sarı düzensiz lekeler ve mozaik desenlerin oluşumudur. Açık yeşil renkli alanlar yapraktaki koyu yeşil renkli alanlardan daha yavaş gelişir. Bunun sonucunda koyu yeşil renkli ısımlar kabararak yaprak yüzeyinde bombeler oluşturur. Bu da yaprağa kıvırcık ve kırışık bir görünüm kazandırır. Bu tip yapraklar sağlıklı yapraklardan daha serttir.')
          st.markdown('Erken dönemdeki enfeksiyonlar genç bitkileri öldürebilir veya bulaşmanın şiddetine bağlı olarak bitkiler bodur kalır. Hasta bitkilerde meyve sayısı azdır. Meyveler normal büyüklüklerine ulaşamazlar. Ayrıca meyvelerde şekil bozuklukları üzerinde kahverengi bölgeler oluşur.')
          st.subheader('Nasıl Mücadele Edilir?')
          st.markdown(""" 
                        1-	Kültürel Önlemler 
                        * Fidelikte ve tarlada şüpheli görülen bitkiler imha edilmelidir.
                        * Fidelikte ve tarlada tütün içilmemelidir.
                        * Kullanılan aletler %5’lik hipolu su ile dezenfekte edilmelidir.
                        * Ekim nöbeti uygulanmalıdır.
                        2-	Kimyasal Mücadele
                        * Çok fazla kimyasal ürün bulunmamasına rağmen; Exirel 100 SE, Superprex, Pestige 250 EC gibi ürünler kullanılabilmektedir.
                        """)
          st.subheader("Detaylı bilgi için: [gardenjornal](https://tr.gardenjornal.com/10369834-target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes)")
          st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

      if ctrl == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
            
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.sarı1.jpg')
            with col2:
                st.image('d.sarı2.jpg')
            st.header('Domates - Sarı Yaprak Kıvırcıklığı')
            st.subheader('Nedir?')
            st.markdown('Bu hastalık beyaz sineklerle taşınmaktadır. Tohumla ve temas ile taşınmaz. Ana konukçusu domatestir.')
            st.markdown('Yaprak kenarlarında ve ayalarında sararmalar oluşturur. Yapraklar küçülür ve kenarlarından kıvrılarak kayık görünümünü alır. Meyveler geç olgunlaşır. Şiddetli bir enfeksiyonda verim kaybı %80’e ulaşır.')
            st.markdown('Hastalık etmeni çift partiküllü geminivirus grubunda yer almaktadır. Gümüşi yaprak beyaz sineği ile persistent olarak taşınmaktadır. İki parçalı DNA kısımları A ve B olarak ikiye ayrılmıştır. Tek sarmal DNA genomunda yaklaşık olarak 2800 nükleotid bulunmaktadır. İzometrik yapılı patiküller 20 nm boyutundadır.')
            st.markdown('Beyaz sineğin etmeni bünyesine alması için 10 – 60 dakikalık bir emgi yapma süresi gerekmektedir. Bünyesine aldığı virüsü nimf döneminden ergin döneme kadar taşımaktadır. Bünyeye alınan virüsün 20 – 24 saatlik bekleme süresine ihtiyacı vardır. Bünyedeki virüs  en fazla 20 gün aktivitesini koruyabilmekte olup bir sonraki nesle aktarılmamaktadır.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Konukçuları')
                st.markdown('Domatesten başka, tütün bitkisi de konukçusudur ancak belirti göstermemektedir. Süs bitkilerinden ise lisiantus konukçusu olup şiddetli belirtiler göstermektedir.')

            with col2:
                st.image('d.sarı3.jpg')
            
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Dayanıklı bitki ve tohum türleri kullanılmalıdır.
                        * Beyaz sinekler ile mücadele edilmelidir.
                        * Yabancı otlar ile mücadele edilmelidir.
                        * Sonbahar ve ilkbahar dikimleri mümkün olduğunca ileri zamana alınmalıdır.
                        * Tuzak bitkilerin kullanılması böceklerin virüsü yaymasını azaltabilir.
                        * Hastalığın yayılmasını engellemek için konukçu bitki olan yerlerde  yetiştiricilik yapılmamalıdır.
                        * Hastalığa dayanıklı bitki çeşitleri tercih edilmelidir.
                        * Seralarda sineklikler kullanılmalıdır.
                        * Vektör böceklerle mücadele teknik talimatlar doğrultusunda yapılmalıdır.
                        2-	Kimyasal Mücadele
                        * Çok bilinen bir kimyasal mücadelesi yoktur.
                        * Bazı durumlarda olgunlaşma döneminden önce sinek ilaçları kullanmanın işe yarayabildiği gözlemlenmiştir.

                        """) 
            st.subheader("Detaylı bilgi için: [yetiştir.net](https://yetistir.net/domateste-sari-yaprak-kivirciklik-virusu/)")
            st.subheader("Detaylı bilgi ve ilaçlar için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/domates-sari-yaprak-kivirciklik-virusu)")







  try:
    prediction(imge)
  except UnboundLocalError:
      st.write('')

def button_one():
    st.header("Tartech'e Hoşgeldiniz;")
    st.markdown("TARTECH'in temel amacı , sahaya gitmeden; imge işleme tabanlı sınıflandırıcı modellerini kullanarak tarımsal ürünlerin kara leke, pas akarı, küllenme, kav, erken ve geç yanıklık gibi 30’a yakın bitki türünü ve hastalığı tahminlemektir. Bunun yanında tarımsal ilaçlama teknikleri kullanılarak erken tedavisinin sağlanıp ekonomik kayıpların önlenmesidir. Bunların dışında bazı sağlıklı bitkiler de tahminlenmektedir. Sağlıklı olan bitkilerin nasıl bakılacağında dair gerekli bilgiler ve daha fazlası aşağıdaki kısımda belirtilmiştir.")
    st.markdown('Tahminleme %81 doğrulukla çalışmaktadır. Tahminleme sayfasında belirtilen yönergelere uygun hareket edilmesi halinde bir sorun yaşanmamaktadır.')
    secim = st.selectbox('Lütfen istediğiniz bitki türünü girin:',('Elma', 'Yabanmersini', 'Kiraz-Vişne', 'Mısır', 'Üzüm', 'Portakal', 'Şeftali', 'Biber', 'Patates','Ahududu','Soya Fasulyesi', 'Kabak', 'Çilek', 'Domates'))
    
    if secim == 'Elma':
        elmas = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı', 'Kara Leke', 'Pas Akarı', 'Siyah Çürüklük'))
        if elmas == 'Sağlıklı':
            
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.sag2.jpg')
            with col2:
                st.image('e.sag1.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Elma ağaçları, serin ve ılıman iklimde yetiştirilmeye uygundur. Bu ağaçlar bol ışıklı ve güneşli ortamları sever.
                        * Nemli ve geçirgen topraklarda kolaylıkla büyüyebilirler. Ülkemizde pek çok yerde çeşitli elma ağaçları bulunur.
                        * Elmanın içeriğinde bulunan vitamin ve mineraller sayesinde hem kozmetik, hem ilaç sektöründe sıkça kullanılıyor.
                        * Elma ağaçları üretimine göre bodur, sarmaşık ve sarkıcı olmak üzere farklı çeşitlerde yetiştirilir.
                        * Elma ağaçları, aşılama, çelik ve kök sürgünleri ile üretilir.""")
            st.subheader('Elma Ağacı Ne Zaman Dikilir?')
            st.markdown('Aşılı kök elma ağacı fidanları, yaprak dökümü ile birlikte genellikle Kasım ayının 1. ya da 2 haftasından itibaren rakıma, bölgeye ve iklim şartlarına göre Nisan sonuna kadar ekilebilir. ')
            st.subheader('Nasıl Yetiştirilir ve Budanır?')
            st.markdown('Elma dünyanın her bölgesinde yetişen ve yaygın olarak ulaşılabilen bir meyvedir. Dünyada yaklaşık 7500 farklı elma çeşidi bulunur. Elmaların sağlıklı şekilde büyümeleri için uygun sıcaklığa ve toprağa sahip olması önem taşır. Elma bitkisinin 7 derece altında 1000 saat kadar bir soğuklanma süresine sahip olması, meyve üretimini artırır ve hızlandırır.')
            st.markdown('Fazla soğuğa gelmeyen elma bitkileri, 20 - 26 derece arası sıcaklıklarda ideal olarak yetişir. Elmanın olgunluk döneminde yağış olaylarının gerçekleşmesi meyve sağlığını olumsuz etkiler. Her çeşit toprakta yetişebilen elma, fazla rüzgarı ve sert hava koşullarını sevmez. Ticari elma yetiştiriciliğinde toprağın yabani otlardan temizlenmesi, havalandırılması ve gübrelenmesi ile birlikte uygun sıcaklık ve güneş ışığının bulunması elmaların sağlıklı ve bol olmasını sağlar.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Tohumdan Elma Yetiştirme Tekniği')
                st.markdown("""
                        * Olgun elma tohumlarını toplayın. 
                        * Bu toplanan tohumları kağıt havlu gibi nemlendirilmiş bir yatak içine koyun
                        * Daha sonra, nemli peçeteleri plastik bir torba içerisinde, uyuşukluklarını kırmak için yaklaşık 30 ila 50 gün boyunca buzdolabı içerisinde bekletin.
                        * Buzdolabından çıkardığınız tohumları toprağa ekin
                        * Elma filizleri göründüğünde, saksınızı güneşli ve açık alana taşıyın, böylece daha hızlı büyüyebilirler
                        * Elma bitkisinin iyi gelişimi için düzenli olarak sulayın. 
                        """)
            with col2:
                st.image('e.sag3.jpg', width=300)
            st.subheader('Nerede Yetiştirilir')
            st.markdown("Batı Asya kökenli olan elma, tarihçede Asya'dan Akdeniz'e ve Batı Avrupa'ya yayılmıştır. Ilıman iklim koşullarının olduğu her ülkede yetişebilen elma, -30 dereceye kadar soğuklara dayanabilir. Dünyada muz üretiminden sonra ikinci sıra gelen elma, her ekonomik seviyede olan bir meyvedir. Bu nedenle herkesin kolayca ulaşabileceği bir meyvedir.")
            
            st.subheader("Detaylı bilgi için: [Hürriyet](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")
            st.subheader("Detaylı bilgi için: [Çiçek Bakım Evi](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")
            st.subheader("Detaylı bilgi için: [Sakarya Üniversitesi](https://www.hurriyet.com.tr/mahmure/elma-agaci-nedir-nerede-ve-nasil-yetisir-elma-agaci-ozellikleri-bakimi-ve-faydalari-hakkinda-bilgi-41770457)")

        elif elmas == 'Kara Leke':
            
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.karaleke1.jpg')
            with col2:
                st.image('e.karaleke2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Elma kara leke hastalığı, temelde bir mantar hastalığıdır. Hastalığın belirtileri ağacın yaprak, meyve ve sürgünlerinde görülür. Yaprağın üst ve alt yüzeyinde oluşan lekeler başlangıçta yağlımsı görünümdedir, giderek zeytin rengini alır ve daha sonra kahverengileşir.')
            st.markdown('Lekeler kadifemsi yapıdadır ve bu kısımdaki dokular zamanla ölür, üzerinde çatlaklar ve delikler oluşur. Ağır hastalıklı yapraklar erkenden sarararak dökülürler. Meyvelerdeki lekeler yeşilimtırak olup zamanla kahverengine dönüşür. Küçük lekeler zamanla birleşirler ve bu kısımlarda meyvenin gelişmesi durduğu için şekilsiz meyveler oluşur.')
            st.markdown('İklim koşullarının, askosporların bırakılması ve enfeksiyon riski üzerindeki etkisi üzerine yapılan araştırmaya dayanarak bir karar destek sistemi oluşturulmuştur. Bu sistem üreticileri, elverişli dönemler ve ne zaman beklenecekleri konusunda uyarır. Aksosporlar şiddetli yağmur sırasında serbest kalır. 6°C ile 26°C arasında çimlenirler. 18°C ve 24°C arasındaki ideal sıcaklıklarda sadece 9 saatlik yaprak ıslaklığı gereklidir; düşük sıcaklıklarda enfeksiyonun başarılı olması için bu süre, 12-28 saate çıkar. Konidyumların da çimlenme için suya ihtiyacı vardır.')
            st.subheader('Zarar Belirtileri')
            st.markdown('İlk önce tomurcuklarda, yapraklarda, yaprak saplarında ve meyvelerde, bazen de dal ve tomurcuk pullarında lezyonlar olarak kendini gösteren elma kara lekesi hastalığına neden olur. Lezyonlar zeytin yeşilidir. Sporlar oluştuğunda, lezyonlar gri ve kabarık hale gelir. Askosporların neden olduğu lezyonlar daha sınırlıdır; konidyumların neden olduğu lezyonlar ise daha hızlı uzar ve birleşebilirler. Enfekte meyve ve yapraklar olgunlaşmadan düşebilir. Bitkilerin savunma mekanizması, mantarın dokuları daha fazla istilasını önlemek için lezyonların etrafında mantarımsı halkalar oluşturmaktır. Geç meyve enfeksiyonu sadece, hasattan önce farkedilemeyebilecek olan küçük koyu lezyonlara neden olur.')
            st.markdown('İlkbaharda yaprakların ve genç meyvelerin ilk enfeksiyonları erken hastalık olarak isimlendirilir. Geç hastalanmalardan ise hemen hemen yetişkin meyvelerin hastalanması anlaşılır. Erken hastalanmalarda lekeler küçük ve meyveler üzerinde yarıklar bulunmaz. Eğer hastalık, meyveler depolandıktan sonra görülürse depo kara lekesinden söz edilir. Bazen bir yıllık sürgünler de hastalanır. Bunlara ***sıracalı dallar*** denir. Sıracalı dallar elma kara leke hastalığında armutta ki gibi büyük bir öneme sahip değildir. Fakat bazı elma çeşitlerinin fazla duyarlı oluşları nedeniyle, çok sayıda sıracalı dallar meydana gelir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1 - Kültürel Önlemler
                        * Sonbaharda yere dökülmüş yaprakları temizlemek, yakmak
                        * Sıracalı dallar budanmalı
                        * Ağaçlar, yapraklardaki nemin daha hızlı kuruyabilmesi için hava akımına izin verecek şekilde taçlandırılmalı ve uygun aralıklar ile dikilmelidir.
                        2 - Kimyasal Tedavi
                        * 1. İlaçlama: Çiçek gözleri kabardığında (dal sıracası bulunan yerlerde ise 3-5 gün önce yapılır)
                        * 2. İlaçlama: Pembe çiçek tomurcuğu döneminde (çiçekler ayrı ayrı görüldüğünde)
                        * 3. İlaçlama: Çiçek taç yaprakları %70-80 oranında döküldüğünde
                        * 4. ve diğer ilaçlamalar: Hastalığın ilerlemesi le paralel olarak ve mantarın etki süresi dikkate alınarak.
                        * İlaçlama sırasında kullanılan Pestisitlerin elmada kara leke için ruhsatlı olmasına ,yetkili kişiler tarafından reçete edilmesine ,son kullanım tarihinin geçmemiş olmasına ve uygun dozda kullanılmasına dikkat edilmelidir.
                        """)
            st.subheader("Detaylı bilgi için: [tarimorman.gov](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/489)")
            st.subheader("Detaylı bilgi için: [koppert](https://www.koppert.com.tr/sorunlar/hastalik-kontrolue/elma-kara-lekesi/)")

        elif elmas == 'Pas Akarı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.pasakarı2.jpg')
            with col2:
                st.image('e.pasakarı1.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Pas Akarı canlısı, iğ şeklinde, sarımsı kahverenginde ve uzunluğu 0.16-0.18 mm’dir. İki çift bacaklı ve gözle görülemeyecek kadar küçüktür.')
            st.markdown('Kışı ergin dişi döneminde, gevşek yapılı ağaç kabukları altında, tomurcuklara yakın yarık ve çatlaklarda, sürgünlerde, tomurcuk pulları altında gruplar halinde geçirir. Tomurcukların patlamasıyla ortaya çıkan zararlı, gelişmekte olan çiçekler ve yaprak dokusu üzerinde beslenmek amacıyla, ayrılan çiçek tomurcuklarına saldırır ve aynı zamanda kabarmakta olan odun gözlerine de geçerler. Mayısta ortaya çıkan erkek ve yazlık dişi bireyler çiftleştikten sonra, dişiler yumurtalarını çiçek tomurcukları ile odun gözlerinin yeşil aksamı üzerine bırakırlar. Çiftleşmeleri ilkbahar ve yaz süresince devam eder ve döller birbirine karışır.')
            st.subheader("Pas Akarının Zararlı Olduğu Bitkiler")
            st.markdown('Öncelikle elmada yaygın olarak bulunur. Armutta da zarara neden olabilir.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Pas Akarı Zarar Şekli')
                st.markdown("""
                        * Zararlı, yaprakların alt yüzünde keçeye benzer düzensiz şekli bozukluğuna neden olur, yaprakların alt yüzü donuk ve solgun, benekli bir görünüm alır.
                        * Akar ile yoğun olarak bulaşık yapraklar gümüşi bir renk alır ve daha sonra pas rengine veya kahverengine dönebilir.
                        * Şiddetli zarar görmiş yapraklar zamanla kuruyup büzülür, ağacın sürgün gelişimi zayıflar
                        * Bazen de zararlı, meyvelerde paslanma meydana getirerek, meyvenin pazar değerinin düşmesine neden olabilir.""")
            with col2:
                st.image('e.pas3.jpg')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Biyolojik Mücadele
                        * Doğal düşmanların korunması ve etkinliklerinin arttırılması için diğer zararlılarla mücadelede kimyasal mücadeleye alternatif metotlara öncelik verilmeli, eğer kimyasal mücadele gerekiyorsa, doğal düşmanlara yan etkisi en az olan bitki koruma ürünleri tercih edilmelidir.
                        2-	Kimyasal Tedavi
                        * Elma Pas Akarları’nın mücadelesine karar vermek için çiçeklenme öncesi ve çiçeklenme sonrası kontroller gereklidir. Mayısta 100 yaprakta yapılan sayımlarda yaprak başına ortalama 300-400 akar, ağustos ve eylül aylarında ise yaprak başına ortalama 700- 1000 akar bulunursa ilaçlama yapılır. Sayımlar, hazirandan başlayarak sürgünlerin uçtan itibaren 1/3’lük kısmındaki yapraklarda akar fırçalama aleti ile yapılır. Genellikle Acrinathrin 22,5 g/l+ Abamectin 12,6 g/l etken maddeli ürünler tercih edilmelidir.
                        """)
            st.subheader("Detaylı bilgi için: [tarimorman.gov](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/524)")
            st.subheader("Detaylı bilgi için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/elma-pasakari)")

        elif elmas == 'Siyah Çürüklük':
            col1, col2 = st.columns(2)
            with col1:
                st.image('e.siyahcurukluk2.jpg')
            with col2:
                st.image('e.sç3.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Elmada siyah çürüklük, Alternata fungal etmeni neden olmaktadır. Etmen, bitkinin zayıflamış veya ölmüş dokularında küçük yara izleri olarak yaşayabilmektedir.')
            st.markdown('Yaygın olarak her yerde bulunabilmektedir. Hastalığın gelişimi nemli ortam ve 26-28°C sıcaklıkta olmakla birlikte, 0°C’de dahi gelişme gösterebilmektedir. 8-10 gün içinde belirtiler ortaya çıkmaktadır. Hastalık çoğunlukla hasat öncesi ve sonrası meyve çürümelerine neden olur. İlk belirtiler, elmanın çiçek çukuru etrafında veya orta kısmında önceleri renk açılması şeklinde gerçekleşir. Daha sonra bu kısımlarda yassı ve kenarları belirgin şekilde çökük, kahverenginden siyah renge dönüşen lekeler gözlenir. Hastalıklı kısımdan kesit alındığında bu lekelerin altında meyve etinden çekirdeğe doğru derinlemesine ilerleyen çürümekte olan bölgeler görülür.')
            st.markdown('Meyvelerde meydana getirdiği zarar ile de direkt kayıplara neden olmaktadırlar. Hastalık etmeni genelde saprofit bir hastalık etmeni olup, hasat sonrası ya da olgun meyvelerde görülür ve yaralardan bitkilere girerek meyvelerin çürümesine neden olur. Hastalık etmeni başlangıçta, yani meyveler olgunlaşmadan önce özellikle meyvelerin çiçek uç noktalarına ve gövdelerine kolonize olmaktadırlar. Meyveler olgunlaşırken ya da hasat sonrası enfeksiyonlarını başlatırlar. Fungal etmen kış gibi olumsuz koşulları yere dökülen yapraklarda, dormant gözlerde ve gövde ya da dallardaki yaralarda geçirmektedir. Başlangıç enfeksiyonları geç bahara doğru ortaya çıkar ve sekonder enfeksiyonlar ise sıcak, yağışlı ve nemli geçen havalarda meydana gelir. Enfeksiyonlar 20-24°C gibi uygun olan sıcaklıklarda 5-6 saat içerisinde gerçekleşmektedir. Hastalık etmeni başlangıçta ya da hasattan önce enfektelenir, fakat meyvelerde herhangi bir enfeksiyona neden olmaksızın çiçek ucu ya da sap kısımlarında dormant olarakkalır. Hastalıktan etkilenen meyvelerin lekeleri üzerinde fungusun grimsi ya da daha koyu pamukumsu miselleri gelişir ve burada oluşan konidi sporları tekrar yeni enfeksiyonlara neden olmaktadır.')
            st.subheader('Siyah Çürüklüğün Görüldüğü Bitkiler')
            st.markdown('Etmenin konukçuları elma ve armuttur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Meyvelerin elle toplanmasında dikkatli olunmalı, toplama ve paketleme esnasında meyveler ezilmemelidir.
                        * Depolama atmosferi ve sıcaklığı uygun olmalı, meyvenin muhafazası optimum şartlarda olmalıdır.
                        * Toplama yapılacak olan kasa veya sepetin yüzeyi uygun bir dezenfektan ile temizlenmeli veya meyve kasalara konmadan önce buhardan geçirilmelidir.
                        2- Kimyasal Tedavi
                        * 1. İlaçlama: Meyve Tatlanma başlangıcında
                        * 2. İlaçlama: İlacın etki süresi ve hasat süresine dikkat edilerek yapılacak ilaçlamalar. Genellikle Trifloxystrobin etken maddelli ilaçlar kullanılabilir.

                        """)
            st.subheader("Detaylı bilgi için: [tarimorman.gov](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/709)")
            st.subheader("Detaylı bilgi için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/elmada-alternaria-meyve-curuklugu)")

    if secim == 'Yabanmersini':
        yabans = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı',''))
        if yabans == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('y.sag1.jpg')
            with col2:
                st.image('y.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Ülkemizde yaban mersininin dört farklı türü görülüyor.
                        * Sonbahar sonunda veya ilkbahar başında 30-40 cm derinliğinde çukurlara dikilen ekinlerin kökleri ince olduğu için dikim sonrası kuru bırakılmaması önem arz ediyor. Bitki dikildikten sonra etrafına 10-15 cm kalınlığında malç seriliyor. Yaban mersini yetiştiriciliğinin 1 sene kadar öncesinde toprağın hazırlanması öneriliyor.
                        * pH değeri dengelenmesi için dikimden 6 ay kadar önce kükürt uygulamasının tamamlanması gerekiyor. Dikim sırasında sıra üzerinde 1.0-1.5 metre, sıra arasında 1.5-3.0m mesafe bırakılıyor. """)
            st.subheader('Yaban Mersini Nerede Yetiştirilir?')
            st.markdown('Ocak şeklinde görünümü olan maviyemiş, dip kısmından yeni sürgünler vererek odunsu çalı formunda büyüyor. Sırık şeklindeki sürgünler 10 ile 20 yıl arasında yaşıyor. Yüksek boylu çalı türleri 120 -130 cm boya ulaşabiliyor. Tozlanma için arı gibi böceklere ihtiyaç duyuyor. Çiçeklenme genellikle bitki üzerinde 3-4 hafta sürüyor. Genellikle nisan-mayıs gibi çiçeklenen yaban mersininin çiçeklerinin %80 kadarı meyveye dönüyor. Samsun Tarım İl Müdürlüğü Dergisi’nde yer alan makaleye göre, her yıl ilkbahar öncesi gözler uyanmadan budanan bitkiler, diğer ekinlere göre çok daha az budamaya ihtiyaç duyuyor. Yabancı ot temizliği de yaban mersini yetiştiriciliği için oldukça önemli görülüyor. Temmuz ayıyla başlayan hasat ise genellikle eylül ayı sonuna kadar devam ediyor')
            st.subheader('Hangi mevsimde ne zaman yetiştirilir?')
            st.markdown('Yaban mersini çeşidine bağlı olarak 4 ile 12 hafta arasında olgunlaşıyor. Genellikte yaz ortasından sonra, yaz sonunda hasada başlanıyor.')
            st.subheader('Kaç günde bir sulanır?')
            st.markdown('Mavi yemişlerin olgunlaşma mevsimi uzun olduğu için hasat süresi boyunca 10 günlük aralıkla 2-3 kez sulama yapılıyor. Sulama için hem damla sulama hem de yağmurlama sulama kullanılabiliyor.')
            st.subheader("Detaylı bilgi için: [yabanmersini.org](https://www.yabanmersini.org/yabanmersini-yetistiriciligi.html)")
            st.subheader("Detaylı bilgi için: [tarfin](https://tarfin.com/blog/yaban-mersini-yetistiriciligi-nasil-yapilir)")

    if secim == 'Kiraz-Vişne':
        kirvis = st.selectbox('Geçerli bir hastalık girin:',('Sağlıklı','Küllenme'))
        if kirvis == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('k.sag1.jpg')
            with col2:
                st.image('k.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Kiraz ve vişne ağaçları 4 yaşında iken budama işlemi yapılır. Budama aletinin iyice temizlenmesine dikkat edilmelidir. Makasın keskin olmaması gerekmektedir. Ağacın ömrünü tamamladığında zaman kök budaması yapılarak, gençleştirme yapılır ve  ağaç yenilenir.
                        * Budama sonrası mutlaka ilaçlama yapılmalıdır.
                        * Toprak analizi yapıldıktan sonra gübreleme işlemi yapılır. Mart ayında hayvan gübresi ile yapılan  ağaçların gübrelenmesi işlemi ile gerekli vitaminler sağlanır. Şubat ayında komposit gübre yapılır.
                        * Her yıl bahar aylarında toprağın havalandırma işlemi yapılır. Çiçekler açmadan önce çapa ile çapalanması önemli bir noktadır. Sonbahar geldiğinde de hasat sonrasında havalandırma yapılır.
                        * Hasat zamanı önemlidir. Meyve toplama aşamasında yapraklara ve dallara zarar verilmemesi gerekir. Özellikle göz kısmının koparılmaması önemlidir.
 """)
            st.subheader('Nasıl Yetiştirilir?')
            st.markdown('Kiraz ağaçları kış aylarında belirli bir süre dinlenmeyi, çiçeklenmeyi ve hasadı seven bir meyve ağacıdır. Üretimi en erken olabileceği gibi çok geç zamana kadar yayılan bir yetiştirme zamanına sahip bir ağaçtır.')
            st.markdown('Kiraz genelde çok düşük ve fazla yüksek sıcakları sevmez. Kiraz ağacı soğukların -20 ve -25 derece altında olduğu bölgelerde yetiştirme yapılmamalıdır. Donlar ağaçlara zarar vermektedir.')
            st.subheader('Kaç günde bir sulanır?')
            st.markdown('Düzenli bir şekilde yılda 600 mm üzerinde yağış olan bölgelerde kiraz ağacının sulanmasına ihtiyaç yoktur. Fakat 600 mm altında yağış alan bir yerde ise yaz aylarında 2-3 defa sulanması yeterlidir. Tabii ki bozuk olmayan topraklar da bu sulama sistemi geçerlidir. Topraklar bozuldukça, su tutmadığı için daha fazla su istemektedir ve masrafları da artmaktadır.')
            st.subheader("Detaylı bilgi için: [cicekal](https://www.cicekal.net/blog/kiraz-agaci-bakimi/)")

        elif kirvis == 'Küllenme':
            col1, col2 = st.columns(2)
            with col1:
                st.image('vk.küllenme1.jpg')
            with col2:
                st.image('vk.küllenme2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Halk arasında basıra adıyla da anılan bir mantar hastalığıdır. Nemli ortamlarda daha sık rastlanan hastalık, yağmurdan, çiğden sonra hızlı yayılma özelliği gösterilmektedir. Alt yapraklardan ilerleyerek kısa sürede tüm ekini saran külleme, taze yaprak ve sürgünleri de etkisi altına alabilmektedir. Yapraklarda un serpilmiş gibi puslu ve tozlu bir görünüm yaratılır. Beyazlayan yapraklarda öbek öbek kümelenme görülmektedir.  Lekelenme artarak yaprağın ve ekinin tüm yüzeyini kaplayabilir.  Canlı bitki hücrelerinden beslenen mantarlar, yaşayan bir mahsül bulamadığında hayatta kalamıyor, müdahale edilmediğinde canlı bitkinin her yerini sarmaktadır. Bulaşıcı bir hastalıktır.')
            st.markdown('Belirti olarak; çiçek açmama görülür, yaprak ve meyve dökümü göze çarpar, zayıflama ve dökülme gerçekleşir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bahçelerin bakımlı tutulması gerekmektedir.
                        * Budama yapılması, fazla dalların çıkarılması ağacın yapraklarının güneş ve hava almasını sağlayarak yayılımı azaltıyor.
                        * Yılda iki kez dip sürgünlerin alınması gerekiyor.
                        * Yabancı ot temizliği önem taşıyor.
                        * Dökülen enfekte yaprakların tırpanla toplanması, yakılarak imha edilmesi önerilir.
                        2-	Kimyasal Tedavi
                        * Hastalık görüldüğü tarihten itibaren 10 günde bir ilaçlama uygulanmalıdır.
                        * Hastalığın üst taraflara ilerlediği durumda, bayrak yaprağa bulaşın önlenmesi için yeşil aksamın ilaçlanmasına başlanıyor. İlaçlar, önerilen dozlarda yaprak alt ve yüzlerini kaplayacak şekilde uygulanıyor. Genellikle peptisit etkili ilaçlar kullanılmalıdır.
                        * 1. ilaçlama çiçeklenme başlangıcında (% 5-10 çiçekte)
                        * 2. ilaçlama tam çiçeklenmede (% 90-100 çiçekte) yapılır
                        * Kirazda meyve monilyasına karşı; meyvelere ben düştüğünde tek bir ilaçlama yapılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [tarfin](https://tarfin.com/blog/kulleme-hastaligi-nedir-nasil-mucadele-edilir)")
            st.subheader("Detaylı bilgi için: [tarimorman.gov](https://kutuphane.tarimorman.gov.tr/vufind/Record/1172235/UserComments)")

    if secim == 'Mısır':
        misirs = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı','Cercospora (Yaprak Lekesi Hastalığı)', 'Paslanma', 'Yaprak Yanıklığı'))
        if misirs == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.sag1.jpg')
            with col2:
                st.image('m.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Toprak havasızlığı mısır yetiştiriciliğinde sorun oluşturuyor. 
                        * Besince zengin, pH’sı 5 ile 8 arasında değişen verimli topraklarda rahatlıkla mısır dikimi yapılabiliyor. 
                        * Çimlenme sıcaklığı 8 ile 10 derece arasında hesaplanıyor. Yüksek sıcaklıklarda (18-20) tohumların çimlenmesi ve çıkışı daha hızlı oluyor. Uygun büyüme sıcaklığı ise 20 ile 30 derece arasını gösteriyor. 
                        * Mısır üretimi için nemli bir tohum yatağı önem taşıyor. İyi bir tohum yatağı hazırlamak için toprak önce pulluk ile 8-10 cm, sonra sonbaharda 18-20 cm derinlikte, iki kez sürülüyor. 
                        """)
            st.subheader('Nasıl Yetiştirilir?')
            st.markdown('Toprakta bol su isteyen mısır, özellikle sapa kalkma ve çiçeklenme dönemlerinde çok su tüketiyor. Eğer doğal yağışlarla su karşılanmıyorsa sulama suyu ile destek verilmesi gerekiyor.  Susuz mısır üretimi, çok yağış alan bölgelerde nadiren yapılabiliyor. Ülkemizde susuz tanelik mısır yetiştiriciliği Karadeniz’de gerçekleştiriliyor. Topraktaki faydalı su oranı %50’nin altına düştüğünde tarlanın sulanması gerekiyor. Mısır yetiştiriciliği sırasında en az 4 kez sulama yapılıyor. İlk sulama, birinci ara çapası sonrası, ekin boyu 10-15 cm’ye geldiğinde yapılıyor. İkinci sulama boğaz doldurmanın ardından, üçüncü sulama tepe püskülü çıkmadan 4-5 gün önce, dördüncü sulama ise süt olum devresinde gerçekleştiriliyor. ')
            st.subheader("Detaylı bilgi için: [link](https://tarfin.com/blog/misir-yetistiriciligi-nasil-yapilir)")
            
        elif misirs == 'Cercospora (Yaprak Lekesi Hastalığı)':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.yapraklekesi1.jpg')
            with col2:
                st.image('m.yapraklekesi2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalığın etmeni Cercospora beticola mantarıdır. Mantarın zararı pancar yapraklarının sürekli lekelenip ölmesi ve bitkinin yeni yapraklar sürmesi şeklindedir. Sonuçta bitkilerin kök büyümesi ve şeker biriktirmesi önemli ölçüde geriler. Hastalığın başlangıcı ve gelişmesi, o yılın sıcaklık ve yağış ortalamaları ile direkt olarak ilintilidir. Hastalık genellikle bölgelerin rakımına göre değişmekle birlikte Haziran başı ile Temmuz ortasında bitkinin ilk olarak yaşlı yaprakları üzerinde görülmeye başlar.')
            st.markdown('İlerleyen dönemlerde sıcaklık ve rutubetin artmasıyla birlikte yaprak üzerindeki lekeler aniden artarak yüzeyin tamamını kaplar. Lekeyle kaplanan yapraklar peyderpey kuruyup ölür. Ağır bulaşıklık durumunda yaprakların çoğu ölür ve bu durumda bitki yeni yapraklar sürmek zorunda kalır. Bu taze yapraklar da sürekli olarak hastalığa yakalanıp ölür ve bitkinin şeker kaybetmesine sebebiyet verir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Çok kısa aralarla mısır üretiminden kaçınılmalıdır
                        * Silo yerlerinde, bu mantarlara depo görevi yapan bitki artıkları bırakılmamalıdır.
                        * Yaprak hastalıklarına toleranslı çeşitler ekilmelidir (Özellikle Cercospora görülen bölgelerde)
                        2-	Kimyasal Tedavi
                        * Bölgelere göre değişmekle beraber, 1-3 ilaçlama gerekebilir. Her ilaçlamada farklı etkili maddeli fungisitlerin kullanılması ve sezon içinde ilaçlamaların geç dönemde yapılmaması çok önemlidir.

                        """)
        elif misirs == 'Paslanma':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.yaprakpası1.jpg')
            with col2:
                st.image('m.yaprakpası2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Mısır bitkisinde üç önemli yaprak pası yaygın olarak görülmektedir. Bunlar Adi Pas, Polysora Pası ve Tropik Pas’tır. Bunlar bitkilerin tepe püskülü çıkmasına yakın bir dönemde çok belirgin olarak görülür. Adi Pas (P. sorghi) yaprakların her iki yüzünde tozlu bir görünüme sahip küçük kahverengi püsçüller meydana getirir. Daha sonra epidermis yırtılır ve bitki olgunlaştığında bu püsçüller siyahlaşır.')
            st.markdown('Polysora spp’nin meydana getirdiği püsçüller adi pasta meydana gelene göre daha açık renkli ve daha yuvarlaktır. Bitkiler olgunlaştıkça püsçüllerin renkleri daha koyulaşır. Bu pas türünde de püsçüller yaprağın her iki yüzünde meydana gelir. Epidermisin yırtılması ise adi pasta olduğundan daha geç olur.')
            st.markdown('Tropikal pasın püskülleri yuvarlak ile oval arasında değişen şekillerde ve küçük yapılı olup, epidermisin altında meydana gelir. Püskülün ortası beyazdan sarıya kadar değişen renkler alabilir. Ayrıca bir de delik görülür. Püskül bazen kararır fakat ortası açık renkliliğini korur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bahçelerin bakımlı tutulması gerekmektedir.
                        * Budama yapılması, fazla dalların çıkarılması ağacın yapraklarının güneş ve hava almasını sağlayarak yayılımı azaltıyor.
                        * Yılda iki kez dip sürgünlerin alınması gerekiyor.
                        * Yabancı ot temizliği önem taşıyor.
                        * Dökülen enfekte yaprakların tırpanla toplanması, yakılarak imha edilmesi önerilir.
                        2-	Kimyasal Tedavi
                        * Hastalık görüldüğü tarihten itibaren 10 günde bir ilaçlama uygulanmalıdır.
                        * Hastalığın üst taraflara ilerlediği durumda, bayrak yaprağa bulaşın önlenmesi için yeşil aksamın ilaçlanmasına başlanıyor. İlaçlar, önerilen dozlarda yaprak alt ve yüzlerini kaplayacak şekilde uygulanıyor. Genellikle peptisit etkili ilaçlar kullanılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [cropscience](https://www.cropscience.bayer.com.tr/turkiye/tarim-haberleri/misir-hastaliklari.html)")
            st.subheader("Detaylı bilgi için: [dergipark](https://dergipark.org.tr/download/article-file/40861)")
        elif misirs == 'Yaprak Yanıklığı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('m.yaprakyanıklığı1.jpg')
            with col2:
                st.image('m.yaprakyanıklığı2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Yaprak yanıklığı, yaprak, kın, koçan yaprağı, koçan sapı ve koçanda bulunabilir. Belirtiler hastalığın ilk evrelerinde baklava dilimini andıran küçük lekeler iken hastalık ilerledikçe bu lekeler büyür ve boyutları 2-3 cm’ye kadar ulaşabilir. Etmen ayrıca fide döneminde kök çürüklüğü ve solgunluğa da neden olabilir. Hastalık ılıman (20-32°C) ve nemli bölgelerde görülmektedir. 18-27°C ve nemli havalar hastalık gelişimini teşvik ederken kuru havalar ise engeller. Etmen kışı mısır artıkları veya mısır tanelerinde miselyum ve spor olarak geçirir.')
            st.markdown('Bitkilerin hastalığa duyarlı devresi olan tozlanma döneminde ağır enfeksiyonlar meydana getirir. Hastalık bu dönemden önce ortaya çıkmışsa %50’ye varan verim kayıplarına sebep olabilir.')
            st.markdown('Hastalığa karşı tercih edilen dayanıklı çeşitler, uygulanan ekim nöbeti, tarladaki hastalıklı bitki artıklarının temizliği, toprak analizi sonucu ve gübre kullanımı gibi birçok kültürel mücadele bulunmaktadır. Gerekli durumlarda kimyasal mücadele önerilebilir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalığa dayanıklı çeşitler ekilmeli
                        * Ekim nöbeti uygulanmalı
                        * Gerekli dönemlerde gübreleme yapılmalı
                        * Hastalıklı bitkiler temizlenmeli
                        2-	Kimyasal Tedavi
                        * Bu hastalığa karşı pek fazla kimyasal mücadele uygulanmamaktadır. Fakat kimyasal savaşta pyraclostrrobin, epoxiconazole+ pyraclostrrobin ve , epoxiconazole + carbendazim önerilebilir.

                        """)
    
    if secim == 'Üzüm':
        uzums = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı', 'Kara Çürüklük', 'Kav', 'Yaprak Yanıklığı'))
        if uzums == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('u.sag3.jpg')
            with col2:
                st.image('u.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Üzüm bağlarında mutlaka, kış budaması yapılmalıdır. Budama amatör kişiler tarafından değil işinin uzmanı kişiler tarafından doğru bir şekilde yapılmalıdır.
                        * Bağlarda toprak işlemesi, sonbahar ve ilkbahar aylarında yapılmalı ve bağlarda yabani otların büyümesine engel olunmalıdır.
                        * Bağlarda gübreleme yapılmalıdır. Gübreleme, için mutlaka toprak analizi yapılmalı ve bu doğrultuda toprağın ihtiyaç duyduğu vitamin ve mineral takviyesi yapılmalıdır.
                        * Üzüm bağlarında sulama için su kontrolleri sağlayan cihazlar kullanıldığı takdirde toprağın suya ihtiyaç duyduğu anlarda toprak sulaması yapılmalıdır.
                        * Üzüm  bağlarında yaz budaması için doğru ay belirlenmeli ve budama yapılmalıdır.
                        * Bağlarda hastalıklara karşı ve böceklere karşı ilaçlama yapılmalıdır. Bunun için böcek cinsi tespit edilmelidir.                        """)
            st.subheader('Üzüm bağlarına kükürt ne zaman atılır?')
            st.markdown('Birçok meyve yetiştiriciliğinde olduğu gibi kükürt, üzüm bağları içinde oldukça gerekli bir vitamindir. Kükürt eksikliği ise şu şekilde anlaşılır; toprakta kireçlenme, besin değerinin düşmesi, enerji düşüklüğü yaşandığı zaman, protein eksikliğinde ve aminoasit yetersizliğinde, bitkide herhangi bir hastalık tespit  edildiğinde,  tuz oranının yükseldiği zaman ve buna bağlı etmenlerin arttığı dönemlerde üzüm bağlarına kükürt takviyesi yapılmalıdır. Kükürt, üzüm bağları için ilkbahar aylarının başlarında uygulaması yapılmalıdır. Toprağın kükürte ihtiyaç duyup duymadığı ise toprak analizleri soncunda meydana çıkar.')
            st.subheader("Detaylı bilgi için: [link](https://www.cicekal.net/blog/uzum-agaci-bakimi-nasil-yapilir/)")

        elif uzums == 'Kara Çürüklük':
            col1, col2 = st.columns(2)
            with col1:
                st.image('u.karaçürüklük1.jpg')
            with col2:
                st.image('u.karaçürüklük2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Üzüm kara çürüklüğü , sıcak ve nemli havalarda üzüm asmalarına saldıran temelde bir mantar hastalığıdır. Hastalık bitkinin sürgünler, yaprak ve meyve saplarına da yansır.')
            st.markdown('Hastalık döngüsü kışlayan yapılarla başlar. İlkbahar yağmurları, kışlayan yapılarda bulunan larvalaşmış mantarları serbest bırakır ve bu sporlar rüzgar ve yağmur sıçramasıyla yapraklara, çiçeklere ve genç meyvelere bulaşmak üzere yayılır. Yerdeki bazı mumyalarda, tomurcukların kırılmasından yaklaşık iki ila üç hafta sonra başlayan ve çiçeklenmenin başlamasından bir ila iki hafta sonra olgunlaşabilir. Nem varlığında, bu mantarlar yavaş yavaş filizlenir, 36 ila 48 saat sürer, ancak sonunda genç yapraklara ve meyve saplarına nüfuz eder. Enfeksiyonlar 8 ila 25 gün sonra görünür hale gelir.')
            st.markdown('Meyvenin enfeksiyonu, hastalığın en ciddi aşamasıdır ve önemli ekonomik kayıplara neden olabilir. Enfekteli meyveler önce açık renkli veya çikolata kahverengisi görünür; kuş gözü gibi çok yuvarlak görünen bir yeri olacak. Bu nokta büyüyecek ve daha fazla meyve salkımına ve daha fazla bitkiye bulaşacaktır.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Üzümün yetiştirileceği bölge için doğru üzüm çeşidinin seçilmesidir. Üzüm çeşitleri, hastalık kara çürüklüğü hastalığındaki farklılıklar da dahil olmak üzere, hastalıklara duyarlılıkları bakımından farklılık gösterir. Bazı çeşitler daha az hassastır, diğerleri ise doğru çevre koşulları oluştuğunda hastalığa daha yatkındır.
                        * Uygun bir budama tekniği, hastalıkları sınırlamak için başka bir kültürel kontrol yöntemidir. Her asmayı uyku döneminde her yıl budayın. Bu hareketsiz budama, dengeli budama terimini sağlamak için yoğun bir şekilde araştırılmıştır.
                        2-	Kimyasal Tedavi
                        * Kimyasal uygulamaları uygulamak için mantar ilacı etiketine bakın. Uygulama nedeniyle mantar ilacının kaymasını ve verimsizliklerini önlemek için koşulların püskürtmek için en uygun olduğundan emin olun. Mantar ilacı kurallarına uyulmalıdır. Hem normal hem de organik yetiştiriciler için çok çeşitli kimyasallar mevcuttur. Ticari olarak maliyetli olabilir.
                        """)
            st.subheader("Detaylı bilgi için: [tarfin](http://www.tarimkutuphanesi.com/baglarda_kav_(esca)_hastaligi_00727.html#:~:text=Kav%20hastal%C4%B1%C4%9F%C4%B1%20asman%C4%B1n%20tamamen%20kurumas%C4%B1na,yapraktaki%20ve%20odun%20dokusundaki%20belirtisi.)")

        elif uzums == 'Kav':
            col1, col2 = st.columns(2)
            with col1:
                st.image('u.kav1.jpg')
            with col2:
                st.image('u.kav2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Asmaları yara yerlerinden enfekte ederek, bitki dokusunda enine ve boyuna yayılır. Miselyum gelişmesi yavaş olduğundan enfeksiyon sonrası belirtilerin ortaya çıkması uzun yıllar alabilmektedir. Hastalık asmanın odun kısmını tahrip eder. Bunun sonucunda yeşil akşamda solgunluğa, gelişme geriliğine hatta bitkinin ölümüne yol açar.')
            st.markdown('Yaşlı yapraklarda damar aralarında önce dış kısımlarda oluşur, daha sonra bu alanlar kurur ve beyaz çeşitlerde sarımsı, renkli çeşitlerde kızıl kahverengiye dönüşür. Daha genç yapraklar şeffaflaşır, salkım silker, yapraklarla birlikte kuruyarak dalında asılı kalır. Hastalıklı asmaların gövde ve kalın dalları enine kesildiğinde, açık renkli yumuşak dokulu hastalıklı kısmın koyu renkli sert dokulu bir kuşakla çevrilmiş olduğu görülür.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Çok yaşlı, verimden düşmüş hastalıklı dal ve yapraklar sökülerek artıkları yakılmalıdır.
                        * Hastalıklı ağaçlar en son budanmalı ve budama aletleri %10’luk sodyum hipoklorit ile dezenfekte edilmelidir. 
                        2-	Kimyasal Tedavi
                        * Bu hastalığa karşı pek fazla kimyasal mücadele uygulanmamaktadır. Fakat kimyasal savaşta pyraclostrrobin tipi ilaçlar kullanılabilmektedir.

                        """)
        elif uzums == 'Yaprak Yanıklığı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('u.yy1.jpg')
            with col2:
                st.image('u.yaprakyanıklığı2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Bakteriyel bir hastalıktır. Birçoğu önemsiz belirtiler gösteren veya hiçbir belirti göstermeyen pek çok konukçuya sahiptir. Gün geçtikçe daha fazla konukçu bitki türleri keşfedilmektedir.')
            st.markdown('Bakteriler; köklerde, damarlarda, gövdelerde, yapraklarda yaşar. Bitki buna, damarlarında tutkal benzeri bir madde olan zamk ve tiloz oluşturarak cevap verir. Bakteriler damarları tıkayarak bitkinin solmasına neden olur. Böcekler sayesinde bitkiden bitkiye aktarılabilir. Yaprakların birincil enfeksiyonu yaprak yanıklığına yol açar. Yeşil yaprağın bir kısmı aniden ölür ve kahverengiye döner; bu sırada bitişik doku sararır veya kızarır. Bu desikasyon yayılır ve yaprağın tamamı büzüşüp düşebilir. Enfekte gövdelerde düzensiz olgunlaşma ve kahverengi ve yeşil doku lekeleri görülür. İzleyen sezonlarda, bu enfekte bitkilerin gelişmesi yavaşlar ve bodur klorotik sürgünler oluştururlar. Enfeksiyon kronik hale geldiğinde, yapraklar damarlar arasında sararmalar ile bozulmaya başlar ve sürgünlerin boğum araları kısalır. Etkilenen asmalar sonunda ölür. Bu, genç asmalarda yaşlılardan daha hızlı gerçekleşir. Hassas çeşitlerde (2-3 yıl içinde) beş yıldan fazla yaşayabilen daha toleranslı çeşitlerde olduğundan daha hızlı olur.')
            st.subheader('Yaşam Döngüsü')
            st.markdown('Bakterilerin sayısı birçok bölgede dormant bitkilerin içindeki bakterilerin öldüğü don dönemleri olan kış koşullarında sınırlı olur. Ayrıca, birçok bölgede yeni mevsimde erken enfeksiyona neden olabilecek yetişkin vektörleri kışlamaz. Bu nedenle, bakteriler ılıman kışlara sahip ve kışlayan yetişkin vektörlerin olduğu bölgelerde en ciddi problemlere neden olur. Bakteriler ayrıca pek çok yabani konukçu ve yabani otta da ortaya çıkar ve varlıkları, kültür bitkilerinde enfeksiyon riskini artırır. Bir konukçu bitki türünden diğerine yayılmanın nasıl olduğu hala araştırılmaktadır ve bu süreç enfekte bitkilerde bakterilerin konumuna bağlı gibi görünmektedir. Örneğin, yapraklarda yüksek seviyede bakteri bulunan enfekte erik ağaçlarından bakterilerin en çok köklerinde olduğu komşu şeftali ağaçlarına aktarım, tersi yönde aktarımdan çok daha başarılıdır.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Tüm dikim ve aşı materyali hastalıkla bulaşık olmayana alanlarda temin edilir.
                        * Budama ve diğer işlemlerde ekipmanlar temizlenmeli ve dezenfekte edilmelidir.
                        * Tamamen ölmüş veya enfekte olmuş bitkiler sökülmeli yayılımı engellenmelidir.
                        * Yağmurlama sulamadan kaçınılmalıdır.
                        2-	Kimyasal Tedavi
                        * Bordo bulamacı spreyi veya fiks bakır spreyi ile budamadan sonra ve periyodik olarak yapraklar yarı büyüklüğünü alıncaya kadar ilaçlama yapılmalıdır.
                        * Bulaşık alanlardan toplanan bulaşıklı bitkisel materyal, yetiştirme ortamı/toprak yakılarak veya derine gömülerek imha edilmelidir. Bulaşık bitkisel materyal, yetiştirme ortamı, toprakla temas eden veya yakın çevresinde bulunan makine, ekipman ve taşıtların bu alanın dışına çıkmasına izin verilmemelidir.
                        """)
    
    if secim == 'Portakal':
        portakals = st.selectbox('Geçerli bir hastalık girin:',('Turunçgil Yeşillenme', ''))
        if portakals == 'Turunçgil Yeşillenme':
            col1, col2 = st.columns(2)
            with col1:
                st.image('p.turunçgil1.jpg')
            with col2:
                st.image('p.turunçgil2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalık anaca bakmaksızın portakal, mandarin ve greyfurtlarda oldukça etkilidir. Bunun yanında limon, kaba limon hastalıktan etkilenmektedir.')
            st.markdown('Belirtileri; hastalık aşırı derecede meyve dökümü görülmektedir. Meyveler olgunluğa erişmesine rağmen yeşil olarak görülmektedir. Ortadan kesildiğinde, küçük, koyu abortif çekirdekler gözlenebilir. Meyve eksenindeki demetler renksizdir. Meyve, özellikle portakal, alacalı bir görüntü alır ve eğer kabuğa bir parmakla bastırılırsa, bastırılan bölgede gümüşi bir alan oluşabilmektedir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Bitkilerin vasküler sisteminde etkili bir bakteri hastalığıdır. Ağaç bir kez hastalandığında herhangi bir tedavisi yoktur. Hastalığın birincil konukçusu turunçgillerdir.
                        * Budama ve diğer işlemlerde ekipmanlar temizlenmeli ve dezenfekte edilmelidir.
                        * Tamamen ölmüş veya enfekte olmuş bitkiler sökülmeli yayılımı engellenmelidir.
                        2-	Kimyasal Tedavi
                        * Özellikle bahar sürgünlerinin korunması gerekmektedir. Çünkü en fazla artış bu dönemde görülür.
                        * İlaçlamanın zamanlaması da önemlidir. Bu nedenle sarı yapışkan tuzak uygulaması ilaçlama zamanını belirlemek açısından önemlidir.
                        * Yayılım engellenemezse karantinaya almak gerekebilmektedir.

                        """)
    
    if secim == 'Şeftali':
        seftalis = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı', 'Bakteriyel Leke'))
        if seftalis == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('ş.sag2.jpg')
            with col2:
                st.image('ş.sag1.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Şeftali ağacının toprağı çok önemlidir. Toprağın derinliği yüksek ve drenajı sağlanabilen toprak türünde olması gerekmektedir. Ph derecesi 6,5 olan toprak türü, şeftali ağacı için olması gereken ölçüttür.
                        * Şeftali ağacı bakımı konusunda bilgi sahibi olmak ve bu tür meyve veren ağaçların tozlaşma yoluyla meyve verebildiğinin bilinmesi gerekmektedir. Şeftali ağacı kendi kendine tozlaşma sağlamaktadır.
                        * Şeftali ağacının etrafı derin şekilde kazılarak, köklerine kadar suyu çekmesi sağlanmalıdır. İlk fide halindeyken bu yöntemin uygulanması, ağacın uzun vadede sağlıklı olması için önemlidir.
                        * Şeftali ağacından iyi verim almak için, ağacın budamasının düzenli olarak yapılması gereklidir. Budama yapılarak, ağacın gövde ve kök kısımlarında denge sağlanarak, kırılması önlenir.
                        * Meyve veren ağaçların gübrelemesinin, düzenli olarak yapılması gerekmektedir. Kaliteli meyve üretimi için toprağın ihtiyacı olan azot ve mineraller, gübre ile desteklenmelidir.
                        * Şeftali ağacı dikilen toprağınızın iyi sürülmüş ve derinliğinin iyi ayarlanmış olması çok önemlidir.
""")
            st.subheader('Şeftali Ağaçlarında İlaçlama')
            st.markdown('Şeftali ağacı ilaçlamada, ağacın hastalığına göre ve mevsime göre ilaçlama yapılmalıdır. Eğer ağacın bütün yaprakları dökülmüş ve ağır hastalık varsa, ağaç kökünden sökülmeli ve yakılmalıdır. İlaçlama ağaçların kış uykusunda olduğu dönemde yapılırsa, ağaç daha verimli olacaktır. Şeftali ağacının yapraklarında delikler ve tomurcuklarında hasarlar oluşmuşsa, bu hastalıklı bölgeler budanmalıdır. Daha sonra ağacın toprağının gübresi ve suyu verilerek, ağacın toprağının havalandırılması sağlanmalıdır. Böylece ağaç hastalıktan korunmuş olacaktır. Şeftali ağacının çiçeklenme zamanları, ağaçta böceklenmeler oluşur. Gündüz vakitlerinde ağaç silkelenerek, böceklerin ağaçtan uzaklaştırılması sağlanmalıdır. Şeftali ağacında, çiçeklenme sonunda da ağaca zarar veren türlerden ağacı kurtarmak için, ilaçlama yapılma zamanlarına dikkat edilmesi gerekmektedir. Topraktaki eksiklikten kaynaklı hastalık oluşumu varsa, toprağın gübresinin düzenli olarak verilmesi gerekmektedir.')
            st.subheader("Detaylı bilgi için: [link](https://www.cicekal.net/blog/seftali-agaci-bakimi-puf-noktalari-nelerdir/#:~:text=Sulamas%C4%B1%20iyi%20yap%C4%B1lan%20%C5%9Feftali%20a%C4%9Fac%C4%B1n%C4%B1n,defada%20bol%20su%20ile%20sulanmal%C4%B1d%C4%B1r.)")

        elif seftalis == 'Bakteriyel Leke':
            col1, col2 = st.columns(2)
            with col1:
                st.image('ş.bakteriyel1.jpg')
            with col2:
                st.image('ş.bakteriyel2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalığın gelişmesi için uygun olan koşullar ilik ve orta derecede sıcaklıklar, sik ve hafif geçen yağmurlu havalar, ağır çiğ ve az şiddetli rüzgârlı hava koşullarıdır. Belirtilen hava koşullarının tamamı ya da birazının hakim olduğu sezonlarda, şiddetli enfeksiyonlar her zaman beklenmelidir. Yine hava koşulları uygun olduğunda, bakteriyel enfeksiyon tomurcukların açılmasından hasat zamanına kadar olabilir. Şiddetli yağan yağmurlardan sonra yeni enfeksiyonlar her zaman çıkabilir, böyle koşullarda hastalık genellikle ağaçların bir tarafında daha yaygın olarak görülmektedir.')
            st.markdown('Hastalık meyve ağaçlarının yeşil aksam, ince dallar ve meyvelerinde görülmektedir. Bazı yetiştiriciler hastalığı genellikle bakteriyel etmeninin yapraklarda neden olduğu saçma deliği belirtisinden karakterize eder ve tanımlarlar. Hastalık belirtisi yapraklarda ilk önce, küçük, açık yeşil ya da beyazımsı renkte ve lekeyi çevreleyen dokudan kesin olarak ayrılmıştır. Bu lekeler çoğunlukla yeşil akşamların uçlarında daha yoğun görülmektedir. Şiddetli olarak enfektelenen yapraklar sarıya döner ve daha dökülürler. Duyarlı çeşitlerde, yapraklarda oluşan bir kaç lezyon yaprakların dökülmesine neden olabilir. Yaz baslarında da ağır yaprak dökülmeleri meyvelerin büyüklüğünü azaltır ve ağaçları zayıflatır.')
            st.markdown('Meyve belirtileri başlangıçta meyvenin yüzeyinde küçük, yuvarlak kahverengi lekeler olarak görülür. daha sora ise bu lekelerde çökme ve lekelerin etrafında ise çatlamalar meydana gelir. Bu tür lekeler meyvelerin görünümünü büyük ölçüde bozmasına rağmen, meyvenin yenilebilir özelliği bozmamaktadır. Yalnız meyvelerde meydana gelen çatlamalar, çürüklük mikroorganizmaların girişine müsaade ettiği için zararlanmalara neden olurlar. Geç sezonlarda görülen lekeler genellikle yüzeyseldir ve meyvelerde sadece benekleneme görüntülerin oluşmasını sağlar.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Kanserli dokuları barındıran ince dal ve sürgünler budanmalı ve imha edilmeli.
                        * Hastalık etmenine karsı dayanıklı kültüvarlar meyve bahçelerinin tesisinde tercih edilmelidir. 
                        * Canlı ve gür gelişen meyve ağaçları bakımsız ve yetersiz beslenen meyve ağaçlarına göre daha dayanıklıdır. Bundan dolayı, gübreleme, budama, sulama ve diğer bakim isleri zamanında ve dikkatli bir şekilde yapılmalıdır.
                        2-	Kimyasal Tedavi
                        * Kimyasal ilaçlama özellikle hasattan sonra yapılmalı ve kanserli dokuların oluşmasına böylelikle izin verilmez. Tomurcuklar patlamadan önce yapılacak bir ilaçlamada hastalığın etkili bir şekilde kontrolü için gereklidir. Bu ilaçlamayı takiben diğer ilaçlamalar hastalığın ortaya çıkmasına uygun ortamlar hakim olursa yapılabilir. Tarım ilacı olarak bakırlı preparatlar tavsiye edilmektedir.

                        """) 
    
    if secim == 'Biber':
        bibers = st.selectbox('Geçerli bir hastalık girin:',('Sağlıklı','Bakteriyel Leke'))
        if bibers == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('b.sag2.jpg')
            with col2:
                st.image('b.sag1.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Biber ılık ve sıcak iklim meyvesidir.Soğuklardan çok etkilenir. Yetiştirme devrelerinde sıfırın altında 2-3 dereceye düştüğünde tamamen ölür.
                        * Biber bitkisinde hava sıcaklığı 15 derecenin altında 32 derecenin üzerine çıktığında alınan verim düşmektedir.
                        * Biberlerde iyi bir gelişme ve yüksek verim oldukça derin, geçirgen, su tutma kabiliyeti yerinde, besin ve organik maddece zengin bahçelerde yetiştirilir.
                        * Erken verim alma maksadıyla yapılan yetiştirmelerde takviye edilmiş kumlu topraklar ve özellikle kumlu-tınlı toprak üzerinde durulmalıdır. Bol mahsul almak için kumlu-killi topraklar tercih edilmelidir.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Ekim Nöbeti: Biber ekim nöbetine girebilecek bitkiler pamuk, buğday ve buğdaygillerdir. En iyi ekim nöbeti; buğday+ikinci ürün+biber olarak belirlenmiştir.
                        * Toprak Hazırlığı: Sonbaharda pullukla derin sürüm yapılır. İlkbaharda ise diskardo çekildikten sonra hafif bir tapan çekilir.
                        * Dikim: Dikim esnasında fideler çapa ile açılan yeterli büyüklükteki çukura olduğu gibi yerleştirilir ve çukurun boş kısımları toprakla doldurulan hafifçe bastırılır.
                        * Sulama: Biber sulamasına dikimden 10-15 gün sonra başlanmalı, ilk meyve görülünceye kadar sulamalardan kaçınılmalıdır. İlk meyveyi gördükten sonra haftalık aralıklarla sulamalara devam edilmeli.
                        """)
            st.subheader("Detaylı bilgi için: [link](http://www.tarimkutuphanesi.com/biber_yetistiriciligi_00026.html)")

            
        elif bibers == 'Bakteriyel Leke':
            col1, col2 = st.columns(2)
            with col1:
                st.image('b.bakteriyel1.jpg')
            with col2:
                st.image('b.bakteriyel2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalıktan dolayı kayıplar hem tohum yataklarında hem de üretim alanlarında görülebilir. Eğer bitkiler tohum yataklarında bulaştı ise, hastalık belirtileri bitkiler tarla ya da sera gibi yetiştirme yerlerine şaşırtıldıktan sonraki 6 hafta içerisinde görülmeye baslar ve hemen hemen tüm bitkilerde ortaya çıkabilir. Erken dönemlerde etkilenen bitkilerde genellikle bodurluk belirtisi görülürken, geç ya da şaşırtıldıktan sonra enfetelenen bitkilerde erken yaprak dökümleri görülmektedir. Bu yaprak dökümünden sonra meyveler de de belirtiler görülür ve aşırı yaprak dökümü nedeniyle de bitkiler güneş yanığı gibi sekonder zararlanmalara maruz kalabilir. Bakteriyel etmen hastalıklı bitkilerin sayesinde aylarca tohum yataklarında ve tohum üzerinde canlılığını muhafaza edebilir. Bakteriyel etmen, tarlada bırakılmış bitkilerin kök ve gövdelerinde, yabancı otlar üzerinde canlılığını korur ve diğer sezona bakteriler taşınmaktadır. Toprakta ise uzun süre canlılığını muhafaza edemeyebilir. İlk bulaşma tohum, bulaşık şaşırtılmış fide, yabancı otlar ve bulaşık bitki ve toprak ile olabilir.')
            st.markdown("Yaprak belirtileri ilk önce küçük suyla ıslanmış alanlar olarak yaprakların alt tarafında görülmeye baslar. Bu lekeler birkaç mm' ye kadar genişler, koyu kahverengiye döner ve hafifçe kabarmaktadır. Yaprak üst yüzeyinde, lekelerin etrafı kahverengi bir hale le kuşatılır. Böyle küçük belirtiler çökerek ölmekte ve nekrotik alanlar yaprak üzerinde oluşur ve bu lekelerin büyük bir kısmi yaprak neminin toplandığı yaprak kenarları ve uçlarında oluşmaktadır. Sonunda yapraklar sararır ve düşer, böyle bitkilerde güneş yanıklığından etkilen meyvelerin sayısında artış görülür. Meyve üzerinde ise pazara değerini azalmış, kabarık ve uyuz halini almış lekeler seklinde kendini gösterir.")
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıktan ari tohum ve fidelerin kullanımı.
                        * Sera ve tohum yataklarında hastalıktan ari toprak, su ve alet ekipmanı kullanılmalı.
                        * 2-3 yıl gibi ürün rotasyonu yapılmalı.
                        * Aşırı sulamadan kaçınılmalı nem oluşumu engellenmeli. Ayrıca nemli koşullarda ve bitkiler ıslak iken çalışmaktan kaçınılmalı.
                        * Hastalıklı fideler hemen yetiştirme ortamlarından uzaklaştırılmalı ve imha edilmeli.
                        2-	Kimyasal Tedavi
                        * Tohum yataklarında Bakir ile karıştırılmış Streptomycin antibiyotiği (200 PPM) 5 gün aralıklara ile kullanılabilir. Fakat pratikte pahalıya gelebilir onun için pek tavsiye edilmiyor. Bakirli preparatlar bitkilerde koruyucu olarak ve yayilmasini engellemek için kullanılabilir. Ayrıca bakirli preparatlar maneb ya da macozeb ile birlikte kullanılarak ilaçların etkinliği artırılabilir ve diğer fungal etmenlere karşı da koruyucu bir etki yapabilir. Genellikle bakteriyel etmenler ile mücadele zor, onun için kültürel önlemlere ve temiz çalışmaya oldukça fazla dikkat edilmelidir.

                        """) 
    
    if secim == 'Patates':
        patatess = st.selectbox('Geçerli bir hastalık girin:',('Sağlıklı','Erken Yanıklık','Geç Yanıklık'))
        if patatess == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('p.sag1.jpg')
            with col2:
                st.image('p.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Patates, fazla bakım isteyen bir bitkidir. Çıkıştan önce düzeltilmiş tırmık çekmek faydalıdır. Hem toprak kaymak tabakası bağladıysa kırılmış, hem de çıkmaya başlayan yabancı otlar örtülmüş olur.
                        * 3-4 yapraklı olunca yüzeye ve dikkatli bir şekilde ilk çapa yapılır. Bu çapa ile toprak kabartılır, yabancı otlar öldürülür ve nemin korunması sağlanır. Bundan sonra 20'şer gün arayla her çapa ile birlikte doldurma işlemi yapılır.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Gübreleme: Genellikle çiftlik gübresi kullanılır. Dekara 1.5-2 ton, eğer toprak çok fakir ise 2.5-3 ton çiftlik gübresi verilirse verim artar. Bu miktardan fazlası nişasta miktarını ve lezzeti olumsuz etkiler.
                        """)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                        * Hasat: Patateste hasat zamanının geldiği yaprak ve sapların sararıp kuruduğu, yumruların normal büyüklüğünü alarak bitkiden kolayca ayrıldığı ve kabuğun kalınlaşıp sertleştiğinden anlaşılır.Yumrunun kesiti ıslak değil, koyu bir görüntüdedir.
                        Patates hasadında çok dikkatli olmak gerekir. Yumrular kesilip zedelenmemeli, toprakta yumru bırakılmamalıdır. Söküm sırasında toprak yaş olmamalıdır. Hasattan sonra yumrular ıslak ise gölgede kurutulur. Hasta, çürük, berelenmiş ve kabuğun soyulmuş olanları ayıklanır. Sonra iri ve küçük boy olmak üzere sınıflandırılarak file çuvallara doldurulur.
                        """)
            with col2:
                st.image('p.arac.jpg')
            st.markdown("""
                        * Sulama: Bitkinin su ihtiyacı alt yapraklardaki solma ve sararmayla kendini belli eder. Topraktaki nem dikkate alınarak ilk sulama, yumrular fındık büyüklüğüne geldiğinde yapılmalıdır. Hafif topraklarda 15-18, ağır 22-25 gün arayla yetiştirme süresince 2-4 sulama yapılır.')
                        En yaygın sulama yöntemi, karık ile sulamadır. İki karık arası mesafe kumlu topraklarda 60-65cm, ağır topraklarda 70-80cm'dir.
                        Patatesin enfazla suya ihtiyaç duyduğu evre, çiçeklenmeden 20 gün önce başlayan ve yumru yapmaya başladığı zamana kadar geçen evredir.
                        Sulama yeterli ve düzenli yapılmadığı taktirde, başta verim kaybı olmak üzere, memeli ve çatlak yumrular, yumru içinde kararmalar ve boşluklar ortaya çıkar.
                        * Depolama: Patates fazla miktarda su ihtiva eden bir ürün olduğundan iyi ibr şekilde depolanmazsa çok zarara uğrar. Yumrular çürür, pörsür, filiz verir ve değerlerini kaybeder.
                        Yumrular en iyi şekilde; olgun zedlenmemiş ve temiz olarak 3-40C sıcaklık, %85-90 nisbi nemde ve solunum sonucu meydana gelen karbondioksit, su ve ısıyı uzaklaştırıp oksijen sağlamak için havalandırma tertibatı iyi olan özel koruma depolarında saklanabilir. Depolamada yığın yüksekliği, yemeklik patateslerde 3-4 metre olabilir. Tokumluk patateslerde ise en fazla 1 metre olmaktadır.
                        """)
            st.subheader("Detaylı bilgi için: [tarım kütüphanesi](http://www.tarimkutuphanesi.com/patates_yetistiriciligi_00005.html#:~:text=Patates%20bitkilerinde%20su%20ihtiyac%C4%B1%20alt,s%C3%BCresince%202%2D4%20sulama%20yap%C4%B1l%C4%B1r)")
            st.subheader("Detaylı bilgi için: [lezzet](https://www.lezzet.com.tr/lezzetten-haberler/patates-ne-zaman-ekilir)")

        elif patatess == 'Erken Yanıklık':
            col1, col2 = st.columns(2)
            with col1:
                st.image('p.yanık1.jpg')
            with col2:
                st.image('p.yanık2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Yaprak, sap ve meyvede gayri muntazam küçük kahverengi lekeler halinde başlar. Lekeler iç içe daireler şeklinde 1–2 cm büyürler. Yapraklarda çoğu kez sarı bir çerçeve ile çevrili kahverengi daire biçiminde lekeler oluşur. Yaprak lekeleri kendine has koyu renkli halkalara sahiptir. Yaprak lekeleri ilk önce yaşlı yapraklarda görülür ve bitkinin üst yapraklarına doğru ilerlemeye başlar. Hastalığın şiddetli olması halinde bütün yapraklar kururlar. ')
            st.markdown('Çiçek ve meyve sapları hastalığa yakalanırlarsa dökülürler, meyvelerde genellikle sapın tutunduğu kısımda koyu renkli çökük, çoğu zamanda sınırlanmış lekeler oluşur. Hastalık için uygun gelişme koşulları 28–30 °C’dir.')
            st.markdown('Hastalığı oluşturan mantar tarafından neden olunan erken yaprak yanıklığı hastalığı, tarlada ürünlere ve depoda yumru kalitesi üzerine önemli bir risk oluşturmaktadır. Bu risk tarla ve depoda oluşabilecek ürün zayiatları göz önüne alınırsa, mücadele edilmediği takdirde oldukça ciddi ekonomik kayıplara sebep olabilir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Küresel Önlemler
                        * Temiz tohum ve temiz fide kullanılmalıdır.
                        * Aşırı sulamadan kaçınılmalıdır.
                        * Fidelik toprağı dezenfekte edilmelidir.
                        * Fidelikler ve seralar sık sık havalandırılmalıdır.
                        * Çiğ oluşumundan kaçınmak için havalandırma iyi olmalı ve bitkilerin üzerinde serbest su oluşumu engellenmeli. Bunun için nemli ve bulutlu havalarda sulamadan kaçınılmalı.
                        * Hastalık görülen yerlerde patlıcan ve patatesle rotasyona girilmemelidir.
                        2-	Kimyasal Tedavi
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır
                        * Bitkinin tüm yüzeyi ilaçlanmalı, ilaçlama serin ve rüzgarsız zamanlarda 7–10 gün arayla yapılmalıdır.
                        * Kimyasal mücadelede kullanılan pek çok pestisitin yanı sıra Syngenta firmasının ruhsatlamış olduğu Revus Pro içerdiği 250 g/l mandipropamid ve 250 g/l difenoconazole ile Patates mildiyösü mücadelesinin yanı sıra Patates erken yaprak yanıklığı hastalığına karşı da üstün etki ve performans gösterir.

                        """) 
        elif patatess == 'Geç Yanıklık':
            col1, col2 = st.columns(2)
            with col1:
                st.image('p.gyanık1.jpg')
            with col2:
                st.image('p.gyanık2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Temelde bir mantar hastalığıdır. Uygun koşullar altında hayat döngüsü bulaştığı bitki yaprağının altında yaklaşık beş gün içinde tamamlanır. Sıcaklığın düştüğü ve nem seviyesinin yükseldiği akşam saatlerinde en az iki gün boyunca sporlar oluşur. Yağmur ve/veya sulama ile bu sporlar topraktaki yeni bitkilere bulaşır. Aynı zamanda rüzgarla da komşu bitkilere taşınabilir. Bulaştıktan sonra kolayca fark edilemez. Bu yüzden kültürel yöntemlerle hastalıkla mücadele etmek neredeyse imkânsızdır.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıklı bitkiler, yumrular imha edilir. Tarlada kalan bitki artıkları temizlenir. Sertifikalı yumrular veya tohumlar kullanılır. Yabancı otlarla mücadele edilir. Hastalığın yayılmasını önlemek için uygun sulama sistemi kurulmalıdır, nemli havalarda sulama yapılmamalıdır. Nem oranın yüksek olması salgın oluşmasına neden olur. Ancak hastalık görülmeye başlandıktan sonra kültürel yöntemlerle mücadele salgını önlemekte başarılı değildir.
                        2-	Kimyasal Tedavi
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır
                        * Bitkinin tüm yüzeyi ilaçlanmalı, ilaçlama serin ve rüzgarsız zamanlarda 7–10 gün arayla yapılmalıdır.
                        * Kimyasal mücadelede kullanılan pek çok pestisitin yanı sıra Syngenta firmasının ruhsatlamış olduğu Revus Pro içerdiği 250 g/l mandipropamid ve 250 g/l difenoconazole ile Patates mildiyösü mücadelesinin yanı sıra Patates erken yaprak yanıklığı hastalığına karşı da üstün etki ve performans gösterir.

                        """) 
    
    if secim == 'Ahududu':
        ahududus = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı',''))
        if ahududus == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('a.sag1.jpg')
            with col2:
                st.image('a.sag2.jpg')
            st.subheader('Özellikleri')
            st.markdown("""
                        * Ahududu bakımında en önemli unsurlardan birisi topraktır. Ahududu toprağında özellikle yabani otlar ile mücadele çok önemlidir. İlk dönemlerden başlanarak hasat zamanına kadar ahududu bakımı için sürekli toprak işlenmelidir. Daha sonra ahududu bakımında gübreleme işlemi önemlidir. Ahududu bakımında gübreleme için ticari tarım gübreleri ve özel çiftlik gübreleri verilerek ahududunun fiziksel yapısının ve bitkinin besin değerlerinin yükseltilmesi çok önemlidir.
                        * Ahududu toprağının da su tutma kapasitesinin artırılması da ahududu bakımı için çok önemlidir. Ahududu bakımı sırasında bitkiye verilen azotlu gübreye azami özen gösterilmelidir. Çünkü verilen azot miktarı iyi ayarlanamaz ise ahududu meyvesinin yumuşaması ve özelliğini kaybederek pazar değerinin düşmesine sebep olmaktadır. Ahududu bakımında bitkiden daha verimli meyve alınması için en doğru gübreleme sıravari yada ocak usulü gübreleme şekilleri olmaktadır.
                        * Ahududu bakımında toprak tahlilleri de her yıl düzenli bir şekilde yapılması gereklidir. Ahududu bakımında sulama işlemi ise genellikle sulamada ahududu hasat zamanına yakın bir zamanda çok daha fazla sulanması gereken bir bitkidir.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Dikim budaması: Ahududu dikiminden hemen sonra en fazla 30 cm yükseklikte budanmalıdır. Ahududu budamada ilk bahar aylarında bakılarak 3-4 adet kuvvetli olan kollar bırakılarak diğer filizler kesilmelidir. Ahududu gövdesinde budama yapılırken bırakılan kuvvetli dallar arası da en az 25 cm olmalıdır.
                        * Kış budaması: Ahududu kış budamasında hasat zamanı geçtikten hemen sonra sonbahar aylarına doğru kuruyan dallar dipten kesilerek temizlenmelidir. Kök kısmından yetişen filizlerin önü açılmalıdır. Ahududu kış budaması için en uygun zaman ise sonbahar ayları yada ilk bahar başlangıcında olmaktadır.
                        * Yaz budaması: Ahududu bakımında yaz budaması bitki tepeleri kesilerek aşırı derecede fazla olan dalların budanması gerekmektedir. Fakat çok aşırı sıcaklarda bu işlemin yapılması bitki için çok zararlıdır. Ahududu bakımında zayıf ve yere yakın kollar budanmalıdır. Ahududu meyvelerinin kuvvetlendirilmesi için fazla kollar gövdeden temizlenmelidir. İri meyve alınması ancak kuvvetlendirilmiş dallardan alınacağı unutulmamalıdır.
                        * Gençleştirme budaması: Son olarak ahududu bakımında gençleştirme budaması olarak bitki artık yaşlandığından kök kısımlarında zayıflama görülür. Bu durumda ahududu bitkisinin kalitesi düşerek verimsizleşir. Bu durumu önlemek için ahududu en az 6 yıl aralıklar ile toprak altında bulunan köke ulaşarak kesilmesi ve bitkinin gençleştirilmesi önemlidir. Yaşlı kökler bitkiden ayrılarak akabinde bol miktarda çiftlik gübresi ve bunun yanı sıra ticari gübre verilerek ahududunun güçlenmesi ve ömrünün uzaması sağlanır.
                        """)
            st.subheader("Detaylı bilgi için: [link](https://www.ahududu.gen.tr/ahududu-bakimi.html)")

    
    if secim == 'Soya Fasulyesi':
        soyas = st.selectbox('Geçerli bir hastalık girin:', ('Sağlıklı',''))
        if soyas == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('s.sag1.jpg')
            with col2:
                st.image('s.sag2.jpg')
            st.subheader('Nasıl- Nerede Yetiştirilir')
            st.markdown("""
                        * Soya fasulyesi, farklı iklim etkilerine uyum sağlayabildiği için dünyanın farklı bölgelerinde yetiştirilir. Buna göre soya ekiminden elde edilebilecek en iyi verim Mayıs ve Eylül ayları arasında kabul edilmektedir. Yetiştirilme için optimum ortam sıcaklığı 25 derecedir. Ancak 18 ile 40 derece arasındaki tüm sıcaklıklarda yetiştirilmesi mümkündür. Bu aralık dışında kalan düşük ve yüksek sıcaklıklar soya fasulyesinin gelişimi üzerinde negatif etki yaratmaktadır.
                        * Soya fasulyesinin toprak isteği de oldukça geniş bir yelpazeye sahiptir. Buna göre aşırı kumlu topraklar dışındaki tüm bölgelerde ekim yapmak ve verim elde etmek mümkündür.
                        * Soya fasulyesi, iklim ve toprak açısından pek seçici değildir. Bu bakımdan dünyanın çok farklı bölümlerinde soya fasulyesi yetiştiriciliği yapmak mümkündür. Ancak üretimin %85 gibi büyük bir kısmı Adana ve Osmaniye tarafından karşılanmaktadır.
""")
            st.subheader('Yetiştirme Tekniği')
            st.markdown("""
                        * Ekim nöbeti: Soya üst üste aynı tarlaya ekilmemelidir. Çünkü hem verimi düşer, hem de hastalık ve zararlar çoğalır.
                        * Gübreleme: Kombine mibrezle yapılan ekimlerde azotlu gübrenin tamamı, toprak sathına serpildikten sonra, fosforlu gübre ve tohum mibrezle banda verilmelidir.
                        * Sulama: Soya yetiştirme süresi boyunca en az 2 defa sulanmalıdır. Bunlardan birincisi bitkiler 20-25 cm boylandığında, diğeri de çiçeklenme öncesi sulanmadır. Eğer bir su verilecekse mutlaka çiçeklenme öncesi verilmelidir. Sulamadan önce toprak nemi önceden kontrol ediilmelidir.
                        * Hasat: Hasat zamanı baklalar çeşide göre kirli sarı veya esmerimsi bir renk alır. Hasat için alt baklalar kontrol edilmelidir. Taneler sertleşir ve dişle zor kırılır. Yaprakların sararıp dökülmesinden 4-6 gün sonra hasada başlayıp kısa sürede bitirmek gerekir.
                        """)
            st.subheader("Detaylı bilgi için: [link](https://arastirma.tarimorman.gov.tr/cukurovataem/Belgeler/Yeti%C5%9Ftiricilik/soya-yetistiriciligi_1.pdf)")

    
    if secim == 'Kabak':
        kabaks = st.selectbox('Geçerli bir hastalık girin:', ('Küllenme',''))
        if kabaks == 'Küllenme':
            col1, col2 = st.columns(2)
            with col1:
                st.image('k.kül1.jpg')
            with col2:
                st.image('k.kül2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalık bitkilerin önce yaşlı yapraklarında görülür, daha sonra genç yapraklara da geçer. Öncelikle yaprağın üst yüzeyinde parça parça, nispeten yuvarlak lekeler belirir, sonradan bu lekeler birleşerek yaprağın her iki yüzeyini, yaprak sapını ve gövdeyi kaplar. Lekeler ilk zamanlarda beyaz renkte toz tabakası gibi görünür, zaman ilerledikçe esmerleşir. Yapraklar kuruyup dökülür ve bitkide gelişme durur. Bunun sonucu olarak da ürün kaybı meydana gelir. Hastalık için en uygun sıcaklık 27 C’dir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hasattan sonra hastalıklı bitki artıkları toplanarak yakılmalıdır.
                        2-	Kimyasal Mücadele
                        * İlk hastalık belirtileri görüldüğünde ilaçlamaya başlanmalıdır.
                        * İlaçlama havanın serin ve sakin olduğu zamanlarda bitkinin her tarafının ilaçla kaplanması şeklinde olmalıdır.
                        * Yağıştan sonra ve fazla çiğ bulunduğunda toz kükürt uygulaması yapılmamalıdır, çünkü çıkabilecek güneş nedeni ile yanıklar meydana gelebilir.
                        * Genellikle günlük sıcaklık ortalaması 27 derecenin üstünde ve orantılı nemin de %50’nin altına düştüğü zamanlarda ilaçlamaya ara verilmeli, şartlar değiştiğinde ise ilaçlamaya devam edilmelidir.

                        """) 

    if secim == 'Çilek':
        cileks = st.selectbox('Geçerli bir hastalık girin:',('Sağlıklı','Yaprak Yanıklığı'))
        if cileks == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('ç.sag1.jpg')
            with col2:
                st.image('ç.sag2.jpg')
            st.subheader('Çilek Yetiştiriciliği')
            st.markdown("""
                        * Çilek meyvesi gerçek bir meyve olmayıp yenen kısmı 40-60 kadar pistilin birleştiği çiçek tablasıdır. Çilek yüzeysel kök yapan otsu bir bitkidir.Kökler iyi drene edillmiş(süzek)topraklarda  60-70 cm' ye kadar iner.Ağır topraklarda ise kökler yatay büyür.
                        * Çilek yaprakları 2/5 düzeninde spiral olarak dizilmiştir.İlkbaharda havalar ısınınca patlayan embriyonik yapraklar 2-3 hafta sonra tam büyüklüğe erişir.Her yaprağın 1-3 ay ömrü vardır. Kollar (stolonlar)yaz boyunca  yeni yaprakların koltuklarındaki tomurcuklarından oluşarak gelişirler. Çilekte çiçekler salkım şeklindedir.Buna değişmiş gövdede denilebilir. Çilekte iyi tozlanma gereklidir. Tozlanmadan sonra meyve genelde 30-35 günde olgunlaşır.
                        * Çilek -10 oC ‘ye kadar yetiştirilebilir. Daha soğuk bölgelerde bitkilerin saman ,kuru  yaprak gibi materyalle örtülerekdondan korunması gerekir. Çilek yetiştiriciliği için en uygun toprak ; süzek, kumlu-tınlı  ve hafif topraklardır. Kireci fazla topraklar çilek için uygun değildir. Toprak  PH’ sı 7.0 - 7.5  olan topraklarda önemli bir problem yaratmamaktadır.
                        * Toprak derin işlendikten sonra dekara 3-4 ton çiftlik gübresi atılmalıdır. Ayrıca dekara 30-35 kg kompoze gübre verilmelidir.
                        * Büyük arazilerde  karık pulluğu ile, küçük alanlarda ise  elle 60-70 cm genişliğinde, 20-30 cm yüksekliğinde masuralar açılarak toprak dikime hazır hale getirilir. Çilek yetiştiriciliğinde ilkbahar dikimi, kış dikimi, yaz dikimi, sonbahar dikimi olmak üzere 4 dikim zamanı vardır.
""")
            st.subheader('Yetiştirme Tekniği Ve Dikim Zamanları')
            st.markdown("""
                        * Çilek -10C‘ ye kadar yetiştirilebilir. Daha soğuk bölgelerde bitkilerin saman ,kuru  yaprak gibi materyalle örtülerekdondan korunması gerekir. Çilek yetiştiriciliği için en uygun toprak ; süzek, kumlu-tınlı  ve hafif topraklardır. Kireci fazla topraklar çilek için uygun değildir. Toprak  PH’ sı 7.0 - 7.5  olan topraklarda önemli bir problem yaratmamaktadır.
                        * Çilek , toprak kökenli mantarsal hastalıklara karşı duyarlı olduğu için dikim yapılacağı toprağın bu hastalıklardan ve nematod yönünden temiz olması gerekir. Bunun için bir önceki mevsimde buğday, arpa gibi tahıl ekilmiş araziler tercih edilmelidir. Böyle topraklar bulunmadığı taktirde toprak metilbromit, vapam, kloropikrin gibi ilaçlarla fümige edilmelidir.
                        * İlkbahar Dikimi: Kışları soğuk geçen bölgelerde genellikle  Nisan ayında yapılan bir dikimdir. Bu dikimde frigo fideler veya fidelikte Ocak - Şubat  aylarında sökülmeyip bekletilen fideler  kullanılır. Bu fideler Mayıs ve Haziran aylarında az miktarda çiçek açarak meyve verirler. Bunların esas ürünü 1 yıl sonraki Haziran ayındadır. Bu bitkilerin 1 yıl boyunca su ,besin maddesi ihtiyaçları  karşılanmalı ve hastalık ve zarlılardan korunmalıdır.
                        * Kış Dikimi: Kışları ılık  geçen yerlerde yapılır. Dekara yaklaşık 8000 adet bitki dikilir. Dikimler fidelikten sökülen yavru bitkilerle yapılır. Akdeniz  Bölgesinde kış dikimi için en uygun zaman Ekim 15 - Kasım 15 arasıdır. Ilkbaharda açıkta Mart ortasından itibaren ürün alınmaya başlanır .Ayrıca alçak ve yüksek tüneller altında çilek yetiştiriciliği yapılırsa, ,açıkta yetiştiriciliğe göre yaklaşık 15- 30 günlük erkencilik sağlanır.
                        * Yaz Dikimi: Frigo bitkilerde yapılır. Bu dikim sisteminde verim kış dikimine göre 2-3 kat daha fazladır. Ancak ürün kış dikimine göre biraz geç kalmaktadır. Akdeniz Bölgesinde yaz dikimi için en uygun zaman Temmuz 15 - Ağustos 15 arasıdır.-20 OC ‘den çıkartılan frigo fideler  bir gece suda bırakılır. Sonra dikim yapılır. Fideler sıra üzeri ve sıra arası 30 x 32 cm olarak dikilir. Yazın sulama büyük problem teşkil eder. Dekara yaklaşık 6200 adet bitki dikilmektedir. Bütün yaz ve sonbahar aylarında büyümelerine devam eden bitkiler giderek kuvvetlenmekte ve kışa 5-10 gövdeli olarak girmektedirler.
                        * Sonbahar Dikimi: Fideler serin ve nemli havalarda dikilmelidir. Fide açılan çukurlara tam kök boğazı seviyesinde dikilir. Dikimden önce kök (8-10 cm kalacak şekilde ) ,taç tuvaleti (2-3 genç yaprak kalacak şekilde)yapılarak bitkilerin tutma oranı arttırılır. Dikimden sonra cansuyu verilir. Yaz dikiminde bitkiler 15 gün ,günde en az 3 defa olmak üzere çok iyi sulanmalıdır. Yaz dikiminde dikimden 6-8 gün sonra açan çiçekler koparılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [link](http://www.tarimkutuphanesi.com/cilek_yetistiriciligi_-_1_00296.html)")
        elif cileks == 'Yaprak Yanıklığı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('ç.yapraky1.jpg')
            with col2:
                st.image('ç.yapraky2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Kavrulmuş çilek yapraklarına, çilek ekimlerinin yapraklarını etkileyen bir mantar enfeksiyonu neden olur. Yaprak kavrulmuş çilekler, ilk önce yaprakların üst kısmında oluşan küçük morumsu lekelerin gelişmesiyle sorun belirtileri gösterebilir. Zamanla, lekeler büyümeye ve kararmaya devam edecektir. Şiddetli vakalarda, koyu lekeler çilek bitkisinin yapraklarının tüm kısımlarını kaplayabilir ve bunların tamamen kurumasına ve bitkiden düşmesine neden olabilir. Enfekte olmuş bitkilerin yaprakları estetik olarak hoş olmasa da bu mantarın varlığının çilek mahsulünün kalitesini etkilemesi nadiren olur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * İyi drene edilmiş topraklarda çilek yetiştirilmeli.
                        * Bitkiler arasında iyi bir hava sirkülasyonu sağlanmalı, dayanıklı çeşitler kullanılmalı.
                        * Sağlıklı üretim materyali kullanılmalı
                        * Kış sürecinde bitki üzerinde kalan enfekteli yaşlı yapraklar, hastalığın inokulum kaynağının azaltılmasına yardımcı olması bakımından, ilkbahar büyüme dönemi başlamadan önce tarlandan uzaklaştırılmalıdır.
                        2-	Kimyasal Mücadele
                        * İlaçlı mücadeleye ilk belirtiler görülür görülmez başlanmalıdır.
                        * Yağıştan sonra ve fazla çiğ bulunduğunda toz kükürt uygulaması yapılmamalıdır, çünkü çıkabilecek güneş nedeni ile yanıklar meydana gelebilir.
                        * Genellikle günlük sıcaklık ortalaması 27 derecenin üstünde ve orantılı nemin de %50’nin altına düştüğü zamanlarda ilaçlamaya ara verilmeli, şartlar değiştiğinde ise ilaçlamaya devam edilmelidir.

                        """) 
    
    if secim == 'Domates':
        domatess = st.selectbox('Geçerli bir hastalık girin:',('Sağlıklı','Bakteriyel Leke','Erken Yanıklık',
        'Geç Yanıklık','Hedef Nokta','İki Noktalı Kırmızı Örümcek Isırığı','Küllenme',
        'Mozaik Virüsü','Sarı Yaprak Kıvırcıklığı','Septoria Yaprak Lekesi'))
        if domatess == 'Sağlıklı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.sag3.png')
            with col2:
                st.image('d.sag2.jpg')
            st.subheader('Domates Yetiştiriciliği')
            st.markdown("""
                        * Sıcaklık: Domates, sıcak ve ılıman iklim sebzesidir. Gündüz 17-26˚C, gece ise 14-18˚C'dir. Sıcaklık -2°C'ye düşerse, bitki tamamen zarar görür. 10˚C'nin altında ve 30˚C'nin üzerinde tozlanma ve döllenmede problemler ortaya çıkmakta, meyve bağlayamamaktadır.
                        * Toprak: Derin, geçirgen ve su tutma özelliği iyi, humus ve besin maddelerince zengin tınlı toprakları sever. Toprak pH’sı 5-7 (hafif asidik) arasında, tuzsuz-az tuzlu (2,3 mS’dan az) toprakları sever. Kazık kök derine inebildiğinden toprak derin sürülmelidir. Gerektiğinde pulluk tabanı kırılmalıdır.
                        * Çapalama: Dikimden 10-15 gün sonra kesekler varsa kırılmalı, fide boğazı gevşekse doldurulmalıdır. Dikimi takiben 25-30 gün sonra ikinci çapa yapılır. Yabancı ot mücadelesi ve toprak neminin muhafazası için 3. ve 4. çapa yapılmalıdır. 
                        * Hasat: Domatesler, açık alanda fide dikiminden hasada kadar 60-80 günlük bir zamanda hasat olgunluğuna gelir. Pazara uzaklık durumuna göre değişik olgunluk devrelerinde hasat edilir. Hasat, havanın kuru ve serin olduğu zamanlarda yapılmalıdır. Meyve avuç içine alınarak, sapı etrafında hafifçe döndürülmek suretiyle zedelenmeden koparılmalıdır.
                        * Tek dallı olarak büyümesini istediğimiz bitkinin şeklini korumuş oluruz. Koltukların alınma devresi 5-15 cm boya eriştikleri zamandır. Erken koparıldıklarında yeniden çıkma ihtimalleri varken, büyük koparıldıklarında hem boşa besin maddesi tüketmiş olurlar hem de bitkide açılacak yara yüzeyi artmış olacaktır.
""")
            st.subheader('Domates ektikten sonra bakım nasıl yapılmaktadır?')
            st.markdown("""
                        Derin sürümle hazır olan toprak, sonbaharda 3-4 ton/da ahır gübresi alır. İlkbaharda ise karık hazırlığından önce taban gübresi alır. Fosforlu gübrenin tamamı gider. Diğerlerin üçte biri taban gübresi olarak gider. Geriye kalan gübreler ise bitkilerim üzerinde meyve görülmeye başladığı zaman verilmelidir. Meyveler fındık büyüklüğüne geldiğinde 10 ila 15 gün arayla 2-3 kez 100 lt suya 400-600 gr olacak şekilde yapılan magnezyum uygulanmaları ve verilen yaprak gübresi meyve kalitesini arttırmaya yönelik olumlu etki etmektedir.
                        """)
            st.markdown("""İlkbahar geç donlarının tehlikesi kalktığında, toprak ve hava sıcaklığı 12-15°C yi bulduğu zaman fide dikimi gerçekleştirilmektedir. Tarlaya dikim esnasında çiçek atmış ya da meyve tutmuş domates fideleri dikilmemelidir. Buna benzer fidelerin verimleri düşük, boyları bodur ve gelişmeleri yavaş olmaktadır.  Güneş altında bekletilmeyen fideler, akşama doğru dikilmelidir. 15-20 cm boyuna gelen fideler genelde dikime hazır hale gelmişlerdir. Dikimde can suyu yeterli miktarda olur. Can suyu ile birlikte, kök ve kök boğazı hastalıklarına karşı gereken ilaçlamalar gerçekleşir. Sıra arası ve üzeri mesafeler domatesin çeşidine göre değişmektedir.
                        
                        """)
            st.subheader('Seralarda Havalandırma İşleminin Önemi')
            st.markdown('Örtü altı domates yetiştiriciliğinde en önemli kültürel işlemlerin biri de yetiştirme ortamın havalandırılması işlemidir. Güneşli bir günde dış ortam soğuk olsa bile örtü altı koşulları bitki için optimum iklim koşullarının üstüne çıkabilir.')
            st.markdown('Örtü altı koşullarında hava oransal nemimin % 60-90 arasında olması istenir. Hava oransal nemi optimum koşullardan aşağı düşerse verim ve kalite kayıplarına sebep olur. Üstüne çıkarsa hastalık ve zararlı yoğunluğu artar. Erken sonbahar veya geç ilkbahar da havalandırma ile ortam sıcaklıkları yeterli düzeye düşmeyebilir.Bu dönemlerde gölgeleme materyalleri ile sera gölgelendirilmeli ve ortam sıcaklıkları düşmesi sağlanmalıdır.')
            st.image('d.st.jpg')
            st.subheader("Detaylı bilgi için: [Tarım Orman](https://adana.tarimorman.gov.tr/Belgeler/SUBELER/bitkisel_uretim_ve_bitki_sagligi_sube_mudurlugu/sebze_yetistiriciligi_ve_mucadelesi/Domates.pdf)")
            st.subheader("Detaylı bilgi için: [Milliyet](https://www.milliyet.com.tr/pembenar/domates-ektikten-sonra-bakimi-nasil-yapilir-domates-fidesi-bakimi-nasil-yapilmalidir-6517133)")

        elif domatess == 'Bakteriyel Leke':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.bakteriyel1.jpg')
            with col2:
                st.image('d.bakteriyel2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalık etmeni bakteri olup, optimum gelişme sıcaklığı 29°C ‘dir. Etmen bir yıl veya daha uzun süre tohum üzerinde veya içinde canlılığını sürdürebilir. Ancak konukçu bitki kalıntısı olmadan toprakta yaşayamaz. Seradaki hava hareketleri, su damlacıkları, yüksek basınçlı ilaçlamalar ve ıslak bitkilere temas edilmesi hastalığın yayılmasını teşvik etmektedir. Bakteri bitkideki doğal açıklıklardan veya herhangi bir nedenle bitkide açılan yaralardan giriş yapmaktadır. Uzun süreli yüksek orantılı nem ve 20-35°C sıcaklık koşulları hastalık gelişimini teşvik ederken 16°C’ den düşük gece sıcaklıkları hastalık gelişimini baskılamaktadır. Domateste yaprak, gövde ve meyve üzerinde bakteriyel leke hastalığının belirtileri görülür.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Üretimde sertifikalı tohum ve fideler kullanılmalıdır.
                        * Hastalığın görüldüğü̈ üretim alanlarında domates ve biber dışındaki bitkilerle en az 2 yıl süre ile ekim nöbeti uygulanmalıdır.
                        * Üretim sezonu sonunda tüm bitki artıkları sökülerek imha edilmelidir.
                        * Dengeli bir gübreleme programı uygulanmalı, özellikle meyve bağlama döneminden önce aşırı gübrelemeden kaçınılmalıdır.
                        * Bitkilerin ıslak olduğu zamanlarda serada çalışılmamalıdır.
                        * Seralarda havalandırmaya özen gösterilmeli ve aşırı nem birikimi önlenmelidir.
                        2-	Kimyasal Mücadele
                        * Yeşil akşam ilaçlamaları fidelikte veya serada hastalık görülür görülmez, fide döneminde haftada bir, serada ise 8-10 gün ara ile 2-3 uygulama yapılmalıdır. Hastalığın seyrine göre uygulama sayısı arttırılabilir Fide ve sera döneminde yapılacak olan yeşil akşam ilaçlamaları kaplama olarak yapılmalıdır.
                        * Özellikle örtü̈ altı üretiminde ilaçsız alan kalmamasına özen gösterilmeli ve bitki yüzeyinde ıslaklık söz konusu ise bitkilerin yüzeyi kuruduktan sonra ilaçlama yapılmalıdır.
                        * Etkili madde olarak Bakır oksiklorid (300-400 g) kullanılmalıdır.
                        """) 
            st.subheader("Detaylı bilgi için: [gardenjornal](https://tr.gardenjornal.com/10369834-target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes)")
            st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

        elif domatess == 'Erken Yanıklık':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.eyanık1.jpg')
            with col2:
                st.image('d.eyanık2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalığa konukçu bitkilerin her evresinde rastlanabilir. Hastalık, fide döneminde kök çürüklüğü veya kök boğazı yanıklığı yapar. Sonraki dönemlerde ise yaprak, gövde ve meyvelerde lekeler halinde görülür. Bu lekeler önce küçük, düzensiz ve esmerdir. Sonra iç içe halkalar halinde 1-2 cm kadar büyürler ve koyu gri renk alırlar. Hastalığın şiddetine göre bütün yapraklar kuruyup dökülebilir. Çiçek ve meyve sapları hastalığa yakalanırsa dökülürler. Meyvelerde genellikle sapın tutunduğu kısımda koyu renkli çökük, çoğunlukla sınırlanmış lekeler meydana gelir. Hastalık kısa zamanda bitkiyi öldürmesi nedeniyle önemlidir.')
            st.markdown('Etmenin konukçuları domates, patlıcan ve patatestir. Hastalık 6-34oC arası sıcaklıkta gelişebilmektedir; ancak optimum gelişme sıcaklığı 28-30oC arasıdır. Görece nemin yüksek olduğu koşullar hastalığın gelişimini teşvik eder.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Sertifikalı tohum veya sağlıklı fide kullanılmalıdır.
                        * Fidelikler ve seralar sık sık havalandırılmalıdır.
                        * Aşırı sulamadan kaçınılmalıdır.
                        * Hasattan sonra hastalıklı bitki artıkları imha edilmelidir.
                        2-	Kimyasal Mücadele
                        * Fidelikte veya tarlada ilaçlamaya ilk lekeler görülür görülmez başlanmalıdır. İklim koşulları hastalık gelişimi için uygun olduğunda ilacın etki süresine bağlı olarak ilaçlama tekrarlamalıdır.
                        * Erken yaprak yanıklığının mücadelesinde Activus® kullanılabilmektedir.
                        * Bir sezonda maksimum 3 kez Activus® kullanılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [syngenta](https://www.syngenta.com.tr/blog/murat-kadioglu/domateste-erken-yaniklik-alternaria-solani#:~:text=Alternaria%20solani%20ya%C5%9Fam%C4%B1n%C4%B1%20topraktaki%20bitki,ve%20k%C3%B6k%20bo%C4%9Faz%C4%B1%20yan%C4%B1kl%C4%B1%C4%9F%C4%B1%20yapar.)")
            st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

        elif domatess == 'Geç Yanıklık':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.gyanık1.jpg')
            with col2:
                st.image('d.gyanık2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Bölgelere göre ilkbahar ve yaz başlagıcında hastalık belirtileri patates bitkilerinde görülmeye başlar. Hastalık etmeni toprakta ve ölü bitki artıklarında canlılığını uzun süre koruyamaz, fakat dayanıklı üreme organı olan oosporları muhafaza edilebilir. Bir alanda epideminin (salgın) başlaması için mikroorganizma patates yumrularında kışı geçirmekte ya da tohumluk patates veya şaşırtılacak domates fideleri ile yeni bir alana tekrar girmelidir veyahutta canlı sporlar yağmurla veya sulama suyu ile taşınmalıdır. Serin, yağışlı havalar (16 - 27 °C) hastalığın gelişmesi için uygun iken, kuru ve sıcak havalar hastalığın gelişmesini engelleyebilir.')
            st.markdown('Enfektelenmiş gövde dokuları hastalık etmenini kuru ve sıcak havalardan korur ve uygun koşullarda hastalık buralardan tekrar gelişir ve büyük epidemilere yol açabilir. Yağmurlu, sisli ve çiğ oluşumu yüksek olan yerlerde hastalık sık olarak karşımıza çıkar. Enfekteli dokular üzerinde fungal etmenin sporları (sporongia) oluşur. Yağmur ya da sulama suları sporları sağlıklı bitkilere taşır ve sporongialar ıslak yaprak ve gövdeleri direkt yada stomalardan infekte ederler. Serin ve nemli koşullarda, sporongia hareketli olan zoosporları da üretebilir ve bu sporlarda bitkileri direkt olarak enfekte edebilir. Fungal etmen yaprak ve gövde de hızla kolonize olur ve infektelen bölge hastalık ilerken nekrotik olur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Yaprak ve gövdeler kontrol edilerek koyu lekeli bitkiler şaşırtılmamalı.
                        * Bitki artıkları uzaklaştırşmalı ve yok edilmelidir.
                        * Sulama esnasında yaprakların ıslanmamalı, özellikle geç ve akşam sulamalarından kaçınılmalı.
                        2-	Kimyasal Mücadele
                        * İlaçlamalar düzenli aralıklarla yapılmalı, özellikle hastalığın görüldüğü bölgelerde hastalık belirtileri ortaya çıkmadan önce, bitkiler koruyucu ilaçlar ile ilaçlanmalıdır.
                        * Kullanılan ilaçlar arasında; Azoxystrobin SC 250 g/l, Bakır Oksiklorid WP 50%, Folpet WP 50% vardır.
                        """)
            st.subheader("Detaylı bilgi için: [syngenta.com](https://www.syngenta.com.tr/blog/murat-kadioglu/domateste-erken-yaniklik-alternaria-solani#:~:text=Alternaria%20solani%20ya%C5%9Fam%C4%B1n%C4%B1%20topraktaki%20bitki,ve%20k%C3%B6k%20bo%C4%9Faz%C4%B1%20yan%C4%B1kl%C4%B1%C4%9F%C4%B1%20yapar.)")

        elif domatess == 'Hedef Nokta':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.hedef1.jpg')
            with col2:
                st.image('d.hedef2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalık domatesin diğer mantar hastalıklarına benzediğinden, domates meyvesindeki hedef noktanın erken aşamalarda tanınması zordur. Bununla birlikte, hastalıklı domatesler olgunlaşıp yeşilden kırmızıya döndükçe, meyve, merkezde hedef benzeri halkalar ve kadifemsi siyah, mantar lezyonları olan dairesel noktalar gösterir. Domates olgunlaştıkça "hedefler" çekirdeksiz hale gelir ve büyür. Domates meyvesindeki hedef noktayı kontrol etmek zordur, çünkü toprakta bitki artıklarında hayatta kalan sporlar mevsimden mevsime taşınır.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Büyüme mevsiminin sonunda eski bitki kalıntılarını çıkarın; aksi takdirde sporlar, bir sonraki büyüme mevsiminde artıklardan yeni ekilen domateslere geçecek ve böylece hastalık yeniden başlayacaktır.
                        * Mahsulleri değiştirin ve geçtiğimiz yıl başta patlıcan, biber, patates veya tabii ki domates olmak üzere hastalığa yatkın diğer bitkilerin bulunduğu alanlara domates dikmeyin.
                        * Sabahları domates bitkilerini sulayın, böylece yaprakların kuruması için zamanınız olur. Yaprakları kuru tutmak için bitkinin tabanında su veya bir sağanak hortumu veya damlama sistemi kullanın.
                        2-	Kimyasal Mücadele
                        * Mantar spreyini de önleyici tedbir olarak mevsimin başlarında veya hastalık fark edilir edilmez uygulayabilirsiniz.
                        """) 
            st.subheader("Detaylı bilgi için: [gardenjornal](https://tr.gardenjornal.com/10369834-target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes)")
            st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

        elif domatess == 'İki Noktalı Kırmızı Örümcek Isırığı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.kırmızı1.jpg')
            with col2:
                st.image('d.kırmızı2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('İki noktalı kırmızı örümcek, tüm dünyada birçok mahsulde görülebilen bir zararlıdır. Küçük boyutlarına rağmen, çok hızlı üreyebildiklerinden dolayı çok hızlı biçimde son derece büyük zarara neden olabilirler.')
            st.markdown('Yumurtalar özellikle yaprakların alt kısmında görülür. Gövdeleri oval şekilli olup arka ucu yuvarlaktır. Turuncu, açık sarı veya açık yeşilden koyu yeşil, kırmızı, kahverengi veya neredeyse siyaha kadar çok çeşitli renklerde olabilirler. Genellikle bitki öz suyundan beslenerek bitkiye zarar verir.')
            st.markdown('Domateste yaprak yüzeyinin %30’luk bir kısmını yiyerek mahsülün tamamen kaybedilmesine neden olabilir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler 
                        * Seraya temiz fideler dikilmeli
                        * Hasattan sonra bitki artıkları tarla ve seradan uzaklaştırılmalı
                        * Ot çapasına önem verilmeli
                        * Gereğinden fazla azotlu gübreler kullanılmamalı
                        * Toprak işlemesi yapılarak kırmızı örümceklerin kışladıkları bitki artıkları toprağa gömülmelidir.
                        2-	Kimyasal Mücadele
                        * Küçük yapraklı sebzelerde yaprak başına 3 adet, büyük yapraklı sebzelerde 5 adet canlı Kırmızı örümcek bulunduğunda ilaçlama yapılır.
                        * Bakanlıkça önerilen ruhsatlı zirai mücadele ilaçlarından biri kullanılır.
                        """) 
            st.subheader("Detaylı bilgi için: [sorhocam](https://www.sorhocam.com/konu.asp?sid=4157&domates-septoria-yaprak-lekesi-hastaligi.html)")
            st.subheader("Detaylı bilgi için: [tarım orman](https://kayseri.tarimorman.gov.tr/Belgeler/SOL%20MEN%C3%9C%20BELGELER%C4%B0/Z%C4%B0RAA%C4%B0%20M%C3%9CCADELE/Sebze%20Hastal%C4%B1klar%C4%B1/sebzelerde_septoria_leke_hastaligi.pdf)")

        elif domatess == 'Küllenme':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.kül3.jpg')
            with col2:
                st.image('d.kül6.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Hastalık, bitki dokusunun içinde ve dışında gelişir. Kışı yapraklar üzerinde; ılıman bölgelerde yeşilliğini muhafaza eden bitki dokularında geçirir. Hastalığın ilk belirtileri domatesin yapraklarında görülen yuvarlakça beyaz küçük lekeler halindedir. Bu küçük lekeler, zamanla birleşerek bütün yaprak ayasını, yaprak sapını ve gövdesini kaplar; mevsim ilerledikçe rengi beyazdan kül rengine döner. Hastalığın ilerlemesi ile yapraklar pörsür, aşağıya doğru sarkar ve kurumalar meydana gelir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Hastalıklı bitki artıkları toplanıp imha edilmelidir.
                        2-	Kimyasal Mücadele
                        * İlaçlamalar tarla ve serada ilk hastalık belirtileri görüldüğünde yapılmalıdır.
                        * Domates küllemesinde Activus ürünleri kullanılabilmektedir.
                        * Bir sezonda en fazla 3 kez kullanılmalıdır.
                        """) 
            st.subheader("Detaylı bilgi için: [agro](https://www.agro.basf.com.tr/tr/Bilgi-Bankas%C4%B1/Hastal%C4%B1k-Zararl%C4%B1-Yabanc%C4%B1-Ot-Bilgi-Bankas%C4%B1/Fungal-Hastal%C4%B1klar/B%C3%BCy%C3%BCme-noktas%C4%B1-yaprak-sap-hastal%C4%B1klar%C4%B1/K%C3%BClleme-(Leveillula-Taurica)/#:~:text=Hastal%C4%B1%C4%9F%C4%B1n%20ilk%20belirtileri%20domatesin%20yapraklar%C4%B1nda,rengi%20beyazdan%20k%C3%BCl%20rengine%20d%C3%B6ner.)")
            st.subheader("Detaylı bilgi için: [tarım orman](https://bku.tarimorman.gov.tr/Zararli/KaynakDetay/1266?csrt=6516937016701123893)")

        elif domatess == 'Mozaik Virüsü':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.mozaik1.jpg')
            with col2:
                st.image('d.mozaik2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Etmen; hastalıklı bitki artıklarında, yabancı otlarda, bulaşık topraklarda, sigara ve tütün kalıntılarında yaşamını sürdürebilir. Konukçularından ve bunların artıklarından mekanik olarak temasla, boğaz doldurma, koltuk ve uç alma gibi bakım işlemleri sırasında yayılma gösterir. Bulaşık domates bitkilerinde en yaygın belirti tipi; yapraklarda açık yeşil veya sarı düzensiz lekeler ve mozaik desenlerin oluşumudur. Açık yeşil renkli alanlar yapraktaki koyu yeşil renkli alanlardan daha yavaş gelişir. Bunun sonucunda koyu yeşil renkli ısımlar kabararak yaprak yüzeyinde bombeler oluşturur. Bu da yaprağa kıvırcık ve kırışık bir görünüm kazandırır. Bu tip yapraklar sağlıklı yapraklardan daha serttir.')
            st.markdown('Erken dönemdeki enfeksiyonlar genç bitkileri öldürebilir veya bulaşmanın şiddetine bağlı olarak bitkiler bodur kalır. Hasta bitkilerde meyve sayısı azdır. Meyveler normal büyüklüklerine ulaşamazlar. Ayrıca meyvelerde şekil bozuklukları üzerinde kahverengi bölgeler oluşur.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler 
                        * Fidelikte ve tarlada şüpheli görülen bitkiler imha edilmelidir.
                        * Fidelikte ve tarlada tütün içilmemelidir.
                        * Kullanılan aletler %5’lik hipolu su ile dezenfekte edilmelidir.
                        * Ekim nöbeti uygulanmalıdır.
                        2-	Kimyasal Mücadele
                        * Çok fazla kimyasal ürün bulunmamasına rağmen; Exirel 100 SE, Superprex, Pestige 250 EC gibi ürünler kullanılabilmektedir.
                        """) 
            st.subheader("Detaylı bilgi için: [gardenjornal](https://tr.gardenjornal.com/10369834-target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes)")
            st.subheader("Detaylı bilgi için: [haenselblatt orman](https://tr.haenselblatt.com/articles/edible-gardens/target-spot-on-tomato-fruit-tips-on-treating-target-spot-on-tomatoes.html)")

        elif domatess == 'Sarı Yaprak Kıvırcıklığı':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.sarı1.jpg')
            with col2:
                st.image('d.sarı2.jpg')
            
            st.subheader('Nedir?')
            st.markdown('Bu hastalık beyaz sineklerle taşınmaktadır. Tohumla ve temas ile taşınmaz. Ana konukçusu domatestir.')
            st.markdown('Yaprak kenarlarında ve ayalarında sararmalar oluşturur. Yapraklar küçülür ve kenarlarından kıvrılarak kayık görünümünü alır. Meyveler geç olgunlaşır. Şiddetli bir enfeksiyonda verim kaybı %80’e ulaşır.')
            st.markdown('Hastalık etmeni çift partiküllü geminivirus grubunda yer almaktadır. Gümüşi yaprak beyaz sineği ile persistent olarak taşınmaktadır. İki parçalı DNA kısımları A ve B olarak ikiye ayrılmıştır. Tek sarmal DNA genomunda yaklaşık olarak 2800 nükleotid bulunmaktadır. İzometrik yapılı patiküller 20 nm boyutundadır.')
            st.markdown('Beyaz sineğin etmeni bünyesine alması için 10 – 60 dakikalık bir emgi yapma süresi gerekmektedir. Bünyesine aldığı virüsü nimf döneminden ergin döneme kadar taşımaktadır. Bünyeye alınan virüsün 20 – 24 saatlik bekleme süresine ihtiyacı vardır. Bünyedeki virüs  en fazla 20 gün aktivitesini koruyabilmekte olup bir sonraki nesle aktarılmamaktadır.')
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Konukçuları')
                st.markdown('Domatesten başka, tütün bitkisi de konukçusudur ancak belirti göstermemektedir. Süs bitkilerinden ise lisiantus konukçusu olup şiddetli belirtiler göstermektedir.')

            with col2:
                st.image('d.sarı3.jpg')
            
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Dayanıklı bitki ve tohum türleri kullanılmalıdır.
                        * Beyaz sinekler ile mücadele edilmelidir.
                        * Yabancı otlar ile mücadele edilmelidir.
                        * Sonbahar ve ilkbahar dikimleri mümkün olduğunca ileri zamana alınmalıdır.
                        * Tuzak bitkilerin kullanılması böceklerin virüsü yaymasını azaltabilir.
                        * Hastalığın yayılmasını engellemek için konukçu bitki olan yerlerde  yetiştiricilik yapılmamalıdır.
                        * Hastalığa dayanıklı bitki çeşitleri tercih edilmelidir.
                        * Seralarda sineklikler kullanılmalıdır.
                        * Vektör böceklerle mücadele teknik talimatlar doğrultusunda yapılmalıdır.
                        2-	Kimyasal Mücadele
                        * Çok bilinen bir kimyasal mücadelesi yoktur.
                        * Bazı durumlarda olgunlaşma döneminden önce sinek ilaçları kullanmanın işe yarayabildiği gözlemlenmiştir.

                        """) 
            st.subheader("Detaylı bilgi için: [yetiştir.net](https://yetistir.net/domateste-sari-yaprak-kivirciklik-virusu/)")
            st.subheader("Detaylı bilgi ve ilaçlar için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/domates-sari-yaprak-kivirciklik-virusu)")

        elif domatess == 'Septoria Yaprak Lekesi':
            col1, col2 = st.columns(2)
            with col1:
                st.image('d.sept3.jpg')
            with col2:
                st.image('d.sept2.png')
            
            st.subheader('Nedir?')
            st.markdown('Esas olarak yapraklarda meydana gelmekle beraber gövdede yaprak ve çiçek sapında da görülmektedir. Yapraklarda küçük sarımsı alanlar şeklinde başlar daha sonra gri veya kahverengiye döner. Lekelerin büyüklüğü hassas çeşitlerde 2.5 cm çapa kadar ulaşır ve yuvarlak şekildedirler. Lekeler üzerinde inokulasyondan 10 gün sonra siyah renkte piknidler gelişir. Piknidiosporları rüzgarla çevreye yayılarak hastalığı başlatır. Hastalık yaşlı yapraklardan genç yapraklara doğru gelişen yaprak dökümüne neden olmaktadır.')
            st.markdown('Hastalığın eşeyli dönemi yoktur. Hastalık etmeni tohumda, tarladaki hastalıklı bitki artıklarında, enfekteli çok yıllık yabancı otlarda canlılığını sürdürür. Enfeksiyonun gerçekleşmesi için nisabi nemin 48 saat süreyle % 100 düzeyinde olması gerekmektedir.')
            st.subheader('Nasıl Mücadele Edilir?')
            st.markdown(""" 
                        1-	Kültürel Önlemler
                        * Temiz tohum kullanılmalıdır. Hastalığın görülmediği bölgelerde tohum üretimi yapılmalıdır.
                        * Hastalık bazı yabancı otlarda da kışladığı için tarlada iyi bir yabancı ot mücadelesi yapılmalıdır.
                        2-	Kimyasal Mücadele
                        * Kimyasal mücadelesinde Mancozeb ve Chlorotholonil ile 7-10 günlük aralıklarla ilaçlama yapılmalıdır.
                        """)
            st.subheader("Detaylı bilgi için: [yetiştir.net](https://yetistir.net/domateste-sari-yaprak-kivirciklik-virusu/)")
            st.subheader("Detaylı bilgi ve ilaçlar için: [hortiturkey](https://www.hortiturkey.com/zirai-mucadele/domates-sari-yaprak-kivirciklik-virusu)")
        
pages = {
    0 : button_one,
    1 : button_two,
}
if "current" not in st.session_state:

    st.session_state.current = 0
st.sidebar.image('tartech2.png', width=300)
# Now you can set the button click to a number and call the linked function


if st.sidebar.button("ANASAYFA"):
        st.session_state.current = 0
if st.sidebar.button("TAHMİNLE"):
        st.session_state.current = 1
st.sidebar.title(' ')
st.sidebar.title(' ')
st.sidebar.write('Danışma için:')
col1, col2, col3, col4 = st.sidebar.columns(4)
with col1:
    st.image('alo.png')
    st.image('alo.png')
    st.image('alo.png')
with col2:
    st.markdown('ALO 180')
    st.markdown('ALO 174')
    st.markdown('ALO 177')
with col3:
    st.image("taror.jpg",width=100)
with col4:
    st.write(' ')


if st.session_state.current != None:
    pages[st.session_state.current]()
    
m = st.markdown("""
            <style>
            div.stButton > button:first-child {
            font-size:23px;
            margin-left: 70px;
            background-color: #ededed);
            }
            </style>""", unsafe_allow_html=True)