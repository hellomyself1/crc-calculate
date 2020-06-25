# -*- coding: utf-8 -*-


class AllCrcItems:
    CRC_8 = 0
    CRC_16 = 1
    CRC_24 = 2
    CRC_32 = 3


DictCommandInfo = {
    "CRC_8": "the poly is : x^8 + x^5 + x^4 + 1",
    "CRC_16": "the poly is : x^16 + x^12 + x^5 + 1",
    "CRC_24": "the poly is : x^24 + x^23 + x^6 + x^5 + x + 1",
    "CRC_32": "the poly is : x^32+ x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1",
}

DictCommandInfoMacro = {
    "CRC_8": AllCrcItems.CRC_8,
    "CRC_16": AllCrcItems.CRC_16,
    "CRC_24": AllCrcItems.CRC_24,
    "CRC_32": AllCrcItems.CRC_32,
}