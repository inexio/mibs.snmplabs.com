#
# PySNMP MIB module HUAWEI-VLL-STATISTIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VLL-STATISTIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Counter64, IpAddress, Integer32, TimeTicks, Counter32, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, Bits, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "IpAddress", "Integer32", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwL2VpnVllStatistic = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7))
if mibBuilder.loadTexts: hwL2VpnVllStatistic.setLastUpdated('200902132100Z')
if mibBuilder.loadTexts: hwL2VpnVllStatistic.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwL2VpnVllStatistic.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwL2VpnVllStatistic.setDescription("The HUAWEI-VLL-STATISTIC-MIB contains objects to manage VLL's statistic.")
hwL2Vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119))
hwVllMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1))
hwVllStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1), )
if mibBuilder.loadTexts: hwVllStatisticTable.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticTable.setDescription("This table contains the VLL's traffic statistic, based on the interface.")
hwVllStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticIfIndex"), (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPwType"))
if mibBuilder.loadTexts: hwVllStatisticEntry.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticEntry.setDescription("Provides the information of the VLL's traffic statistic.")
hwVllStatisticIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwVllStatisticIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticIfIndex.setDescription('This object indicates the interface index.')
hwVllStatisticPwType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))))
if mibBuilder.loadTexts: hwVllStatisticPwType.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticPwType.setDescription('This object indicates the type of PW.')
hwVllStatisticEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVllStatisticEnable.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticEnable.setDescription("This object indicates the enable sign of VSI's traffic statistics, based on the interface.")
hwVllStatisticResetTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("unknownStatus", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVllStatisticResetTraffic.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticResetTraffic.setDescription('reset the traffic statistic.')
hwVllStatisticResetTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllStatisticResetTime.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticResetTime.setDescription('Last time of clean out.')
hwVllStatisticPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllStatisticPackets.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticPackets.setDescription('The packets sent on the PW.')
hwVllStatisticBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllStatisticBytes.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticBytes.setDescription('The bytes sent on the PW.')
hwVllStatisticPacketsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllStatisticPacketsRate.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticPacketsRate.setDescription('The packet rate sent on the PW.')
hwVllStatisticBytesRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllStatisticBytesRate.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticBytesRate.setDescription('The byte rate sent on the PW.')
hwVllQosStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2), )
if mibBuilder.loadTexts: hwVllQosStatisticTable.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticTable.setDescription("This table contains the VLL's traffic statistic, based on the interface.")
hwVllQosStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1), ).setIndexNames((0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticIfIndex"), (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPwType"), (0, "HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticQueueId"))
if mibBuilder.loadTexts: hwVllQosStatisticEntry.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticEntry.setDescription("Provides the information of the VLL's traffic statistic.")
hwVllQosStatisticIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwVllQosStatisticIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticIfIndex.setDescription('This object indicates the interface index.')
hwVllQosStatisticPwType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2))))
if mibBuilder.loadTexts: hwVllQosStatisticPwType.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticPwType.setDescription('This object indicates the type of PW.')
hwVllQosStatisticQueueId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("be", 1), ("af1", 2), ("af2", 3), ("af3", 4), ("af4", 5), ("ef", 6), ("cs6", 7), ("cs7", 8))))
if mibBuilder.loadTexts: hwVllQosStatisticQueueId.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticQueueId.setDescription("This object indicates the queue's ID. The value must be be,af1,af2,af3,af4,ef,cs6,cs7.")
hwVllQosStatisticPassPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticPassPacket.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticPassPacket.setDescription('Number of passed packets, based on the interface.')
hwVllQosStatisticPassByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticPassByte.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticPassByte.setDescription('Number of passed bytes, based on the interface.')
hwVllQosStatisticDiscardPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticDiscardPacket.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticDiscardPacket.setDescription('Number of discarded packets, based on the interface.')
hwVllQosStatisticDiscardByte = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticDiscardByte.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticDiscardByte.setDescription('Number of discarded bytes, based on the interface.')
hwVllQosStatisticPassPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticPassPacketRate.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticPassPacketRate.setDescription('Rate of passed packets for the past 30 seconds, based on the interface. Unit: pps')
hwVllQosStatisticPassByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticPassByteRate.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticPassByteRate.setDescription('Rate of passed bytes for the past 30 seconds, based on the interface. Unit: bps')
hwVllQosStatisticDiscardPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticDiscardPacketRate.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticDiscardPacketRate.setDescription('Rate of discarded packets for the past 30 seconds, based on the interface. Unit: pps')
hwVllQosStatisticDiscardByteRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVllQosStatisticDiscardByteRate.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticDiscardByteRate.setDescription('Rate of discarded bytes for the past 30 seconds, based on the interface. Unit: bps')
hwVllMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 2))
hwVllMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3))
hwVllMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1))
hwVllMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 1, 1)).setObjects(("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticGroup"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVllMIBCompliance = hwVllMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwVllMIBCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-VLL-STATISTIC-MIB.')
hwVllMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2))
hwVllStatisticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 1)).setObjects(("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticEnable"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticResetTraffic"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticResetTime"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPackets"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticBytes"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticPacketsRate"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllStatisticBytesRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVllStatisticGroup = hwVllStatisticGroup.setStatus('current')
if mibBuilder.loadTexts: hwVllStatisticGroup.setDescription("The VLL's statistic group.")
hwVllQosStatisticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 7, 3, 2, 2)).setObjects(("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassPacket"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassByte"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardPacket"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardByte"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassPacketRate"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticPassByteRate"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardPacketRate"), ("HUAWEI-VLL-STATISTIC-MIB", "hwVllQosStatisticDiscardByteRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVllQosStatisticGroup = hwVllQosStatisticGroup.setStatus('current')
if mibBuilder.loadTexts: hwVllQosStatisticGroup.setDescription("The VLL's QoS statistic group.")
mibBuilder.exportSymbols("HUAWEI-VLL-STATISTIC-MIB", hwL2Vpn=hwL2Vpn, hwVllStatisticPackets=hwVllStatisticPackets, hwVllQosStatisticDiscardByte=hwVllQosStatisticDiscardByte, hwVllQosStatisticEntry=hwVllQosStatisticEntry, hwVllMIBTraps=hwVllMIBTraps, hwVllQosStatisticIfIndex=hwVllQosStatisticIfIndex, hwVllStatisticEnable=hwVllStatisticEnable, hwVllMIBCompliance=hwVllMIBCompliance, hwVllStatisticBytesRate=hwVllStatisticBytesRate, hwVllQosStatisticPassByte=hwVllQosStatisticPassByte, hwVllQosStatisticPassPacketRate=hwVllQosStatisticPassPacketRate, hwVllQosStatisticPassByteRate=hwVllQosStatisticPassByteRate, hwVllQosStatisticDiscardPacketRate=hwVllQosStatisticDiscardPacketRate, hwVllQosStatisticDiscardByteRate=hwVllQosStatisticDiscardByteRate, hwVllStatisticEntry=hwVllStatisticEntry, PYSNMP_MODULE_ID=hwL2VpnVllStatistic, hwVllStatisticResetTime=hwVllStatisticResetTime, hwVllStatisticResetTraffic=hwVllStatisticResetTraffic, hwVllQosStatisticTable=hwVllQosStatisticTable, hwVllStatisticPacketsRate=hwVllStatisticPacketsRate, hwVllMIBGroups=hwVllMIBGroups, hwVllQosStatisticQueueId=hwVllQosStatisticQueueId, hwVllQosStatisticPassPacket=hwVllQosStatisticPassPacket, hwVllMIBCompliances=hwVllMIBCompliances, hwVllStatisticIfIndex=hwVllStatisticIfIndex, hwVllMIBObjects=hwVllMIBObjects, hwVllQosStatisticPwType=hwVllQosStatisticPwType, hwVllMIBConformance=hwVllMIBConformance, hwVllStatisticBytes=hwVllStatisticBytes, hwL2VpnVllStatistic=hwL2VpnVllStatistic, hwVllStatisticTable=hwVllStatisticTable, hwVllQosStatisticDiscardPacket=hwVllQosStatisticDiscardPacket, hwVllQosStatisticGroup=hwVllQosStatisticGroup, hwVllStatisticGroup=hwVllStatisticGroup, hwVllStatisticPwType=hwVllStatisticPwType)
