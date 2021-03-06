#
# PySNMP MIB module XYLAN-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, NotificationType, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, iso, TimeTicks, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "iso", "TimeTicks", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanSonetArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanSonetArch")
xylanSonetErrConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 23, 1))
xylanSonetTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1), )
if mibBuilder.loadTexts: xylanSonetTable.setStatus('mandatory')
xylanSonetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xylanSonetEntry.setStatus('mandatory')
xylanSonetStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanSonetStatsEnable.setStatus('mandatory')
xylanSonetNumOfSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 96))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanSonetNumOfSamples.setStatus('mandatory')
xylanSonetClearCurrentSample = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 23, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanSonetClearCurrentSample.setStatus('mandatory')
xylanSonetErrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 23, 3))
xylanSonetSlotIndex = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9)))
if mibBuilder.loadTexts: xylanSonetSlotIndex.setStatus('mandatory')
xylanSonetPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9)))
if mibBuilder.loadTexts: xylanSonetPortIndex.setStatus('mandatory')
xylanSonetHardwareIndex = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 3), Integer32())
if mibBuilder.loadTexts: xylanSonetHardwareIndex.setStatus('mandatory')
xylanSonetErrType = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 23, 3, 4), Integer32())
if mibBuilder.loadTexts: xylanSonetErrType.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-SONET-MIB", xylanSonetNumOfSamples=xylanSonetNumOfSamples, xylanSonetErrConfig=xylanSonetErrConfig, xylanSonetEntry=xylanSonetEntry, xylanSonetErrType=xylanSonetErrType, xylanSonetErrGroup=xylanSonetErrGroup, xylanSonetHardwareIndex=xylanSonetHardwareIndex, xylanSonetPortIndex=xylanSonetPortIndex, xylanSonetSlotIndex=xylanSonetSlotIndex, xylanSonetTable=xylanSonetTable, xylanSonetStatsEnable=xylanSonetStatsEnable, xylanSonetClearCurrentSample=xylanSonetClearCurrentSample)
