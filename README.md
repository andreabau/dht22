Aosong DHT22
=============

This module contains the [Zerynth](https://www.zerynth.com/) driver for Aosong DHT22 temperature and humidity sensor (also named AM2302, [datasheet](http://akizukidenshi.com/download/ds/aosong/AM2302.pdf)).

It uses a single wire for data communication so a pin with ICU peripheral is needed.

This library is based on the work of:
[link 1](https://hackaday.io/project/8242-viperphoton-weather-station/log/28666-dht22-temperaturehumidity-sensor)
[link 2](https://community.zerynth.com/discussion/249/reading-temperature-and-humidity)

Example:

    import dht22
    
    temp, hum = dht22.get_temp_hum(D3, D3.ICU)
    
