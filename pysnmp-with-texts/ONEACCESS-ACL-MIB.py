#
# PySNMP MIB module ONEACCESS-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
oacEventSeverityLevel, oacEventText = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventSeverityLevel", "oacEventText")
oacExpIMIpAcl, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIpAcl", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, TimeTicks, ObjectIdentity, Counter64, Counter32, NotificationType, MibIdentifier, Unsigned32, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "iso", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacAclMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 669))
oacAclMIBModule.setRevisions(('2011-06-15 00:00', '2010-07-08 10:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacAclMIBModule.setRevisionsDescriptions(('Added Interface type and fixed minor corrections.', 'This MIB module describes IP ACL Management objects.',))
if mibBuilder.loadTexts: oacAclMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacAclMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacAclMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacAclMIBModule.setDescription('Contact updated')
class InterfaceType(TextualConvention, Integer32):
    description = 'The interface type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("mainInterface", 1), ("subInterface", 2))

oacExpIMIpAclStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1))
oacExpIMIpAclNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2))
oacExpIMIpAccountingStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3))
oacAclNotificationMaximumSessionReached = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 1))
if mibBuilder.loadTexts: oacAclNotificationMaximumSessionReached.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationMaximumSessionReached.setDescription('An ACL Notification maximum session reached signifies that the number of ACL sessions has reached its configured limit')
oacAclNotificationWarningSessionReachingLimit = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 2))
if mibBuilder.loadTexts: oacAclNotificationWarningSessionReachingLimit.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationWarningSessionReachingLimit.setDescription('An ACL Notification warning session reaching limit signifies that the number of ACL sessions is near from its maximum configured limit')
oacAclNotificationMaximumHalfSessionReached = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 3))
if mibBuilder.loadTexts: oacAclNotificationMaximumHalfSessionReached.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationMaximumHalfSessionReached.setDescription('An ACL Notification maximum half-session reached signifies that the number of ACL half-sessions has reached its configured limit, as stateful inspection is enabled on the device')
oacAclNotificationWarningHalfSessionReachingLimit = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 4))
if mibBuilder.loadTexts: oacAclNotificationWarningHalfSessionReachingLimit.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationWarningHalfSessionReachingLimit.setDescription('An ACL Notification warning half-session reaching limit signifies that the number of ACL half-sessions is near from its configured limit. Note that this notification is received only if stateful inspection is enabled on the device')
oacAclNotificationMaximumSessionReachedPerHost = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 5)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"), ("ONEACCESS-EVENTS-MIB", "oacEventSeverityLevel"))
if mibBuilder.loadTexts: oacAclNotificationMaximumSessionReachedPerHost.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationMaximumSessionReachedPerHost.setDescription('An ACL Notification maximum session per host reached signifies that the number of ACL sessions per host has reached its configured limit for the host whose IP address is added to the notification message. This trap is sent only if inspection per host and stateful inspection is enabled ')
oacAclNotificationMaximumHalfSessionReachedPerHost = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 2, 6))
if mibBuilder.loadTexts: oacAclNotificationMaximumHalfSessionReachedPerHost.setStatus('current')
if mibBuilder.loadTexts: oacAclNotificationMaximumHalfSessionReachedPerHost.setDescription('An ACL Notification maximum half-session per host reached signifies that the number of ACL half-sessions per host has reached its configured limit, for the host whose IP address is added to the notification message. This trap is sent only if inspection per host and stateful inspection are enabled ')
oacAclStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1))
oacAclStatNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 2))
oacAclStatConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3))
oacAclStatGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1))
oacAclMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclMaxSessions.setStatus('current')
if mibBuilder.loadTexts: oacAclMaxSessions.setDescription(' Maximum number of sessions ')
oacAclActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclActiveSessions.setStatus('current')
if mibBuilder.loadTexts: oacAclActiveSessions.setDescription('Number of active sessions ')
oacAclSessionsClosed = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclSessionsClosed.setStatus('current')
if mibBuilder.loadTexts: oacAclSessionsClosed.setDescription('Total number of sessions closed')
oacAclDynamicAllocFailures = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclDynamicAllocFailures.setStatus('current')
if mibBuilder.loadTexts: oacAclDynamicAllocFailures.setDescription('Dynamic allocation failures')
oacAclInboundPkts = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclInboundPkts.setStatus('current')
if mibBuilder.loadTexts: oacAclInboundPkts.setDescription('Total inbound packets')
oacAclOutboundPkts = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclOutboundPkts.setStatus('current')
if mibBuilder.loadTexts: oacAclOutboundPkts.setDescription('Total outbound packets')
oacAclInboundPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclInboundPktsDropped.setStatus('current')
if mibBuilder.loadTexts: oacAclInboundPktsDropped.setDescription('Total inbound packets')
oacAclOutboundPktsDropped = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacAclOutboundPktsDropped.setStatus('current')
if mibBuilder.loadTexts: oacAclOutboundPktsDropped.setDescription('Total outbound packets')
oacIpAccountingTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1), )
if mibBuilder.loadTexts: oacIpAccountingTable.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingTable.setDescription('Interface Accounting Table')
oacIpAccountingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1), ).setIndexNames((0, "ONEACCESS-ACL-MIB", "oacIpAccountingIndex"))
if mibBuilder.loadTexts: oacIpAccountingEntry.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingEntry.setDescription('Description')
oacIpAccountingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingIndex.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingIndex.setDescription('IP Accounting Index')
oacIpAccountingIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingIfIndex.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingIfIndex.setDescription('IP Accounting Interface Index')
oacIpAccountingIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 1, 1, 3), InterfaceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingIfType.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingIfType.setDescription('IP Accounting Interface Type')
oacIpAccountingStatTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2), )
if mibBuilder.loadTexts: oacIpAccountingStatTable.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatTable.setDescription('IP Accounting Statistic Table')
oacIpAccountingStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1), ).setIndexNames((0, "ONEACCESS-ACL-MIB", "oacIpAccountingIndex"))
if mibBuilder.loadTexts: oacIpAccountingStatEntry.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatEntry.setDescription('Description')
oacIpAccountingStatIpSource = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingStatIpSource.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatIpSource.setDescription('Ip Source')
oacIpAccountingStatIpDest = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingStatIpDest.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatIpDest.setDescription('Ip Destination')
oacIpAccountingStatNbPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingStatNbPackets.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatNbPackets.setDescription('Nb packets')
oacIpAccountingStatNbBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingStatNbBytes.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingStatNbBytes.setDescription('Nb Bytes')
oacIpAccoutingGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3))
oacIpAccountingMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingMaxSessions.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingMaxSessions.setDescription(' Maximum number of Ip Accounting sessions ')
oacIpAccountingCurrentSessions = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingCurrentSessions.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingCurrentSessions.setDescription(' Number of current Ip Accounting sessions ')
oacIpAccountingAge = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingAge.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingAge.setDescription(' IP Accounting data Age')
oacIpAccountingNbNotAnalysedBytes = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingNbNotAnalysedBytes.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingNbNotAnalysedBytes.setDescription(' Number of not annalysed bytes')
oacIpAccountingNbNotAnalysedPackets = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 3, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpAccountingNbNotAnalysedPackets.setStatus('current')
if mibBuilder.loadTexts: oacIpAccountingNbNotAnalysedPackets.setDescription(' Number of not annalysed packets')
oacIpAccoutingClear = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpAccoutingClear.setStatus('current')
if mibBuilder.loadTexts: oacIpAccoutingClear.setDescription('Set this to 1 to clear IP accounting statistics')
oacAclStatGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 1))
oacAclStatCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 2))
oacAclStatCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 2, 1)).setObjects(("ONEACCESS-ACL-MIB", "oacAclStatGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacAclStatCompliance = oacAclStatCompliance.setStatus('current')
if mibBuilder.loadTexts: oacAclStatCompliance.setDescription('The compliance statement for agents that support the ONEACCESS-ACL-MIB.')
oacAclStatGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 2, 1, 3, 1, 1)).setObjects(("ONEACCESS-ACL-MIB", "oacAclMaxSessions"), ("ONEACCESS-ACL-MIB", "oacAclActiveSessions"), ("ONEACCESS-ACL-MIB", "oacAclSessionsClosed"), ("ONEACCESS-ACL-MIB", "oacAclDynamicAllocFailures"), ("ONEACCESS-ACL-MIB", "oacAclInboundPkts"), ("ONEACCESS-ACL-MIB", "oacAclOutboundPkts"), ("ONEACCESS-ACL-MIB", "oacAclInboundPktsDropped"), ("ONEACCESS-ACL-MIB", "oacAclOutboundPktsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacAclStatGeneralGroup = oacAclStatGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: oacAclStatGeneralGroup.setDescription('This group is mandatory for all ACL entities.')
mibBuilder.exportSymbols("ONEACCESS-ACL-MIB", oacExpIMIpAclStatistics=oacExpIMIpAclStatistics, oacAclOutboundPktsDropped=oacAclOutboundPktsDropped, oacAclNotificationMaximumHalfSessionReachedPerHost=oacAclNotificationMaximumHalfSessionReachedPerHost, oacIpAccountingAge=oacIpAccountingAge, oacAclMaxSessions=oacAclMaxSessions, InterfaceType=InterfaceType, oacIpAccountingTable=oacIpAccountingTable, oacIpAccountingStatTable=oacIpAccountingStatTable, oacIpAccoutingGlobal=oacIpAccoutingGlobal, oacExpIMIpAccountingStatistics=oacExpIMIpAccountingStatistics, oacAclStatConformance=oacAclStatConformance, oacIpAccountingMaxSessions=oacIpAccountingMaxSessions, oacIpAccountingIfType=oacIpAccountingIfType, oacAclOutboundPkts=oacAclOutboundPkts, oacExpIMIpAclNotifications=oacExpIMIpAclNotifications, oacIpAccountingNbNotAnalysedBytes=oacIpAccountingNbNotAnalysedBytes, oacIpAccountingEntry=oacIpAccountingEntry, oacAclStatObjects=oacAclStatObjects, oacAclStatGlobal=oacAclStatGlobal, PYSNMP_MODULE_ID=oacAclMIBModule, oacIpAccountingStatNbBytes=oacIpAccountingStatNbBytes, oacIpAccountingCurrentSessions=oacIpAccountingCurrentSessions, oacAclStatNotifications=oacAclStatNotifications, oacIpAccountingStatNbPackets=oacIpAccountingStatNbPackets, oacIpAccountingStatEntry=oacIpAccountingStatEntry, oacAclStatCompliance=oacAclStatCompliance, oacAclNotificationWarningHalfSessionReachingLimit=oacAclNotificationWarningHalfSessionReachingLimit, oacAclNotificationMaximumSessionReachedPerHost=oacAclNotificationMaximumSessionReachedPerHost, oacIpAccountingNbNotAnalysedPackets=oacIpAccountingNbNotAnalysedPackets, oacAclStatGeneralGroup=oacAclStatGeneralGroup, oacAclMIBModule=oacAclMIBModule, oacAclSessionsClosed=oacAclSessionsClosed, oacIpAccountingStatIpDest=oacIpAccountingStatIpDest, oacIpAccoutingClear=oacIpAccoutingClear, oacAclStatCompliances=oacAclStatCompliances, oacAclInboundPktsDropped=oacAclInboundPktsDropped, oacAclStatGroups=oacAclStatGroups, oacAclNotificationWarningSessionReachingLimit=oacAclNotificationWarningSessionReachingLimit, oacAclActiveSessions=oacAclActiveSessions, oacAclNotificationMaximumSessionReached=oacAclNotificationMaximumSessionReached, oacIpAccountingStatIpSource=oacIpAccountingStatIpSource, oacAclNotificationMaximumHalfSessionReached=oacAclNotificationMaximumHalfSessionReached, oacIpAccountingIndex=oacIpAccountingIndex, oacAclInboundPkts=oacAclInboundPkts, oacIpAccountingIfIndex=oacIpAccountingIfIndex, oacAclDynamicAllocFailures=oacAclDynamicAllocFailures)
