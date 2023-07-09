#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from klvdata.common import hexstr_to_bytes
from klvdata.element import UnknownElement
from klvdata.elementparser import BytesElementParser
from klvdata.elementparser import DateTimeElementParser
from klvdata.elementparser import MappedElementParser
# from klvdata.elementparser import StringElementParser
from klvdata.setparser import SetParser
from klvdata.streamparser import StreamParser


class UnknownElement(UnknownElement):
    pass


@StreamParser.add_parser
class FlirMetadataSet(SetParser):
    """FLIR UAS Local Metadata Set
    """
    key = hexstr_to_bytes('FA AB 94 31 - BB 11 4A AA – BD C6 FA 9E - B1 B6 24 5A')
    name = 'FLIR Datalink Local Set'
    key_length = 3
    parsers = {}

    _unknown_element = UnknownElement


@FlirMetadataSet.add_parser
class Checksum(BytesElementParser):
    """Checksum used to detect errors within a UAV Local Set packet.

    Checksum formed as lower 16-bits of summation performed on entire
    LS packet, including 16-byte US key and 1-byte checksum length.

    Initialized from bytes value as BytesValue.
    """
    key = b'\x01'
    TAG = 1
    UDSKey = "-"
    LDSName = "Checksum"
    ESDName = ""
    UDSName = ""


@FlirMetadataSet.add_parser
class FlirField_00(BytesElementParser):
    key = b'\x82\x50\x00' # len 8
    TAG = 8540160
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_01(BytesElementParser):
    key = b'\x82\x50\x01' # len 2
    TAG = 8540161
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_02(BytesElementParser):
    key = b'\x82\x50\x02' # len 2
    TAG = 8540162
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_03(BytesElementParser):
    key = b'\x82\x50\x03' # len 2
    TAG = 8540163
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_04(BytesElementParser):
    key = b'\x82\x50\x04' # len 1
    TAG = 8540164
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_05(BytesElementParser):
    key = b'\x82\x50\x05' # len 2
    TAG = 8540165
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_06(BytesElementParser):
    key = b'\x82\x50\x06' # len 1
    TAG = 8540166
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_07(BytesElementParser):
    key = b'\x82\x50\x07' # len 1
    TAG = 8540167
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_08(BytesElementParser):
    key = b'\x82\x50\x08' # len 1
    TAG = 8540168
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_09(BytesElementParser):
    key = b'\x82\x50\x09' # len 1
    TAG = 8540169
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_0A(BytesElementParser):
    key = b'\x82\x50\x0A' # len 2
    TAG = 8540170
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_0B(BytesElementParser):
    key = b'\x82\x50\x0B' # len 2
    TAG = 8540171
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_0C(BytesElementParser):
    key = b'\x82\x50\x0C' # len 2
    TAG = 8540172
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_0D(BytesElementParser):
    key = b'\x82\x50\x0D' # len 2
    TAG = 8540173
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_16(BytesElementParser):
    key = b'\x82\x50\x16' # len 2
    TAG = 8540182
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_17(BytesElementParser):
    key = b'\x82\x50\x17' # len 1
    TAG = 8540183
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_18(BytesElementParser):
    key = b'\x82\x50\x18' # len 2
    TAG = 8540184
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_19(BytesElementParser):
    key = b'\x82\x50\x19' # len 1
    TAG = 8540185
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1A(BytesElementParser):
    key = b'\x82\x50\x1A' # len 2
    TAG = 8540186
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1B(BytesElementParser):
    key = b'\x82\x50\x1B' # len 2
    TAG = 8540187
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1C(BytesElementParser):
    key = b'\x82\x50\x1C' # len 1
    TAG = 8540188
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1D(BytesElementParser):
    key = b'\x82\x50\x1D' # len 1
    TAG = 8540189
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1E(BytesElementParser):
    key = b'\x82\x50\x1E' # len 2
    TAG = 8540190
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_1F(BytesElementParser):
    key = b'\x82\x50\x1F' # len 1
    TAG = 8540191
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_20(BytesElementParser):
    key = b'\x82\x50\x20' # len 1
    TAG = 8540192
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_26(DateTimeElementParser):
    key = b'\x82\x50\x26' # len 8 timestamp
    TAG = 8540198
    UDSKey = "06 0E 2B 34 01 01 01 03 07 02 01 01 01 05 00 00"
    LDSName = "Precision Time Stamp"
    ESDName = ""
    UDSName = "User Defined Time Stamp"

@FlirMetadataSet.add_parser
class FlirField_27(BytesElementParser):
    key = b'\x82\x50\x27' # len 1
    TAG = 8540199
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_28(BytesElementParser):
    key = b'\x82\x50\x28' # len 1
    TAG = 8540200
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_29(BytesElementParser):
    key = b'\x82\x50\x29' # len 0
    TAG = 8540201
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_2A(BytesElementParser):
    key = b'\x82\x50\x2A' # len 4
    TAG = 8540202
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_2B(BytesElementParser):
    key = b'\x82\x50\x2B' # len 4
    TAG = 8540203
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_2D(BytesElementParser):
    key = b'\x82\x50\x2D' # len 1
    TAG = 8540205
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_2E(BytesElementParser):
    key = b'\x82\x50\x2E' # len 1
    TAG = 8540206
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_2F(BytesElementParser):
    key = b'\x82\x50\x2F' # len 24
    TAG = 8540207
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_33(BytesElementParser):
    key = b'\x82\x50\x33' # len 1
    TAG = 8540211
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_34(BytesElementParser):
    key = b'\x82\x50\x34' # len 24
    TAG = 8540212
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_35(BytesElementParser):
    key = b'\x82\x50\x35' # len 1
    TAG = 8540213
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_36(BytesElementParser):
    key = b'\x82\x50\x36' # len 1
    TAG = 8540214
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_39(BytesElementParser):
    key = b'\x82\x50\x39' # len 2
    TAG = 8540217
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_3F(BytesElementParser):
    key = b'\x82\x50\x3F' # len 2
    TAG = 8540223
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_40(BytesElementParser):
    key = b'\x82\x50\x40' # len 2
    TAG = 8540225
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_41(BytesElementParser):
    key = b'\x82\x50\x41' # len 2
    TAG = 8540225
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField_42(BytesElementParser):
    key = b'\x82\x50\x42' # len 2
    TAG = 8540226
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""

@FlirMetadataSet.add_parser
class FlirField50:
    key = b'\x82\x50\x50' # len 2
    TAG = 8540240
    UDSKey = "-"
    LDSName = "Unknown"
    ESDName = ""
    UDSName = ""
