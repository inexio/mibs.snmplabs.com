#
# PySNMP MIB module CISCO-NS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, FcAddressId, FcClassOfServices, FcNameIdOrZero = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId", "FcAddressId", "FcClassOfServices", "FcNameIdOrZero")
vsanIndex, notifyVsanIndex = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex", "notifyVsanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Bits, ObjectIdentity, Integer32, IpAddress, Unsigned32, NotificationType, Counter64, Gauge32, iso, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Bits", "ObjectIdentity", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "Counter64", "Gauge32", "iso", "TimeTicks", "ModuleIdentity")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
ciscoNsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 293))
ciscoNsMIB.setRevisions(('2004-08-30 00:00', '2004-02-19 00:00', '2003-03-06 00:00', '2002-10-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNsMIB.setRevisionsDescriptions(('Added fcNameServerPermanentPortName object to fcNameServerTable.', 'Added notifications fcNameServerEntryAdd, fcNameServerEntryDelete.', 'Added fcNameServerPortFunction object.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoNsMIB.setLastUpdated('200408300000Z')
if mibBuilder.loadTexts: ciscoNsMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoNsMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoNsMIB.setDescription('The MIB module for the management of the Cisco Name Server which realizes the FC-GS3 requirements for Name Server (NS).')
ciscoNameServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1))
fcNameServerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 2))
fcNameServerConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1))
fcNameServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2))
fcNameServerInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3))
fcNameServerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4))
fcNameServerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0))
class FcGs3RejectReasonCode(TextualConvention, Integer32):
    description = 'The GS-3 reject reason code for a request. none(1) - no error. invalidCmdCode(2) - req contains an invalid command code. invalidVerLevel(3) - req contains an invalid version number. logicalError(4) - there is a logical error. invalidIUSize(5) - Information Unit (IU) size is invalid. logicalBusy(6) - the module is busy. protocolError(7) - there is a protocol error. unableToPerformCmdReq(8) - the command specified in the req could not be executed. The details of exactly what failed will be in the corresponding reason code explanation. cmdNotSupported(9) - the command is not supported. vendorError(10) - specific vendor error.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("none", 1), ("invalidCmdCode", 2), ("invalidVerLevel", 3), ("logicalError", 4), ("invalidIUSize", 5), ("logicalBusy", 6), ("protocolError", 7), ("unableToPerformCmdReq", 8), ("cmdNotSupported", 9), ("vendorError", 10))

class FcNameServerRejReasonExpl(TextualConvention, Integer32):
    description = 'The reject reason code explanation. noAdditionalExplanation(1) - no additional explanation. portIdentifierNotRegistered(2) - port Id not registered. portNameNotRegistered(3) - port name not registered. nodeNameNotRegistered(4) - node name not registered. classOfServiceNotRegistered(5) - class of service not registered. nodeIpAddressNotRegistered(6) - node IP address not registered. ipaNotRegistered(7) - Initial Process Associator (IPA) not registered. fc4TypeNotRegistered(8) - FC4 type not registered. symbolicPortNameNotRegistered(9) - symbolic port name not registered. symbolicNodeNameNotRegistered(10) - symbolic node name not registered. portTypeNotRegistered(11) - type of port not registered. portIpAddressNotRegistered(12) - port IP address not registered. fabricPortNameNotRegistered(13) - fabric port name not registered. hardAddressNotRegistered(14) - hard address not registered fc4DescriptorNotRegistered(15) - FC4 descriptor not registered. fc4FeaturesNotRegistered(16) - FC4 features not registered. accessDenied(17) - access is denied. unacceptablePortIdentifier(18) - port Id is invalid. databaseEmpty(19) - database is empty. noObjectRegInSpecifiedScope(20) - no object has been registered in the specified scope.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("noAdditionalExplanation", 1), ("portIdentifierNotRegistered", 2), ("portNameNotRegistered", 3), ("nodeNameNotRegistered", 4), ("classOfServiceNotRegistered", 5), ("nodeIpAddressNotRegistered", 6), ("ipaNotRegistered", 7), ("fc4TypeNotRegistered", 8), ("symbolicPortNameNotRegistered", 9), ("symbolicNodeNameNotRegistered", 10), ("portTypeNotRegistered", 11), ("portIpAddressNotRegistered", 12), ("fabricPortNameNotRegistered", 13), ("hardAddressNotRegistered", 14), ("fc4DescriptorNotRegistered", 15), ("fc4FeaturesNotRegistered", 16), ("accessDenied", 17), ("unacceptablePortIdentifier", 18), ("databaseEmpty", 19), ("noObjectRegInSpecifiedScope", 20))

fcNameServerProxyPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1), )
if mibBuilder.loadTexts: fcNameServerProxyPortTable.setStatus('current')
if mibBuilder.loadTexts: fcNameServerProxyPortTable.setDescription('This table contains a list of proxy ports on all configured VSANs on the local switch. Only one proxy port is allowed on a VSAN.')
fcNameServerProxyPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: fcNameServerProxyPortEntry.setStatus('current')
if mibBuilder.loadTexts: fcNameServerProxyPortEntry.setDescription('An entry (conceptual row) in this table.')
fcNameServerProxyPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 1, 1, 1), FcNameIdOrZero().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerProxyPortName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerProxyPortName.setDescription("Name of the proxy port which can register/deregister for other ports on this VSAN. Users can enable third party registrations by setting this object. In order to disable third party registrations, this object should be set to ''H.")
fcNameServerTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerTableLastChange.setStatus('current')
if mibBuilder.loadTexts: fcNameServerTableLastChange.setDescription('The value of sysUpTime at the time of the last update to the fcNameServerTable. This includes creation of an entry, deletion of an entry and modification of an existing entry. If no updates have taken place since the last re-initialization of the local network management subsystem, then this object contains a zero value.')
fcNameServerNumRows = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerNumRows.setStatus('current')
if mibBuilder.loadTexts: fcNameServerNumRows.setDescription('The number of Nx_Ports currently registered with this device fabric wide.')
fcNameServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4), )
if mibBuilder.loadTexts: fcNameServerTable.setStatus('current')
if mibBuilder.loadTexts: fcNameServerTable.setDescription('This table contains entries for all Nx_Ports registered with Fx_Ports on all the VSANs configured on the local switch.')
fcNameServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"), (0, "CISCO-NS-MIB", "fcNameServerPortIdentifier"))
if mibBuilder.loadTexts: fcNameServerEntry.setStatus('current')
if mibBuilder.loadTexts: fcNameServerEntry.setDescription('An entry (conceptual row) in the fcNameServerTable. This contains information about an Nx_Port represented by fcNameServerPortIdentifier for a particular VSAN identified by vsanIndex.')
fcNameServerPortIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 1), FcAddressId())
if mibBuilder.loadTexts: fcNameServerPortIdentifier.setStatus('current')
if mibBuilder.loadTexts: fcNameServerPortIdentifier.setDescription('The Fibre Channel Identifier (FC-ID) of this Nx_Port.')
fcNameServerPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 2), FcNameId().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerPortName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerPortName.setDescription("The fibre channel Port_Name (WWN) of this Nx_port. If this object is not set, then it will contain the null value '0000000000000000'h.")
fcNameServerNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 3), FcNameId().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerNodeName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerNodeName.setDescription("The fibre channel Node_Name (WWN) of this Nx_port. If this object is not set, then it will contain the null value '0000000000000000'h.")
fcNameServerClassOfSvc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 4), FcClassOfServices()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerClassOfSvc.setStatus('current')
if mibBuilder.loadTexts: fcNameServerClassOfSvc.setDescription('The class of service indicator. This object is a array of bits that contain a bit map of the classes of service supported by the associated port. If a bit in this object is 1, it indicates that the class of service is supported by the associated port. When a bit is set to 0, it indicates that no class of service is supported by this Nx_port.')
fcNameServerNodeIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerNodeIpAddress.setReference('ANSI NCITS xxx-200x, Fibre Channel - Generic Services-3 (FC-GS-3), T11/Project 1356D/Rev 7.01 Section 5.1.4.40 and Section 5.1.2.5')
if mibBuilder.loadTexts: fcNameServerNodeIpAddress.setStatus('current')
if mibBuilder.loadTexts: fcNameServerNodeIpAddress.setDescription("The IP address of the node of this Nx_port, as indicated by the Nx_Port in a GS3 message that it transmitted. The GS3 format specifies a 32-bit IPv4 address or a 128-bit IPv6 address. For the former, the leftmost 96 bits (12 bytes) are set to x'00 00 00 00 00 00 00 00 00 00 FF FF' and the rightmost 32 bits are supposed to contain the IPv4 address.")
fcNameServerProcAssoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerProcAssoc.setStatus('current')
if mibBuilder.loadTexts: fcNameServerProcAssoc.setDescription('The Fibre Channel initial process associator (IPA).')
fcNameServerFC4Type = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerFC4Type.setReference('ANSI NCITS xxx-200x, Fibre Channel - Generic Services-3 (FC-GS-3), T11/Project 1356D/Rev 7.01 Section 5.1.2.7.')
if mibBuilder.loadTexts: fcNameServerFC4Type.setStatus('current')
if mibBuilder.loadTexts: fcNameServerFC4Type.setDescription('The FC-4 protocol types supported by this Nx_port. This is an array of 256-bits. Each bit in the array corresponds to a Type value as defined by the fibre channel standards and contained in the Type field of the frame header.')
fcNameServerPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("nPort", 2), ("nlPort", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerPortType.setStatus('current')
if mibBuilder.loadTexts: fcNameServerPortType.setDescription('The port type of this port.')
fcNameServerPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerPortIpAddress.setReference('ANSI NCITS xxx-200x, Fibre Channel - Generic Services-3, (FC-GS-3), T11/Project 1356D/Rev 7.01 Section 5.1.4.36 and Section 5.1.2.5')
if mibBuilder.loadTexts: fcNameServerPortIpAddress.setStatus('current')
if mibBuilder.loadTexts: fcNameServerPortIpAddress.setDescription("This object contains the IP address of the associated port in either 32-bit IPv4 format or 128-bit IPv6 format. When this object contains a IPv4 address, the leftmost 96 bits (12 bytes) should contain x'00 00 00 00 00 00 00 00 00 00 FF FF'. The IPv4 address should be present in the rightmost 32 bits. Note that the value of this object is the IP address value that is received in the GS3 message Register IP address (Port) RIPP_ID. It is not validated against any IP address format.")
fcNameServerFabricPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 10), FcNameId().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerFabricPortName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerFabricPortName.setDescription("The Fabric Port Name (WWN) of the Fx_port to which this Nx_port is attached. If this object is not set, then it will contain the null value '0000000000000000'h.")
fcNameServerHardAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 11), FcAddressId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerHardAddress.setStatus('current')
if mibBuilder.loadTexts: fcNameServerHardAddress.setDescription('The format of this object is identical to the format of Hard Address defined in the Discover Address (ADISC) Extended Link Service (FC-PH-2). Hard Address is the 24-bit NL_Port identifier which consists of - the 8-bit Domain Id in the most significant byte - the 8-bit Area Id in the next most significant byte - the 8-bit AL-PA(Arbitrated Loop Physical Address) which an NL_port attempts acquire during FC-AL initialization in the least significant byte. If the port is not an NL_Port, or if it is an NL_Port but does not have a hard address, then all bits are reported as 0s.')
fcNameServerSymbolicPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerSymbolicPortName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerSymbolicPortName.setDescription('The user-defined name of this port. If this object has not been set, then the value of this object is the zero length string.')
fcNameServerSymbolicNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 13), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerSymbolicNodeName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerSymbolicNodeName.setDescription('The user-defined name of the node of this port. If this object has not been set, then the value of this object is the zero length string.')
fcNameServerFC4Features = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerFC4Features.setReference('ANSI NCITS xxx-200x, Fibre Channel - Generic Services-3 (FC-GS-3), T11/Project 1356D/Rev 7.01 Section 5.1.2.14')
if mibBuilder.loadTexts: fcNameServerFC4Features.setStatus('current')
if mibBuilder.loadTexts: fcNameServerFC4Features.setDescription("The FC-4 Features associated with this port and the FC-4 Type. Refer to FC-GS3 specification for the format of this object. This object is an array of 4-bit values, one for each TYPE code value. The 5 most significant bits of the TYPE field will be used to identify the word for the FC-4 Features object. - Word 0 contains information related to TYPE code '00' thru' '07'; - Word 1 contains information related to TYPE code '08' thru' 0F'; - and so forth to Word 31 that contains information related to TYPE code 'F8' thru' 'FF'. The 3 least significant bits of the TYPE field will be used to identify the position within the word for the 4-bit FC-4 Features value.")
fcNameServerPortFunction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 15), Bits().clone(namedValues=NamedValues(("trapPort", 0), ("vep", 1), ("volOwner", 2), ("ipfcPort", 3), ("intPort", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerPortFunction.setReference('CISCO-VEDM-MIB')
if mibBuilder.loadTexts: fcNameServerPortFunction.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerPortFunction.setDescription('The function of this port. trapPort(0) indicates that this port is functioning as a Trap Port. vep(1) indicates that this port is functioning as a Virtual Enclosure Port (VEP). volOwner(2) indicates that this port is functioning as a Volume Owner. ipfcPort(3) indicates that this port is functioning as a IP-FC port. intPort(4) indicates that this port is functioning as an internal port.')
fcNameServerPermanentPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 4, 1, 16), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerPermanentPortName.setReference('Fibre-Channel - Generic Services - 4 T11/ Project 1505-D/Rev 7.91 Section 5.2.3.16')
if mibBuilder.loadTexts: fcNameServerPermanentPortName.setStatus('current')
if mibBuilder.loadTexts: fcNameServerPermanentPortName.setDescription("The Permanent Port Name of this Nx_port. If multiple Port_Name(s) are associated with this Nx_port via FDISC (Discover F_Port Service Parameters), the Permanent Port Name is the original Port_Name associated with this Nx_port at login. If this object is not set, then it will contain the null value '0000000000000000'h.")
fcNameServerTotalRejects = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerTotalRejects.setStatus('current')
if mibBuilder.loadTexts: fcNameServerTotalRejects.setDescription('The total number of requests rejected by the local switch across all VSANs.')
fcNameServerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2), )
if mibBuilder.loadTexts: fcNameServerStatsTable.setStatus('current')
if mibBuilder.loadTexts: fcNameServerStatsTable.setDescription('This table contains statistic counters which are maintained by the Name Server. These counters are maintained per VSAN.')
fcNameServerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: fcNameServerStatsEntry.setStatus('current')
if mibBuilder.loadTexts: fcNameServerStatsEntry.setDescription('An entry (conceptual row) in this table.')
fcNameServerInGetReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerInGetReqs.setStatus('current')
if mibBuilder.loadTexts: fcNameServerInGetReqs.setDescription('The total number of Get Requests received by the local switch on this VSAN.')
fcNameServerOutGetReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerOutGetReqs.setStatus('current')
if mibBuilder.loadTexts: fcNameServerOutGetReqs.setDescription('The total number of Get Requests sent by the local switch on this VSAN.')
fcNameServerInRegReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerInRegReqs.setStatus('current')
if mibBuilder.loadTexts: fcNameServerInRegReqs.setDescription('The total number of Registration Requests received by the local switch on this VSAN.')
fcNameServerInDeRegReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerInDeRegReqs.setStatus('current')
if mibBuilder.loadTexts: fcNameServerInDeRegReqs.setDescription('The total number of De-registration Requests received by the local switch on this VSAN.')
fcNameServerInRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerInRscns.setStatus('current')
if mibBuilder.loadTexts: fcNameServerInRscns.setDescription('The total number of RSCN commands received by the local switch on this VSAN.')
fcNameServerOutRscns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerOutRscns.setStatus('current')
if mibBuilder.loadTexts: fcNameServerOutRscns.setDescription('The total number of RSCN commands sent by the local switch on this VSAN.')
fcNameServerRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerRejects.setStatus('current')
if mibBuilder.loadTexts: fcNameServerRejects.setDescription('The total number of requests rejected by the local switch on this VSAN.')
fcNameServerRejectReasonCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3, 1), FcGs3RejectReasonCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerRejectReasonCode.setStatus('current')
if mibBuilder.loadTexts: fcNameServerRejectReasonCode.setDescription('The registration reject reason code. This object contains the reason code corresponding to the most recent Name Server Registration request failure.')
fcNameServerRejReasonCodeExp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 3, 2), FcNameServerRejReasonExpl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fcNameServerRejReasonCodeExp.setStatus('current')
if mibBuilder.loadTexts: fcNameServerRejReasonCodeExp.setDescription("The registration reject reason code explanation. This object contains the reason code explanation if the above object has a reason code corresponding to 'Unable to perform command request'. This object like the one above, corresponds to the most recent Name Server Registration request rejection.")
fcNameServerRejReqNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fcNameServerRejReqNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: fcNameServerRejReqNotifyEnable.setDescription("This object specifies if the Name Server should generate 'fcNameServerRejectRegNotify' notifications. If value of this object is 'true', then the notification is generated when a request is rejected. If it is 'false', the notification is not generated.")
fcNameServerRejectRegNotify = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 1)).setObjects(("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerRejectReasonCode"), ("CISCO-NS-MIB", "fcNameServerRejReasonCodeExp"))
if mibBuilder.loadTexts: fcNameServerRejectRegNotify.setStatus('current')
if mibBuilder.loadTexts: fcNameServerRejectRegNotify.setDescription("This notification is generated by the Name Server whenever it rejects a registration request. The Name Server should update the 'fcNameServerRejectReasonCode' and 'fcNameServerRejReasonCodeExp' objects with the corresponding reason code and reason code explanation before sending the notification. These two objects are also included along with the notification to provide the reason for the reject.")
fcNameServerDatabaseFull = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 2)).setObjects(("CISCO-VSAN-MIB", "notifyVsanIndex"))
if mibBuilder.loadTexts: fcNameServerDatabaseFull.setStatus('current')
if mibBuilder.loadTexts: fcNameServerDatabaseFull.setDescription('This notification is generated by the Name Server when the Name Server cannot allocate space for a new entry.')
fcNameServerEntryAdd = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 3)).setObjects(("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerPortType"))
if mibBuilder.loadTexts: fcNameServerEntryAdd.setStatus('current')
if mibBuilder.loadTexts: fcNameServerEntryAdd.setDescription('This notification is generated by the Name Server when a new entry gets added to the Name Server database.')
fcNameServerEntryDelete = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 293, 1, 4, 0, 4)).setObjects(("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerPortType"))
if mibBuilder.loadTexts: fcNameServerEntryDelete.setStatus('current')
if mibBuilder.loadTexts: fcNameServerEntryDelete.setDescription('This notification is generated by the Name Server when an existing entry is deleted from the Name Server database.')
fcNameServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1))
fcNameServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2))
fcNameServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 1)).setObjects(("CISCO-NS-MIB", "fcNameServerDBGroup"), ("CISCO-NS-MIB", "fcNameServerStatsGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyControlGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerMIBCompliance = fcNameServerMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerMIBCompliance.setDescription('The compliance statement for entities which implement the name server.')
fcNameServerMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 2)).setObjects(("CISCO-NS-MIB", "fcNameServerDBGroup1"), ("CISCO-NS-MIB", "fcNameServerStatsGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyControlGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerMIBCompliance1 = fcNameServerMIBCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerMIBCompliance1.setDescription('The compliance statement for entities which implement the name server.')
fcNameServerMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 3)).setObjects(("CISCO-NS-MIB", "fcNameServerDBGroup2"), ("CISCO-NS-MIB", "fcNameServerStatsGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyControlGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerMIBCompliance2 = fcNameServerMIBCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerMIBCompliance2.setDescription('The compliance statement for entities which implement the name server.')
fcNameServerMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 1, 4)).setObjects(("CISCO-NS-MIB", "fcNameServerDBGroup3"), ("CISCO-NS-MIB", "fcNameServerStatsGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyControlGroup"), ("CISCO-NS-MIB", "fcNameServerNotifyGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerMIBCompliance3 = fcNameServerMIBCompliance3.setStatus('current')
if mibBuilder.loadTexts: fcNameServerMIBCompliance3.setDescription('The compliance statement for entities which implement the name server.')
fcNameServerDBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 1)).setObjects(("CISCO-NS-MIB", "fcNameServerProxyPortName"), ("CISCO-NS-MIB", "fcNameServerNumRows"), ("CISCO-NS-MIB", "fcNameServerTableLastChange"), ("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerNodeName"), ("CISCO-NS-MIB", "fcNameServerClassOfSvc"), ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"), ("CISCO-NS-MIB", "fcNameServerProcAssoc"), ("CISCO-NS-MIB", "fcNameServerFC4Type"), ("CISCO-NS-MIB", "fcNameServerPortType"), ("CISCO-NS-MIB", "fcNameServerPortIpAddress"), ("CISCO-NS-MIB", "fcNameServerFabricPortName"), ("CISCO-NS-MIB", "fcNameServerHardAddress"), ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"), ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"), ("CISCO-NS-MIB", "fcNameServerFC4Features"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerDBGroup = fcNameServerDBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerDBGroup.setDescription('A collection of objects for displaying and configuring Name Server objects.')
fcNameServerStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 2)).setObjects(("CISCO-NS-MIB", "fcNameServerTotalRejects"), ("CISCO-NS-MIB", "fcNameServerInGetReqs"), ("CISCO-NS-MIB", "fcNameServerOutGetReqs"), ("CISCO-NS-MIB", "fcNameServerInRegReqs"), ("CISCO-NS-MIB", "fcNameServerInDeRegReqs"), ("CISCO-NS-MIB", "fcNameServerInRscns"), ("CISCO-NS-MIB", "fcNameServerOutRscns"), ("CISCO-NS-MIB", "fcNameServerRejects"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerStatsGroup = fcNameServerStatsGroup.setStatus('current')
if mibBuilder.loadTexts: fcNameServerStatsGroup.setDescription('A collection of objects for displaying Name Server statistics.')
fcNameServerNotifyControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 3)).setObjects(("CISCO-NS-MIB", "fcNameServerRejectReasonCode"), ("CISCO-NS-MIB", "fcNameServerRejReasonCodeExp"), ("CISCO-NS-MIB", "fcNameServerRejReqNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerNotifyControlGroup = fcNameServerNotifyControlGroup.setStatus('current')
if mibBuilder.loadTexts: fcNameServerNotifyControlGroup.setDescription('A collection of notification control and notification information objects for monitoring Name Server registrations/de-registrations.')
fcNameServerNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 4)).setObjects(("CISCO-NS-MIB", "fcNameServerRejectRegNotify"), ("CISCO-NS-MIB", "fcNameServerDatabaseFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerNotifyGroup = fcNameServerNotifyGroup.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerNotifyGroup.setDescription('A collection of notifications for monitoring Name Server registrations/de-registrations.')
fcNameServerDBGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 5)).setObjects(("CISCO-NS-MIB", "fcNameServerProxyPortName"), ("CISCO-NS-MIB", "fcNameServerNumRows"), ("CISCO-NS-MIB", "fcNameServerTableLastChange"), ("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerNodeName"), ("CISCO-NS-MIB", "fcNameServerClassOfSvc"), ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"), ("CISCO-NS-MIB", "fcNameServerProcAssoc"), ("CISCO-NS-MIB", "fcNameServerFC4Type"), ("CISCO-NS-MIB", "fcNameServerPortType"), ("CISCO-NS-MIB", "fcNameServerPortIpAddress"), ("CISCO-NS-MIB", "fcNameServerFabricPortName"), ("CISCO-NS-MIB", "fcNameServerHardAddress"), ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"), ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"), ("CISCO-NS-MIB", "fcNameServerFC4Features"), ("CISCO-NS-MIB", "fcNameServerPortFunction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerDBGroup1 = fcNameServerDBGroup1.setStatus('deprecated')
if mibBuilder.loadTexts: fcNameServerDBGroup1.setDescription('A collection of objects for displaying and configuring Name Server objects.')
fcNameServerNotifyGroupRev1 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 6)).setObjects(("CISCO-NS-MIB", "fcNameServerRejectRegNotify"), ("CISCO-NS-MIB", "fcNameServerDatabaseFull"), ("CISCO-NS-MIB", "fcNameServerEntryAdd"), ("CISCO-NS-MIB", "fcNameServerEntryDelete"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerNotifyGroupRev1 = fcNameServerNotifyGroupRev1.setStatus('current')
if mibBuilder.loadTexts: fcNameServerNotifyGroupRev1.setDescription('A collection of notifications for monitoring Name Server registrations/de-registrations.')
fcNameServerDBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 7)).setObjects(("CISCO-NS-MIB", "fcNameServerProxyPortName"), ("CISCO-NS-MIB", "fcNameServerNumRows"), ("CISCO-NS-MIB", "fcNameServerTableLastChange"), ("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerNodeName"), ("CISCO-NS-MIB", "fcNameServerClassOfSvc"), ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"), ("CISCO-NS-MIB", "fcNameServerProcAssoc"), ("CISCO-NS-MIB", "fcNameServerFC4Type"), ("CISCO-NS-MIB", "fcNameServerPortType"), ("CISCO-NS-MIB", "fcNameServerPortIpAddress"), ("CISCO-NS-MIB", "fcNameServerFabricPortName"), ("CISCO-NS-MIB", "fcNameServerHardAddress"), ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"), ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"), ("CISCO-NS-MIB", "fcNameServerFC4Features"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerDBGroup2 = fcNameServerDBGroup2.setStatus('current')
if mibBuilder.loadTexts: fcNameServerDBGroup2.setDescription('A collection of objects for displaying and configuring Name Server objects.')
fcNameServerDBGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 293, 2, 2, 8)).setObjects(("CISCO-NS-MIB", "fcNameServerProxyPortName"), ("CISCO-NS-MIB", "fcNameServerNumRows"), ("CISCO-NS-MIB", "fcNameServerTableLastChange"), ("CISCO-NS-MIB", "fcNameServerPortName"), ("CISCO-NS-MIB", "fcNameServerNodeName"), ("CISCO-NS-MIB", "fcNameServerClassOfSvc"), ("CISCO-NS-MIB", "fcNameServerNodeIpAddress"), ("CISCO-NS-MIB", "fcNameServerProcAssoc"), ("CISCO-NS-MIB", "fcNameServerFC4Type"), ("CISCO-NS-MIB", "fcNameServerPortType"), ("CISCO-NS-MIB", "fcNameServerPortIpAddress"), ("CISCO-NS-MIB", "fcNameServerFabricPortName"), ("CISCO-NS-MIB", "fcNameServerHardAddress"), ("CISCO-NS-MIB", "fcNameServerSymbolicPortName"), ("CISCO-NS-MIB", "fcNameServerSymbolicNodeName"), ("CISCO-NS-MIB", "fcNameServerFC4Features"), ("CISCO-NS-MIB", "fcNameServerPermanentPortName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fcNameServerDBGroup3 = fcNameServerDBGroup3.setStatus('current')
if mibBuilder.loadTexts: fcNameServerDBGroup3.setDescription('A collection of objects for displaying and configuring Name Server objects.')
mibBuilder.exportSymbols("CISCO-NS-MIB", FcNameServerRejReasonExpl=FcNameServerRejReasonExpl, ciscoNsMIB=ciscoNsMIB, fcNameServerRejectReasonCode=fcNameServerRejectReasonCode, fcNameServerStatsTable=fcNameServerStatsTable, fcNameServerSymbolicPortName=fcNameServerSymbolicPortName, fcNameServerMIBCompliance=fcNameServerMIBCompliance, fcNameServerPermanentPortName=fcNameServerPermanentPortName, fcNameServerNodeIpAddress=fcNameServerNodeIpAddress, ciscoNameServerMIBObjects=ciscoNameServerMIBObjects, fcNameServerNotifyGroupRev1=fcNameServerNotifyGroupRev1, fcNameServerNodeName=fcNameServerNodeName, fcNameServerRejReqNotifyEnable=fcNameServerRejReqNotifyEnable, fcNameServerDatabaseFull=fcNameServerDatabaseFull, fcNameServerDBGroup1=fcNameServerDBGroup1, fcNameServerProxyPortName=fcNameServerProxyPortName, fcNameServerFabricPortName=fcNameServerFabricPortName, fcNameServerPortIdentifier=fcNameServerPortIdentifier, fcNameServerProcAssoc=fcNameServerProcAssoc, fcNameServerHardAddress=fcNameServerHardAddress, fcNameServerRejects=fcNameServerRejects, fcNameServerTable=fcNameServerTable, fcNameServerMIBCompliance2=fcNameServerMIBCompliance2, fcNameServerPortName=fcNameServerPortName, fcNameServerTableLastChange=fcNameServerTableLastChange, fcNameServerMIBConformance=fcNameServerMIBConformance, fcNameServerProxyPortEntry=fcNameServerProxyPortEntry, fcNameServerSymbolicNodeName=fcNameServerSymbolicNodeName, fcNameServerMIBCompliances=fcNameServerMIBCompliances, fcNameServerFC4Features=fcNameServerFC4Features, fcNameServerFC4Type=fcNameServerFC4Type, fcNameServerTotalRejects=fcNameServerTotalRejects, fcNameServerPortIpAddress=fcNameServerPortIpAddress, fcNameServerInRscns=fcNameServerInRscns, fcNameServerInformation=fcNameServerInformation, fcNameServerRejReasonCodeExp=fcNameServerRejReasonCodeExp, fcNameServerNumRows=fcNameServerNumRows, fcNameServerStatsGroup=fcNameServerStatsGroup, fcNameServerOutRscns=fcNameServerOutRscns, fcNameServerStatsEntry=fcNameServerStatsEntry, fcNameServerInDeRegReqs=fcNameServerInDeRegReqs, fcNameServerNotifications=fcNameServerNotifications, fcNameServerClassOfSvc=fcNameServerClassOfSvc, fcNameServerEntryDelete=fcNameServerEntryDelete, fcNameServerNotifyGroup=fcNameServerNotifyGroup, fcNameServerStats=fcNameServerStats, fcNameServerProxyPortTable=fcNameServerProxyPortTable, FcGs3RejectReasonCode=FcGs3RejectReasonCode, fcNameServerRejectRegNotify=fcNameServerRejectRegNotify, PYSNMP_MODULE_ID=ciscoNsMIB, fcNameServerPortType=fcNameServerPortType, fcNameServerPortFunction=fcNameServerPortFunction, fcNameServerInGetReqs=fcNameServerInGetReqs, fcNameServerOutGetReqs=fcNameServerOutGetReqs, fcNameServerMIBGroups=fcNameServerMIBGroups, fcNameServerNotification=fcNameServerNotification, fcNameServerEntryAdd=fcNameServerEntryAdd, fcNameServerMIBCompliance1=fcNameServerMIBCompliance1, fcNameServerDBGroup=fcNameServerDBGroup, fcNameServerNotifyControlGroup=fcNameServerNotifyControlGroup, fcNameServerDBGroup3=fcNameServerDBGroup3, fcNameServerMIBCompliance3=fcNameServerMIBCompliance3, fcNameServerDBGroup2=fcNameServerDBGroup2, fcNameServerInRegReqs=fcNameServerInRegReqs, fcNameServerEntry=fcNameServerEntry, fcNameServerConfiguration=fcNameServerConfiguration)
