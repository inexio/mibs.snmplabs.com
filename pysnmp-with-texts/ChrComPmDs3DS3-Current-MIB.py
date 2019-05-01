#
# PySNMP MIB module ChrComPmDs3DS3-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmDs3DS3-Current-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmDs3, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmDs3")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, NotificationType, TimeTicks, Unsigned32, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "NotificationType", "TimeTicks", "Unsigned32", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmDs3DS3_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10), ).setLabel("chrComPmDs3DS3-CurrentTable")
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentTable.setDescription('')
chrComPmDs3DS3_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1), ).setLabel("chrComPmDs3DS3-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3DS3_CurrentEntry.setDescription('')
chrComPmDs3SuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setDescription('')
chrComPmDs3ElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setDescription('')
chrComPmDs3SuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setDescription('')
chrComPmDs3LCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LCV.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3LCV.setDescription('')
chrComPmDs3LES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3LES.setDescription('')
chrComPmDs3LSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3LSES.setDescription('')
chrComPmDs3LOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3LOSS.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3LOSS.setDescription('')
chrComPmDs3PCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PCV.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3PCV.setDescription('')
chrComPmDs3CCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CCV.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3CCV.setDescription('')
chrComPmDs3PES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3PES.setDescription('')
chrComPmDs3CES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3CES.setDescription('')
chrComPmDs3PSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3PSES.setDescription('')
chrComPmDs3CSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3CSES.setDescription('')
chrComPmDs3SAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3SAS.setDescription('')
chrComPmDs3AISS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3AISS.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3AISS.setDescription('')
chrComPmDs3UASP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASP.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3UASP.setDescription('')
chrComPmDs3UASCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASCP.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3UASCP.setDescription('')
chrComPmDs3PSC = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 18), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3PSC.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3PSC.setDescription('')
chrComPmDs3ESPLCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 19), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setDescription('')
chrComPmDs3ThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ThresholdProfIndex.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3ThresholdProfIndex.setDescription('')
chrComPmDs3ResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 10, 1, 21), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ResetPmCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmDs3ResetPmCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmDs3DS3-Current-MIB", chrComPmDs3PES=chrComPmDs3PES, chrComPmDs3PCV=chrComPmDs3PCV, chrComPmDs3SAS=chrComPmDs3SAS, chrComPmDs3LSES=chrComPmDs3LSES, chrComPmDs3SuspectedInterval=chrComPmDs3SuspectedInterval, chrComPmDs3AISS=chrComPmDs3AISS, chrComPmDs3ThresholdProfIndex=chrComPmDs3ThresholdProfIndex, chrComPmDs3ResetPmCountersAction=chrComPmDs3ResetPmCountersAction, chrComPmDs3SuppressedIntrvls=chrComPmDs3SuppressedIntrvls, chrComPmDs3CCV=chrComPmDs3CCV, chrComPmDs3LCV=chrComPmDs3LCV, chrComPmDs3DS3_CurrentTable=chrComPmDs3DS3_CurrentTable, chrComPmDs3CSES=chrComPmDs3CSES, chrComPmDs3UASCP=chrComPmDs3UASCP, chrComPmDs3PSES=chrComPmDs3PSES, chrComPmDs3ESPLCP=chrComPmDs3ESPLCP, chrComPmDs3LOSS=chrComPmDs3LOSS, chrComPmDs3ElapsedTime=chrComPmDs3ElapsedTime, chrComPmDs3CES=chrComPmDs3CES, chrComPmDs3UASP=chrComPmDs3UASP, chrComPmDs3LES=chrComPmDs3LES, chrComPmDs3PSC=chrComPmDs3PSC, chrComPmDs3DS3_CurrentEntry=chrComPmDs3DS3_CurrentEntry)
