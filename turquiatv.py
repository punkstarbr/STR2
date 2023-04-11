#! /usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import requests
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
channel_no = 0
m3u = None
def get_live_info(channel_id):
    try:
        webpage = urlopen(f"{channel_id}/live").read()
        soup = BeautifulSoup(webpage, 'html.parser')
        urlMeta = soup.find("meta", property="og:url")
        if urlMeta is None:
            return None
        url = urlMeta.get("content")
        if(url is None or url.find("/watch?v=") == -1):
            return None
        titleMeta = soup.find("meta", property="og:title")
        imageMeta = soup.find("meta", property="og:image")
        descriptionMeta = soup.find("meta", property="og:description")
        return {
            "url": url,
            "title": titleMeta.get("content"),
            "image": imageMeta.get("content"),
            "description": descriptionMeta.get("content")
        }
    
    except Exception as e:
                return None

banner = r'''
#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/tr/tvplus.com.tr.xml"
"https://iptv-org.github.io/epg/guides/tr/tvplus.com.tr.xml"


ULUSAL KANALLAR 
TRT 1
#EXTINF:-1 tvg-id="TRT1.tr" tvg-language="" tvg-logo="   https://i.ibb.co/d6c87Km/trt122.png  " group-title="TURQUIA",TRT 1
https://tv-trt1-dai.medya.trt.com.tr/master_4.m3u8
https://ddc75c8a6akqr.cloudfront.net/v1/master/80dbfc318ab6b980679b32095ba497236de6d2f9/TRT-1/master.m3u8
TRT 2
#EXTINF:-1 tvg-id="TRT2.tr" tvg-language="" tvg-logo="   https://i.ibb.co/TB5N8cN/trt2.png  " group-title="TURQUIA",TRT 2
http://167.114.115.233:8080/trt2fhd/index.m3u8 
https://tv-trt2.medya.trt.com.tr/master.m3u8
https://tv-trt2.medya.trt.com.tr/master_720.m3u8
TRT BELGESEL
#EXTINF:-1 tvg-id="TRTBelgesel.tr" tvg-language="" tvg-logo="   https://i.ibb.co/N1h8m96/trtbelgesel.png    " group-title="TURQUIA",TRT Belgesel
https://mn-nl.mncdn.com/blutv_trtbelgesel2/live.m3u8 
https://tv-trtbelgesel.live.trt.com.tr/master_720.m3u8
TRT HABER
#EXTINF:-1 tvg-id="TRTHaber.tr" tvg-language="" tvg-logo="   https://i.ibb.co/Bt6frts/trthaber.png   " group-title="TURQUIA",TRT Haber
https://trthaber.blutv.com/blutv_trthaber_live/live_720p2000000kbps/index.m3u8 
TRT MÜZİK
#EXTINF:-1 tvg-id="TRTMuzik.tr" tvg-language="" tvg-logo="     https://i.ibb.co/d6Zfm2P/trtmuzik21c.png    " group-title="TURQUIA",TRT Muzik
https://mn-nl.mncdn.com/blutv_trtmuzik2/live_720p2000000kbps/index.m3u8 
TRT ÇOCUK
#EXTINF:-1 tvg-id="TRTCocuk.tr" tvg-language="" tvg-logo="   https://i.ibb.co/YjkMYbF/trtcocuk21a.png    " group-title="TURQUIA",TRT Cocuk
https://mn-nl.mncdn.com/blutv_trtcocuk_2/trtcocuk.smil/playlist.m3u8 
TRT TÜRK
#EXTINF:-1 tvg-id="TRTTurk.tr" tvg-language="" tvg-logo="       https://i.ibb.co/swtn1kV/trtturk.png      " group-title="TURQUIA",TRT Turk
https://tv-trtturk.medya.trt.com.tr/master_720.m3u8
TRT AVAZ
#EXTINF:-1 tvg-id="TRTAvaz.tr" tvg-language="" tvg-logo="      https://i.ibb.co/xzZk0Yq/trtavaz.png    " group-title="TURQUIA",TRT Avaz
https://tv-trtavaz.medya.trt.com.tr/master_720.m3u8 

TRT SPOR
#EXTINF:-1 tvg-id="TRTSpor.tr" tvg-language="" tvg-logo="    https://i.ibb.co/3WmLjwG/trtspor22c.png      " group-title="TURQUIA",TRT Spor
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9013
http://195.155.98.170:5858/play/a09m
TRT SPOR YILDIZ
#EXTINF:-1 tvg-id="TRTSporYildiz.tr" tvg-language="" tvg-logo=" https://i.ibb.co/ky3qVPc/trtspory2.png  " group-title="TURQUIA",TRT Spor Yıldız
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/18651
http://195.155.98.170:5858/play/a09u
A SPOR
#EXTINF:-1 tvg-id="ASpor.tr" tvg-name="" tvg-language="" tvg-logo="  https://i.ibb.co/xSjB51j/aspor.png  " group-title="TURQUIA",a spor
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9012
DISCOVERY SCIENCE
#EXTINF:-1 tvg-id="DiscoveryScienceTurkey.tr" tvg-name="" group-title="TURQUIA"  tvg-logo=" https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Discovery_Science_2017_Logo.svg/1280px-Discovery_Science_2017_Logo.svg.png   "   ,Discovery Science Turkey
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/237
VIASAT HISTORY
#EXTINF:-1 tvg-id="" tvg-name="" group-title="TURQUIA"  tvg-logo=" https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Viasat_History_Logo.jpg/167px-Viasat_History_Logo.jpg   "   ,Viasat History Turkey
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/239
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/16891



FOX
#EXTINF:-1 tvg-id="FoxTurkey.us" tvg-language="" tvg-logo="    https://i.ibb.co/4tyCssZ/fox.png     " group-title="TURQUIA",Fox Turkey
https://foxtv.blutv.com/blutv_foxtv_live/live_720p2000000kbps/index.m3u8 
SHOW
#EXTINF:-1 tvg-id="ShowTV.tr" tvg-language="" tvg-logo="   https://i.ibb.co/BrGNZJ4/showtv.png       " group-title="TURQUIA",Show TV
https://showtv.blutv.com/blutv_showtv_live/live.m3u8
SHOW TÜRK
#EXTINF:-1 tvg-id="ShowTurk.tr" tvg-language=""   tvg-logo="      https://i.ibb.co/WvhGGP0/showturk1.png    " group-title="TURQUIA",Show Turk
https://mn-nl.mncdn.com/blutv_showturk2/live_720p2000000kbps/index.m3u8 
STAR
#EXTINF:-1 tvg-id="StarTV.tr" tvg-language="" tvg-logo="    https://i.ibb.co/PcDpxSH/startr1.png      " group-title="TURQUIA",Star TV
https://startv.blutv.com/blutv_startv_live/live_720p2000000kbps/index.m3u8 
EURO STAR
#EXTINF:-1 tvg-id="EuroStar.tr" tvg-language="" tvg-logo="    https://i.ibb.co/Lg90xsB/eurostar22.png      " group-title="TURQUIA",Euro Star
https://mn-nl.mncdn.com/blutv_eurostar2/live.m3u8 
KANAL D
#EXTINF:-1 tvg-id="KanalD.tr" tvg-language="" tvg-logo="     https://i.ibb.co/s9mVqWH/kanald.png    " group-title="TURQUIA",Kanal D 
https://demiroren-live.daioncdn.net/kanald/kanald_1080p.m3u8
https://kanald.blutv.com/blutv_kanald_live/live.m3u8
EURO D
#EXTINF:-1 tvg-id="EuroD.tr" tvg-language="" tvg-logo="     https://i.ibb.co/THj0Jrg/eurod22.png     " group-title="TURQUIA",Euro D 
https://live.duhnet.tv/S2/HLS_LIVE/eurodnp/playlist.m3u8
https://mn-nl.mncdn.com/blutv_eurod2/live.m3u8 
KANAL 7
#EXTINF:-1 tvg-id="Kanal7.tr" tvg-language="" tvg-logo="    https://i.ibb.co/1s3fHfm/k7tr1.png     " group-title="TURQUIA",Kanal 7 
https://kanal7.blutv.com/blutv_kanal7_live/live_720p2000000kbps/index.m3u8 
KANAL 7 AVRUPA
#EXTINF:-1 tvg-id="Kanal7Avrupa.tr" tvg-language="" tvg-logo="     https://i.ibb.co/cDxKJy1/k7avr1.png   " group-title="TURQUIA",Kanal 7 Avrupa 
https://live.kanal7.com/live/kanal7AvrupaLive/index.m3u8 

ATV
EXTINF:-1 tvg-id="  ATV.tr  " tvg-name="" group-title="TURQUIA"tvg-logo=" https://seeklogo.com/images/A/atv-logo-C72353DBDA-seeklogo.com.png",ATV
https://api1.canlitvplayer.com/streamer1.ruslanatv.ru/turkey/atv_turk_stream_sd_2023/playlist.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9NS8xMi8yMDE4IDEwOjExOjA2IFBNJmhhc2hfdmFsdWU9cGtzUElvZjBwOUFIcDZRenpxQmxLdz09JnZhbGlkbWludXRlcz01
#EXTINF:-1 tvg-id="  ATV.tr  " tvg-name="" group-title="TURQUIA"tvg-logo=" https://seeklogo.com/images/A/atv-logo-C72353DBDA-seeklogo.com.png",ATV
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/483

TV8
#EXTINF:-1 tvg-id="TV8.tr" tvg-language=""  tvg-name="" tvg-logo="    https://i.ibb.co/tXKXNDz/tv8.png      " group-title="TURQUIA",TV8 
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/487
https://tv8.daioncdn.net/tv8/tv8_1080p.m3u8?&app=7ddc255a-ef47-4e81-ab14-c0e5f2949788&ce=3
TV 8.5
#EXTINF:-1 tvg-id="TV85.tr" tvg-name="" tvg-language="" tvg-logo="    https://i.ibb.co/dgj3MTh/tv85.png      " group-title="TURQUIA",TV 8.5 
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9014

TLC
#EXTINF:-1 tvg-id="TLCTurkey.tr" tvg-language="" tvg-logo="    https://i.ibb.co/Z1vHy41/tlc.png   " group-title="TURQUIA",TLC 
https://tlc.blutv.com/blutv_tlc_live/live.m3u8 
DMAX
#EXTINF:-1 tvg-id="DMAXTurkey.tr" tvg-language="" tvg-logo="   https://i.ibb.co/QQQR6VK/dmax.png      " group-title="TURQUIA",DMAX 
https://mn-nl.mncdn.com/blutv_dmax_dvr/live.m3u8 
CNNTÜRK
#EXTINF:-1 tvg-id="CNNTurk.us" tvg-language="" tvg-logo="    https://i.ibb.co/JqWCczW/cnnturk1.png  " group-title="TURQUIA",CNN Turk 
https://live.duhnet.tv/S2/HLS_LIVE/cnnturknp/playlist.m3u8
https://cnnturk.blutv.com/blutv_cnnturk_live/live.m3u8
HABERTÜRK
#EXTINF:-1 tvg-id="Haberturk.tr" tvg-language="" tvg-logo="   https://i.ibb.co/wdwm0fn/haberturk.png     " group-title="TURQUIA",Haberturk 
https://haberturk.blutv.com/blutv_haberturk_live/live_720p2000000kbps/index.m3u8 

BLOOMBERG 
EXTINF:-1 tvg-id="BloombergHT.us" tvg-logo="    https://i.ibb.co/HXKrJRC/blght22.png   " group-title="TURQUIA",Bloomberg HT 
https://mn-nl.mncdn.com/blutv_bloomberght2/live_720p2000000kbps/index.m3u8 
HABER GLOBAL
EXTINF:-1 tvg-id="Haberglobal.tr" tvg-logo="     https://i.ibb.co/vw0q9KH/haberglobal22.png   " group-title="TURQUIA",Haber Global 
https://mn-nl.mncdn.com/blutv_haberglobal2/live.m3u8

HALK TV
#EXTINF:-1 tvg-id="HalkTV.tr" tvg-language="" tvg-logo="    https://i.ibb.co/BtYMK4q/halk21a.png     " group-title="TURQUIA",Halk TV 
https://mn-nl.mncdn.com/blutv_halktv2/live.m3u8
https://halktv-live.ercdn.net/halktv/halktv.m3u8
KRT
#EXTINF:-1 tvg-id="KRT.tr" tvg-language="" tvg-logo="   https://i.ibb.co/ZT2fQq3/krt.png      " group-title="TURQUIA",KRT 
https://krt.blutv.com/blutv_krt_live/live_720p2000000kbps/index.m3u8 
TELE 1
#EXTINF:-1 tvg-id="Tele1.tr" tvg-language="" tvg-logo="  https://i.ibb.co/4Mhmggc/tele1.png    " group-title="TURQUIA",Tele 1 
https://tele1.blutv.com/blutv_tele1_live/live.m3u8 
NTV
#EXTINF:-1 tvg-id="NTV.tr" tvg-language="" tvg-logo="   https://i.ibb.co/9c7MvWX/ntv.png     " group-title="TURQUIA",NTV 
https://ntvdvr.blutv.com/blutv_ntv_dvr2/live_720p2000000kbps/index.m3u8 
TV100
#EXTINF:-1 tvg-id="TV100.tr" tvg-language="" tvg-logo="     https://i.ibb.co/bLpTdYZ/tv100.png    " group-title="TURQUIA",TV 100 
https://mn-nl.mncdn.com/blutv_tv1002/live_720p2000000kbps/index.m3u8 
BEYAZ
#EXTINF:-1 tvg-id="BeyazTV.tr" tvg-language="" tvg-logo="   https://i.ibb.co/0tc3PYz/beyaz22b.png    " group-title="TURQUIA",Beyaz TV 
https://mn-nl.mncdn.com/blutv_beyaztv2/live.m3u8 
360
#EXTINF:-1 tvg-id="360.tr" tvg-language="" tvg-logo="    https://i.ibb.co/FVnG3Zr/360tv.png   " group-title="TURQUIA",360
https://360tv.blutv.com/blutv_360tv_live/live_720p2000000kbps/index.m3u8 
FLASH
#EXTINF:-1 tvg-id="FlashTV.tr" tvg-language="" tvg-logo="    https://i.ibb.co/F5FcvbZ/flash4ok.png   " group-title="TURQUIA",Flash TV 
https://mn-nl.mncdn.com/blutv_flashtv/live.m3u8 

AKILLI
EXTINF:-1 tvg-id="AkilliTV.tr" tvg-language="" tvg-logo="  https://i.ibb.co/8dQdNrv/akilli22.png     " group-title="TURQUIA",Akilli TV 
http://iptvmasterlink.dyndns.org:8080/AkilliTv/playlist.m3u8 

DİYANET
#EXTINF:-1 tvg-id="DiyanetTV.tr" tvg-language="" tvg-logo="    https://i.ibb.co/k9phm3v/diyanettv.png      " group-title="TURQUIA",Diyanet TV 
https://mn-nl.mncdn.com/blutv_diyanet2/live.m3u8

UÇANKUŞ
EXTINF:-1 tvg-id="UcanKusTV.tr" tvg-logo="    https://i.ibb.co/8dyQHrQ/ucankus22.png    " group-title="TURQUIA",Uçankuş TV 
https://mn-nl.mncdn.com/blutv_ucankus2/live_720p2000000kbps/index.m3u8 

MAVİ KARADENİZ TV
EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  http://www.mavikaradeniztv.com.tr/logo.png  " group-title="TURQUIA",mavi karadeniz
https://h125.artiyerelmedya.net/mavikaradeniz/bant1/chunks.m3u8?nimblesessionid=105806626
https://waw3.artiyerelmedya.net/mavikaradeniz/bant1/playlist.m3u8

TRT EBA
EXTINF:-1 tvg-logo="https://i.ibb.co/zfwmCCp/ilkoku22.png" group-title="TURQUIA",TRT EBA Ilkokul
https://mn-nl.mncdn.com/blutv_ebai2/live.m3u8
EXTINF:-1 tvg-logo="https://i.ibb.co/1JbF8xB/ortaoku22.png.png" group-title="TURQUIA",TRT EBA Ortaokul
https://mn-nl.mncdn.com/blutv_ebao2/live.m3u8
EXTINF:-1 tvg-logo="https://i.ibb.co/v42mWjF/lise22.png" group-title="TURQUIA",TRT EBA Lise
https://mn-nl.mncdn.com/blutv_ebal2/live.m3u8

TEVE2
#EXTINF:-1 tvg-id="Teve2.tr" tvg-language="" tvg-logo="    https://i.ibb.co/1Z22dCY/teve2.png      " group-title="TURQUIA",Teve2 
https://demiroren-live.daioncdn.net/teve2/teve2.m3u8
https://teve2.blutv.com/blutv_teve2_live/live.m3u8
DENIZPOSTASI
#EXTINF:-1 tvg-logo="  https://yerelmedya.tv/logosTV/denizpostasitv.png   " group-title="TURQUIA",DENiZ POSTASI TV
https://h125.artiyerelmedya.net/denizpostasitv/bant1/chunks.m3u8
TV6
#EXTINF:-1 tvg-logo="https://i.ibb.co/sRNHKjS/tivi622.png" group-title="TURQUIA",TIVI 6
https://waw1.artiyerelmedya.net/tivi6/bant1/playlist.m3u8
TİVİ TÜRK
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="   https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6U0FimhNMRWumIIiBOgbuQw9cDfaiLcS7c5c9ZBQ&s       " group-title="TURQUIA",tivi TÜRK 
https://stream.tiviturk.de/live/tiviturk.m3u8 
NTN
#EXTINF:-1 tvg-id="  " tvg-language="" tvg-logo="    https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAgWUBiuFNXnxf12orAZisRQMSI128YiioeSjiOBHq4CXivyWUBH7i47-Uiifq2g25bVTPV92zxqWNC6u6UvebRJKVjRydTdrufYOzE9ER-lS5-cQN1MEbPVJ3oIBMJXMn10Om7Hz4CUvC0MhPgCT42L1Odizl19YeP5C9O6_cEzD3tPKEFcbUW6N-Wg/s1600/ntns.jpg      " group-title="TURQUIA",NTN 
https://tv.ntnhd.com:3588/multi_web/play_1080.m3u8 

YANSIMA CLASSIC
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnqd9MMDintAoyNlZ0auLUY2ZvztJF463rwGr-O5Dnhw8cTJxef7cTOwPzoFD61kCG6Hg8ykmZ6DE6svUb-40PGJaoywE9iEJ7uh_V6o1q0LFVJG5KZekcoMVgr1X9Lw6LT-h3tygQJG6Dqg9FYeZSU0FtuLiAlZ-bTrazs0cBmSALMcVRWEr_jWeexA/s1600/classic.jpg  " group-title="TURQUIA",Yansıma Classic
https://stream.mylive.in.th/live/yansimaclassic/yansimaclassic.m3u8
YANSIMA SİNEMA
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1eYQOGF6-ELbkd5rIxFwqU5d2_zshA6n7L9DRruWGm_g-W5NoBwgO5lHoNPv6Kz0myhpb6VVdZDiXEk_hwH5JY2uAXqAMiGf8IVhR3NuB48KPLXviOEIJqgFvZbR_xWQXIX-w1NuCQ_zi_-RFxHmDdV8DLvfmQYiKzn-GMnNMNrri7tLTFgqN8Uv1qg/s1600/sinema.jpg  " group-title="TURQUIA",Yansıma Sinema
https://stream.mylive.in.th/live/yansimatv/yansimatv.m3u8

YEŞİLÇAM
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://upload.wikimedia.org/wikipedia/tr/d/d5/Ye%C5%9Fil%C3%A7am_TV_logosu.png  " group-title="TURQUIA",Yeşilçam
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9121
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://upload.wikimedia.org/wikipedia/tr/d/d5/Ye%C5%9Fil%C3%A7am_TV_logosu.png  " group-title="TURQUIA",Yeşilçam
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/273

#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://upload.wikimedia.org/wikipedia/tr/d/d5/Ye%C5%9Fil%C3%A7am_TV_logosu.png  " group-title="TURQUIA",Yeşilçam
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9099
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://upload.wikimedia.org/wikipedia/tr/d/d5/Ye%C5%9Fil%C3%A7am_TV_logosu.png  " group-title="TURQUIA",Yeşilçam
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9120
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="  https://upload.wikimedia.org/wikipedia/tr/d/d5/Ye%C5%9Fil%C3%A7am_TV_logosu.png  " group-title="TURQUIA",Yeşilçam
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/16911

BEIN MOVIES STARS
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="    " group-title="TURQUIA",beIN Movies Stars Turkey
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/284
BEIN SERIES SCI-FI
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo="    " group-title="TURQUIA",beIN Series Sci-Fi Turkey
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/17897
SINEMA TV 1001
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema 1001
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9006
SINEMA TV 1002
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema 1002
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9005
SINEMA TV
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema TV
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9108
SINEMA 2
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema 2
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/17891
SINEMA AİLE 
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema Aile
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/9109
SINEMA AKSIYON
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema Aksiyon
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/268
SINEMA TV
#EXTINF:-1 tvg-id="" tvg-language="" tvg-logo=" " group-title="TURQUIA",Sinema Yerli
http://stream.detr.xyz:8080/Dwabash500/V6R8UtakqW/267

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000
'''


