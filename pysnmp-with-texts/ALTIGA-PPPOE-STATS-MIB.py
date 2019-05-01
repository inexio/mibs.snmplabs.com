#
# PySNMP MIB module ALTIGA-PPPOE-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-PPPOE-STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:21:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alPPPoEMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alPPPoEMibModule")
alStatsPPPoE, alPPPoEGroup = mibBuilder.importSymbols("ALTIGA-MIB", "alStatsPPPoE", "alPPPoEGroup")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, iso, TimeTicks, Counter64, MibIdentifier, IpAddress, Unsigned32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "TimeTicks", "Counter64", "MibIdentifier", "IpAddress", "Unsigned32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
altigaPPPoEStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2))
altigaPPPoEStatsMibModule.setRevisions(('2007-07-11 00:00', '2002-09-05 13:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaPPPoEStatsMibModule.setRevisionsDescriptions(('Added range for Index Object alPPPoEStatsIfIndex object ', 'Added module compliance.', 'Updated with new header',))
if mibBuilder.loadTexts: altigaPPPoEStatsMibModule.setLastUpdated('200707110000Z')
if mibBuilder.loadTexts: altigaPPPoEStatsMibModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaPPPoEStatsMibModule.setContactInfo('Cisco Systems 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaPPPoEStatsMibModule.setDescription('The Altiga PPPoE Statistics MIB models counters and objects that are of management interest for PPPoE. Acronyms The following acronyms are used in this document: MIB: Management Information Base PADI: PPPoE Active Discovery Initiation PADO: PPPoE Active Discovery Offer PADS: PPPoE Active Discovery Session-confirmation PADT: PPPoE Active Discovery Terminate PPPoE: Point-to-Point Protocol over Ethernet ')
alStatsPPPoEGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1))
alPPPoEStatsActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsActiveSessions.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsActiveSessions.setDescription('The number of active sessions on the interface (currently should max at 1).')
alPPPoEStatsTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsTotalSessions.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsTotalSessions.setDescription('Total Sessions since last reset.')
alPPPoEStatsMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsMaxSessions.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsMaxSessions.setDescription('Peak number of sessions since last reset.')
alPPPoEStatsIfTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2), )
if mibBuilder.loadTexts: alPPPoEStatsIfTable.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfTable.setDescription('Contains the PPPoE binding entries for stats.')
alPPPoEStatsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1), ).setIndexNames((0, "ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfIndex"))
if mibBuilder.loadTexts: alPPPoEStatsIfEntry.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfEntry.setDescription('Contains the PPPoE entries for the status binding table.')
alPPPoEStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfIndex.setDescription('The interface index for PPPoE status binding table.')
alPPPoEStatsIfPADTRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPADTRx.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPADTRx.setDescription('Number of PADT received.')
alPPPoEStatsIfPADTTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPADTTx.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPADTTx.setDescription('Number of PADT transmitted.')
alPPPoEStatsIfGenericErrorsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfGenericErrorsRx.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfGenericErrorsRx.setDescription('Number of Generic Errors Received.')
alPPPoEStatsIfMalformedPacketsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfMalformedPacketsRx.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfMalformedPacketsRx.setDescription('Number of back packets received.')
alPPPoEStatsIfPADITimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPADITimeouts.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPADITimeouts.setDescription('Number of times timedout waiting for a PADO.')
alPPPoEStatsIfPADRTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPADRTimeouts.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPADRTimeouts.setDescription('Number of times timed out waiting for a PADS.')
alPPPoEStatsIfMultPADORx = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfMultPADORx.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfMultPADORx.setDescription('Number of times we received more than 1 PADO.')
alPPPoEStatsIfSessionID = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfSessionID.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfSessionID.setDescription('Session ID given by the AC.')
alPPPoEStatsIfPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPeerAddr.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPeerAddr.setDescription('MAC address of the remote AC.')
alPPPoEStatsIfSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("noState", 1), ("pADISent", 2), ("pADIRcvd", 3), ("pADOSent", 4), ("pADORcvd", 5), ("pADRSent", 6), ("pADRRcvd", 7), ("pADSSent", 8), ("pADSRcvd", 9), ("sessionStage", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfSessionState.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfSessionState.setDescription('State that the session is in.')
alPPPoEStatsIfVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfVersion.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfVersion.setDescription('Version as given in the PPPoE RFC.')
alPPPoEStatsIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfType.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfType.setDescription('Type as given in the PPPoE RFC.')
alPPPoEStatsIfConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfConnectTime.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfConnectTime.setDescription('Time_t of when the session was established.')
alPPPoEStatsIfDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfDuration.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfDuration.setDescription('Number of seconds since the session was established.')
alPPPoEStatsIfPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfPeerName.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfPeerName.setDescription('UTF-8 string of the AC name.')
alPPPoEStatsIfACCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfACCookie.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfACCookie.setDescription('Binary sequence representing the AC cookie given in negotiations.')
alPPPoEStatsIfHostUnique = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfHostUnique.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfHostUnique.setDescription('Binary sequence representing the value we assigned the PADI.')
alPPPoEStatsIfRelaySessID = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alPPPoEStatsIfRelaySessID.setStatus('current')
if mibBuilder.loadTexts: alPPPoEStatsIfRelaySessID.setDescription('12 octets representing the Relay session if one exists.')
altigaPPPoEStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1))
altigaPPPoEStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1, 1))
altigaPPPoEStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1, 1, 1)).setObjects(("ALTIGA-PPPOE-STATS-MIB", "altigaPPPoEStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaPPPoEStatsMibCompliance = altigaPPPoEStatsMibCompliance.setStatus('current')
if mibBuilder.loadTexts: altigaPPPoEStatsMibCompliance.setDescription('The compliance statement for agents which implement the Altiga PPPoE Statistics MIB.')
altigaPPPoEStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 40, 2)).setObjects(("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsActiveSessions"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsTotalSessions"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsMaxSessions"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfIndex"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADTRx"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADTTx"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfGenericErrorsRx"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfMalformedPacketsRx"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADITimeouts"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADRTimeouts"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfMultPADORx"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfSessionID"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPeerAddr"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfSessionState"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfVersion"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfType"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfConnectTime"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfDuration"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPeerName"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfACCookie"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfHostUnique"), ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfRelaySessID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaPPPoEStatsGroup = altigaPPPoEStatsGroup.setStatus('current')
if mibBuilder.loadTexts: altigaPPPoEStatsGroup.setDescription('The objects for PPPoE Statistics.')
mibBuilder.exportSymbols("ALTIGA-PPPOE-STATS-MIB", alPPPoEStatsIfConnectTime=alPPPoEStatsIfConnectTime, alPPPoEStatsIfSessionID=alPPPoEStatsIfSessionID, alPPPoEStatsIfPADTRx=alPPPoEStatsIfPADTRx, alPPPoEStatsActiveSessions=alPPPoEStatsActiveSessions, alPPPoEStatsIfEntry=alPPPoEStatsIfEntry, alPPPoEStatsIfPADRTimeouts=alPPPoEStatsIfPADRTimeouts, altigaPPPoEStatsMibConformance=altigaPPPoEStatsMibConformance, altigaPPPoEStatsMibCompliance=altigaPPPoEStatsMibCompliance, alPPPoEStatsIfMalformedPacketsRx=alPPPoEStatsIfMalformedPacketsRx, alPPPoEStatsIfDuration=alPPPoEStatsIfDuration, alPPPoEStatsIfVersion=alPPPoEStatsIfVersion, alPPPoEStatsIfPADITimeouts=alPPPoEStatsIfPADITimeouts, alPPPoEStatsIfTable=alPPPoEStatsIfTable, alPPPoEStatsIfHostUnique=alPPPoEStatsIfHostUnique, alPPPoEStatsIfGenericErrorsRx=alPPPoEStatsIfGenericErrorsRx, alStatsPPPoEGlobal=alStatsPPPoEGlobal, alPPPoEStatsTotalSessions=alPPPoEStatsTotalSessions, alPPPoEStatsIfPeerAddr=alPPPoEStatsIfPeerAddr, alPPPoEStatsMaxSessions=alPPPoEStatsMaxSessions, altigaPPPoEStatsGroup=altigaPPPoEStatsGroup, alPPPoEStatsIfRelaySessID=alPPPoEStatsIfRelaySessID, alPPPoEStatsIfSessionState=alPPPoEStatsIfSessionState, PYSNMP_MODULE_ID=altigaPPPoEStatsMibModule, alPPPoEStatsIfPADTTx=alPPPoEStatsIfPADTTx, alPPPoEStatsIfPeerName=alPPPoEStatsIfPeerName, altigaPPPoEStatsMibCompliances=altigaPPPoEStatsMibCompliances, alPPPoEStatsIfMultPADORx=alPPPoEStatsIfMultPADORx, altigaPPPoEStatsMibModule=altigaPPPoEStatsMibModule, alPPPoEStatsIfType=alPPPoEStatsIfType, alPPPoEStatsIfACCookie=alPPPoEStatsIfACCookie, alPPPoEStatsIfIndex=alPPPoEStatsIfIndex)
