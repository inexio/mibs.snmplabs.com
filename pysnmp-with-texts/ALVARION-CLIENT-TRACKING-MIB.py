#
# PySNMP MIB module ALVARION-CLIENT-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-CLIENT-TRACKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionNotificationEnable, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionNotificationEnable")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, ModuleIdentity, NotificationType, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Gauge32, iso, Counter64, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso", "Counter64", "Counter32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionClientTrackingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19))
if mibBuilder.loadTexts: alvarionClientTrackingMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionClientTrackingMIB.setOrganization('Alvarion Ltd.')
if mibBuilder.loadTexts: alvarionClientTrackingMIB.setContactInfo('Alvarion Ltd. Postal: 21a HaBarzel St. P.O. Box 13139 Tel-Aviv 69710 Israel Phone: +972 3 645 6262')
if mibBuilder.loadTexts: alvarionClientTrackingMIB.setDescription('Alvarion Client Tracking module.')
alvarionClientTrackingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1))
clientTrackingConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1))
clientTrackingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 2))
clientTrackingSuccessfulAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 1), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociationNotificationEnabled.setDescription('Specifies if clientTrackingSuccessfulAssociation notifications are generated.')
clientTrackingAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 2), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingAssociationFailureNotificationEnabled.setDescription('Specifies if clientTrackingAssociationFailure notifications are generated.')
clientTrackingSuccessfulReAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 3), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociationNotificationEnabled.setDescription('Specifies if clientTrackingSuccessfulReAssociation notifications are generated.')
clientTrackingReAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 4), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingReAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingReAssociationFailureNotificationEnabled.setDescription('Specifies if clientTrackingReAssociationFailure notifications are generated.')
clientTrackingSuccessfulAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 5), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthenticationNotificationEnabled.setDescription('Specifies if clientTrackingSuccessfulAuthentication notifications are generated.')
clientTrackingAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 6), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingAuthenticationFailureNotificationEnabled.setDescription('Specifies if clientTrackingAuthenticationFailure notifications are generated.')
clientTrackingSuccessfulDisAssociationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 7), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociationNotificationEnabled.setDescription('Specifies if clientTrackingSuccessfulDisAssociation notifications are generated.')
clientTrackingDisAssociationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 8), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingDisAssociationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingDisAssociationFailureNotificationEnabled.setDescription('Specifies if clientTrackingDisAssociationFailure notifications are generated.')
clientTrackingSuccessfulDeAuthenticationNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 9), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setDescription('Specifies if clientTrackingSuccessfulDeAuthentication notifications are generated.')
clientTrackingDeAuthenticationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 1, 10), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailureNotificationEnabled.setDescription('Specifies if clientTrackingDeAuthenticationFailure notifications are generated.')
clientTrackingEventInformation = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clientTrackingEventInformation.setStatus('current')
if mibBuilder.loadTexts: clientTrackingEventInformation.setDescription('Gives a detailed description of an event in the system.')
alvarionClientTrackingMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2))
alvarionClientTrackingMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0))
clientTrackingSuccessfulAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 1)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociation.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulAssociation.setDescription('Sent when a user is successfully associated with the AP.')
clientTrackingAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 2)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: clientTrackingAssociationFailure.setDescription('Sent when a user has failed to associate with the AP.')
clientTrackingSuccessfulReAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 3)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociation.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulReAssociation.setDescription('Sent when a user is successfully reassociated with the AP.')
clientTrackingReAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 4)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingReAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: clientTrackingReAssociationFailure.setDescription('Sent when a user has failed to reassociate with the AP.')
clientTrackingSuccessfulAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 5)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthentication.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulAuthentication.setDescription('Sent when a user is successfully authenticated.')
clientTrackingAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 6)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: clientTrackingAuthenticationFailure.setDescription('Sent when a user has failed to authenticate.')
clientTrackingSuccessfulDisAssociation = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 7)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociation.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulDisAssociation.setDescription('Sent when a user is successfully disassociated from the AP.')
clientTrackingDisAssociationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 8)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingDisAssociationFailure.setStatus('current')
if mibBuilder.loadTexts: clientTrackingDisAssociationFailure.setDescription('Sent when a user has failed to disassociate from the AP.')
clientTrackingSuccessfulDeAuthentication = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 9)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthentication.setStatus('current')
if mibBuilder.loadTexts: clientTrackingSuccessfulDeAuthentication.setDescription('Sent when a user is successfully deauthenticated.')
clientTrackingDeAuthenticationFailure = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 2, 0, 10)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailure.setStatus('current')
if mibBuilder.loadTexts: clientTrackingDeAuthenticationFailure.setDescription('Sent when a user has failed to deauthenticate.')
alvarionClientTrackingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3))
alvarionClientTrackingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 1))
alvarionClientTrackingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2))
alvarionClientTrackingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 1, 1)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "alvarionClientTrackingConfigMIBGroup"), ("ALVARION-CLIENT-TRACKING-MIB", "alvarionClientTrackingInfoMIBGroup"), ("ALVARION-CLIENT-TRACKING-MIB", "alvarionClientTrackingNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionClientTrackingMIBCompliance = alvarionClientTrackingMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alvarionClientTrackingMIBCompliance.setDescription('The compliance statement for entities which implement the Alvarion Tools MIB.')
alvarionClientTrackingConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 1)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociationNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailureNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociationNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailureNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthenticationNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailureNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociationNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailureNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthenticationNotificationEnabled"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionClientTrackingConfigMIBGroup = alvarionClientTrackingConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionClientTrackingConfigMIBGroup.setDescription('A collection of objects providing control over the client tracking MIB capability.')
alvarionClientTrackingInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 2)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingEventInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionClientTrackingInfoMIBGroup = alvarionClientTrackingInfoMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionClientTrackingInfoMIBGroup.setDescription('A collection of objects providing information over the client tracking MIB capability.')
alvarionClientTrackingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 19, 3, 2, 3)).setObjects(("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAssociation"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAssociationFailure"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulReAssociation"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingReAssociationFailure"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulAuthentication"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingAuthenticationFailure"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDisAssociation"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDisAssociationFailure"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingSuccessfulDeAuthentication"), ("ALVARION-CLIENT-TRACKING-MIB", "clientTrackingDeAuthenticationFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionClientTrackingNotificationGroup = alvarionClientTrackingNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: alvarionClientTrackingNotificationGroup.setDescription('A collection of supported notifications.')
mibBuilder.exportSymbols("ALVARION-CLIENT-TRACKING-MIB", clientTrackingInfo=clientTrackingInfo, alvarionClientTrackingMIBNotificationPrefix=alvarionClientTrackingMIBNotificationPrefix, clientTrackingSuccessfulAuthentication=clientTrackingSuccessfulAuthentication, clientTrackingSuccessfulDeAuthentication=clientTrackingSuccessfulDeAuthentication, alvarionClientTrackingMIBGroups=alvarionClientTrackingMIBGroups, clientTrackingDeAuthenticationFailureNotificationEnabled=clientTrackingDeAuthenticationFailureNotificationEnabled, PYSNMP_MODULE_ID=alvarionClientTrackingMIB, alvarionClientTrackingNotificationGroup=alvarionClientTrackingNotificationGroup, clientTrackingSuccessfulDeAuthenticationNotificationEnabled=clientTrackingSuccessfulDeAuthenticationNotificationEnabled, clientTrackingEventInformation=clientTrackingEventInformation, alvarionClientTrackingMIBCompliance=alvarionClientTrackingMIBCompliance, clientTrackingConfig=clientTrackingConfig, clientTrackingAuthenticationFailure=clientTrackingAuthenticationFailure, alvarionClientTrackingConfigMIBGroup=alvarionClientTrackingConfigMIBGroup, clientTrackingAuthenticationFailureNotificationEnabled=clientTrackingAuthenticationFailureNotificationEnabled, alvarionClientTrackingMIBNotifications=alvarionClientTrackingMIBNotifications, alvarionClientTrackingMIBObjects=alvarionClientTrackingMIBObjects, alvarionClientTrackingMIB=alvarionClientTrackingMIB, clientTrackingSuccessfulReAssociation=clientTrackingSuccessfulReAssociation, clientTrackingSuccessfulReAssociationNotificationEnabled=clientTrackingSuccessfulReAssociationNotificationEnabled, clientTrackingReAssociationFailure=clientTrackingReAssociationFailure, alvarionClientTrackingInfoMIBGroup=alvarionClientTrackingInfoMIBGroup, clientTrackingSuccessfulAssociation=clientTrackingSuccessfulAssociation, clientTrackingSuccessfulDisAssociation=clientTrackingSuccessfulDisAssociation, clientTrackingReAssociationFailureNotificationEnabled=clientTrackingReAssociationFailureNotificationEnabled, alvarionClientTrackingMIBCompliances=alvarionClientTrackingMIBCompliances, clientTrackingDisAssociationFailure=clientTrackingDisAssociationFailure, clientTrackingDisAssociationFailureNotificationEnabled=clientTrackingDisAssociationFailureNotificationEnabled, clientTrackingSuccessfulAuthenticationNotificationEnabled=clientTrackingSuccessfulAuthenticationNotificationEnabled, alvarionClientTrackingMIBConformance=alvarionClientTrackingMIBConformance, clientTrackingSuccessfulAssociationNotificationEnabled=clientTrackingSuccessfulAssociationNotificationEnabled, clientTrackingAssociationFailure=clientTrackingAssociationFailure, clientTrackingAssociationFailureNotificationEnabled=clientTrackingAssociationFailureNotificationEnabled, clientTrackingDeAuthenticationFailure=clientTrackingDeAuthenticationFailure, clientTrackingSuccessfulDisAssociationNotificationEnabled=clientTrackingSuccessfulDisAssociationNotificationEnabled)