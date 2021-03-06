#
# PySNMP MIB module ChrComPmDs3DS3-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmDs3DS3-Interval-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmDs3, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmDs3")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, TimeTicks, Gauge32, Unsigned32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmDs3DS3_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12), ).setLabel("chrComPmDs3DS3-IntervalTable")
if mibBuilder.loadTexts: chrComPmDs3DS3_IntervalTable.setStatus('current')
chrComPmDs3DS3_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1), ).setLabel("chrComPmDs3DS3-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmDs3DS3-Interval-MIB", "chrComPmDs3IntervalNumber"))
if mibBuilder.loadTexts: chrComPmDs3DS3_IntervalEntry.setStatus('current')
chrComPmDs3IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3IntervalNumber.setStatus('current')
chrComPmDs3SuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setStatus('current')
chrComPmDs3ElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setStatus('current')
chrComPmDs3SuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setStatus('current')
chrComPmDs3LCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LCV.setStatus('current')
chrComPmDs3LES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LES.setStatus('current')
chrComPmDs3LSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LSES.setStatus('current')
chrComPmDs3LOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LOSS.setStatus('current')
chrComPmDs3PCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PCV.setStatus('current')
chrComPmDs3CCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CCV.setStatus('current')
chrComPmDs3PES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PES.setStatus('current')
chrComPmDs3CES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CES.setStatus('current')
chrComPmDs3PSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSES.setStatus('current')
chrComPmDs3CSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CSES.setStatus('current')
chrComPmDs3SAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SAS.setStatus('current')
chrComPmDs3AISS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3AISS.setStatus('current')
chrComPmDs3UASP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASP.setStatus('current')
chrComPmDs3UASCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 18), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASCP.setStatus('current')
chrComPmDs3PSC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 19), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSC.setStatus('current')
chrComPmDs3ESPLCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 12, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setStatus('current')
mibBuilder.exportSymbols("ChrComPmDs3DS3-Interval-MIB", chrComPmDs3LOSS=chrComPmDs3LOSS, chrComPmDs3PES=chrComPmDs3PES, chrComPmDs3SAS=chrComPmDs3SAS, chrComPmDs3CSES=chrComPmDs3CSES, chrComPmDs3ElapsedTime=chrComPmDs3ElapsedTime, chrComPmDs3IntervalNumber=chrComPmDs3IntervalNumber, chrComPmDs3SuppressedIntrvls=chrComPmDs3SuppressedIntrvls, chrComPmDs3CCV=chrComPmDs3CCV, chrComPmDs3CES=chrComPmDs3CES, chrComPmDs3LCV=chrComPmDs3LCV, chrComPmDs3UASCP=chrComPmDs3UASCP, chrComPmDs3ESPLCP=chrComPmDs3ESPLCP, chrComPmDs3PCV=chrComPmDs3PCV, chrComPmDs3DS3_IntervalTable=chrComPmDs3DS3_IntervalTable, chrComPmDs3PSES=chrComPmDs3PSES, chrComPmDs3SuspectedInterval=chrComPmDs3SuspectedInterval, chrComPmDs3AISS=chrComPmDs3AISS, chrComPmDs3PSC=chrComPmDs3PSC, chrComPmDs3DS3_IntervalEntry=chrComPmDs3DS3_IntervalEntry, chrComPmDs3LES=chrComPmDs3LES, chrComPmDs3LSES=chrComPmDs3LSES, chrComPmDs3UASP=chrComPmDs3UASP)
