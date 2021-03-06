#
# PySNMP MIB module HPN-ICF-LBV2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LBV2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, NotificationType, MibIdentifier, IpAddress, Counter64, iso, Integer32, TimeTicks, Bits, ObjectIdentity, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "iso", "Integer32", "TimeTicks", "Bits", "ObjectIdentity", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hpnicfLBv2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148))
hpnicfLBv2.setRevisions(('2013-11-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLBv2.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: hpnicfLBv2.setLastUpdated('201311010000Z')
if mibBuilder.loadTexts: hpnicfLBv2.setOrganization('')
if mibBuilder.loadTexts: hpnicfLBv2.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLBv2.setDescription('The private MIB file includes the LB information of the device.')
hpnicfLBv2GlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 1))
hpnicfLBv2TrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfLBv2TrapEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2TrapEnable.setDescription("Indicates whether the module of LB will generate traps for events defined in this MIB. 'enabled' results in SNMP traps; 'disabled', no traps are sent.")
hpnicfLBv2ActionTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2))
hpnicfLBv2ActionTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1), )
if mibBuilder.loadTexts: hpnicfLBv2ActionTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionTable.setDescription('Action table for LB.')
hpnicfLBv2ActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionName"))
if mibBuilder.loadTexts: hpnicfLBv2ActionEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionEntry.setDescription('An entry contains the information of the action.')
hpnicfLBv2ActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2ActionName.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionName.setDescription('Name of the action.')
hpnicfLBv2ActionDefaultSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2ActionDefaultSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionDefaultSF.setDescription('Default server farm quoted by the action. A zero length string indicates no default server farm has been assigned.')
hpnicfLBv2ActionBackupSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2ActionBackupSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionBackupSF.setDescription('Backup server farm quoted by the action. A zero length string indicates no backup server farm has been assigned.')
hpnicfLBv2ActionInUseSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2ActionInUseSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionInUseSF.setDescription('Server farm in use quoted by the action.')
hpnicfLBv2ActionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2ActionRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionRowStatus.setDescription('Status of this conceptual row. When create an action, default server farm and backup server farm are optional.')
hpnicfLBv2VSTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3))
hpnicfLBv2VSTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1), )
if mibBuilder.loadTexts: hpnicfLBv2VSTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSTable.setDescription('Virtual server table for LB.')
hpnicfLBv2VSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"))
if mibBuilder.loadTexts: hpnicfLBv2VSEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSEntry.setDescription('An entry contains the information of the virtual server.')
hpnicfLBv2VSName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2VSName.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSName.setDescription('Name of the virtual server.')
hpnicfLBv2VSConnectionsLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2VSConnectionsLimit.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnectionsLimit.setDescription('Max connections limit of the virtual server. 0 means there is no limit.')
hpnicfLBv2VSConnectionsRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2VSConnectionsRateLimit.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnectionsRateLimit.setDescription('Max connections rate limit of the virtual server. 0 means there is no limit.')
hpnicfLBv2VSDefaultSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2VSDefaultSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSDefaultSF.setDescription('Default server farm quoted by the virtual server. A zero length string indicates no default server farm has been assigned.')
hpnicfLBv2VSBackupSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2VSBackupSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSBackupSF.setDescription('Backup server farm quoted by the virtual server. A zero length string indicates no backup server farm has been assigned.')
hpnicfLBv2VSInUseSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSInUseSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSInUseSF.setDescription('Server farm in use quoted by the virtual server.')
hpnicfLBv2VSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2VSRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSRowStatus.setDescription('Status of this conceptual row. When create an virtual server, default server farm and backup server farm are optional.')
hpnicfLBv2VSStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2), )
if mibBuilder.loadTexts: hpnicfLBv2VSStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatsTable.setDescription('Virtual server statistic table for LB.')
hpnicfLBv2VSStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"))
if mibBuilder.loadTexts: hpnicfLBv2VSStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatsEntry.setDescription('An entry contains the statistic information of the virtual server.')
hpnicfLBv2VSStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2VSStatChassis.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatChassis.setDescription('ID of the device that holds the card.')
hpnicfLBv2VSStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2VSStatSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatSlot.setDescription('Member ID of the card on device.')
hpnicfLBv2VSStatCpuid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2VSStatCpuid.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatCpuid.setDescription('ID of the CPU on the card.')
hpnicfLBv2VSStatTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatTotalConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatTotalConnections.setDescription('Total number of connections that the virtual server received.')
hpnicfLBv2VSStatActiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatActiveConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatActiveConnections.setDescription('Active connections that the virtual server received.')
hpnicfLBv2VSStatClientSidePKTsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSidePKTsIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSidePKTsIn.setDescription('Number of packets that the virtual server received from client.')
hpnicfLBv2VSStatClientSidePKTsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSidePKTsOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSidePKTsOut.setDescription('Number of packets that the virtual server sent to client.')
hpnicfLBv2VSStatDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatDroppedPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatDroppedPackets.setDescription('Number of packets that the virtual server dropped.')
hpnicfLBv2VSStatClientSideBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 9), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSideBytesIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSideBytesIn.setDescription('Number of bytes that the virtual server received from client.')
hpnicfLBv2VSStatClientSideBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 10), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSideBytesOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatClientSideBytesOut.setDescription('Number of bytes that the virtual server sent to client.')
hpnicfLBv2VSStatReceivedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatReceivedRequests.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatReceivedRequests.setDescription('Number of requests that the virtual server received from client.')
hpnicfLBv2VSStatSentResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatSentResponses.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatSentResponses.setDescription('Number of responses that the virtual server sent to client.')
hpnicfLBv2VSStatConnectionsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 3, 2, 1, 13), Unsigned32()).setUnits('cps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2VSStatConnectionsRate.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSStatConnectionsRate.setDescription('Connections rate of the virtual server.')
hpnicfLBv2RSTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4))
hpnicfLBv2RSTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1), )
if mibBuilder.loadTexts: hpnicfLBv2RSTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSTable.setDescription('Real server table for LB.')
hpnicfLBv2RSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"))
if mibBuilder.loadTexts: hpnicfLBv2RSEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSEntry.setDescription('An entry contains the information of the real server.')
hpnicfLBv2RSName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2RSName.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSName.setDescription('Name of the real server.')
hpnicfLBv2RSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2RSRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSRowStatus.setDescription('Status of this conceptual row.')
hpnicfLBv2RSStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2), )
if mibBuilder.loadTexts: hpnicfLBv2RSStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatsTable.setDescription('Real server statistic table for LB.')
hpnicfLBv2RSStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatChassis"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatSlot"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2RSStatCpuid"))
if mibBuilder.loadTexts: hpnicfLBv2RSStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatsEntry.setDescription('An entry contains the statistic information of the real server.')
hpnicfLBv2RSStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2RSStatChassis.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatChassis.setDescription('ID of the device that holds the card.')
hpnicfLBv2RSStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2RSStatSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatSlot.setDescription('Member ID of the card on device.')
hpnicfLBv2RSStatCpuid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2RSStatCpuid.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatCpuid.setDescription('ID of the CPU on the card.')
hpnicfLBv2RSStatTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatTotalConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatTotalConnections.setDescription('Total number of connections that the real server received.')
hpnicfLBv2RSStatActiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatActiveConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatActiveConnections.setDescription('Active connections that the real server received.')
hpnicfLBv2RSStatServerSidePKTsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSidePKTsIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSidePKTsIn.setDescription('Number of packets that the real server received from device.')
hpnicfLBv2RSStatServerSidePKTsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSidePKTsOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSidePKTsOut.setDescription('Number of packets that the real server sent.')
hpnicfLBv2RSStatDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatDroppedPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatDroppedPackets.setDescription('Number of packets that the real server dropped.')
hpnicfLBv2RSStatServerSideBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 9), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSideBytesIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSideBytesIn.setDescription('Number of bytes that the real server received from device.')
hpnicfLBv2RSStatServerSideBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 10), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSideBytesOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatServerSideBytesOut.setDescription('Number of bytes that the real server sent.')
hpnicfLBv2RSStatReceivedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatReceivedRequests.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatReceivedRequests.setDescription('Number of requests that the real server received from device.')
hpnicfLBv2RSStatSentResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 4, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2RSStatSentResponses.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSStatSentResponses.setDescription('Number of responses that the real server sent to device.')
hpnicfLBv2SFTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5))
hpnicfLBv2SFTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1), )
if mibBuilder.loadTexts: hpnicfLBv2SFTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFTable.setDescription('Server farm table for LB.')
hpnicfLBv2SFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"))
if mibBuilder.loadTexts: hpnicfLBv2SFEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFEntry.setDescription('An entry contains the information of the server farm.')
hpnicfLBv2SFName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfLBv2SFName.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFName.setDescription('Name of the server farm.')
hpnicfLBv2SFRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfLBv2SFRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFRowStatus.setDescription('Status of this conceptual row.')
hpnicfLBv2SFStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2), )
if mibBuilder.loadTexts: hpnicfLBv2SFStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatsTable.setDescription('Server farm statistic for LB.')
hpnicfLBv2SFStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1), ).setIndexNames((0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatChassis"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatSlot"), (0, "HPN-ICF-LBV2-MIB", "hpnicfLBv2SFStatCpuid"))
if mibBuilder.loadTexts: hpnicfLBv2SFStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatsEntry.setDescription('An entry contains the statistic information of the server farm.')
hpnicfLBv2SFStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2SFStatChassis.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatChassis.setDescription('ID of the device that holds the card.')
hpnicfLBv2SFStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2SFStatSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatSlot.setDescription('Member ID of the card on device.')
hpnicfLBv2SFStatCpuid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hpnicfLBv2SFStatCpuid.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatCpuid.setDescription('ID of the CPU on the card.')
hpnicfLBv2SFStatTotalConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatTotalConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatTotalConnections.setDescription('Total number of connections that the server farm received.')
hpnicfLBv2SFStatActiveConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatActiveConnections.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatActiveConnections.setDescription('Active connections that the server farm received.')
hpnicfLBv2SFStatServerSidePKTsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSidePKTsIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSidePKTsIn.setDescription('Number of packets that the server farm received from device.')
hpnicfLBv2SFStatServerSidePKTsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSidePKTsOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSidePKTsOut.setDescription('Number of packets that the server farm sent.')
hpnicfLBv2SFStatDroppedPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatDroppedPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatDroppedPackets.setDescription('Number of packets that the server farm dropped.')
hpnicfLBv2SFStatServerSideBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 9), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSideBytesIn.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSideBytesIn.setDescription('Number of bytes that the server farm received.')
hpnicfLBv2SFStatServerSideBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 10), Counter64()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSideBytesOut.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatServerSideBytesOut.setDescription('Number of bytes that the server farm sent.')
hpnicfLBv2SFStatReceivedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatReceivedRequests.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatReceivedRequests.setDescription('Number of requests that all real servers in the server farm received from device.')
hpnicfLBv2SFStatSentResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 5, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLBv2SFStatSentResponses.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFStatSentResponses.setDescription('Number of responses that the server farm sent to device.')
hpnicfLBv2Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6))
hpnicfLBv2TrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0))
hpnicfLBv2VSConnOverloadTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 1)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsLimit"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatActiveConnections"))
if mibBuilder.loadTexts: hpnicfLBv2VSConnOverloadTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnOverloadTrap.setDescription('A hpnicfLBv2VSConnOverloadTrap notification is sent when the number of active connections of the virtual server has reached the upper limit. ')
hpnicfLBv2VSConnRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 2)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsLimit"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatActiveConnections"))
if mibBuilder.loadTexts: hpnicfLBv2VSConnRecoveryTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnRecoveryTrap.setDescription('A hpnicfLBv2VSConnRecoveryTrap notification is sent when the number of active connections of the virtual server is less than the upper limit.')
hpnicfLBv2VSConnsRateOverloadTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 3)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsRateLimit"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatConnectionsRate"))
if mibBuilder.loadTexts: hpnicfLBv2VSConnsRateOverloadTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnsRateOverloadTrap.setDescription('A hpnicfLBv2VSConnsRateOverloadTrap notification is sent when the connection rate of the virtual server has reached the upper limit.')
hpnicfLBv2VSConnsRateRecoveryTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 4)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSConnectionsRateLimit"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatChassis"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatSlot"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatCpuid"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSStatConnectionsRate"))
if mibBuilder.loadTexts: hpnicfLBv2VSConnsRateRecoveryTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSConnsRateRecoveryTrap.setDescription('A hpnicfLBv2VSConnsRateRecoveryTrap notification is sent connection rate of the virtual server is smaller than the upper limit.')
hpnicfLBv2VSActiveTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 5)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"))
if mibBuilder.loadTexts: hpnicfLBv2VSActiveTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSActiveTrap.setDescription('A hpnicfLBv2VSStatusTrap notification is sent when virtual server status changes to active.')
hpnicfLBv2VSInactiveTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 6)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"))
if mibBuilder.loadTexts: hpnicfLBv2VSInactiveTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSInactiveTrap.setDescription('A hpnicfLBv2VSStatusTrap notification is sent when virtual server status changes to inactive.')
hpnicfLBv2RSAvailableTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 7)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"))
if mibBuilder.loadTexts: hpnicfLBv2RSAvailableTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSAvailableTrap.setDescription('A hpnicfLBv2RSStatusTrap notification is sent when the status of the real server changes to available.')
hpnicfLBv2RSUnavailableTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 8)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2RSName"))
if mibBuilder.loadTexts: hpnicfLBv2RSUnavailableTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2RSUnavailableTrap.setDescription('A hpnicfLBv2RSStatusTrap notification is sent when the status of the real server changes to unavailable.')
hpnicfLBv2SFActiveTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 9)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"))
if mibBuilder.loadTexts: hpnicfLBv2SFActiveTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFActiveTrap.setDescription('A hpnicfLBv2SFStatusTrap notification is sent when the status of the server farm changes to active.')
hpnicfLBv2SFInactiveTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 10)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2SFName"))
if mibBuilder.loadTexts: hpnicfLBv2SFInactiveTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2SFInactiveTrap.setDescription('A hpnicfLBv2SFStatusTrap notification is sent when the status of the server farm changes to inactive.')
hpnicfLBv2ActionInUseSFChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 11)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionDefaultSF"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionBackupSF"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2ActionInUseSF"))
if mibBuilder.loadTexts: hpnicfLBv2ActionInUseSFChangeTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2ActionInUseSFChangeTrap.setDescription('A hpnicfLBv2VSInUseSFChangeTrap notification is sent when the server farm which is in use quoted by action changes.')
hpnicfLBv2VSInUseSFChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148, 6, 0, 12)).setObjects(("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSName"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSDefaultSF"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSBackupSF"), ("HPN-ICF-LBV2-MIB", "hpnicfLBv2VSInUseSF"))
if mibBuilder.loadTexts: hpnicfLBv2VSInUseSFChangeTrap.setStatus('current')
if mibBuilder.loadTexts: hpnicfLBv2VSInUseSFChangeTrap.setDescription('A hpnicfLBv2ActionInUseSFChangeTrap notification is sent when the server farm which is in use quoted by virtual server changes.')
mibBuilder.exportSymbols("HPN-ICF-LBV2-MIB", hpnicfLBv2=hpnicfLBv2, hpnicfLBv2SFStatSlot=hpnicfLBv2SFStatSlot, hpnicfLBv2RSStatServerSidePKTsIn=hpnicfLBv2RSStatServerSidePKTsIn, hpnicfLBv2SFStatServerSideBytesOut=hpnicfLBv2SFStatServerSideBytesOut, hpnicfLBv2SFRowStatus=hpnicfLBv2SFRowStatus, hpnicfLBv2VSStatConnectionsRate=hpnicfLBv2VSStatConnectionsRate, hpnicfLBv2RSStatSentResponses=hpnicfLBv2RSStatSentResponses, hpnicfLBv2VSRowStatus=hpnicfLBv2VSRowStatus, hpnicfLBv2SFStatsTable=hpnicfLBv2SFStatsTable, hpnicfLBv2GlobalObjects=hpnicfLBv2GlobalObjects, hpnicfLBv2VSBackupSF=hpnicfLBv2VSBackupSF, hpnicfLBv2VSStatClientSideBytesOut=hpnicfLBv2VSStatClientSideBytesOut, hpnicfLBv2VSStatsTable=hpnicfLBv2VSStatsTable, hpnicfLBv2TrapEnable=hpnicfLBv2TrapEnable, hpnicfLBv2SFActiveTrap=hpnicfLBv2SFActiveTrap, hpnicfLBv2SFStatsEntry=hpnicfLBv2SFStatsEntry, hpnicfLBv2SFStatServerSidePKTsOut=hpnicfLBv2SFStatServerSidePKTsOut, hpnicfLBv2RSStatReceivedRequests=hpnicfLBv2RSStatReceivedRequests, hpnicfLBv2SFInactiveTrap=hpnicfLBv2SFInactiveTrap, hpnicfLBv2RSTables=hpnicfLBv2RSTables, hpnicfLBv2VSConnsRateRecoveryTrap=hpnicfLBv2VSConnsRateRecoveryTrap, hpnicfLBv2VSConnsRateOverloadTrap=hpnicfLBv2VSConnsRateOverloadTrap, hpnicfLBv2RSStatServerSidePKTsOut=hpnicfLBv2RSStatServerSidePKTsOut, hpnicfLBv2RSTable=hpnicfLBv2RSTable, hpnicfLBv2RSStatsTable=hpnicfLBv2RSStatsTable, hpnicfLBv2VSTables=hpnicfLBv2VSTables, hpnicfLBv2VSStatDroppedPackets=hpnicfLBv2VSStatDroppedPackets, hpnicfLBv2VSStatClientSidePKTsOut=hpnicfLBv2VSStatClientSidePKTsOut, hpnicfLBv2SFStatReceivedRequests=hpnicfLBv2SFStatReceivedRequests, hpnicfLBv2RSStatsEntry=hpnicfLBv2RSStatsEntry, hpnicfLBv2VSStatReceivedRequests=hpnicfLBv2VSStatReceivedRequests, hpnicfLBv2SFStatActiveConnections=hpnicfLBv2SFStatActiveConnections, hpnicfLBv2SFStatServerSideBytesIn=hpnicfLBv2SFStatServerSideBytesIn, hpnicfLBv2ActionInUseSFChangeTrap=hpnicfLBv2ActionInUseSFChangeTrap, hpnicfLBv2SFStatTotalConnections=hpnicfLBv2SFStatTotalConnections, hpnicfLBv2VSStatSentResponses=hpnicfLBv2VSStatSentResponses, hpnicfLBv2ActionInUseSF=hpnicfLBv2ActionInUseSF, hpnicfLBv2VSInUseSFChangeTrap=hpnicfLBv2VSInUseSFChangeTrap, hpnicfLBv2ActionTable=hpnicfLBv2ActionTable, hpnicfLBv2RSName=hpnicfLBv2RSName, hpnicfLBv2RSUnavailableTrap=hpnicfLBv2RSUnavailableTrap, hpnicfLBv2RSStatSlot=hpnicfLBv2RSStatSlot, hpnicfLBv2SFName=hpnicfLBv2SFName, hpnicfLBv2VSDefaultSF=hpnicfLBv2VSDefaultSF, PYSNMP_MODULE_ID=hpnicfLBv2, hpnicfLBv2SFStatServerSidePKTsIn=hpnicfLBv2SFStatServerSidePKTsIn, hpnicfLBv2ActionRowStatus=hpnicfLBv2ActionRowStatus, hpnicfLBv2ActionDefaultSF=hpnicfLBv2ActionDefaultSF, hpnicfLBv2VSInUseSF=hpnicfLBv2VSInUseSF, hpnicfLBv2VSStatTotalConnections=hpnicfLBv2VSStatTotalConnections, hpnicfLBv2VSTable=hpnicfLBv2VSTable, hpnicfLBv2VSEntry=hpnicfLBv2VSEntry, hpnicfLBv2VSConnRecoveryTrap=hpnicfLBv2VSConnRecoveryTrap, hpnicfLBv2RSStatDroppedPackets=hpnicfLBv2RSStatDroppedPackets, hpnicfLBv2VSInactiveTrap=hpnicfLBv2VSInactiveTrap, hpnicfLBv2VSStatClientSidePKTsIn=hpnicfLBv2VSStatClientSidePKTsIn, hpnicfLBv2ActionEntry=hpnicfLBv2ActionEntry, hpnicfLBv2RSStatCpuid=hpnicfLBv2RSStatCpuid, hpnicfLBv2ActionName=hpnicfLBv2ActionName, hpnicfLBv2RSEntry=hpnicfLBv2RSEntry, hpnicfLBv2SFTables=hpnicfLBv2SFTables, hpnicfLBv2SFTable=hpnicfLBv2SFTable, hpnicfLBv2VSStatSlot=hpnicfLBv2VSStatSlot, hpnicfLBv2RSStatChassis=hpnicfLBv2RSStatChassis, hpnicfLBv2RSStatServerSideBytesOut=hpnicfLBv2RSStatServerSideBytesOut, hpnicfLBv2VSStatActiveConnections=hpnicfLBv2VSStatActiveConnections, hpnicfLBv2VSStatCpuid=hpnicfLBv2VSStatCpuid, hpnicfLBv2SFStatCpuid=hpnicfLBv2SFStatCpuid, hpnicfLBv2SFStatChassis=hpnicfLBv2SFStatChassis, hpnicfLBv2RSStatServerSideBytesIn=hpnicfLBv2RSStatServerSideBytesIn, hpnicfLBv2RSStatTotalConnections=hpnicfLBv2RSStatTotalConnections, hpnicfLBv2SFStatSentResponses=hpnicfLBv2SFStatSentResponses, hpnicfLBv2RSRowStatus=hpnicfLBv2RSRowStatus, hpnicfLBv2RSAvailableTrap=hpnicfLBv2RSAvailableTrap, hpnicfLBv2TrapPrefix=hpnicfLBv2TrapPrefix, hpnicfLBv2VSName=hpnicfLBv2VSName, hpnicfLBv2Trap=hpnicfLBv2Trap, hpnicfLBv2VSStatClientSideBytesIn=hpnicfLBv2VSStatClientSideBytesIn, hpnicfLBv2SFStatDroppedPackets=hpnicfLBv2SFStatDroppedPackets, hpnicfLBv2VSActiveTrap=hpnicfLBv2VSActiveTrap, hpnicfLBv2VSStatsEntry=hpnicfLBv2VSStatsEntry, hpnicfLBv2SFEntry=hpnicfLBv2SFEntry, hpnicfLBv2RSStatActiveConnections=hpnicfLBv2RSStatActiveConnections, hpnicfLBv2VSConnectionsRateLimit=hpnicfLBv2VSConnectionsRateLimit, hpnicfLBv2ActionBackupSF=hpnicfLBv2ActionBackupSF, hpnicfLBv2VSStatChassis=hpnicfLBv2VSStatChassis, hpnicfLBv2VSConnOverloadTrap=hpnicfLBv2VSConnOverloadTrap, hpnicfLBv2ActionTables=hpnicfLBv2ActionTables, hpnicfLBv2VSConnectionsLimit=hpnicfLBv2VSConnectionsLimit)
