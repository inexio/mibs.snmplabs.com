#
# PySNMP MIB module RAISECOM-PONSERIES-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAISECOM-PONSERIES-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:51:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Counter32, Counter64, Bits, ObjectIdentity, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "Bits", "ObjectIdentity", "Integer32", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PONDeviceType(TextualConvention, Integer32):
    description = 'Iscom EPON and GPON device series Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 550400, 550401, 550402, 550800, 550801, 560000, 580000, 580001, 680000, 510100, 510101, 510102, 510103, 510104, 510000, 510001, 510002, 510003, 510004, 510005, 510008, 510204, 510222, 510224, 510300, 510301, 510400, 510401, 510402, 510403, 510404, 510405, 510406, 510407, 510408, 510410, 510411, 510415, 510460, 510461, 510462, 510500, 510501, 510503, 510504, 510505, 510506, 510600, 510507, 510508, 510509, 520100, 530402, 540400, 540401, 510510, 510511, 510601, 510512, 510513, 510515, 510516, 510517, 510563, 510800, 510801, 510802, 510803, 510804, 511600, 511601, 511605, 511602, 511604, 512400, 512401, 512402, 512404, 520400, 520401, 520402, 520403, 520404, 520405, 520800, 520801, 521600, 521601, 521602, 522400, 522401, 522402, 530400, 530401, 510006, 510007, 510409, 510604, 540402, 540403, 530403, 520407, 540406, 510806, 510518, 510805, 510603, 510564, 561000, 520406))
    namedValues = NamedValues(("unknow", 0), ("others", 1), ("onu-1", 2), ("onu-2", 3), ("onu-4", 4), ("onu-8", 5), ("onu-16", 6), ("onu-24", 7), ("iscom5504A", 550400), ("iscom5504B", 550401), ("iscom5504PI", 550402), ("iscom5508", 550800), ("iscom5508GP", 550801), ("iscom5600", 560000), ("iscom5800", 580000), ("iscom5800e", 580001), ("iscom6800", 680000), ("iscom5101A", 510100), ("iscom5101B", 510101), ("iscom5101-FE", 510102), ("iscom5101-EA", 510103), ("ht801", 510104), ("sc200-GB-EPON", 510000), ("dlcom2096-SMC-EPON", 510001), ("ic-epon", 510002), ("im-epon", 510003), ("iscom5100-m1", 510004), ("iscom5100-m2", 510005), ("rcvs1500-p01u", 510008), ("rcvs300-p41", 510204), ("rcvs300-p42", 510222), ("rcvs300-p44", 510224), ("rcvs300-p11-b", 510300), ("rcvs300-p41-b", 510301), ("iscom5104", 510400), ("iscom5104Q", 510401), ("iscom5104-LM", 510402), ("iscom5104-AC60", 510403), ("iscom5104C", 510404), ("iscom5104P", 510405), ("iscom5104-NP", 510406), ("iscom5104-4E1T1", 510407), ("iscom5104P-2R", 510408), ("iscom5104-PE", 510410), ("iscom5104-H1", 510411), ("iscom5104PI-4R", 510415), ("iscom5104P-4R3", 510460), ("iscom5104P-4R8", 510461), ("iscom5104P-4R", 510462), ("iscom5104-4R", 510500), ("iscom5104-HA", 510501), ("iscom5104PI-DN", 510503), ("iscom5104QB", 510504), ("iscom5104-GE-NP", 510505), ("iscom5104G", 510506), ("iscom5104G-NP", 510600), ("iscom5104Q-EA", 510507), ("iscom5104P-NR", 510508), ("ht803", 510509), ("ht811", 520100), ("ht816", 530402), ("ht825", 540400), ("ht826", 540401), ("iscom5104-HB", 510510), ("iscom5104-EA", 510511), ("iscom5104-PE-B", 510601), ("iscom5104PI-4RB", 510512), ("iscom5104-NP-YP", 510513), ("iscom5104P-EA", 510515), ("iscom5104P-4R-EA", 510516), ("iscom5104-4R-EA", 510517), ("iscom5104PI-DN-4R", 510563), ("iscom5108", 510800), ("iscom5108-PE", 510801), ("iscom5108-PSE", 510802), ("iscom5108C", 510803), ("iscom5108-PE-C", 510804), ("iscom5116", 511600), ("iscom5116-PE", 511601), ("iscom5116-PE-C", 511605), ("iscom5116B", 511602), ("iscom5116C", 511604), ("iscom5124A", 512400), ("iscom5124B", 512401), ("iscom5124S", 512402), ("iscom5124SC", 512404), ("iscom5204", 520400), ("iscom5204-PE", 520401), ("iscom5204-H1", 520402), ("ht815", 520403), ("ht821", 520404), ("iscom5204PI-C4V", 520405), ("iscom5208", 520800), ("iscom5208C", 520801), ("iscom5216", 521600), ("iscom5216B", 521601), ("iscom5216C", 521602), ("iscom5224", 522400), ("iscom5224B", 522401), ("iscom5224C", 522402), ("iscom5304", 530400), ("iscom5304D", 530401), ("iscom5100-m1-yf", 510006), ("iscom5100-m2-yf", 510007), ("iscom5104d", 510409), ("iscom5104-hf", 510604), ("ht825-e8", 540402), ("ht826-e8", 540403), ("ht803-r", 530403), ("ht803-v", 520407), ("ht803-w", 540406), ("iscom5108-pse-b", 510806), ("iscom5104-pse-yf", 510518), ("iscom5108-pse-yf", 510805), ("iscom5104-pse", 510603), ("iscom5104PI", 510564), ("iscom6104", 561000), ("iscom5204-H1B", 520406))

