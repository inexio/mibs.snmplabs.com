#
# PySNMP MIB module COPS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COPS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Gauge32, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, NotificationType, mib_2, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "NotificationType", "mib-2", "Counter64", "ObjectIdentity")
DisplayString, TimeStamp, TextualConvention, RowStatus, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention", "RowStatus", "TimeInterval")
copsClientMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 89))
copsClientMIB.setRevisions(('2000-09-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: copsClientMIB.setRevisionsDescriptions(('This version published as RFC 2940',))
if mibBuilder.loadTexts: copsClientMIB.setLastUpdated('200009280000Z')
if mibBuilder.loadTexts: copsClientMIB.setOrganization('IETF RSVP Admission Policy Working Group')
if mibBuilder.loadTexts: copsClientMIB.setContactInfo(' Andrew Smith (WG co-chair) Phone: +1 408 579 2821 Email: ah_smith@pacbell.net Mark Stevens (WG co-chair) Phone: +1 978 287 9102 Email: markstevens@lucent.com Editor: Andrew Smith Phone: +1 408 579 2821 Email: ah_smith@pacbell.net Editor: David Partain Phone: +46 13 28 41 44 Email: David.Partain@ericsson.com Editor: John Seligson Phone: +1 408 495 2992 Email: jseligso@nortelnetworks.com')
if mibBuilder.loadTexts: copsClientMIB.setDescription('The COPS Client MIB module')
copsClientMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1))
class CopsClientState(TextualConvention, Integer32):
    description = 'A value indicating the state of a COPS client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("copsClientInvalid", 1), ("copsClientTcpconnected", 2), ("copsClientAuthenticating", 3), ("copsClientSecAccepted", 4), ("copsClientAccepted", 5), ("copsClientTimingout", 6))

class CopsServerEntryType(TextualConvention, Integer32):
    description = 'A value indicating how a COPS server entry came into existence.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("copsServerStatic", 1), ("copsServerRedirect", 2))

class CopsErrorCode(TextualConvention, Integer32):
    description = 'A value describing a COPS protocol error. Codes are identical to those used by the COPS protocol itself.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("errorOther", 0), ("errorBadHandle", 1), ("errorInvalidHandleReference", 2), ("errorBadMessageFormat", 3), ("errorUnableToProcess", 4), ("errorMandatoryClientSiMissing", 5), ("errorUnsupportedClientType", 6), ("errorMandatoryCopsObjectMissing", 7), ("errorClientFailure", 8), ("errorCommunicationFailure", 9), ("errorUnspecified", 10), ("errorShuttingDown", 11), ("errorRedirectToPreferredServer", 12), ("errorUnknownCopsObject", 13), ("errorAuthenticationFailure", 14), ("errorAuthenticationMissing", 15))

class CopsTcpPort(TextualConvention, Integer32):
    description = 'A value indicating a TCP protocol port number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CopsAuthType(TextualConvention, Integer32):
    description = 'A value indicating a type of security authentication mechanism.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("authNone", 0), ("authOther", 1), ("authIpSecAh", 2), ("authIpSecEsp", 3), ("authTls", 4), ("authCopsIntegrity", 5))

copsClientCapabilitiesGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 1))
copsClientCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 1, 1), Bits().clone(namedValues=NamedValues(("copsClientVersion1", 0), ("copsClientAuthIpSecAh", 1), ("copsClientAuthIpSecEsp", 2), ("copsClientAuthTls", 3), ("copsClientAuthInteg", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientCapabilities.setStatus('current')
if mibBuilder.loadTexts: copsClientCapabilities.setDescription('A list of the optional capabilities that this COPS client supports.')
copsClientStatusGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 2))
copsClientServerCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 2, 1), )
if mibBuilder.loadTexts: copsClientServerCurrentTable.setStatus('current')
if mibBuilder.loadTexts: copsClientServerCurrentTable.setDescription('A table of information regarding COPS servers as seen from the point of view of a COPS client. This table contains entries for both statically-configured and dynamically-learned servers (from a PDP Redirect operation). One entry exists in this table for each COPS Client-Type served by the COPS server. In addition, an entry will exist with copsClientServerClientType 0 (zero) representing information about the underlying connection itself: this is consistent with the COPS specification which reserves this value for this purpose.')
copsClientServerCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1), ).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerAddressType"), (0, "COPS-CLIENT-MIB", "copsClientServerAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerClientType"))
if mibBuilder.loadTexts: copsClientServerCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: copsClientServerCurrentEntry.setDescription('A set of information regarding a single COPS server serving a single COPS Client-Type from the point of view of a COPS client.')
copsClientServerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: copsClientServerAddressType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerAddressType.setDescription('The type of address in copsClientServerAddress.')
copsClientServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: copsClientServerAddress.setReference('RFC 2748 section 2.3')
if mibBuilder.loadTexts: copsClientServerAddress.setStatus('current')
if mibBuilder.loadTexts: copsClientServerAddress.setDescription('The IPv4, IPv6 or DNS address of a COPS Server. Note that, since this is an index to the table, the DNS name must be short enough to fit into the maximum length of indices allowed by the management protocol in use.')
copsClientServerClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: copsClientServerClientType.setReference('RFC 2748 section 6, IANA')
if mibBuilder.loadTexts: copsClientServerClientType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerClientType.setDescription('The COPS protocol Client-Type for which this entry applies. Multiple Client-Types can be served by a single COPS server. The value 0 (zero) indicates that this entry contains information about the underlying connection itself.')
copsClientServerTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 4), CopsTcpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerTcpPort.setStatus('current')
if mibBuilder.loadTexts: copsClientServerTcpPort.setDescription('The TCP port number on the COPS server to which the client should connect/is connected.')
copsClientServerType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 5), CopsServerEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerType.setDescription('Indicator of the source of this COPS server information. COPS servers may be configured by network management into copsClientServerConfigTable and appear in this entry with type copsServerStatic(1). Alternatively, the may be notified from another COPS server by means of the COPS PDP-Redirect mechanism and appear as copsServerRedirect(2).')
copsClientServerAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 6), CopsAuthType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerAuthType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerAuthType.setDescription('Indicator of the current security mode in use between client and this COPS server.')
copsClientServerLastConnAttempt = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerLastConnAttempt.setStatus('current')
if mibBuilder.loadTexts: copsClientServerLastConnAttempt.setDescription('Timestamp of the last time that this client attempted to connect to this COPS server.')
copsClientState = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 8), CopsClientState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientState.setStatus('current')
if mibBuilder.loadTexts: copsClientState.setDescription('The state of the connection and COPS protocol with respect to this COPS server.')
copsClientServerKeepaliveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 9), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerKeepaliveTime.setReference('RFC 2748 section 3.7, 4.4')
if mibBuilder.loadTexts: copsClientServerKeepaliveTime.setStatus('current')
if mibBuilder.loadTexts: copsClientServerKeepaliveTime.setDescription('The value of the COPS protocol Keepalive timeout, in centiseconds, currently in use by this client, as specified by this COPS server in the Client-Accept operation. A value of zero indicates no keepalive activity is expected.')
copsClientServerAccountingTime = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 10), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientServerAccountingTime.setReference('RFC 2748 section 3.7')
if mibBuilder.loadTexts: copsClientServerAccountingTime.setStatus('current')
if mibBuilder.loadTexts: copsClientServerAccountingTime.setDescription('The value of the COPS protocol Accounting timeout, in centiseconds, currently in use by this client, as specified by the COPS server in the Client-Accept operation. A value of zero indicates no accounting activity is to be performed.')
copsClientInPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientInPkts.setStatus('current')
if mibBuilder.loadTexts: copsClientInPkts.setDescription('A count of the total number of COPS messages that this client has received from this COPS server marked for this Client-Type. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientOutPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOutPkts.setStatus('current')
if mibBuilder.loadTexts: copsClientOutPkts.setDescription('A count of the total number of COPS messages that this client has sent to this COPS server marked for this Client-Type. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientInErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientInErrs.setStatus('current')
if mibBuilder.loadTexts: copsClientInErrs.setDescription('A count of the total number of COPS messages that this client has received from this COPS server marked for this Client-Type that contained errors in syntax. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 14), CopsErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientLastError.setReference('RFC 2748 section 2.2.8')
if mibBuilder.loadTexts: copsClientLastError.setStatus('current')
if mibBuilder.loadTexts: copsClientLastError.setDescription('The code contained in the last COPS protocol Error Object received by this client from this COPS server marked for this Client-Type. This value is not zeroed on COPS Client-Open operations.')
copsClientTcpConnectAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientTcpConnectAttempts.setStatus('current')
if mibBuilder.loadTexts: copsClientTcpConnectAttempts.setDescription('A count of the number of times that this COPS client has tried (successfully or otherwise) to open an TCP connection to a COPS server. This value is cumulative since agent restart and is not zeroed on new connections. This value is not incremented for entries representing a non-zero Client-Type.')
copsClientTcpConnectFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientTcpConnectFailures.setStatus('current')
if mibBuilder.loadTexts: copsClientTcpConnectFailures.setDescription('A count of the number of times that this COPS client has failed to open an TCP connection to a COPS server. This value is cumulative since agent restart and is not zeroed on new connections. This value is not incremented for entries representing a non-zero Client-Type.')
copsClientOpenAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOpenAttempts.setStatus('current')
if mibBuilder.loadTexts: copsClientOpenAttempts.setDescription('A count of the number of times that this COPS client has tried to perform a COPS Client-Open to a COPS server for this Client-Type. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientOpenFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientOpenFailures.setStatus('current')
if mibBuilder.loadTexts: copsClientOpenFailures.setDescription('A count of the number of times that this COPS client has failed to perform a COPS Client-Open to a COPS server for this Client-Type. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrUnsupportClienttype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnsupportClienttype.setStatus('current')
if mibBuilder.loadTexts: copsClientErrUnsupportClienttype.setDescription('A count of the total number of COPS messages that this client has received from COPS servers that referred to Client-Types that are unsupported by this client. This value is cumulative since agent restart and is not zeroed on new connections. This value is not incremented for entries representing a non-zero Client-Type.')
copsClientErrUnsupportedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnsupportedVersion.setStatus('current')
if mibBuilder.loadTexts: copsClientErrUnsupportedVersion.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that had a COPS protocol Version number that is unsupported by this client. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrLengthMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrLengthMismatch.setStatus('current')
if mibBuilder.loadTexts: copsClientErrLengthMismatch.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that had a COPS protocol Message Length that did not match the actual received message. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrUnknownOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnknownOpcode.setStatus('current')
if mibBuilder.loadTexts: copsClientErrUnknownOpcode.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that had a COPS protocol Op Code that was unrecognised by this client. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrUnknownCnum = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrUnknownCnum.setStatus('current')
if mibBuilder.loadTexts: copsClientErrUnknownCnum.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that contained a COPS protocol object C-Num that was unrecognised by this client. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrBadCtype = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrBadCtype.setStatus('current')
if mibBuilder.loadTexts: copsClientErrBadCtype.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that contained a COPS protocol object C-Type that was not defined for the C-Nums known by this client. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrBadSends = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrBadSends.setStatus('current')
if mibBuilder.loadTexts: copsClientErrBadSends.setDescription('A count of the total number of COPS messages that this client attempted to send to COPS servers marked for this Client-Type that resulted in a transmit error. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrWrongObjects = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrWrongObjects.setStatus('current')
if mibBuilder.loadTexts: copsClientErrWrongObjects.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that did not contain a permitted set of COPS protocol objects. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrWrongOpcode = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrWrongOpcode.setStatus('current')
if mibBuilder.loadTexts: copsClientErrWrongOpcode.setDescription('A count of the total number of COPS messages that this client has received from COPS servers marked for this Client-Type that had a COPS protocol Op Code that should not have been sent to a COPS client e.g. Open-Requests. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientKaTimedoutClients = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientKaTimedoutClients.setStatus('current')
if mibBuilder.loadTexts: copsClientKaTimedoutClients.setDescription('A count of the total number of times that this client has been shut down for this Client-Type by COPS servers that had detected a COPS protocol Keepalive timeout. This value is cumulative since agent restart and is not zeroed on new connections.')
copsClientErrAuthFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrAuthFailures.setStatus('current')
if mibBuilder.loadTexts: copsClientErrAuthFailures.setDescription('A count of the total number of times that this client has received a COPS message marked for this Client-Type which could not be authenticated using the authentication mechanism used by this client.')
copsClientErrAuthMissing = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 2, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: copsClientErrAuthMissing.setStatus('current')
if mibBuilder.loadTexts: copsClientErrAuthMissing.setDescription('A count of the total number of times that this client has received a COPS message marked for this Client-Type which did not contain authentication information.')
copsClientConfigGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 1, 3))
copsClientServerConfigTable = MibTable((1, 3, 6, 1, 2, 1, 89, 1, 3, 1), )
if mibBuilder.loadTexts: copsClientServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigTable.setDescription('Table of possible COPS servers to try to connect to in order of copsClientServerConfigPriority. There may be multiple entries in this table for the same server and client-type which specify different security mechanisms: these mechanisms will be attempted by the client in the priority order given. Note that a server learned by means of PDPRedirect always takes priority over any of these configured entries.')
copsClientServerConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1), ).setIndexNames((0, "COPS-CLIENT-MIB", "copsClientServerConfigAddrType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAddress"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigClientType"), (0, "COPS-CLIENT-MIB", "copsClientServerConfigAuthType"))
if mibBuilder.loadTexts: copsClientServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigEntry.setDescription('A set of configuration information regarding a single COPS server from the point of view of a COPS client.')
copsClientServerConfigAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: copsClientServerConfigAddrType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigAddrType.setDescription('The type of address in copsClientServerConfigAddress.')
copsClientServerConfigAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: copsClientServerConfigAddress.setReference('RFC 2748 section 2.3')
if mibBuilder.loadTexts: copsClientServerConfigAddress.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigAddress.setDescription('The IPv4, IPv6 or DNS address of a COPS Server. Note that, since this is an index to the table, the DNS name must be short enough to fit into the maximum length of indices allowed by the management protocol in use.')
copsClientServerConfigClientType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: copsClientServerConfigClientType.setReference('RFC 2748 section 6, IANA')
if mibBuilder.loadTexts: copsClientServerConfigClientType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigClientType.setDescription('The COPS protocol Client-Type for which this entry applies and for which this COPS server is capable of serving. Multiple Client-Types can be served by a single COPS server.')
copsClientServerConfigAuthType = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 4), CopsAuthType())
if mibBuilder.loadTexts: copsClientServerConfigAuthType.setReference('RFC 2748 section 4.')
if mibBuilder.loadTexts: copsClientServerConfigAuthType.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigAuthType.setDescription('The type of authentication mechanism for this COPS client to request when negotiating security at the start of a connection to a COPS server.')
copsClientServerConfigTcpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 5), CopsTcpPort()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigTcpPort.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigTcpPort.setDescription('The TCP port number on the COPS server to which the client should connect.')
copsClientServerConfigPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigPriority.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigPriority.setDescription('The priority of this entry relative to other entries. COPS client will attempt to contact COPS servers for the appropriate Client-Type. Higher numbers are tried first. The order to be used amongst server entries with the same priority is undefined. COPS servers that are notified to the client using the COPS protocol PDP-Redirect mechanism are always used in preference to any entries in this table.')
copsClientServerConfigRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 89, 1, 3, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: copsClientServerConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigRowStatus.setDescription('State of this entry in the table.')
copsClientServerConfigRetryAlgrm = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("sequential", 2), ("roundRobin", 3))).clone('sequential')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: copsClientServerConfigRetryAlgrm.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigRetryAlgrm.setDescription('The algorithm by which the client should retry when it fails to connect to a COPS server.')
copsClientServerConfigRetryCount = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 3), Unsigned32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: copsClientServerConfigRetryCount.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigRetryCount.setDescription("A retry count for use by the retry algorithm. Each retry algorithm needs to specify how it uses this value. For the 'sequential(2)' algorithm, this value is the number of times the client should retry to connect to one COPS server before moving on to another. For the 'roundRobin(3)' algorithm, this value is not used.")
copsClientServerConfigRetryIntvl = MibScalar((1, 3, 6, 1, 2, 1, 89, 1, 3, 4), TimeInterval().clone(1000)).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: copsClientServerConfigRetryIntvl.setStatus('current')
if mibBuilder.loadTexts: copsClientServerConfigRetryIntvl.setDescription("A retry interval for use by the retry algorithm. Each retry algorithm needs to specify how it uses this value. For the 'sequential(2)' algorithm, this value is the time to wait between retries of a connection to the same COPS server. For the 'roundRobin(3)' algorithm, the client always attempts to connect to each Server in turn, until one succeeds or they all fail; if they all fail, then the client waits for the value of this interval before restarting the algorithm.")
copsClientConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2))
copsClientGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 1))
copsClientCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 89, 2, 2))
copsDeviceStatusGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 1)).setObjects(("COPS-CLIENT-MIB", "copsClientCapabilities"), ("COPS-CLIENT-MIB", "copsClientServerTcpPort"), ("COPS-CLIENT-MIB", "copsClientServerType"), ("COPS-CLIENT-MIB", "copsClientServerAuthType"), ("COPS-CLIENT-MIB", "copsClientServerLastConnAttempt"), ("COPS-CLIENT-MIB", "copsClientState"), ("COPS-CLIENT-MIB", "copsClientServerKeepaliveTime"), ("COPS-CLIENT-MIB", "copsClientServerAccountingTime"), ("COPS-CLIENT-MIB", "copsClientInPkts"), ("COPS-CLIENT-MIB", "copsClientOutPkts"), ("COPS-CLIENT-MIB", "copsClientInErrs"), ("COPS-CLIENT-MIB", "copsClientLastError"), ("COPS-CLIENT-MIB", "copsClientTcpConnectAttempts"), ("COPS-CLIENT-MIB", "copsClientTcpConnectFailures"), ("COPS-CLIENT-MIB", "copsClientOpenAttempts"), ("COPS-CLIENT-MIB", "copsClientOpenFailures"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportClienttype"), ("COPS-CLIENT-MIB", "copsClientErrUnsupportedVersion"), ("COPS-CLIENT-MIB", "copsClientErrLengthMismatch"), ("COPS-CLIENT-MIB", "copsClientErrUnknownOpcode"), ("COPS-CLIENT-MIB", "copsClientErrUnknownCnum"), ("COPS-CLIENT-MIB", "copsClientErrBadCtype"), ("COPS-CLIENT-MIB", "copsClientErrBadSends"), ("COPS-CLIENT-MIB", "copsClientErrWrongObjects"), ("COPS-CLIENT-MIB", "copsClientErrWrongOpcode"), ("COPS-CLIENT-MIB", "copsClientKaTimedoutClients"), ("COPS-CLIENT-MIB", "copsClientErrAuthFailures"), ("COPS-CLIENT-MIB", "copsClientErrAuthMissing"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    copsDeviceStatusGroup = copsDeviceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: copsDeviceStatusGroup.setDescription('A collection of objects for monitoring the status of connections to COPS servers and statistics for a COPS client.')
copsDeviceConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 89, 2, 1, 2)).setObjects(("COPS-CLIENT-MIB", "copsClientServerConfigTcpPort"), ("COPS-CLIENT-MIB", "copsClientServerConfigPriority"), ("COPS-CLIENT-MIB", "copsClientServerConfigRowStatus"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryAlgrm"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryCount"), ("COPS-CLIENT-MIB", "copsClientServerConfigRetryIntvl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    copsDeviceConfigGroup = copsDeviceConfigGroup.setStatus('current')
if mibBuilder.loadTexts: copsDeviceConfigGroup.setDescription('A collection of objects for configuring COPS server information.')
copsClientCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 89, 2, 2, 1)).setObjects(("COPS-CLIENT-MIB", "copsDeviceStatusGroup"), ("COPS-CLIENT-MIB", "copsDeviceConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    copsClientCompliance = copsClientCompliance.setStatus('current')
if mibBuilder.loadTexts: copsClientCompliance.setDescription('The compliance statement for device support of management of the COPS client.')
mibBuilder.exportSymbols("COPS-CLIENT-MIB", copsClientServerConfigRowStatus=copsClientServerConfigRowStatus, copsClientServerConfigTable=copsClientServerConfigTable, CopsClientState=CopsClientState, copsClientOpenAttempts=copsClientOpenAttempts, copsClientServerConfigClientType=copsClientServerConfigClientType, copsClientServerConfigAddress=copsClientServerConfigAddress, copsClientInPkts=copsClientInPkts, copsClientServerAccountingTime=copsClientServerAccountingTime, copsClientErrAuthMissing=copsClientErrAuthMissing, copsClientGroups=copsClientGroups, copsClientCompliances=copsClientCompliances, copsClientStatusGroup=copsClientStatusGroup, copsClientServerCurrentTable=copsClientServerCurrentTable, copsClientErrUnsupportClienttype=copsClientErrUnsupportClienttype, copsClientServerConfigAddrType=copsClientServerConfigAddrType, PYSNMP_MODULE_ID=copsClientMIB, copsClientErrLengthMismatch=copsClientErrLengthMismatch, copsClientServerType=copsClientServerType, copsClientKaTimedoutClients=copsClientKaTimedoutClients, copsClientMIB=copsClientMIB, copsClientCapabilitiesGroup=copsClientCapabilitiesGroup, copsClientServerKeepaliveTime=copsClientServerKeepaliveTime, CopsAuthType=CopsAuthType, copsClientCompliance=copsClientCompliance, CopsTcpPort=CopsTcpPort, copsClientServerConfigPriority=copsClientServerConfigPriority, copsDeviceStatusGroup=copsDeviceStatusGroup, CopsServerEntryType=CopsServerEntryType, copsClientLastError=copsClientLastError, copsClientServerConfigAuthType=copsClientServerConfigAuthType, copsClientErrWrongObjects=copsClientErrWrongObjects, copsClientServerLastConnAttempt=copsClientServerLastConnAttempt, copsClientMIBObjects=copsClientMIBObjects, copsClientState=copsClientState, copsClientConformance=copsClientConformance, copsClientServerTcpPort=copsClientServerTcpPort, copsClientServerAddressType=copsClientServerAddressType, copsClientErrBadCtype=copsClientErrBadCtype, copsClientServerConfigRetryIntvl=copsClientServerConfigRetryIntvl, copsClientTcpConnectAttempts=copsClientTcpConnectAttempts, copsClientErrUnknownCnum=copsClientErrUnknownCnum, copsClientServerAddress=copsClientServerAddress, copsClientCapabilities=copsClientCapabilities, copsClientServerConfigEntry=copsClientServerConfigEntry, copsClientTcpConnectFailures=copsClientTcpConnectFailures, copsClientServerConfigTcpPort=copsClientServerConfigTcpPort, copsClientServerClientType=copsClientServerClientType, CopsErrorCode=CopsErrorCode, copsClientConfigGroup=copsClientConfigGroup, copsClientServerCurrentEntry=copsClientServerCurrentEntry, copsClientServerConfigRetryCount=copsClientServerConfigRetryCount, copsClientServerAuthType=copsClientServerAuthType, copsClientErrWrongOpcode=copsClientErrWrongOpcode, copsClientErrAuthFailures=copsClientErrAuthFailures, copsDeviceConfigGroup=copsDeviceConfigGroup, copsClientOpenFailures=copsClientOpenFailures, copsClientServerConfigRetryAlgrm=copsClientServerConfigRetryAlgrm, copsClientInErrs=copsClientInErrs, copsClientErrBadSends=copsClientErrBadSends, copsClientOutPkts=copsClientOutPkts, copsClientErrUnknownOpcode=copsClientErrUnknownOpcode, copsClientErrUnsupportedVersion=copsClientErrUnsupportedVersion)
