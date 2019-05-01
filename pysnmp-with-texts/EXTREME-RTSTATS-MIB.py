#
# PySNMP MIB module EXTREME-RTSTATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeRtStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 11))
if mibBuilder.loadTexts: extremeRtStats.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: extremeRtStats.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeRtStats.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeRtStats.setDescription('Extreme real time stats related objects')
extremeRtStatsTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1), )
if mibBuilder.loadTexts: extremeRtStatsTable.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsTable.setDescription('A list of real time stats entries.')
extremeRtStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1), ).setIndexNames((0, "EXTREME-RTSTATS-MIB", "extremeRtStatsIndex"))
if mibBuilder.loadTexts: extremeRtStatsEntry.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsEntry.setDescription('The last sample of Ethernet statistics on a particular Ethernet interface. This sample is associated with the RMON historyControlEntry which set up the parameters for a regular collection of these samples.')
extremeRtStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsIndex.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsIndex.setDescription('The history of which this entry is a part. The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex of the RMON historyControl table.')
extremeRtStatsIntervalStart = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsIntervalStart.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsIntervalStart.setDescription('The value of sysUpTime at the start of the interval over which this sample was measured.')
extremeRtStatsCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsCRCAlignErrors.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsCRCAlignErrors.setDescription('The number of packets received during the last sampling interval that had a length (excluding framing bits but including FCS octets) between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).')
extremeRtStatsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsUndersizePkts.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsUndersizePkts.setDescription('The number of packets received during the last sampling interval that were less than 64 octets long (excluding framing bits but including FCS octets) and were otherwise well formed.')
extremeRtStatsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsOversizePkts.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsOversizePkts.setDescription('The number of packets received during the last sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets) but were otherwise well formed.')
extremeRtStatsFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsFragments.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsFragments.setDescription('The total number of packets received during the last sampling interval that were less than 64 octets in length (excluding framing bits but including FCS octets) had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).')
extremeRtStatsJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsJabbers.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsJabbers.setDescription('The number of packets received during the last sampling interval that were longer than 1518 octets (excluding framing bits but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).')
extremeRtStatsCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsCollisions.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsCollisions.setDescription('The best estimate of the total number of collisions on this Ethernet segment during this sampling interval.')
extremeRtStatsTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsTotalErrors.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsTotalErrors.setDescription('The total number of errors on this Ethernet segment during this sampling interval. This is the sum of the crc, fragments, jabbers and collisions counters over this sampling interval.')
extremeRtStatsUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 11, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeRtStatsUtilization.setStatus('current')
if mibBuilder.loadTexts: extremeRtStatsUtilization.setDescription('The best estimate of the mean physical layer network utilization on this interface during this sampling interval, in hundredths of a percent.')
mibBuilder.exportSymbols("EXTREME-RTSTATS-MIB", extremeRtStats=extremeRtStats, extremeRtStatsCollisions=extremeRtStatsCollisions, extremeRtStatsFragments=extremeRtStatsFragments, extremeRtStatsJabbers=extremeRtStatsJabbers, extremeRtStatsCRCAlignErrors=extremeRtStatsCRCAlignErrors, extremeRtStatsOversizePkts=extremeRtStatsOversizePkts, extremeRtStatsTotalErrors=extremeRtStatsTotalErrors, extremeRtStatsIndex=extremeRtStatsIndex, extremeRtStatsTable=extremeRtStatsTable, PYSNMP_MODULE_ID=extremeRtStats, extremeRtStatsIntervalStart=extremeRtStatsIntervalStart, extremeRtStatsUtilization=extremeRtStatsUtilization, extremeRtStatsEntry=extremeRtStatsEntry, extremeRtStatsUndersizePkts=extremeRtStatsUndersizePkts)
