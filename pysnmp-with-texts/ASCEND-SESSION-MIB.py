#
# PySNMP MIB module ASCEND-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-SESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
sessionStatusGroup, = mibBuilder.importSymbols("ASCEND-MIB", "sessionStatusGroup")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Integer32, ModuleIdentity, Unsigned32, MibIdentifier, Counter32, Gauge32, Bits, iso, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter32", "Gauge32", "Bits", "iso", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

ssnStatusMaximumSessions = MibScalar((1, 3, 6, 1, 4, 1, 529, 12, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusMaximumSessions.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusMaximumSessions.setDescription('The maximum number of sessions that can exist in the system.')
sessionStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 2), )
if mibBuilder.loadTexts: sessionStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: sessionStatusTable.setDescription('A list of session status entries.')
sessionStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 2, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "ssnStatusIndex"))
if mibBuilder.loadTexts: sessionStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sessionStatusEntry.setDescription('An entry containing object variables to describe a session.')
ssnStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusIndex.setDescription("The index number for this session status entry. Its value ranges from 1 to 'ssnStatusMaximumSessions'.")
ssnStatusValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssnStatusValidFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusValidFlag.setDescription('Value indicates whether this entry contains valid information or not. Setting a valid(2) session to invalid(1) causes an effective session termination.')
ssnStatusUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserName.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusUserName.setDescription('The name of the remote user. The null string is returned if entry is invalid. For a Radius DNIS authenticated session, value of User-Name provided in Radius reply will be used if no second tier authentication is involved.')
ssnStatusUserIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusUserIPAddress.setDescription('The IP address of the remote user. The value 0.0.0.0 is returned if entry is invalid.')
ssnStatusUserSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusUserSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusUserSubnetMask.setDescription('The subnet mask of the remote user. The value 0.0.0.0 is returned if entry is invalid.')
ssnStatusCurrentService = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("ppp", 3), ("slip", 4), ("mpp", 5), ("x25", 6), ("combinet", 7), ("frameRelay", 8), ("euraw", 9), ("euui", 10), ("telnet", 11), ("telnetBinary", 12), ("rawTcp", 13), ("terminalServer", 14), ("mp", 15), ("virtualConnect", 16), ("dchannelX25", 17), ("dtpt", 18), ("ipFax", 19), ("atm", 20), ("hdlcNrm", 21), ("voip", 22), ("visa2", 23), ("netToNet", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusCurrentService.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusCurrentService.setDescription('The current service provided to the remote user. The value none(1) is returned if entry is invalid OR if user dials into the terminal server and is in midst of a login sequence.')
ssnStatusCallReferenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnStatusCallReferenceNum.setStatus('mandatory')
if mibBuilder.loadTexts: ssnStatusCallReferenceNum.setDescription('A unique number identifying this session. The value 0 is returned if entry is invalid.')
sessionActiveTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 3), )
if mibBuilder.loadTexts: sessionActiveTable.setStatus('mandatory')
if mibBuilder.loadTexts: sessionActiveTable.setDescription('A list of active session entries. This table is similar to sessionStatusTable with invalid entries screened out and indexed by ssnActiveCallReferenceNum. ssnActiveCallReferenceNum tracks ssnStatusCallReferenceNum of sessionStatusTable.')
sessionActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 3, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "ssnActiveCallReferenceNum"))
if mibBuilder.loadTexts: sessionActiveEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sessionActiveEntry.setDescription('An entry containing object variables to describe an active session.')
ssnActiveCallReferenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveCallReferenceNum.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveCallReferenceNum.setDescription('A unique number identifying this active session. Refer to ssnStatusCallReferenceNum for more information.')
ssnActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveIndex.setDescription("The index number for this session status entry. Its value ranges from 1 to 'ssnStatusMaximumSessions'. Refer to ssnStatusIndex for more information.")
ssnActiveValidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ssnActiveValidFlag.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveValidFlag.setDescription('All entries will be valid(2). Refer to ssnStatusValidFlag for more information. Setting a vaild(2) session as invalid(1) causes an effective session termination.')
ssnActiveUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserName.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveUserName.setDescription('The name of the remote user. Refer to ssnStatusUserName for more information. For a Radius DNIS authenticated session, value of User-Name provided in Radius reply will be used if no second tier authentication is involved.')
ssnActiveUserIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveUserIPAddress.setDescription('The IP address of the remote user. Refer to ssnStatusUserIPAddress for more information.')
ssnActiveUserSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveUserSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveUserSubnetMask.setDescription('The subnet mask of the remote user. Refer to ssnStatusUserSubnetMask for more information.')
ssnActiveCurrentService = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25))).clone(namedValues=NamedValues(("none", 1), ("other", 2), ("ppp", 3), ("slip", 4), ("mpp", 5), ("x25", 6), ("combinet", 7), ("frameRelay", 8), ("euraw", 9), ("euui", 10), ("telnet", 11), ("telnetBinary", 12), ("rawTcp", 13), ("terminalServer", 14), ("mp", 15), ("virtualConnect", 16), ("dchannelX25", 17), ("dtpt", 18), ("ipFax", 19), ("atm", 20), ("hdlcNrm", 21), ("voip", 22), ("visa2", 23), ("netToNet", 25)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveCurrentService.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveCurrentService.setDescription('The current service provided to the remote user. The value none(1) is returned if entry is invalid OR if user dials into the terminal server and is in midst of a login sequence. Refer to ssnStatusCurrentService for more information.')
ssnActiveIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 3, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssnActiveIdleTime.setStatus('mandatory')
if mibBuilder.loadTexts: ssnActiveIdleTime.setDescription('The time current session has been idle. Valid only for sessions terminated on any of the host cards(i.e. dial up sessions), for others 0 is always reported. For non-TNT and non-Max platforms 0 is always reported.')
mppActiveStatsTable = MibTable((1, 3, 6, 1, 4, 1, 529, 12, 4), )
if mibBuilder.loadTexts: mppActiveStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mppActiveStatsTable.setDescription('A list of active MPP session statistics with invalid entries screened out and indexed by mppStatsMpID.')
mppActiveStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 12, 4, 1), ).setIndexNames((0, "ASCEND-SESSION-MIB", "mppStatsMpID"))
if mibBuilder.loadTexts: mppActiveStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mppActiveStatsEntry.setDescription('An entry containing object variables to describe an active MPP session. The variables are those seen in the Dyn Stat area of the LCD display.')
mppStatsMpID = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsMpID.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsMpID.setDescription('The MpID number for this active MPP session entry.')
mppStatsRemoteName = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsRemoteName.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsRemoteName.setDescription('The name of the remote user.')
mppStatsQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("good", 1), ("fair", 2), ("marginal", 3), ("poor", 4), ("na", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsQuality.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsQuality.setDescription('Line quality. N/A: No MPP sessions currenly active, Good: <%1 CRC errors, Fair: <%5 CRC errors, Marginal: <%10 CRC errors, Poor: %10 or > CRC errors')
mppStatsBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsBandwidth.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsBandwidth.setDescription('Total bit rate (Kbps) for the MPP session.')
mppStatsTotalChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsTotalChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsTotalChannels.setDescription('The total number of channels associated with this MPP session.')
mppStatsCLU = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsCLU.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsCLU.setDescription('Current percentage of line utilization for transmitted packets during this MPP session.')
mppStatsALU = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsALU.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsALU.setDescription('Average percentage of line utilization for transmitted packets during this MPP session.')
mppStatsStartingTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 12, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mppStatsStartingTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: mppStatsStartingTimeStamp.setDescription('The starting time for this MPP session in seconds since startup.')
mibBuilder.exportSymbols("ASCEND-SESSION-MIB", mppStatsCLU=mppStatsCLU, ssnStatusUserIPAddress=ssnStatusUserIPAddress, ssnStatusUserSubnetMask=ssnStatusUserSubnetMask, ssnStatusCallReferenceNum=ssnStatusCallReferenceNum, ssnStatusMaximumSessions=ssnStatusMaximumSessions, mppStatsQuality=mppStatsQuality, ssnStatusUserName=ssnStatusUserName, ssnActiveValidFlag=ssnActiveValidFlag, ssnActiveIndex=ssnActiveIndex, ssnActiveCallReferenceNum=ssnActiveCallReferenceNum, ssnActiveCurrentService=ssnActiveCurrentService, sessionStatusTable=sessionStatusTable, mppActiveStatsEntry=mppActiveStatsEntry, mppStatsRemoteName=mppStatsRemoteName, ssnStatusIndex=ssnStatusIndex, sessionActiveEntry=sessionActiveEntry, sessionStatusEntry=sessionStatusEntry, ssnActiveUserName=ssnActiveUserName, mppActiveStatsTable=mppActiveStatsTable, sessionActiveTable=sessionActiveTable, ssnActiveIdleTime=ssnActiveIdleTime, ssnActiveUserSubnetMask=ssnActiveUserSubnetMask, mppStatsALU=mppStatsALU, ssnStatusCurrentService=ssnStatusCurrentService, ssnActiveUserIPAddress=ssnActiveUserIPAddress, DisplayString=DisplayString, mppStatsStartingTimeStamp=mppStatsStartingTimeStamp, mppStatsTotalChannels=mppStatsTotalChannels, ssnStatusValidFlag=ssnStatusValidFlag, mppStatsBandwidth=mppStatsBandwidth, mppStatsMpID=mppStatsMpID)
