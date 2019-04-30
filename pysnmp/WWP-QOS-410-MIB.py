#
# PySNMP MIB module WWP-QOS-410-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-QOS-410-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, NotificationType, IpAddress, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "NotificationType", "IpAddress", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpQos410MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 29))
wwpQos410MIB.setRevisions(('2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpQos410MIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpQos410MIB.setOrganization('World Wide Packets, Inc')
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpQos410MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1))
wwpQos410 = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1))
wwpQos410NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2))
wwpQos410Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0))
wwpQos410MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3))
wwpQos410MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 1))
wwpQos410MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 29, 3, 2))
wwpQos410Table = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1), )
if mibBuilder.loadTexts: wwpQos410Table.setStatus('current')
wwpQos410Entry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410VlanId"), (0, "WWP-QOS-410-MIB", "wwpQos410IngressPortId"), (0, "WWP-QOS-410-MIB", "wwpQos410EgressPortId"))
if mibBuilder.loadTexts: wwpQos410Entry.setStatus('current')
wwpQos410VlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410VlanId.setStatus('current')
wwpQos410IngressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410IngressPortId.setStatus('current')
wwpQos410EgressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410EgressPortId.setStatus('current')
wwpQos410MinRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128000))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410MinRateLimit.setStatus('current')
wwpQos410MaxRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128000))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410MaxRateLimit.setStatus('current')
wwpQos410QueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("qSize16kb", 1), ("qSize32kb", 2), ("qSize64kb", 3), ("qSize128kb", 4), ("qSize256kb", 5), ("qSize512kb", 6), ("qSize1mb", 7), ("qSize2mb", 8), ("qSize4mb", 9), ("qSize8mb", 10), ("qSize16mb", 11), ("qSize32mb", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410QueueSize.setStatus('current')
wwpQos410Weight = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("qw1", 1), ("qw2", 2), ("qw3", 3), ("qw4", 4), ("qw5", 5), ("qw6", 6), ("qw7", 7), ("qw8", 8), ("qw10", 9), ("qw12", 10), ("qw14", 11), ("qw16", 12), ("qw20", 13), ("qw24", 14), ("qw28", 15), ("qw32", 16), ("qw40", 17), ("qw48", 18), ("qw56", 19), ("qw64", 20), ("qw80", 21), ("qw96", 22), ("qw112", 23), ("qw128", 24), ("qw160", 25), ("qw192", 26), ("qw224", 27), ("qw256", 28), ("qw320", 29), ("qw384", 30), ("qw448", 31), ("qw512", 32), ("qw640", 33), ("qw768", 34), ("qw896", 35), ("qw1024", 36)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410Weight.setStatus('current')
wwpQos410RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpQos410RowStatus.setStatus('current')
wwpQos410StatsTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2), )
if mibBuilder.loadTexts: wwpQos410StatsTable.setStatus('current')
wwpQos410StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410StatsVlanId"), (0, "WWP-QOS-410-MIB", "wwpQos410StatsIngressPortId"), (0, "WWP-QOS-410-MIB", "wwpQos410StatsEgressPortId"))
if mibBuilder.loadTexts: wwpQos410StatsEntry.setStatus('current')
wwpQos410StatsVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsVlanId.setStatus('current')
wwpQos410StatsIngressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsIngressPortId.setStatus('current')
wwpQos410StatsEgressPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410StatsEgressPortId.setStatus('current')
wwpQos410StatsType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accepted", 1), ("discarded", 2))).clone('accepted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410StatsType.setStatus('current')
wwpQos410RxBytesHi = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxBytesHi.setStatus('current')
wwpQos410RxBytesLo = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxBytesLo.setStatus('current')
wwpQos410PriToQMapTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3), )
if mibBuilder.loadTexts: wwpQos410PriToQMapTable.setStatus('current')
wwpQos410PriToQMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410RxPriority"))
if mibBuilder.loadTexts: wwpQos410PriToQMapEntry.setStatus('current')
wwpQos410RxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410RxPriority.setStatus('current')
wwpQos410TxPriQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410TxPriQueue.setStatus('current')
wwpQos410PortTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4), )
if mibBuilder.loadTexts: wwpQos410PortTable.setStatus('current')
wwpQos410PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1), ).setIndexNames((0, "WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortEntry.setStatus('current')
wwpQos410PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortIndex.setStatus('current')
wwpQos410PortProvisionedBW = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortProvisionedBW.setStatus('current')
wwpQos410PortTotalBW = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpQos410PortTotalBW.setStatus('current')
wwpQos410PortProvisionedNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 29, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpQos410PortProvisionedNotifEnabled.setStatus('current')
wwpQos410PortOverProvisionedTrap = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 1)).setObjects(("WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortOverProvisionedTrap.setStatus('current')
wwpQos410PortUnderProvisionedTrap = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 29, 2, 0, 2)).setObjects(("WWP-QOS-410-MIB", "wwpQos410PortIndex"))
if mibBuilder.loadTexts: wwpQos410PortUnderProvisionedTrap.setStatus('current')
mibBuilder.exportSymbols("WWP-QOS-410-MIB", wwpQos410PortEntry=wwpQos410PortEntry, wwpQos410Entry=wwpQos410Entry, wwpQos410StatsTable=wwpQos410StatsTable, wwpQos410MaxRateLimit=wwpQos410MaxRateLimit, wwpQos410MIBCompliances=wwpQos410MIBCompliances, wwpQos410PortProvisionedNotifEnabled=wwpQos410PortProvisionedNotifEnabled, wwpQos410PriToQMapTable=wwpQos410PriToQMapTable, PYSNMP_MODULE_ID=wwpQos410MIB, wwpQos410PortIndex=wwpQos410PortIndex, wwpQos410Notifications=wwpQos410Notifications, wwpQos410PortUnderProvisionedTrap=wwpQos410PortUnderProvisionedTrap, wwpQos410RowStatus=wwpQos410RowStatus, wwpQos410MIBObjects=wwpQos410MIBObjects, wwpQos410TxPriQueue=wwpQos410TxPriQueue, wwpQos410PriToQMapEntry=wwpQos410PriToQMapEntry, wwpQos410StatsEntry=wwpQos410StatsEntry, wwpQos410NotificationPrefix=wwpQos410NotificationPrefix, wwpQos410StatsEgressPortId=wwpQos410StatsEgressPortId, wwpQos410MIB=wwpQos410MIB, wwpQos410EgressPortId=wwpQos410EgressPortId, wwpQos410StatsVlanId=wwpQos410StatsVlanId, wwpQos410PortTotalBW=wwpQos410PortTotalBW, wwpQos410StatsType=wwpQos410StatsType, wwpQos410RxBytesLo=wwpQos410RxBytesLo, VlanId=VlanId, wwpQos410PortOverProvisionedTrap=wwpQos410PortOverProvisionedTrap, wwpQos410StatsIngressPortId=wwpQos410StatsIngressPortId, wwpQos410MinRateLimit=wwpQos410MinRateLimit, wwpQos410IngressPortId=wwpQos410IngressPortId, wwpQos410QueueSize=wwpQos410QueueSize, wwpQos410RxPriority=wwpQos410RxPriority, wwpQos410MIBGroups=wwpQos410MIBGroups, wwpQos410VlanId=wwpQos410VlanId, wwpQos410MIBConformance=wwpQos410MIBConformance, wwpQos410PortTable=wwpQos410PortTable, wwpQos410=wwpQos410, wwpQos410RxBytesHi=wwpQos410RxBytesHi, wwpQos410Table=wwpQos410Table, wwpQos410PortProvisionedBW=wwpQos410PortProvisionedBW, wwpQos410Weight=wwpQos410Weight)