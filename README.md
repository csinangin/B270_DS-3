# Ana Sınıf ve Alt Sınıflar İle Modüler Yapı

## Ana Sınıf (Parent Class)
Ana bir sınıf oluşturup, temel işlevleri burada tanımlayabilirsiniz. Örneğin, MLToolkit isimli bir ana sınıf oluşturabilirsiniz. Bu sınıf, genel özellikleri ve başlatma işlemlerini barındırır.

## Alt Sınıflar (Subclassing)
Alt sınıflar, her bir amaca yönelik işlevsellik içerecek şekilde organize edilebilir:

1. **Preprocessing**
Veriyi temizleme, eksik değerleri işleme, normalizasyon gibi ön işlem adımları için bir alt sınıf.

2. **FeatureEngineering:**
Öznitelik oluşturma ve dönüştürme gibi işlemler için bir alt sınıf.

3. **Modeling:**
Model eğitimi, model seçimi ve hiperparametre ayarları için bir alt sınıf.

4. **Evaluation:**
Model değerlendirme metrikleri ve karşılaştırmalar için bir alt sınıf.

5. **Visualization:**
Grafiklerle veri ve model sonuçlarını görselleştirme için bir alt sınıf.

## Yapının Avantajları
Bu alt sınıflar, MLToolkit ana sınıfına bağlanarak gerektiğinde aynı kütüphane içinde birden fazla fonksiyon kullanabilmenizi sağlar. Bu, kodunuzu daha modüler ve yeniden kullanılabilir hale getirir.
