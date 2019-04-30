#
# PySNMP MIB module CISCO-CIPLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CIPLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32, ObjectIdentity, iso, Counter64, Gauge32, TimeTicks, NotificationType, Integer32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32", "ObjectIdentity", "iso", "Counter64", "Gauge32", "TimeTicks", "NotificationType", "Integer32", "MibIdentifier", "IpAddress")
RowStatus, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString")
ciscoCipLanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 34))
ciscoCipLanMIB.setRevisions(('1998-01-06 00:00', '1995-04-28 00:00',))
if mibBuilder.loadTexts: ciscoCipLanMIB.setLastUpdated('9504280000Z')
if mibBuilder.loadTexts: ciscoCipLanMIB.setOrganization('cisco IBM engineering Working Group')
cipLanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 34, 1))
cipLan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1))
cipCardLanAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1), )
if mibBuilder.loadTexts: cipCardLanAdminTable.setStatus('current')
cipCardLanAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanType"), (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanId"))
if mibBuilder.loadTexts: cipCardLanAdminEntry.setStatus('current')
cipCardLanAdminLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("iso88023csmacd", 1), ("iso88025tokenRing", 2), ("fddi", 3))))
if mibBuilder.loadTexts: cipCardLanAdminLanType.setStatus('current')
cipCardLanAdminLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: cipCardLanAdminLanId.setStatus('current')
cipCardLanAdminBridgeType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transparentOnly", 1), ("sourcerouteOnly", 2), ("transpAndSourceRoute", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminBridgeType.setStatus('current')
cipCardLanAdminSrbLocalRing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminSrbLocalRing.setStatus('current')
cipCardLanAdminSrbBridgeNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminSrbBridgeNum.setStatus('current')
cipCardLanAdminSrbTargetRing = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminSrbTargetRing.setStatus('current')
cipCardLanAdminTbBridgeGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminTbBridgeGrp.setStatus('current')
cipCardLanAdminRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdminRowStatus.setStatus('current')
cipCardLanAdaptAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2), )
if mibBuilder.loadTexts: cipCardLanAdaptAdminTable.setStatus('current')
cipCardLanAdaptAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanType"), (0, "CISCO-CIPLAN-MIB", "cipCardLanAdminLanId"), (0, "CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminAdaptNo"))
if mibBuilder.loadTexts: cipCardLanAdaptAdminEntry.setStatus('current')
cipCardLanAdaptAdminAdaptNo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31)))
if mibBuilder.loadTexts: cipCardLanAdaptAdminAdaptNo.setStatus('current')
cipCardLanAdaptAdminMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdaptAdminMacAddress.setStatus('current')
cipCardLanAdaptAdminAdaptName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdaptAdminAdaptName.setStatus('current')
cipCardLanAdaptAdminRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 34, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipCardLanAdaptAdminRowStatus.setStatus('current')
ciscoCipLanMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 34, 2))
ciscoCipLanMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 1))
ciscoCipLanMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2))
ciscoCipLanMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 1, 1)).setObjects(("CISCO-CIPLAN-MIB", "ciscoLanGroup"), ("CISCO-CIPLAN-MIB", "ciscoLanAdaptGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipLanMibCompliance = ciscoCipLanMibCompliance.setStatus('current')
ciscoLanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 1)).setObjects(("CISCO-CIPLAN-MIB", "cipCardLanAdminBridgeType"), ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbLocalRing"), ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbBridgeNum"), ("CISCO-CIPLAN-MIB", "cipCardLanAdminSrbTargetRing"), ("CISCO-CIPLAN-MIB", "cipCardLanAdminTbBridgeGrp"), ("CISCO-CIPLAN-MIB", "cipCardLanAdminRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLanGroup = ciscoLanGroup.setStatus('current')
ciscoLanAdaptGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 34, 2, 2, 2)).setObjects(("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminMacAddress"), ("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminAdaptName"), ("CISCO-CIPLAN-MIB", "cipCardLanAdaptAdminRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLanAdaptGroup = ciscoLanAdaptGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CIPLAN-MIB", PYSNMP_MODULE_ID=ciscoCipLanMIB, cipCardLanAdminSrbBridgeNum=cipCardLanAdminSrbBridgeNum, cipCardLanAdminRowStatus=cipCardLanAdminRowStatus, cipCardLanAdaptAdminRowStatus=cipCardLanAdaptAdminRowStatus, cipCardLanAdminBridgeType=cipCardLanAdminBridgeType, ciscoCipLanMibCompliance=ciscoCipLanMibCompliance, ciscoLanGroup=ciscoLanGroup, cipLan=cipLan, cipCardLanAdminLanType=cipCardLanAdminLanType, cipCardLanAdminSrbTargetRing=cipCardLanAdminSrbTargetRing, cipCardLanAdminEntry=cipCardLanAdminEntry, cipLanObjects=cipLanObjects, cipCardLanAdminSrbLocalRing=cipCardLanAdminSrbLocalRing, cipCardLanAdaptAdminMacAddress=cipCardLanAdaptAdminMacAddress, cipCardLanAdminLanId=cipCardLanAdminLanId, cipCardLanAdminTable=cipCardLanAdminTable, ciscoLanAdaptGroup=ciscoLanAdaptGroup, ciscoCipLanMibGroups=ciscoCipLanMibGroups, cipCardLanAdminTbBridgeGrp=cipCardLanAdminTbBridgeGrp, cipCardLanAdaptAdminTable=cipCardLanAdaptAdminTable, ciscoCipLanMIB=ciscoCipLanMIB, cipCardLanAdaptAdminEntry=cipCardLanAdaptAdminEntry, ciscoCipLanMibConformance=ciscoCipLanMibConformance, ciscoCipLanMibCompliances=ciscoCipLanMibCompliances, cipCardLanAdaptAdminAdaptName=cipCardLanAdaptAdminAdaptName, cipCardLanAdaptAdminAdaptNo=cipCardLanAdaptAdminAdaptNo)