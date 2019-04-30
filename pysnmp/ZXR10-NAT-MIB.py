#
# PySNMP MIB module ZXR10-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-NAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Unsigned32, ModuleIdentity, ObjectIdentity, experimental, Integer32, iso, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, Gauge32, MibIdentifier, NotificationType, mgmt, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "experimental", "Integer32", "iso", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "Gauge32", "MibIdentifier", "NotificationType", "mgmt", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxr10protocol, = mibBuilder.importSymbols("ZXR10-PROTOCOL-MIB", "zxr10protocol")
class Zxr10NatType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 6, 17))
    namedValues = NamedValues(("snat", 0), ("icmp", 1), ("ip", 4), ("tcp", 6), ("udp", 17))

zxr10nat = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3))
class DisplayString(OctetString):
    pass

zxr10natConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1))
zxr10natStatistic = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2))
zxr10natStaticMapping = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3))
zxr10natConfEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfEnable.setStatus('current')
zxr10natInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2), )
if mibBuilder.loadTexts: zxr10natInterfaceTable.setStatus('current')
zxr10natInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natInterfaceIndex"))
if mibBuilder.loadTexts: zxr10natInterfaceEntry.setStatus('current')
zxr10natInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natInterfaceIndex.setStatus('current')
zxr10natInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natInterfaceName.setStatus('current')
zxr10natInterfaceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inside", 1), ("outside", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natInterfaceStorageType.setStatus('current')
zxr10natConfigTimeout = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3))
zxr10natConfTimeoutClassTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1), )
if mibBuilder.loadTexts: zxr10natConfTimeoutClassTable.setStatus('current')
zxr10natConfTimeoutClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natConfTimeoutClassIndex"))
if mibBuilder.loadTexts: zxr10natConfTimeoutClassEntry.setStatus('current')
zxr10natConfTimeoutClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("a", 0), ("b", 1), ("c", 2), ("d", 3), ("e", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutClassIndex.setStatus('current')
zxr10natConfTimeoutClassValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutClassValue.setStatus('current')
zxr10natConfTimeoutProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5), )
if mibBuilder.loadTexts: zxr10natConfTimeoutProtocolTable.setStatus('current')
zxr10natConfTimeoutProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natConfTimeoutProtocolIndex"))
if mibBuilder.loadTexts: zxr10natConfTimeoutProtocolEntry.setStatus('current')
zxr10natConfTimeoutProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutProtocolIndex.setStatus('current')
zxr10natConfTimeoutProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 2), Zxr10NatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutProtocol.setStatus('current')
zxr10natConfTimeoutPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65534))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutPort.setStatus('current')
zxr10natConfTimeoutClass = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 3, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("a", 0), ("b", 1), ("c", 2), ("d", 3), ("e", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfTimeoutClass.setStatus('current')
zxr10natConfigMaximal = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4))
zxr10natConfMaximalDefault = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfMaximalDefault.setStatus('current')
zxr10natConfMaximalTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2), )
if mibBuilder.loadTexts: zxr10natConfMaximalTable.setStatus('current')
zxr10natConfMaximalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natConfMaximalAclNo"))
if mibBuilder.loadTexts: zxr10natConfMaximalEntry.setStatus('current')
zxr10natConfMaximalAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfMaximalAclNo.setStatus('current')
zxr10natConfMaximalVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfMaximalVlaue.setStatus('current')
zxr10natConfStaticAddrMapTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5), )
if mibBuilder.loadTexts: zxr10natConfStaticAddrMapTable.setStatus('current')
zxr10natConfStaticAddrMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natConfStaticRuleIndex"))
if mibBuilder.loadTexts: zxr10natConfStaticAddrMapEntry.setStatus('current')
zxr10natConfStaticRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticRuleIndex.setStatus('current')
zxr10natConfStaticLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticLocalAddr.setStatus('current')
zxr10natConfStaticLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticLocalPort.setStatus('current')
zxr10natConfStaticGlobalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticGlobalAddr.setStatus('current')
zxr10natConfStaticGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticGlobalPort.setStatus('current')
zxr10natConfStaticProtoType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 5, 1, 6), Zxr10NatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfStaticProtoType.setStatus('current')
zxr10natConfDynAddrMapTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6), )
if mibBuilder.loadTexts: zxr10natConfDynAddrMapTable.setStatus('current')
zxr10natConfDynAddrMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natConfDynRuleIndex"))
if mibBuilder.loadTexts: zxr10natConfDynAddrMapEntry.setStatus('current')
zxr10natConfDynRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynRuleIndex.setStatus('current')
zxr10natConfDynAccessListNum = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynAccessListNum.setStatus('current')
zxr10natConfDynRuleOverlay = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("overlay", 1), ("nooverlay", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynRuleOverlay.setStatus('current')
zxr10natConfDynInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynInterfaceName.setStatus('current')
zxr10natConfDynGlobalIpStart = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynGlobalIpStart.setStatus('current')
zxr10natConfDynGlobalIpRange = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 1, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natConfDynGlobalIpRange.setStatus('current')
zxr10natHitStatsTotal = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natHitStatsTotal.setStatus('current')
zxr10natHitStatsFwd = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natHitStatsFwd.setStatus('current')
zxr10natHitStatsProtocl = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natHitStatsProtocl.setStatus('current')
zxr10natHitStatsUEng = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natHitStatsUEng.setStatus('current')
zxr10natMissStatsTotal = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMissStatsTotal.setStatus('current')
zxr10natMissStatsFwd = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMissStatsFwd.setStatus('current')
zxr10natMissStatsProtocol = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMissStatsProtocol.setStatus('current')
zxr10natMissStatsUEng = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMissStatsUEng.setStatus('current')
zxr10natTimeoutStatsTotal = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natTimeoutStatsTotal.setStatus('current')
zxr10natMappingStatsTotal = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMappingStatsTotal.setStatus('current')
zxr10natMappingUsedStatsTotal = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMappingUsedStatsTotal.setStatus('current')
zxr10natMappingStatsStaticRule = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMappingStatsStaticRule.setStatus('current')
zxr10natMappingStatsDynRule = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMappingStatsDynRule.setStatus('current')
zxr10natMappingStatsMax = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natMappingStatsMax.setStatus('current')
zxr10natStaticMappingTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1), )
if mibBuilder.loadTexts: zxr10natStaticMappingTable.setStatus('current')
zxr10natStaticMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1), ).setIndexNames((0, "ZXR10-NAT-MIB", "zxr10natStaticRuleIndex"))
if mibBuilder.loadTexts: zxr10natStaticMappingEntry.setStatus('current')
zxr10natStaticRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natStaticRuleIndex.setStatus('current')
zxr10natStaticMappingLocalIpaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natStaticMappingLocalIpaddr.setStatus('current')
zxr10natStaticMappingLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natStaticMappingLocalPort.setStatus('current')
zxr10natStaticMappingGlobalIpaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natStaticMappingGlobalIpaddr.setStatus('current')
zxr10natStaticMappingGlobalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 101, 3, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10natStaticMappingGlobalPort.setStatus('current')
mibBuilder.exportSymbols("ZXR10-NAT-MIB", zxr10natConfig=zxr10natConfig, zxr10natConfDynAddrMapTable=zxr10natConfDynAddrMapTable, zxr10natHitStatsTotal=zxr10natHitStatsTotal, zxr10natConfDynAddrMapEntry=zxr10natConfDynAddrMapEntry, zxr10natMissStatsFwd=zxr10natMissStatsFwd, zxr10natConfStaticRuleIndex=zxr10natConfStaticRuleIndex, zxr10natConfTimeoutProtocol=zxr10natConfTimeoutProtocol, zxr10natMappingStatsTotal=zxr10natMappingStatsTotal, zxr10natStaticMapping=zxr10natStaticMapping, zxr10natMissStatsUEng=zxr10natMissStatsUEng, zxr10natConfTimeoutClassTable=zxr10natConfTimeoutClassTable, zxr10natConfDynRuleOverlay=zxr10natConfDynRuleOverlay, zxr10natStaticMappingLocalIpaddr=zxr10natStaticMappingLocalIpaddr, zxr10natConfTimeoutClassIndex=zxr10natConfTimeoutClassIndex, zxr10natConfStaticGlobalAddr=zxr10natConfStaticGlobalAddr, zxr10natConfDynInterfaceName=zxr10natConfDynInterfaceName, zxr10natStaticMappingEntry=zxr10natStaticMappingEntry, zxr10natTimeoutStatsTotal=zxr10natTimeoutStatsTotal, zxr10natConfDynGlobalIpRange=zxr10natConfDynGlobalIpRange, zxr10natConfDynGlobalIpStart=zxr10natConfDynGlobalIpStart, zxr10natConfTimeoutClassValue=zxr10natConfTimeoutClassValue, zxr10natConfStaticAddrMapTable=zxr10natConfStaticAddrMapTable, zxr10natHitStatsProtocl=zxr10natHitStatsProtocl, zxr10natMappingStatsStaticRule=zxr10natMappingStatsStaticRule, zxr10natConfMaximalAclNo=zxr10natConfMaximalAclNo, zxr10natMissStatsTotal=zxr10natMissStatsTotal, zxr10natConfStaticLocalPort=zxr10natConfStaticLocalPort, zxr10natMissStatsProtocol=zxr10natMissStatsProtocol, zxr10natHitStatsUEng=zxr10natHitStatsUEng, zxr10natConfMaximalTable=zxr10natConfMaximalTable, zxr10natHitStatsFwd=zxr10natHitStatsFwd, zxr10natConfTimeoutProtocolIndex=zxr10natConfTimeoutProtocolIndex, zxr10natConfMaximalEntry=zxr10natConfMaximalEntry, zxr10natConfTimeoutClassEntry=zxr10natConfTimeoutClassEntry, zxr10natMappingStatsMax=zxr10natMappingStatsMax, Zxr10NatType=Zxr10NatType, zxr10natConfTimeoutPort=zxr10natConfTimeoutPort, zxr10natInterfaceName=zxr10natInterfaceName, zxr10natConfStaticGlobalPort=zxr10natConfStaticGlobalPort, zxr10natConfDynRuleIndex=zxr10natConfDynRuleIndex, zxr10natConfTimeoutProtocolTable=zxr10natConfTimeoutProtocolTable, zxr10natConfigMaximal=zxr10natConfigMaximal, zxr10natConfDynAccessListNum=zxr10natConfDynAccessListNum, zxr10natMappingStatsDynRule=zxr10natMappingStatsDynRule, zxr10natStaticMappingGlobalIpaddr=zxr10natStaticMappingGlobalIpaddr, zxr10natConfMaximalVlaue=zxr10natConfMaximalVlaue, zxr10natConfTimeoutClass=zxr10natConfTimeoutClass, zxr10natInterfaceIndex=zxr10natInterfaceIndex, zxr10natInterfaceTable=zxr10natInterfaceTable, zxr10natConfStaticAddrMapEntry=zxr10natConfStaticAddrMapEntry, zxr10natStatistic=zxr10natStatistic, zxr10nat=zxr10nat, DisplayString=DisplayString, zxr10natConfStaticProtoType=zxr10natConfStaticProtoType, zxr10natStaticMappingTable=zxr10natStaticMappingTable, zxr10natInterfaceEntry=zxr10natInterfaceEntry, zxr10natInterfaceStorageType=zxr10natInterfaceStorageType, zxr10natConfTimeoutProtocolEntry=zxr10natConfTimeoutProtocolEntry, zxr10natStaticMappingLocalPort=zxr10natStaticMappingLocalPort, zxr10natMappingUsedStatsTotal=zxr10natMappingUsedStatsTotal, zxr10natStaticRuleIndex=zxr10natStaticRuleIndex, zxr10natConfigTimeout=zxr10natConfigTimeout, zxr10natConfEnable=zxr10natConfEnable, zxr10natConfMaximalDefault=zxr10natConfMaximalDefault, zxr10natConfStaticLocalAddr=zxr10natConfStaticLocalAddr, zxr10natStaticMappingGlobalPort=zxr10natStaticMappingGlobalPort)