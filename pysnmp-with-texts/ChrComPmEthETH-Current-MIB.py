#
# PySNMP MIB module ChrComPmEthETH-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmEthETH-Current-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmEth, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmEth")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, ObjectIdentity, TimeTicks, Integer32, Gauge32, Counter32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ObjectIdentity", "TimeTicks", "Integer32", "Gauge32", "Counter32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "MibIdentifier", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmEthETH_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10), ).setLabel("chrComPmEthETH-CurrentTable")
if mibBuilder.loadTexts: chrComPmEthETH_CurrentTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthETH_CurrentTable.setDescription('')
chrComPmEthETH_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1), ).setLabel("chrComPmEthETH-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmEthETH_CurrentEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthETH_CurrentEntry.setDescription('')
chrComPmEthSuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthSuspectedInterval.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthSuspectedInterval.setDescription('')
chrComPmEthElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthElapsedTime.setDescription('')
chrComPmEthSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthSuppressedIntrvls.setDescription('')
chrComPmEthdot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsFCSErrors.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthdot3StatsFCSErrors.setDescription('')
chrComPmEthdot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsLateCollisions.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthdot3StatsLateCollisions.setDescription('')
chrComPmEthdot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsFrameTooLongs.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthdot3StatsFrameTooLongs.setDescription('')
chrComPmEthdot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthdot3StatsInternalMacReceiveErrors.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthdot3StatsInternalMacReceiveErrors.setDescription('')
chrComPmEthifInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInOctets.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInOctets.setDescription('')
chrComPmEthifInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInUcastPkts.setDescription('')
chrComPmEthifInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInDiscards.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInDiscards.setDescription('')
chrComPmEthifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInErrors.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInErrors.setDescription('')
chrComPmEthifOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutOctets.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifOutOctets.setDescription('')
chrComPmEthifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifOutUcastPkts.setDescription('')
chrComPmEthifInMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInMulticastPkts.setDescription('')
chrComPmEthifInBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifInBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifInBroadcastPkts.setDescription('')
chrComPmEthifOutMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 16), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifOutMulticastPkts.setDescription('')
chrComPmEthifOutBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthifOutBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthifOutBroadcastPkts.setDescription('')
chrComPmEthchrFrames64Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 18), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames64Bytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames64Bytes.setDescription('')
chrComPmEthchrFrames65to127Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 19), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames65to127Bytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames65to127Bytes.setDescription('')
chrComPmEthchrFrames128to256Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames128to256Bytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames128to256Bytes.setDescription('')
chrComPmEthchrFrames257to512Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 21), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames257to512Bytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames257to512Bytes.setDescription('')
chrComPmEthchrFrames513to1024Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 22), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames513to1024Bytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames513to1024Bytes.setDescription('')
chrComPmEthchrFrames1024toMaxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 23), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmEthchrFrames1024toMaxBytes.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthchrFrames1024toMaxBytes.setDescription('')
chrComPmEthResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 10, 1, 24), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmEthResetPmCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmEthResetPmCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmEthETH-Current-MIB", chrComPmEthResetPmCountersAction=chrComPmEthResetPmCountersAction, chrComPmEthifOutMulticastPkts=chrComPmEthifOutMulticastPkts, chrComPmEthSuspectedInterval=chrComPmEthSuspectedInterval, chrComPmEthifOutOctets=chrComPmEthifOutOctets, chrComPmEthchrFrames128to256Bytes=chrComPmEthchrFrames128to256Bytes, chrComPmEthifInOctets=chrComPmEthifInOctets, chrComPmEthdot3StatsFrameTooLongs=chrComPmEthdot3StatsFrameTooLongs, chrComPmEthSuppressedIntrvls=chrComPmEthSuppressedIntrvls, chrComPmEthdot3StatsFCSErrors=chrComPmEthdot3StatsFCSErrors, chrComPmEthifInMulticastPkts=chrComPmEthifInMulticastPkts, chrComPmEthifInBroadcastPkts=chrComPmEthifInBroadcastPkts, chrComPmEthifOutUcastPkts=chrComPmEthifOutUcastPkts, chrComPmEthchrFrames64Bytes=chrComPmEthchrFrames64Bytes, chrComPmEthETH_CurrentEntry=chrComPmEthETH_CurrentEntry, chrComPmEthElapsedTime=chrComPmEthElapsedTime, chrComPmEthifInDiscards=chrComPmEthifInDiscards, chrComPmEthdot3StatsInternalMacReceiveErrors=chrComPmEthdot3StatsInternalMacReceiveErrors, chrComPmEthETH_CurrentTable=chrComPmEthETH_CurrentTable, chrComPmEthifInUcastPkts=chrComPmEthifInUcastPkts, chrComPmEthdot3StatsLateCollisions=chrComPmEthdot3StatsLateCollisions, chrComPmEthchrFrames1024toMaxBytes=chrComPmEthchrFrames1024toMaxBytes, chrComPmEthifInErrors=chrComPmEthifInErrors, chrComPmEthchrFrames513to1024Bytes=chrComPmEthchrFrames513to1024Bytes, chrComPmEthifOutBroadcastPkts=chrComPmEthifOutBroadcastPkts, chrComPmEthchrFrames65to127Bytes=chrComPmEthchrFrames65to127Bytes, chrComPmEthchrFrames257to512Bytes=chrComPmEthchrFrames257to512Bytes)