class PONDeviceCardType(TextualConvention, Integer32):
    description = 'Iscom EPON and GPON device series Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 550400, 550401, 550402, 510100, 510101, 510102, 510103, 510104, 510000, 510001, 510002, 510003, 510004, 510005, 510006, 510007, 510400, 510401, 510402, 510403, 510404, 510405, 510406, 510407, 510408, 510409, 510410, 510411, 510460, 510461, 510501, 510504, 510503, 510505, 510506, 510507, 510508, 510509, 520100, 530402, 540400, 540401, 510510, 510511, 510512, 510513, 510563, 510800, 510801, 510802, 511600, 511601, 511602, 512400, 512401, 512402, 512403, 520400, 520401, 520402, 520403, 520404, 520405, 520800, 3003, 521600, 521601, 3001, 522400, 522401, 3002, 4001, 530400, 530401, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1187, 1188, 1189, 510006, 510007, 510409, 510604, 540402, 540403, 530403, 520407, 540406, 510806, 510518, 510805, 510603, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1299, 200001, 200002, 200003, 200004, 200005, 200006, 200007, 200008))
    namedValues = NamedValues(("unknow", 0), ("others", 1), ("null", 2), ("FANS-General", 3), ("PWR-General", 4), ("PWR-DC-General", 5), ("PWR-AC-General", 6), ("iscom5504ACard", 550400), ("iscom5504BCard", 550401), ("iscom5504PICard", 550402), ("iscom5101ACard", 510100), ("iscom5101BCard", 510101), ("iscom5101-FECard", 510102), ("iscom5101-EACard", 510103), ("ht801Card", 510104), ("sc200-GB-EPONCard", 510000), ("dlcom2096-SMC-EPONCard", 510001), ("ic-eponCard", 510002), ("im-eponCard", 510003), ("iscom5100-M1Card", 510004), ("iscom5100-M2Card", 510005), ("iscom5100-M1-YFCard", 510006), ("iscom5100-M2-YFCard", 510007), ("iscom5104Card", 510400), ("iscom5104QCard", 510401), ("iscom5104-LMCard", 510402), ("iscom5104-AC60Card", 510403), ("iscom5104CCard", 510404), ("iscom5104PCard", 510405), ("iscom5104-NPCard", 510406), ("iscom5104-4E1T1Card", 510407), ("iscom5104P-2RCard", 510408), ("iscom5104DCard", 510409), ("iscom5104-PECard", 510410), ("iscom5104-H1Card", 510411), ("iscom5104P-4R3Card", 510460), ("iscom5104P-4R8Card", 510461), ("iscom5104-HACard", 510501), ("iscom5104QBCard", 510504), ("iscom5104PI-DNCard", 510503), ("iscom5104-GE-NPCard", 510505), ("iscom5104GCard", 510506), ("iscom5104Q-EACard", 510507), ("iscom5104P-NRCard", 510508), ("ht803Card", 510509), ("ht811Card", 520100), ("ht816Card", 530402), ("ht825Card", 540400), ("ht826Card", 540401), ("iscom5104-HBCard", 510510), ("iscom5104-EACard", 510511), ("iscom5104PI-4RBCard", 510512), ("iscom5104-NP-YPCard", 510513), ("iscom5104PI-DN-4RCard", 510563), ("iscom5108Card", 510800), ("iscom5108-PECard", 510801), ("iscom5108-PSECard", 510802), ("iscom5116Card", 511600), ("iscom5116-PECard", 511601), ("iscom5116BCard", 511602), ("iscom5124ACard", 512400), ("iscom5124BCard", 512401), ("iscom5124SCard", 512402), ("iscom5124SCCard", 512403), ("iscom5204Card", 520400), ("iscom5204-PECard", 520401), ("iscom5204-H1Card", 520402), ("ht815Card", 520403), ("ht821Card", 520404), ("iscom5204PI-C4VCard", 520405), ("iscom5208Card", 520800), ("iscom5208-SC-8POTS", 3003), ("iscom5216Card", 521600), ("iscom5216BCard", 521601), ("iscom5216-SC-16POTS", 3001), ("iscom5224Card", 522400), ("iscom5224BCard", 522401), ("iscom5224-SC-24POTS", 3002), ("video-hi3512", 4001), ("iscom5304Card", 530400), ("iscom5304DCard", 530401), ("iscom5600-NMS", 1001), ("iscom5600-2PON", 1002), ("iscom5600-2PON-P", 1003), ("iscom5508-SMC", 1004), ("iscom5508-EP4", 1005), ("iscom5508-EPSC", 1006), ("iscom5508-EP4B", 1007), ("iscom5508-GE4B", 1008), ("iscom5508-GPSC", 1009), ("iscom5508-GP4A", 1010), ("iscom5800-SMC", 1101), ("iscom5800-2PON", 1102), ("iscom5800-4GE", 1103), ("iscom5800-2GE", 1104), ("iscom5800-4PON", 1105), ("iscom5800-4GEB", 1106), ("iscom5800-2GEB", 1107), ("iscom5800-SMCB", 1108), ("iscom5800e-10GEX2-2GE", 1109), ("iscom5800e-10GE-2GE", 1110), ("iscom5800e-SMC", 1111), ("iscom5800e-EP4A", 1112), ("iscom5800e-GE8A", 1113), ("iscom5800e-SMCB", 1114), ("iscom5800e-VE8A", 1115), ("iscom5800e-2GEMP", 1116), ("iscom5800e-4GEMP", 1117), ("iscom5800e-OMU8", 1118), ("iscom5800e-OAD1D-S-27", 1119), ("iscom5800e-OAD1D-S-31", 1120), ("iscom5800e-OAD1D-S-35", 1121), ("iscom5800e-OAD1D-S-39", 1122), ("iscom5800e-OAD1D-S-43", 1123), ("iscom5800e-OAD1D-S-47", 1124), ("iscom5800e-OAD1D-S-51", 1125), ("iscom5800e-OAD1D-S-55", 1126), ("iscom5800e-OAD1D-S-59", 1127), ("rcvs3200-GE4A", 1128), ("rcvs3200-GE8A", 1129), ("rcvs3200-EP4A", 1130), ("rcvs3200-SMCB", 1131), ("iscom5800e_EP4B", 1132), ("rcvs3200_10GEX2_2GE", 1133), ("rcvs3100-EPSC", 1134), ("rcvs3100-EP4B", 1135), ("rcvs3100-GE4B", 1136), ("sub-pwrm-ac", 1187), ("sub-pwrm-dc", 1188), ("sub-pwrii-ac", 1189), ("iscom5100-m1-yfCard", 510006), ("iscom5100-m2-yfCard", 510007), ("iscom5104dCard", 510409), ("iscom5104-hfCard", 510604), ("ht825-e8Card", 540402), ("ht826-e8Card", 540403), ("ht803-rCard", 530403), ("ht803-vCard", 520407), ("ht803-wCard", 540406), ("iscom5108-pse-bCard", 510806), ("iscom5104-pse-yfCard", 510518), ("iscom5108-pse-yfCard", 510805), ("iscom5104-pseCard", 510603), ("iscom6800-SMCA", 1201), ("iscom6800-XP4A", 1202), ("iscom6800-EP12", 1203), ("iscom6800-EP16", 1204), ("iscom6800-GE16", 1205), ("iscom6800-CICA", 1206), ("iscom6800-EP1X", 1207), ("iscom6800-XP2A", 1208), ("iscom6800-RPD2151", 1209), ("iscom6800-FANS382", 1210), ("iscom6800-SMCB", 1211), ("iscom6800-XP4L", 1212), ("iscom6800-GP8A", 1213), ("iscom6800-XEP8", 1214), ("iscom6800-GP16", 1215), ("iscom6800-XP4T", 1299), ("msg3600-SMCA", 200001), ("msg3600-GE4T", 200002), ("msg3600-48FXS", 200003), ("msg3600-IMPA", 200004), ("msg3600-GWA", 200005), ("msg3600-8FXO", 200006), ("msg3600-2VE1", 200007), ("msg3600-IMPS", 200008))

