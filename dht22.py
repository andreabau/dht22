"""
.. module:: dht22

**************
Aosong DHT22
**************

This module contains the driver for Aosong DHT22 temperature and humidity sensor (also named AM2302).
It uses a single wire for data communication so a pin with ICU peripheral is needed (`datasheet <http://akizukidenshi.com/download/ds/aosong/AM2302.pdf>`_).

This library is based on the work of:
`link 1 <https://hackaday.io/project/8242-viperphoton-weather-station/log/28666-dht22-temperaturehumidity-sensor>`_
`link 2 <https://community.zerynth.com/discussion/249/reading-temperature-and-humidity>`_

Example: ::
    
    import dht22
    
    temp, hum = dht22.get_temp_hum(D3, D3.ICU)
    
    """

# Modified: 05/06/2017

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

    
import icu

def _bitlist_to_int(bit_list):
    int = 0
    for i in range(len(bit_list)):
        int |= bit_list[i] << i
    return int


def get_temp_hum(pin, pin_icu):
    """
    .. function:: get_temp_hum(pin, pin_icu)
    
        Returns temperature in degree Celsius and relative humidity.
    
    """
    pinMode(pin, OUTPUT)

    digitalWrite(pin, HIGH)
    sleep(10)
    digitalWrite(pin, LOW)
    sleep(10)

    tmpICU = icu.capture(pin_icu, LOW, 86, 10000, time_unit=MICROS)

    digitalWrite(pin, HIGH)
    pinMode(pin, INPUT_PULLUP)

    bits_list = [0 if e < 35 else 1 for e in tmpICU[3::2]]

    t_bit = bits_list[16:32]
    t_bit = t_bit[::-1]
    t_sign = 1
    if t_bit[-1] == 1:
        t_sign = -1
        t_bit[-1] = 0

    h_bit = bits_list[0:16]
    h_bit = h_bit[::-1]

    t = t_sign * _bitlist_to_int(t_bit) / 10
    h = _bitlist_to_int(h_bit) / 10

    return t, h
