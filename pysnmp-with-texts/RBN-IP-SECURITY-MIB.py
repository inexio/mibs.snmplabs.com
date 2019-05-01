#
# PySNMP MIB module RBN-IP-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-IP-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
IANAItuProbableCause, IANAItuEventType = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuProbableCause", "IANAItuEventType")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, TimeTicks, Counter64, ObjectIdentity, Counter32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Integer32, IpAddress, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "Counter32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "Bits")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
rbnIpSecurityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 55))
rbnIpSecurityMib.setRevisions(('2011-01-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnIpSecurityMib.setRevisionsDescriptions(('Initial Version.',))
if mibBuilder.loadTexts: rbnIpSecurityMib.setLastUpdated('201101140000Z')
if mibBuilder.loadTexts: rbnIpSecurityMib.setOrganization('Ericsson AB')
if mibBuilder.loadTexts: rbnIpSecurityMib.setContactInfo(' Ericsson AB 100 Headquarters Dr San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 ')
if mibBuilder.loadTexts: rbnIpSecurityMib.setDescription('Defines the objects necessary to support the management of IPSEC objects.')
rbnIpSecNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0))
rbnIpSecObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1))
rbnIpSecConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2))
rbnIpSecNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1))
rbnIpSecEventDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecEventDateAndTime.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecEventDateAndTime.setDescription('The date and time when the event was raised.')
rbnIpSecEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 2), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecEventSeverity.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecEventSeverity.setDescription('The current severity of the event.')
rbnIpSecEventType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 3), IANAItuEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecEventType.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecEventType.setDescription('The type of the event.')
rbnIpSecEventProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 4), IANAItuProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecEventProbableCause.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecEventProbableCause.setDescription('The probable cause for this event.')
rbnIpSecTunnelIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 270))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecTunnelIdentifier.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelIdentifier.setDescription('Key to identify the tunnel alarm, consists of the remote-id type and remote-id, or tunnel name. The string starts with a sub-string identifying the type, followed by the value. ipv4- fqdn- rfc822Addr- ipv6- derAsn1Dn- derAsn1Gn- keyId- name-')
rbnIpSecTunnelName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecTunnelName.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelName.setDescription('Name of the tunnel.')
rbnIpSecTunnelType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("manual", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecTunnelType.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelType.setDescription('Type of tunnel.')
rbnIpSecTunnelDownCause = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("general", 0), ("noRoute", 1), ("aspHomingFailure", 2), ("ppaHomingFailure", 3), ("configuredDown", 4), ("keepaliveFailure", 5), ("downByPeer", 6), ("rekeyFailure", 7), ("aspSoftReset", 8), ("indeterminate", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecTunnelDownCause.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelDownCause.setDescription('Additional information to describe the cause for tunnel being down.')
rbnIpSecRemoteIdType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 9, 10, 11))).clone(namedValues=NamedValues(("reserved", 0), ("ipv4", 1), ("fqdn", 2), ("rfcAddr", 3), ("ipv6", 5), ("derAsn1Dn", 9), ("derAsn1Gn", 10), ("keyId", 11)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecRemoteIdType.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRemoteIdType.setDescription('Remote Id Type of rbnIpSecRemoteId ')
rbnIpSecRemoteId = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecRemoteId.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRemoteId.setDescription('Remote Id.')
rbnIpSecLocalAddrContextName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecLocalAddrContextName.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecLocalAddrContextName.setDescription('Context name of the local address .')
rbnIpSecLocalAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 12), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecLocalAddressType.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecLocalAddressType.setDescription('Specifies the type of local address to be used.')
rbnIpSecLocalAddress = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 13), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecLocalAddress.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecLocalAddress.setDescription('Local IP address of the tunnel.')
rbnIpSecRemoteAddressType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 14), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecRemoteAddressType.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRemoteAddressType.setDescription('Specifies the type of remote address to be used.')
rbnIpSecRemoteAddress = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 15), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecRemoteAddress.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRemoteAddress.setDescription('Remote IP address of the tunnel.')
rbnIpSecTunnelState = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecTunnelState.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelState.setDescription('Tunnel State.')
rbnIpSecSelfCertificateIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 17), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 522))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecSelfCertificateIdentifier.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecSelfCertificateIdentifier.setDescription('<Subject Name> :ISSUER- <Issuer Name>')
rbnIpSecCertificateHandle = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 18), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecCertificateHandle.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecCertificateHandle.setDescription('Self Certificate Handle.')
rbnIpSecExpiryDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 19), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecExpiryDateAndTime.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecExpiryDateAndTime.setDescription('Date and Time the certificate will expire.')
rbnIpSecCertificateSubjectName = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 55, 1, 1, 20), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnIpSecCertificateSubjectName.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecCertificateSubjectName.setDescription('Subject Name of the self certificate')
rbnIpSecTunnelStatusChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 1)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelIdentifier"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelDownCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteIdType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteId"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddrContextName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddressType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddress"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddressType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddress"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelState"))
if mibBuilder.loadTexts: rbnIpSecTunnelStatusChangeAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecTunnelStatusChangeAlarm.setDescription("This notification signifies a change in the IpSecTunnelState. When IPSecTunnelState has the value 'down', rbnIpSecEventSeverity has the value 'major'. When IPSecTunnelState has the value 'up' or is obsoleted due to configuration change rbnIpSecEventSeverity has the value 'clear'")
rbnIpSecNoValidRSASelfCertificateAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 2)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"))
if mibBuilder.loadTexts: rbnIpSecNoValidRSASelfCertificateAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecNoValidRSASelfCertificateAlarm.setDescription('This alarm is set, when there is no valid RSA self-certificate for a context. It.s cleared when a valid self-certificate is configured or when system time is change to make the existing certificate valid. As long as any valid RSA self-certificate exists from any CA, this alarm will not be set. This alarm is set at .Major. severity.')
rbnIpSecNoValidRSATrustedCertificateAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 3)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"))
if mibBuilder.loadTexts: rbnIpSecNoValidRSATrustedCertificateAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecNoValidRSATrustedCertificateAlarm.setDescription('This alarm is raised, when there is no valid RSA trusted-certificate for a context. It.s cleared, when a valid trusted-certificate is configured or when system time is change to make the existing certificate valid. As long as any valid RSA trusted-certificate exists for any CA, this alarm will not be raised. This alarm is set at .Major. severity.')
rbnIpSecRSASelfCertificateNearingExpiryAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 4)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecSelfCertificateIdentifier"), ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"), ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
if mibBuilder.loadTexts: rbnIpSecRSASelfCertificateNearingExpiryAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRSASelfCertificateNearingExpiryAlarm.setDescription(' This alarm notifies the operator that the RSA self certificate expiration is near. It will be raised at the user specified time before the expiration. It will be cleared when a new certificate with the self subject name is added, the certificate is deleted, or the system time pulled up. This alarm is set at .Warning. severity.')
rbnIpSecRSATrustedCertificateNearingExpiryAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 55, 0, 5)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateSubjectName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"), ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
if mibBuilder.loadTexts: rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setDescription(' This alarm notifies the operator that the RSA self certificate expiration is near. It will be raised at the user specified time before the expiration. It will be cleared when a new certificate with the self subject name is added, the certificate is deleted, or the system time is pulled up. This alarm is set at .Warning. severity.')
rbnIpSecCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 1))
rbnIpSecGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2))
rbnIpSecCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 1, 1)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecNotifyObjectGroup"), ("RBN-IP-SECURITY-MIB", "rbnIpSecNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpSecCompliance = rbnIpSecCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecCompliance.setDescription('The compliance statement for SNMP entities which implement the IPSEC MIB.')
rbnIpSecNotifyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2, 1)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecEventDateAndTime"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventSeverity"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecEventProbableCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelIdentifier"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelDownCause"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteIdType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteId"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddrContextName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddressType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecLocalAddress"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddressType"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRemoteAddress"), ("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelState"), ("RBN-IP-SECURITY-MIB", "rbnIpSecSelfCertificateIdentifier"), ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateSubjectName"), ("RBN-IP-SECURITY-MIB", "rbnIpSecCertificateHandle"), ("RBN-IP-SECURITY-MIB", "rbnIpSecExpiryDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpSecNotifyObjectGroup = rbnIpSecNotifyObjectGroup.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecNotifyObjectGroup.setDescription('The collection of objects related to IPSEC notifications.')
rbnIpSecNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 55, 2, 2, 2)).setObjects(("RBN-IP-SECURITY-MIB", "rbnIpSecTunnelStatusChangeAlarm"), ("RBN-IP-SECURITY-MIB", "rbnIpSecNoValidRSASelfCertificateAlarm"), ("RBN-IP-SECURITY-MIB", "rbnIpSecNoValidRSATrustedCertificateAlarm"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRSASelfCertificateNearingExpiryAlarm"), ("RBN-IP-SECURITY-MIB", "rbnIpSecRSATrustedCertificateNearingExpiryAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpSecNotifyGroup = rbnIpSecNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: rbnIpSecNotifyGroup.setDescription('Notification for tracking IPSEC events.')
mibBuilder.exportSymbols("RBN-IP-SECURITY-MIB", rbnIpSecObjects=rbnIpSecObjects, rbnIpSecurityMib=rbnIpSecurityMib, rbnIpSecRemoteIdType=rbnIpSecRemoteIdType, rbnIpSecEventProbableCause=rbnIpSecEventProbableCause, rbnIpSecLocalAddressType=rbnIpSecLocalAddressType, rbnIpSecTunnelName=rbnIpSecTunnelName, rbnIpSecNoValidRSASelfCertificateAlarm=rbnIpSecNoValidRSASelfCertificateAlarm, rbnIpSecRSATrustedCertificateNearingExpiryAlarm=rbnIpSecRSATrustedCertificateNearingExpiryAlarm, rbnIpSecLocalAddress=rbnIpSecLocalAddress, rbnIpSecConformance=rbnIpSecConformance, rbnIpSecNoValidRSATrustedCertificateAlarm=rbnIpSecNoValidRSATrustedCertificateAlarm, rbnIpSecGroups=rbnIpSecGroups, rbnIpSecNotifyGroup=rbnIpSecNotifyGroup, rbnIpSecTunnelStatusChangeAlarm=rbnIpSecTunnelStatusChangeAlarm, rbnIpSecExpiryDateAndTime=rbnIpSecExpiryDateAndTime, rbnIpSecTunnelIdentifier=rbnIpSecTunnelIdentifier, PYSNMP_MODULE_ID=rbnIpSecurityMib, rbnIpSecTunnelDownCause=rbnIpSecTunnelDownCause, rbnIpSecEventDateAndTime=rbnIpSecEventDateAndTime, rbnIpSecCompliances=rbnIpSecCompliances, rbnIpSecNotify=rbnIpSecNotify, rbnIpSecEventType=rbnIpSecEventType, rbnIpSecCertificateSubjectName=rbnIpSecCertificateSubjectName, rbnIpSecTunnelState=rbnIpSecTunnelState, rbnIpSecCertificateHandle=rbnIpSecCertificateHandle, rbnIpSecRemoteAddressType=rbnIpSecRemoteAddressType, rbnIpSecRemoteAddress=rbnIpSecRemoteAddress, rbnIpSecRSASelfCertificateNearingExpiryAlarm=rbnIpSecRSASelfCertificateNearingExpiryAlarm, rbnIpSecTunnelType=rbnIpSecTunnelType, rbnIpSecSelfCertificateIdentifier=rbnIpSecSelfCertificateIdentifier, rbnIpSecCompliance=rbnIpSecCompliance, rbnIpSecLocalAddrContextName=rbnIpSecLocalAddrContextName, rbnIpSecEventSeverity=rbnIpSecEventSeverity, rbnIpSecNotifications=rbnIpSecNotifications, rbnIpSecNotifyObjectGroup=rbnIpSecNotifyObjectGroup, rbnIpSecRemoteId=rbnIpSecRemoteId)
