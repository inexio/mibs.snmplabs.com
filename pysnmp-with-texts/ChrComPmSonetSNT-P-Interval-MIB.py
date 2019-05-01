#
# PySNMP MIB module ChrComPmSonetSNT-P-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmSonetSNT-P-Interval-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmSonet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, MibIdentifier, Gauge32, iso, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "MibIdentifier", "Gauge32", "iso", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmSonetSNT_P_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11), ).setLabel("chrComPmSonetSNT-P-IntervalTable")
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalTable.setDescription('')
chrComPmSonetSNT_P_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1), ).setLabel("chrComPmSonetSNT-P-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmSonetSNT-P-Interval-MIB", "chrComPmSonetIntervalNumber"))
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSNT_P_IntervalEntry.setDescription('')
chrComPmSonetIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetIntervalNumber.setDescription('')
chrComPmSonetSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSuspectedInterval.setDescription('')
chrComPmSonetElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetElapsedTime.setDescription('')
chrComPmSonetSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSuppressedIntrvls.setDescription('')
chrComPmSonetES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetES.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetES.setDescription('')
chrComPmSonetSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetSES.setDescription('')
chrComPmSonetCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetCV.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetCV.setDescription('')
chrComPmSonetUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetUAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetUAS.setDescription('')
chrComPmSonetPS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 2, 11, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmSonetPS.setStatus('current')
if mibBuilder.loadTexts: chrComPmSonetPS.setDescription('')
mibBuilder.exportSymbols("ChrComPmSonetSNT-P-Interval-MIB", chrComPmSonetCV=chrComPmSonetCV, chrComPmSonetSNT_P_IntervalTable=chrComPmSonetSNT_P_IntervalTable, chrComPmSonetSES=chrComPmSonetSES, chrComPmSonetSuppressedIntrvls=chrComPmSonetSuppressedIntrvls, chrComPmSonetElapsedTime=chrComPmSonetElapsedTime, chrComPmSonetES=chrComPmSonetES, chrComPmSonetUAS=chrComPmSonetUAS, chrComPmSonetIntervalNumber=chrComPmSonetIntervalNumber, chrComPmSonetSuspectedInterval=chrComPmSonetSuspectedInterval, chrComPmSonetSNT_P_IntervalEntry=chrComPmSonetSNT_P_IntervalEntry, chrComPmSonetPS=chrComPmSonetPS)
