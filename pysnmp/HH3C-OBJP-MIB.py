#
# PySNMP MIB module HH3C-OBJP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-OBJP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, IpAddress, Unsigned32, Integer32, TimeTicks, NotificationType, Gauge32, Counter64, Bits, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cObjp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 155))
hh3cObjp.setRevisions(('2014-03-10 15:36',))
if mibBuilder.loadTexts: hh3cObjp.setLastUpdated('201403101536Z')
if mibBuilder.loadTexts: hh3cObjp.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cObjpZonePairObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1))
hh3cObjpZonePairRunningInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1), )
if mibBuilder.loadTexts: hh3cObjpZonePairRunningInfoTable.setStatus('current')
hh3cObjpZonePairRunningInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1), ).setIndexNames((0, "HH3C-OBJP-MIB", "hh3cObjpZonePairSrcZone"), (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairDstZone"), (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairIPVersion"), (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairRuleID"))
if mibBuilder.loadTexts: hh3cObjpZonePairRunningInfoEntry.setStatus('current')
hh3cObjpZonePairSrcZone = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hh3cObjpZonePairSrcZone.setStatus('current')
hh3cObjpZonePairDstZone = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: hh3cObjpZonePairDstZone.setStatus('current')
hh3cObjpZonePairIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: hh3cObjpZonePairIPVersion.setStatus('current')
hh3cObjpZonePairRuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hh3cObjpZonePairRuleID.setStatus('current')
hh3cObjpZonePairMatchPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cObjpZonePairMatchPacketCount.setStatus('current')
hh3cObjpZonePairLastMatchTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cObjpZonePairLastMatchTime.setStatus('current')
mibBuilder.exportSymbols("HH3C-OBJP-MIB", hh3cObjp=hh3cObjp, hh3cObjpZonePairRunningInfoEntry=hh3cObjpZonePairRunningInfoEntry, hh3cObjpZonePairRunningInfoTable=hh3cObjpZonePairRunningInfoTable, hh3cObjpZonePairMatchPacketCount=hh3cObjpZonePairMatchPacketCount, hh3cObjpZonePairDstZone=hh3cObjpZonePairDstZone, hh3cObjpZonePairSrcZone=hh3cObjpZonePairSrcZone, PYSNMP_MODULE_ID=hh3cObjp, hh3cObjpZonePairLastMatchTime=hh3cObjpZonePairLastMatchTime, hh3cObjpZonePairRuleID=hh3cObjpZonePairRuleID, hh3cObjpZonePairObjects=hh3cObjpZonePairObjects, hh3cObjpZonePairIPVersion=hh3cObjpZonePairIPVersion)