def generate_youtube_tv():
    global channel_no
    ydl_opts = {
        'format': 'best',
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with open('turquiatv.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            channel = get_live_info(line)
            if channel is None:
                continue
            try:
                with ydl:
                    result = ydl.extract_info(
                        f"{line}/live",
                        download=False  # We just want to extract the info
                    )

                    if 'entries' in result:
                        # Can be a playlist or a list of videos
                        video = result['entries'][-1]
                    else:
                        # Just a video
                        video = result
                video_url = video['url']
                canalnome = video['channel']

                channel_no += 1
                channel_name = f"{channel_no}-{line.split('/')[-1]}"
                playlistInfo = f"#EXTINF:-1 tvg-chno=\"{channel_no}\" tvg-id=\"{canalnome}\" tvg-base=\"{line}\" tvg-name=\"{channel_name}\" tvg-logo=\"{channel.get('image')}\" group-title=\"TURQUIA\",{channel.get('title')}\n"
                write_to_playlist(playlistInfo)
                write_to_playlist(video_url)
                write_to_playlist("\n")
            except Exception as e:
                print(e)
                        



def write_to_playlist(content):
    global m3u    
    m3u.write(content)
    

def create_playlist():
    global m3u
    m3u = open("turquiatv.m3u", "w")
  
        
    m3u.write("\n")

    
def close_playlist():
    global m3u
    m3u.close()
def generate_youtube_PlayList():
    create_playlist()
        
    m3u.write(banner)

    generate_youtube_tv()
    

    close_playlist()


    
if __name__ == '__main__':
    generate_youtube_PlayList()   
