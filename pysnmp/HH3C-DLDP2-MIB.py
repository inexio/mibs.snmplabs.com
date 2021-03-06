#
# PySNMP MIB module HH3C-DLDP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DLDP2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, Unsigned32, Counter64, NotificationType, iso, ObjectIdentity, Integer32, TimeTicks, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "Counter64", "NotificationType", "iso", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "Bits", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
hh3cDldp2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 117))
hh3cDldp2.setRevisions(('2011-12-26 15:30',))
if mibBuilder.loadTexts: hh3cDldp2.setLastUpdated('201112261530Z')
if mibBuilder.loadTexts: hh3cDldp2.setOrganization('Hangzhou H3C Technologies. Co., Ltd.')
hh3cDldp2ScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1))
hh3cDldp2GlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2GlobalEnable.setStatus('current')
hh3cDldp2Interval = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2Interval.setStatus('current')
hh3cDldp2AuthMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("simple", 3), ("md5", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2AuthMode.setStatus('current')
hh3cDldp2AuthPassword = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2AuthPassword.setStatus('current')
hh3cDldp2UniShutdown = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 117, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("auto", 2), ("manual", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2UniShutdown.setStatus('current')
hh3cDldp2TableGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2))
hh3cDldp2PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 1), )
if mibBuilder.loadTexts: hh3cDldp2PortConfigTable.setStatus('current')
hh3cDldp2PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDldp2PortConfigEntry.setStatus('current')
hh3cDldp2PortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDldp2PortEnable.setStatus('current')
hh3cDldp2PortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 2), )
if mibBuilder.loadTexts: hh3cDldp2PortStatusTable.setStatus('current')
hh3cDldp2PortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDldp2PortStatusEntry.setStatus('current')
hh3cDldp2PortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("initial", 2), ("inactive", 3), ("unidirectional", 4), ("bidirectional", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDldp2PortOperStatus.setStatus('current')
hh3cDldp2PortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDldp2PortLinkStatus.setStatus('current')
hh3cDldp2NeighborTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3), )
if mibBuilder.loadTexts: hh3cDldp2NeighborTable.setStatus('current')
hh3cDldp2NeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HH3C-DLDP2-MIB", "hh3cDldp2NeighborBridgeMac"), (0, "HH3C-DLDP2-MIB", "hh3cDldp2NeighborPortIndex"))
if mibBuilder.loadTexts: hh3cDldp2NeighborEntry.setStatus('current')
hh3cDldp2NeighborBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hh3cDldp2NeighborBridgeMac.setStatus('current')
hh3cDldp2NeighborPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cDldp2NeighborPortIndex.setStatus('current')
hh3cDldp2NeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("unconfirmed", 2), ("confirmed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDldp2NeighborStatus.setStatus('current')
hh3cDldp2NeighborAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 117, 2, 3, 1, 4), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDldp2NeighborAgingTime.setStatus('current')
hh3cDldp2TrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117, 3))
hh3cDldp2Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117, 4))
hh3cDldp2TrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117, 4, 0))
hh3cDldp2TrapUniLink = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 117, 4, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cDldp2TrapUniLink.setStatus('current')
hh3cDldp2TrapBidLink = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 117, 4, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cDldp2TrapBidLink.setStatus('current')
mibBuilder.exportSymbols("HH3C-DLDP2-MIB", hh3cDldp2NeighborTable=hh3cDldp2NeighborTable, hh3cDldp2AuthPassword=hh3cDldp2AuthPassword, hh3cDldp2NeighborAgingTime=hh3cDldp2NeighborAgingTime, hh3cDldp2PortConfigTable=hh3cDldp2PortConfigTable, hh3cDldp2TrapPrefix=hh3cDldp2TrapPrefix, hh3cDldp2Trap=hh3cDldp2Trap, hh3cDldp2GlobalEnable=hh3cDldp2GlobalEnable, hh3cDldp2=hh3cDldp2, hh3cDldp2PortConfigEntry=hh3cDldp2PortConfigEntry, hh3cDldp2PortStatusTable=hh3cDldp2PortStatusTable, PYSNMP_MODULE_ID=hh3cDldp2, hh3cDldp2UniShutdown=hh3cDldp2UniShutdown, hh3cDldp2PortEnable=hh3cDldp2PortEnable, hh3cDldp2NeighborBridgeMac=hh3cDldp2NeighborBridgeMac, hh3cDldp2TrapBindObjects=hh3cDldp2TrapBindObjects, hh3cDldp2PortStatusEntry=hh3cDldp2PortStatusEntry, hh3cDldp2AuthMode=hh3cDldp2AuthMode, hh3cDldp2ScalarGroup=hh3cDldp2ScalarGroup, hh3cDldp2TableGroup=hh3cDldp2TableGroup, hh3cDldp2TrapUniLink=hh3cDldp2TrapUniLink, hh3cDldp2NeighborEntry=hh3cDldp2NeighborEntry, hh3cDldp2PortLinkStatus=hh3cDldp2PortLinkStatus, hh3cDldp2NeighborStatus=hh3cDldp2NeighborStatus, hh3cDldp2TrapBidLink=hh3cDldp2TrapBidLink, hh3cDldp2NeighborPortIndex=hh3cDldp2NeighborPortIndex, hh3cDldp2PortOperStatus=hh3cDldp2PortOperStatus, hh3cDldp2Interval=hh3cDldp2Interval)
