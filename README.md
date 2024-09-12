# Spotify Data Visualization Project

Bu proje, Spotify API'sini kullanarak belirli bir sanatçının albümlerini ve parçalarını analiz etmek ve görselleştirmek için tasarlanmıştır. Spotify API'den gelen verilerle şarkıların ses özellikleri (audio features) alınır ve bunlar çeşitli grafikler ile görselleştirilir.

## Gereksinimler (`requirements.txt`)

Bu projeyi çalıştırmadan önce aşağıdaki bileşenlerin sisteminizde yüklü olduğundan emin olun:

- Python 3.6 veya üstü
- `requests` kütüphanesi
- `pandas` kütüphanesi
- `matplotlib`, `seaborn`, `plotly` gibi görselleştirme kütüphaneleri

Bu projeyi kullanmak için aşağıdaki adımları takip edin:

### 1. Spotify API'ye Kaydolun ve Gerekli Bilgileri Alın

Projeyi çalıştırmak için Spotify Developer hesabına ihtiyacınız var. [Spotify Developer](https://developer.spotify.com/dashboard/login) üzerinden bir hesap oluşturun ve bir uygulama yaratın. Bu uygulama size **Client ID** ve **Client Secret** verecektir.

### 2. Gerekli Kütüphaneleri Yükleyin

Gerekli Python kütüphanelerini `requirements.txt` dosyasını kullanarak yükleyebilirsiniz:

```bash
pip install -r requirements.txt