class ShelfId(TextualConvention, Integer32):
    description = 'shelf id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 5)

class SlotId(TextualConvention, Integer32):
    description = 'slot id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 179)

class SlotIndex(TextualConvention, Integer32):
    description = 'slot index'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 179)

class PortId(TextualConvention, Integer32):
    description = 'shelf id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 511)

class OltPortIndex(TextualConvention, Integer32):
    description = 'SlotId*10000000+PortId'
    status = 'current'

class OnuId(TextualConvention, Integer32):
    description = 'shelf id'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class OnuIndex(TextualConvention, Integer32):
    description = 'SlotId*10000000+PONPortId*100000+OnuId'
    status = 'current'

class LlidIndex(TextualConvention, Integer32):
    description = 'SlotId*10000000+PONPortId*100000+OnuId'
    status = 'current'

class Olt_OnuPortIndex(TextualConvention, Integer32):
    description = 'SlotId*10000000+ PONPortId*100000+ONUid*1000+ONUPortId'
    status = 'current'

class Olt_OnuIfIndex(TextualConvention, Integer32):
    description = 'SlotId*10000000+ PONPortId*100000+ONUid*1000+ONUPortId'
    status = 'current'

mibBuilder.exportSymbols("RAISECOM-PONSERIES-TC", Olt_OnuIfIndex=Olt_OnuIfIndex, OnuId=OnuId, OltPortIndex=OltPortIndex, PortId=PortId, PONDeviceType=PONDeviceType, SlotIndex=SlotIndex, OnuIndex=OnuIndex, LlidIndex=LlidIndex, Olt_OnuPortIndex=Olt_OnuPortIndex, ShelfId=ShelfId, SlotId=SlotId, PONDeviceCardType=PONDeviceCardType)
