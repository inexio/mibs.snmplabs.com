#
# PySNMP MIB module COLUBRIS-DEVICE-DOT1X-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COLUBRIS-DEVICE-DOT1X-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ModuleIdentity, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, NotificationType, Counter32, TimeTicks, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "NotificationType", "Counter32", "TimeTicks", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
colubrisDeviceDot1xMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 32))
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setContactInfo('Colubris Networks Postal: 200 West Street Ste 300 Waltham, Massachusetts 02451-1121 UNITED STATES Phone: +1 781 684 0001 Fax: +1 781 684 0009 E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIB.setDescription('Colubris Device IEEE 802.1x MIB.')
colubrisDeviceDot1xMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1))
coDeviceDot1xConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 1))
coDeviceDot1xStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2))
coDeviceDot1xStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3))
coDeviceDot1xStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatusTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatusTable.setDescription('Device IEEE 802.1x wireless station status attributes.')
coDeviceDot1xStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaIndex"))
if mibBuilder.loadTexts: coDeviceDot1xStatusEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatusEntry.setDescription('An entry in the coDeviceDot1xStatusTable. coDevDisIndex - Uniquely identifies a device on the controller. coDev1xStaIndex - Uniquely identifies a 802.1X station on the device.')
coDev1xStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDev1xStaIndex.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaIndex.setDescription('Specifies the index of a 802.1X station on the device.')
coDev1xStaMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaMacAddress.setDescription('Wireless MAC address of the 802.1X station.')
coDev1xStaUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaUserName.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaUserName.setDescription('The User-Name representing the identity of the Supplicant PAE.')
coDev1xStaPaeState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("initialize", 1), ("disconnected", 2), ("connecting", 3), ("authenticating", 4), ("authenticated", 5), ("aborting", 6), ("held", 7), ("forceAuth", 8), ("forceUnauth", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPaeState.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaPaeState.setDescription('The current value of the Authenticator PAE state machine.')
coDev1xStaBackendAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("request", 1), ("response", 2), ("success", 3), ("fail", 4), ("timeout", 5), ("idle", 6), ("initialize", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthState.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthState.setDescription('The current state of the Backend Authentication state machine.')
coDev1xStaPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authorized", 1), ("unauthorized", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaPortStatus.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaPortStatus.setDescription('The current value of the controlled Port status parameter for the Port.')
coDev1xStaSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 7), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaSessionTime.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaSessionTime.setDescription('The duration of the session in seconds.')
coDev1xStaTerminateCause = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 999))).clone(namedValues=NamedValues(("supplicantLogoff", 1), ("portFailure", 2), ("supplicantRestart", 3), ("reauthFailed", 4), ("authControlForceUnauth", 5), ("portReInit", 6), ("portAdminDisabled", 7), ("notTerminatedYet", 999)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaTerminateCause.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaTerminateCause.setDescription('The reason for session termination.')
coDeviceDot1xStatsTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceDot1xStatsTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatsTable.setDescription('Device IEEE 802.1X wireless client statistic attributes.')
coDeviceDot1xStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1), )
coDeviceDot1xStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-DOT1X-MIB", "coDeviceDot1xStatsEntry"))
coDeviceDot1xStatsEntry.setIndexNames(*coDeviceDot1xStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceDot1xStatsEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceDot1xStatsEntry.setDescription('An entry in the coDeviceDot1xStatsTable. coDevDisIndex - Uniquely identify a device on the controller. coDev1xStaIndex - Uniquely identify a 802.1X station on the device.')
coDev1xStaEapolRxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolRxFrame.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaEapolRxFrame.setDescription('The number of valid EAPOL frames of any type that have been received by this Authenticator.')
coDev1xStaEapolTxFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaEapolTxFrame.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaEapolTxFrame.setDescription('The number of EAPOL frames of any type that have been transmitted by this Authenticator.')
coDev1xStaBackendResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendResponses.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendResponses.setDescription('Counts the number of times that the state machine sends an initial Access-Request packet to the Authentication server (i.e., executes sendRespToServer on entry to the RESPONSE state). Indicates that the Authenticator attempted communication with the Authentication Server.')
coDev1xStaBackendChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendChallenges.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendChallenges.setDescription('Counts the number of times that the state machine receives an initial Access-Challenge packet from the Authentication server (i.e., aReq becomes TRUE, causing exit from the RESPONSE state). Indicates that the Authentication Server has communication with the Authenticator.')
coDev1xStaBackendAuthSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthSuccesses.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthSuccesses.setDescription('Counts the number of times that the state machine receives an EAP-Success message from the Authentication Server (i.e., aSuccess becomes TRUE, causing a transition from RESPONSE to SUCCESS). Indicates that the Supplicant has successfully authenticated to the Authentication Server.')
coDev1xStaBackendAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDev1xStaBackendAuthFails.setStatus('current')
if mibBuilder.loadTexts: coDev1xStaBackendAuthFails.setDescription('Counts the number of times that the state machine receives an EAP-Failure message from the Authentication Server (i.e., aFail becomes TRUE, causing a transition from RESPONSE to FAIL). Indicates that the Supplicant has not authenticated to the Authentication Server.')
colubrisDeviceDot1xMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2))
colubrisDeviceDot1xMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1))
colubrisDeviceDot1xMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2))
colubrisDeviceDot1xMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1, 1)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "colubrisDeviceDot1xStatusMIBGroup"), ("COLUBRIS-DEVICE-DOT1X-MIB", "colubrisDeviceDot1xStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xMIBCompliance = colubrisDeviceDot1xMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xMIBCompliance.setDescription('The compliance statement for the Device MIB.')
colubrisDeviceDot1xStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 1)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaMacAddress"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaUserName"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPaeState"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthState"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPortStatus"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaSessionTime"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaTerminateCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xStatusMIBGroup = colubrisDeviceDot1xStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xStatusMIBGroup.setDescription('A collection of status objects for IEEE 802.1x stations connected to colubris devices.')
colubrisDeviceDot1xStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 2)).setObjects(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolRxFrame"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolTxFrame"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendResponses"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendChallenges"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthSuccesses"), ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthFails"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDot1xStatsMIBGroup = colubrisDeviceDot1xStatsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDot1xStatsMIBGroup.setDescription('A collection of statistical objects for IEEE 802.1X stations connected to HP devices.')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-DOT1X-MIB", coDeviceDot1xStatsGroup=coDeviceDot1xStatsGroup, PYSNMP_MODULE_ID=colubrisDeviceDot1xMIB, coDev1xStaEapolRxFrame=coDev1xStaEapolRxFrame, colubrisDeviceDot1xMIBCompliances=colubrisDeviceDot1xMIBCompliances, coDeviceDot1xStatusTable=coDeviceDot1xStatusTable, colubrisDeviceDot1xStatsMIBGroup=colubrisDeviceDot1xStatsMIBGroup, coDev1xStaBackendResponses=coDev1xStaBackendResponses, coDeviceDot1xStatsTable=coDeviceDot1xStatsTable, coDev1xStaUserName=coDev1xStaUserName, colubrisDeviceDot1xMIBConformance=colubrisDeviceDot1xMIBConformance, coDev1xStaIndex=coDev1xStaIndex, coDev1xStaEapolTxFrame=coDev1xStaEapolTxFrame, coDev1xStaTerminateCause=coDev1xStaTerminateCause, colubrisDeviceDot1xMIBGroups=colubrisDeviceDot1xMIBGroups, coDev1xStaBackendChallenges=coDev1xStaBackendChallenges, coDev1xStaPortStatus=coDev1xStaPortStatus, coDeviceDot1xStatusGroup=coDeviceDot1xStatusGroup, coDev1xStaMacAddress=coDev1xStaMacAddress, colubrisDeviceDot1xMIBObjects=colubrisDeviceDot1xMIBObjects, coDeviceDot1xStatusEntry=coDeviceDot1xStatusEntry, coDev1xStaBackendAuthSuccesses=coDev1xStaBackendAuthSuccesses, coDeviceDot1xConfigGroup=coDeviceDot1xConfigGroup, colubrisDeviceDot1xMIBCompliance=colubrisDeviceDot1xMIBCompliance, colubrisDeviceDot1xMIB=colubrisDeviceDot1xMIB, coDev1xStaBackendAuthFails=coDev1xStaBackendAuthFails, colubrisDeviceDot1xStatusMIBGroup=colubrisDeviceDot1xStatusMIBGroup, coDev1xStaBackendAuthState=coDev1xStaBackendAuthState, coDev1xStaSessionTime=coDev1xStaSessionTime, coDeviceDot1xStatsEntry=coDeviceDot1xStatsEntry, coDev1xStaPaeState=coDev1xStaPaeState)