import os,sys,telebot,requests,time
from google import google

token = ""
id = "rapor_yollanacak_kişinin_idsi"

###
bot = telebot.TeleBot(token)
#

#
try:
    @bot.message_handler(["start"])
    def ilk(mesaj):
        bot.send_message(mesaj.chat.id,f"{mesaj.chat.first_name} Hoşgeldin !\n\nKulla. adı : {mesaj.chat.username}\nKulla. id    : {mesaj.chat.id}\n\n@pngmerkez with TG Search Engine k:@telegoogleTRBot\n\nKomutlar için : /komutlar")
    #
    #
    #
    @bot.message_handler(["yardım","help","komutlar","notlar","yardim","Yardım","Yardim","Help","Komutlar","Notlar","not","Not","komut","Komut"])
    def yardim(mesaj):
        bot.send_message(mesaj.chat.id,f"""Bu mesajı görüntülemek için : /komutlar\n\nGoogle'da ara : /google aranacak kelimeler\nYandex'de ara : /yandex aranacak kelime\nDuckduck'da ara : /duck aranacak kelime\n\nSunucu cihaz : {os.uname().machine}{os.uname().release}\nPy sürümü : {sys.version}\nKaynak Kodları : bit.ly/2TYOdFm | bit.ly/3d7FKXX\n\n@pngmerkez 'de paylaşılan tüm kodlar GNU Genel Açık Lisans v3 ile korunmaktadır . İstediğiniz yerde istediğiniz gibi kullanabilirsiniz . Yeterki bilgi yayalım virüs değil :)""")


    @bot.message_handler(["google","Google","ara"])
    def google(mesaj,google=google):
        try:
            try:
                from google import google
                ara = mesaj.text.split()[1:]
                ara = " ".join(ara)
                if not ara:bot.reply_to(mesaj,f"Örnek :   {mesaj.text.split()[0]} kekik akademi ")
                else:
                    log = ara + f" :  {mesaj.chat.first_name} | {mesaj.chat.username} | {mesaj.chat.id} "
                    print(log)
                    with open("log.txt","a") as logtxt:
                        logtxt.write(log+"\n")
                    bot.reply_to(mesaj,"Aranıyor lütfen bekleyin !")
                    sonuc = google.search(ara)
                    
                    bot.send_message(mesaj.chat.id,f"'{ara} ' Sonuçları : \n")
                    if not sonuc:
                        bot.reply_to(mesaj,f"Görünüşe göre arama bulunamadı ! Tekrar dene yada bildir  [ /bildir geri bildirim mesajı ]")
                        print(log ," \033[31mBaşarısız !\033[0m")
                    else:
                        for i in sonuc:
                            bot.send_message(mesaj.chat.id,f"{i.name}\n{i.link}")
            except IndexError:
                bot.send_message(mesaj.chat.id,"Örnek : /google Python")
            except requests.exceptions.ConnectionError:
                bot.send_message(mesaj.chat.id,"Ağ hatası ! | Bildirildi")
                print("Req ağ hatası")
                bot.send_message(id,f"Req ağ hatası !\n\n{hata}\n\nAtan kişinin: \n\nIsim : {mesaj.chat.first_name}\nKull. adi : {mesaj.chat.username}\n Id : {mesaj.chat.id}\n\nMesaj : {str(mesaj.text)}")

            except Exception as hata:
                bot.send_message(mesaj.chat.id,"Attığın mesaj kabul edilmiyor | Bildirildi !")
                print("Genel hata !")
                bot.send_message(id,f"Genel Hata !\n\n{hata}\n\nAtan kişinin: \n\nIsim : {mesaj.chat.first_name}\nKull. adi : {mesaj.chat.username}\n Id : {mesaj.chat.id}\n\nMesaj : {str(mesaj.text)}")
        except Exception as hata:
            try:requests.post("https://api.telegram.org/bot"+token,data={"chat_id":id,"text":hata +"\n\nTümden hata alındı !\n\nSavuşturuldu .."})
            except:time.sleep(10)
    
    @bot.message_handler(["ping"])
    def mesaj(mesaj):
        bot.reply_to(mesaj,"Çalışıyor !")

    @bot.message_handler(["yandex","duck"])
    def diger(mesaj):
        bot.reply_to(mesaj,"Merhaba , henüz bu motorları desteklmiyoruz\n\n/ara veya \google ile googlayın :)")

except Exception as hata:
    print(f"Genel hata alındı ! {id}'ye yollanıyor !\n\n{hata}")
    try:
        bot.send_message(id,f"Genel hata tespit edildi ! \n\n{hata}")
        bot.
    except:
        print("\n\n\aMesaj yollanamadı . Internet bağlantısında sıkıntı olabilir . 10 saniye Bekleniyor !")
        time.sleep(10)
bot.polling()
