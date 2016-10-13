# -*- coding: utf-8 -*-
#
#    bitcoinlib secp256k1.py
#    Copyright (C) 2016 October 
#    1200 Web Development
#    http://1200wd.com/
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import ecdsa


# Parameters secp256k1
#  from http://www.secg.org/sec2-v2.pdf, par 2.4.1
secp256k1_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
secp256k1_n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
secp256k1_b = 0x0000000000000000000000000000000000000000000000000000000000000007L
secp256k1_a = 0x0000000000000000000000000000000000000000000000000000000000000000L
secp256k1_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
secp256k1_Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8L

curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(secp256k1_p, secp256k1_a, secp256k1_b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, secp256k1_Gx, secp256k1_Gy, secp256k1_n)

# oid_secp256k1 = (1, 3, 132, 0, 10)
# SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1)
# ec_order = _r

curve = curve_secp256k1
generator = generator_secp256k1