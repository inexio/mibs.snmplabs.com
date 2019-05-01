#
# PySNMP MIB module ALVARION-USER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-USER-SESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSIDOrNone, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSIDOrNone")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, TimeTicks, iso, Bits, MibIdentifier, ModuleIdentity, Unsigned32, Counter32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "iso", "Bits", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Counter32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionUserSessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36))
if mibBuilder.loadTexts: alvarionUserSessionMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionUserSessionMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionUserSessionMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionUserSessionMIB.setDescription('Alvarion User Session MIB.')
alvarionUserSessionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1))
coUserSessionInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1))
coUserSessionStGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2))
coUserSessACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserMaxCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessACUserMaxCount.setDescription('Indicates the maximum number of concurrent authenticated AC users.')
coUserSessNonACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserMaxCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessNonACUserMaxCount.setDescription('Indicates the maximum number of concurrent authenticated non AC users.')
coUserSessACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessACUserCount.setDescription('Indicates the number of currently authenticated AC users.')
coUserSessNonACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserCount.setStatus('current')
if mibBuilder.loadTexts: coUserSessNonACUserCount.setDescription('Indicates the number of currently authenticated non AC users.')
coUserSessionTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1), )
if mibBuilder.loadTexts: coUserSessionTable.setStatus('current')
if mibBuilder.loadTexts: coUserSessionTable.setDescription('A table containing specific information for users authenticated (AC and non-AC) by the authentication system.')
coUserSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-USER-SESSION-MIB", "coUserSessIndex"))
if mibBuilder.loadTexts: coUserSessionEntry.setStatus('current')
if mibBuilder.loadTexts: coUserSessionEntry.setDescription('Information about a particular user that has been authenticated by the authentication system. coUserSessIndex - Uniquely identifies a user in the table.')
coUserSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coUserSessIndex.setStatus('current')
if mibBuilder.loadTexts: coUserSessIndex.setDescription('Index of a user in the coUserSessionTable.')
coUserSessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessUserName.setStatus('current')
if mibBuilder.loadTexts: coUserSessUserName.setDescription("Indicates the user's name.")
coUserSessClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: coUserSessClientIpAddress.setDescription("Indicates the user's IP address.")
coUserSessSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSessionDuration.setStatus('current')
if mibBuilder.loadTexts: coUserSessSessionDuration.setDescription("Indicates how long the user's session has been active. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.")
coUserSessIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessIdleTime.setStatus('current')
if mibBuilder.loadTexts: coUserSessIdleTime.setDescription("Indicates for how long the user's session has been idle. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.")
coUserSessMAPGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessMAPGroupName.setStatus('current')
if mibBuilder.loadTexts: coUserSessMAPGroupName.setDescription("Indicates the user's MultiService Access Point Group Name.")
coUserSessVSCName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVSCName.setStatus('current')
if mibBuilder.loadTexts: coUserSessVSCName.setDescription("Indicates the user's Virtual Service Community Name.")
coUserSessSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 8), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSSID.setStatus('current')
if mibBuilder.loadTexts: coUserSessSSID.setDescription("Indicates the user's Access Point SSID (ONLY when Location-aware is enabled and properly configured). If this information is not available, a zero-Length string is returned.")
coUserSessVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVLAN.setStatus('current')
if mibBuilder.loadTexts: coUserSessVLAN.setDescription('Specifies the VLAN currently assigned to the user.')
coUserSessPHYType = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPHYType.setStatus('current')
if mibBuilder.loadTexts: coUserSessPHYType.setDescription("Specifies the user's radio type.")
coUserSessAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("nonAc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessAuthType.setStatus('current')
if mibBuilder.loadTexts: coUserSessAuthType.setDescription("User's authentication type.")
coUserSessCalledStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCalledStationID.setStatus('current')
if mibBuilder.loadTexts: coUserSessCalledStationID.setDescription("Indicates the user's called station ID.")
coUserSessCallingStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCallingStationID.setStatus('current')
if mibBuilder.loadTexts: coUserSessCallingStationID.setDescription("Indicates the user's calling station ID.")
coUserSessRADIUSServerProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerProfileName.setStatus('current')
if mibBuilder.loadTexts: coUserSessRADIUSServerProfileName.setDescription('Indicates the RADIUS server profile name used to authenticate the user.')
coUserSessRADIUSServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: coUserSessRADIUSServerIpAddress.setDescription('Indicates the RADIUS server IP address used to authenticate the user.')
coUserSessBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesSent.setStatus('current')
if mibBuilder.loadTexts: coUserSessBytesSent.setDescription('Indicates the total number of bytes sent by the user. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.')
coUserSessBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesReceived.setStatus('current')
if mibBuilder.loadTexts: coUserSessBytesReceived.setDescription('Indicates the total number of bytes received by the user. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.')
coUserSessPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsSent.setStatus('current')
if mibBuilder.loadTexts: coUserSessPacketsSent.setDescription('Indicates the total number of IP packets sent by the user. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.')
coUserSessPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsReceived.setStatus('current')
if mibBuilder.loadTexts: coUserSessPacketsReceived.setDescription('Indicates the total number of IP packets received by the user. When this counter reaches its maximum value, it wraps around and starts increasing again from zero.')
userSessionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2))
userSessionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2, 0))
alvarionUserSessionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3))
alvarionUserSessionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1))
alvarionUserSessionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2))
alvarionUserSessionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1, 1)).setObjects(("ALVARION-USER-SESSION-MIB", "alvarionUserSessionInfoMIBGroup"), ("ALVARION-USER-SESSION-MIB", "alvarionUserSessionStMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionMIBCompliance = alvarionUserSessionMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionUserSessionMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion User Session MIB.')
alvarionUserSessionInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 1)).setObjects(("ALVARION-USER-SESSION-MIB", "coUserSessACUserMaxCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserMaxCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessACUserCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionInfoMIBGroup = alvarionUserSessionInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionUserSessionInfoMIBGroup.setDescription('A collection of objects providing global information for the User Session MIB.')
alvarionUserSessionStMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 2)).setObjects(("ALVARION-USER-SESSION-MIB", "coUserSessUserName"), ("ALVARION-USER-SESSION-MIB", "coUserSessClientIpAddress"), ("ALVARION-USER-SESSION-MIB", "coUserSessSessionDuration"), ("ALVARION-USER-SESSION-MIB", "coUserSessIdleTime"), ("ALVARION-USER-SESSION-MIB", "coUserSessMAPGroupName"), ("ALVARION-USER-SESSION-MIB", "coUserSessVSCName"), ("ALVARION-USER-SESSION-MIB", "coUserSessSSID"), ("ALVARION-USER-SESSION-MIB", "coUserSessVLAN"), ("ALVARION-USER-SESSION-MIB", "coUserSessPHYType"), ("ALVARION-USER-SESSION-MIB", "coUserSessAuthType"), ("ALVARION-USER-SESSION-MIB", "coUserSessCalledStationID"), ("ALVARION-USER-SESSION-MIB", "coUserSessCallingStationID"), ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerProfileName"), ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerIpAddress"), ("ALVARION-USER-SESSION-MIB", "coUserSessBytesSent"), ("ALVARION-USER-SESSION-MIB", "coUserSessBytesReceived"), ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsSent"), ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionStMIBGroup = alvarionUserSessionStMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionUserSessionStMIBGroup.setDescription('A collection of objects providing the user session MIB capability.')
mibBuilder.exportSymbols("ALVARION-USER-SESSION-MIB", coUserSessACUserMaxCount=coUserSessACUserMaxCount, coUserSessIndex=coUserSessIndex, coUserSessPHYType=coUserSessPHYType, coUserSessMAPGroupName=coUserSessMAPGroupName, coUserSessPacketsReceived=coUserSessPacketsReceived, coUserSessBytesSent=coUserSessBytesSent, coUserSessSSID=coUserSessSSID, coUserSessClientIpAddress=coUserSessClientIpAddress, coUserSessUserName=coUserSessUserName, coUserSessionStGroup=coUserSessionStGroup, alvarionUserSessionInfoMIBGroup=alvarionUserSessionInfoMIBGroup, coUserSessionTable=coUserSessionTable, alvarionUserSessionMIBGroups=alvarionUserSessionMIBGroups, coUserSessNonACUserCount=coUserSessNonACUserCount, userSessionMIBNotificationPrefix=userSessionMIBNotificationPrefix, coUserSessCallingStationID=coUserSessCallingStationID, alvarionUserSessionMIBCompliance=alvarionUserSessionMIBCompliance, coUserSessNonACUserMaxCount=coUserSessNonACUserMaxCount, userSessionMIBNotifications=userSessionMIBNotifications, coUserSessPacketsSent=coUserSessPacketsSent, alvarionUserSessionMIBConformance=alvarionUserSessionMIBConformance, alvarionUserSessionMIB=alvarionUserSessionMIB, alvarionUserSessionStMIBGroup=alvarionUserSessionStMIBGroup, coUserSessVLAN=coUserSessVLAN, PYSNMP_MODULE_ID=alvarionUserSessionMIB, coUserSessVSCName=coUserSessVSCName, coUserSessRADIUSServerProfileName=coUserSessRADIUSServerProfileName, coUserSessionInfoGroup=coUserSessionInfoGroup, coUserSessAuthType=coUserSessAuthType, coUserSessSessionDuration=coUserSessSessionDuration, coUserSessRADIUSServerIpAddress=coUserSessRADIUSServerIpAddress, alvarionUserSessionMIBObjects=alvarionUserSessionMIBObjects, coUserSessCalledStationID=coUserSessCalledStationID, coUserSessACUserCount=coUserSessACUserCount, alvarionUserSessionMIBCompliances=alvarionUserSessionMIBCompliances, coUserSessionEntry=coUserSessionEntry, coUserSessBytesReceived=coUserSessBytesReceived, coUserSessIdleTime=coUserSessIdleTime)
