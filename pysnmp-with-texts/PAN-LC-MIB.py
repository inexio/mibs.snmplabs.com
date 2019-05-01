#
# PySNMP MIB module PAN-LC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAN-LC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
panModules, panProductsMibs = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules", "panProductsMibs")
panM_100, = mibBuilder.importSymbols("PAN-PRODUCTS-MIB", "panM-100")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, MibIdentifier, Bits, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Counter64, IpAddress, ObjectIdentity, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "iso")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
panLogCollectorMibsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 5))
panLogCollectorMibsModule.setRevisions(('2012-01-11 10:13',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panLogCollectorMibsModule.setRevisionsDescriptions((' Rev 1.0 Initial version of MIB module PAN-LC-MIB.',))
if mibBuilder.loadTexts: panLogCollectorMibsModule.setLastUpdated('201201111013Z')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setContactInfo(' Customer Support Palo Alto Networks 4401 Great America Pkwy Santa Clara, CA 95054-1211 +1 866-898-9087 support at paloaltonetworks dot com')
if mibBuilder.loadTexts: panLogCollectorMibsModule.setDescription(' A MIB module containing definitions of managed objects implemented by Log Collector Appliances from Palo Alto Networks.')
panLcStat = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1))
if mibBuilder.loadTexts: panLcStat.setStatus('current')
if mibBuilder.loadTexts: panLcStat.setDescription(' Sub-tree for the Log collection statistics.')
panLcLogRate = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogRate.setStatus('current')
if mibBuilder.loadTexts: panLcLogRate.setDescription('The write rate in logs/s on the Log Collection')
panLcLogDuration = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2))
if mibBuilder.loadTexts: panLcLogDuration.setStatus('current')
if mibBuilder.loadTexts: panLcLogDuration.setDescription(' Sub-tree for the Log Duration on the Log Collector. Log Duration is Expressed in Days of storage.')
panLcDiskUsage = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3))
if mibBuilder.loadTexts: panLcDiskUsage.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsage.setDescription(' Sub-tree for the Log Disk Usage on the Log Collector. Log Disk Usage is available as MB in use.')
panLcDiskUsageLd1 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd1.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd1.setDescription('The Log disk usage on logical disk 1 on the Log Collector')
panLcDiskUsageLd2 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd2.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd2.setDescription('The Log disk usage on logical disk 2 on the Log Collector')
panLcDiskUsageLd3 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd3.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd3.setDescription('The Log disk usage on logical disk 3 on the Log Collector')
panLcDiskUsageLd4 = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcDiskUsageLd4.setStatus('current')
if mibBuilder.loadTexts: panLcDiskUsageLd4.setDescription('The Log disk usage on logical disk 4 on the Log Collector')
panLcLogDurationTraffic = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTraffic.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationTraffic.setDescription('The Log duration (in days) for the traffic logs on the Log Collector')
panLcLogDurationConfig = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationConfig.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationConfig.setDescription('The Log duration (in days) for the config logs on the Log Collector')
panLcLogDurationSystem = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationSystem.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationSystem.setDescription('The Log duration (in days) for the system logs on the Log Collector')
panLcLogDurationThreat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThreat.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationThreat.setDescription('The Log duration (in days) for the threat logs on the Log Collector')
panLcLogDurationAppstat = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAppstat.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationAppstat.setDescription('The Log duration (in days) for the appstat logs on the Log Collector')
panLcLogDurationTrsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationTrsum.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationTrsum.setDescription('The Log duration (in days) for the trsum logs on the Log Collector')
panLcLogDurationThsum = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationThsum.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationThsum.setDescription('The Log duration (in days) for the thsum logs on the Log Collector')
panLcLogDurationEvent = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationEvent.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationEvent.setDescription('The Log duration (in days) for the event logs on the Log Collector')
panLcLogDurationAlarm = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationAlarm.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationAlarm.setDescription('The Log duration (in days) for the alarm logs on the Log Collector')
panLcLogDurationHipmatch = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationHipmatch.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationHipmatch.setDescription('The Log duration (in days) for the hipmatch logs on the Log Collector')
panLcLogDurationUserid = MibScalar((1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panLcLogDurationUserid.setStatus('current')
if mibBuilder.loadTexts: panLcLogDurationUserid.setDescription('The Log duration (in days) for the userid logs on the Log Collector')
mibBuilder.exportSymbols("PAN-LC-MIB", panLcDiskUsageLd1=panLcDiskUsageLd1, PYSNMP_MODULE_ID=panLogCollectorMibsModule, panLcLogDurationSystem=panLcLogDurationSystem, panLcLogDurationThsum=panLcLogDurationThsum, panLcLogDurationConfig=panLcLogDurationConfig, panLcLogDurationUserid=panLcLogDurationUserid, panLcLogDurationAlarm=panLcLogDurationAlarm, panLcDiskUsageLd4=panLcDiskUsageLd4, panLcLogDurationTrsum=panLcLogDurationTrsum, panLcStat=panLcStat, panLcLogDurationTraffic=panLcLogDurationTraffic, panLcLogDurationHipmatch=panLcLogDurationHipmatch, panLcLogDurationEvent=panLcLogDurationEvent, panLcLogDurationAppstat=panLcLogDurationAppstat, panLcDiskUsageLd3=panLcDiskUsageLd3, panLcLogDurationThreat=panLcLogDurationThreat, panLcDiskUsage=panLcDiskUsage, panLcLogRate=panLcLogRate, panLcDiskUsageLd2=panLcDiskUsageLd2, panLcLogDuration=panLcLogDuration, panLogCollectorMibsModule=panLogCollectorMibsModule)
