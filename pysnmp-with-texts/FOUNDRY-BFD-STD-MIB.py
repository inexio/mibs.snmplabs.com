#
# PySNMP MIB module FOUNDRY-BFD-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-BFD-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
bfd, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "bfd")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Integer32, ObjectIdentity, Bits, TimeTicks, iso, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Integer32", "ObjectIdentity", "Bits", "TimeTicks", "iso", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "Gauge32", "NotificationType")
TimeStamp, StorageType, TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "StorageType", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
bfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1))
bfdMIB.setRevisions(('2005-08-22 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bfdMIB.setRevisionsDescriptions(('Initial version. Published as RFC xxxx.',))
if mibBuilder.loadTexts: bfdMIB.setLastUpdated('200507221200Z')
if mibBuilder.loadTexts: bfdMIB.setOrganization('IETF')
if mibBuilder.loadTexts: bfdMIB.setContactInfo(' Thomas D. Nadeau Cisco Systems, Inc. Email: tnadeau@cisco.com Zafar Ali Cisco Systems, Inc. Email: zali@cisco.com ')
if mibBuilder.loadTexts: bfdMIB.setDescription('Bidirectional Forwarding Management Information Base.')
bfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0))
bfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1))
bfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3))
bfdScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1))
class BfdSessIndexTC(TextualConvention, Unsigned32):
    description = 'An index used to uniquely identify BFD sessions.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdInterval(TextualConvention, Unsigned32):
    description = 'The BFD interval delay in microseconds.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class BfdDiag(TextualConvention, Integer32):
    description = 'A common BFD diagnostic code.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("noDiagnostic", 1), ("controlDetectionTimeExpired", 2), ("echoFunctionFailed", 3), ("neighborSignaledSessionDown", 4), ("forwardingPlaneReset", 5), ("pathDown", 6), ("concatenatedPathDown", 7), ("administrativelyDown", 8), ("reverseConcatenatedPathDown", 9))

bfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdAdminStatus.setStatus('current')
if mibBuilder.loadTexts: bfdAdminStatus.setDescription("The global administrative status of BFD in this router. The value 'enabled' denotes that the BFD Process is active on at least one interface; 'disabled' disables it on all interfaces.")
bfdVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdVersionNumber.setReference(' BFD Version 0 (draft-katz-ward-bfd-02.txt)')
if mibBuilder.loadTexts: bfdVersionNumber.setStatus('current')
if mibBuilder.loadTexts: bfdVersionNumber.setDescription('The current version number of the BFD protocol.')
bfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2), )
if mibBuilder.loadTexts: bfdSessTable.setReference('BFD Version 0 (draft-katz-ward-bfd-02.txt)')
if mibBuilder.loadTexts: bfdSessTable.setStatus('current')
if mibBuilder.loadTexts: bfdSessTable.setDescription('The BFD Session Table describes the BFD sessions.')
bfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1), ).setIndexNames((0, "FOUNDRY-BFD-STD-MIB", "bfdSessIndex"))
if mibBuilder.loadTexts: bfdSessEntry.setStatus('current')
if mibBuilder.loadTexts: bfdSessEntry.setDescription('The BFD Session Entry describes BFD session.')
bfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 1), BfdSessIndexTC())
if mibBuilder.loadTexts: bfdSessIndex.setStatus('current')
if mibBuilder.loadTexts: bfdSessIndex.setDescription('This object contains an index used to represent a unique BFD session on this device.')
bfdSessApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessApplicationId.setStatus('current')
if mibBuilder.loadTexts: bfdSessApplicationId.setDescription('This object contains an index used to indicate a local application which owns or maintains this BFD session. For instance, the MPLS VPN process may maintain a subset of the total number of BFD sessions. This application ID provides a convenient way to segregate sessions by the applications which maintain them.')
bfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDiscriminator.setStatus('current')
if mibBuilder.loadTexts: bfdSessDiscriminator.setDescription('This object specifies the local discriminator for this BFD session, used to uniquely identify it.')
bfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteDiscr.setStatus('current')
if mibBuilder.loadTexts: bfdSessRemoteDiscr.setDescription('This object specifies the session discriminator chosen by the remote system for this BFD session.')
bfdSessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 5), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessUdpPort.setReference('draft-katz-ward-bfd-02.txt and draft-raggarwa-mpls-bfd-00.txt')
if mibBuilder.loadTexts: bfdSessUdpPort.setStatus('current')
if mibBuilder.loadTexts: bfdSessUdpPort.setDescription('The UDP Port for BFD. The default value is the well-known value for this port.')
bfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessState.setStatus('current')
if mibBuilder.loadTexts: bfdSessState.setDescription('The perceived state of the BFD session.')
bfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteHeardFlag.setStatus('current')
if mibBuilder.loadTexts: bfdSessRemoteHeardFlag.setDescription('This object specifies status of BFD packet reception from the remote system. Specifically, it is set to true(1) if the local system is actively receiving BFD packets from the remote system, and is set to false(0) if the local system has not received BFD packets recently (within the detection time) or if the local system is attempting to tear down the BFD session.')
bfdSessDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bfdSessDiag.setStatus('current')
if mibBuilder.loadTexts: bfdSessDiag.setDescription("A diagnostic code specifying the local system's reason for the last transition of the session from up(1) to some other state.")
bfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("asyncModeWEchoFun", 1), ("asynchModeWOEchoFun", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessOperMode.setStatus('current')
if mibBuilder.loadTexts: bfdSessOperMode.setDescription('This object specifies current operating mode that BFD session is operating in. A value of AsyncModeWEchoFun(1) ... A value of AsynchModeWOEchoFun(2) ... A value of DemandModeWEchoFunction(3) ... A value of DemandModeWOEchoFunction(4) ... ')
bfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDemandModeDesiredFlag.setStatus('current')
if mibBuilder.loadTexts: bfdSessDemandModeDesiredFlag.setDescription("This object indicates that the local system's desire to use Demand mode. Specifically, it is set to true(1) if the local system wishes to use Demand mode or false(0) if not")
bfdSessEchoFuncModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessEchoFuncModeDesiredFlag.setStatus('current')
if mibBuilder.loadTexts: bfdSessEchoFuncModeDesiredFlag.setDescription("This object indicates that the local system's desire to use Echo mode. Specifically, it is set to true(1) if the local system wishes to use Echo mode or false(0) if not")
bfdSessControlPlanIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessControlPlanIndepFlag.setStatus('current')
if mibBuilder.loadTexts: bfdSessControlPlanIndepFlag.setDescription("This object indicates that the local system's ability to continue to function through a disruption of the control plane. Specifically, it is set to true(1) if the local system BFD implementation is independent of the control plane. Otherwise, the value is set to false(0)")
bfdSessAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 13), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAddrType.setStatus('current')
if mibBuilder.loadTexts: bfdSessAddrType.setDescription('This object specifies IP address of the interface associated with this BFD session. Only values unknown(0), ipv4(1) or ipv6(2) have to be supported. A value of unknown(0) is allowed only when the outgoing interface is of type point-to-point, or when the BFD session is not associated with a specific interface. If any other unsupported values are attempted in a set operation, the agent MUST return an inconsistentValue error. ')
bfdSessAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 14), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAddr.setStatus('current')
if mibBuilder.loadTexts: bfdSessAddr.setDescription('This object specifies IP address of the interface associated with this BFD session. It can also be used to enabled BFD on a specific interface. The value is set to zero when BFD session is not associated with a specific interface. ')
bfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 15), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDesiredMinTxInterval.setStatus('current')
if mibBuilder.loadTexts: bfdSessDesiredMinTxInterval.setDescription('This object specifies the minimum interval, in microseconds, that the local system would like to use when transmitting BFD Control packets.')
bfdSessReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 16), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessReqMinRxInterval.setStatus('current')
if mibBuilder.loadTexts: bfdSessReqMinRxInterval.setDescription('This object specifies the minimum interval, in microseconds, between received BFD Control packets the local system is capable of supporting.')
bfdSessReqMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 17), BfdInterval()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessReqMinEchoRxInterval.setStatus('current')
if mibBuilder.loadTexts: bfdSessReqMinEchoRxInterval.setDescription('This object specifies the minimum interval, in microseconds, between received BFD Echo packets that this system is capable of supporting.')
bfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 18), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDetectMult.setStatus('current')
if mibBuilder.loadTexts: bfdSessDetectMult.setDescription('This object specifies the Detect time multiplier.')
bfdSessStorType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 19), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessStorType.setStatus('current')
if mibBuilder.loadTexts: bfdSessStorType.setDescription("This variable indicates the storage type for this object. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
bfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessRowStatus.setStatus('current')
if mibBuilder.loadTexts: bfdSessRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the bfdSessRowStatus and bfdSessStorageType.')
bfdSessAuthPresFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 21), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthPresFlag.setStatus('current')
if mibBuilder.loadTexts: bfdSessAuthPresFlag.setDescription("This object indicates that the local system's desire to use Authentication. Specifically, it is set to true(1) if the local system wishes the session to be authenticated or false(0) if not")
bfdSessAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthenticationType.setStatus('current')
if mibBuilder.loadTexts: bfdSessAuthenticationType.setDescription('The Authentication Type used for this BFD session. This field is valid only when the Authentication Present bit is set')
bfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3), )
if mibBuilder.loadTexts: bfdSessPerfTable.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfTable.setDescription('This table specifies BFD Session performance counters.')
bfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1), )
bfdSessEntry.registerAugmentions(("FOUNDRY-BFD-STD-MIB", "bfdSessPerfEntry"))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: bfdSessPerfEntry.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfEntry.setDescription('An entry in this table is created by a BFD-enabled node for every BFD Session. bfdCounterDiscontinuityTime is used to indicate potential discontinuity for all counter objects in this table.')
bfdSessPerfPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktIn.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfPktIn.setDescription('The total number of BFD messages received for this BFD session.')
bfdSessPerfPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOut.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfPktOut.setDescription('The total number of BFD messages sent for this BFD session.')
bfdSessPerfUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfUpTime.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfUpTime.setDescription('The value of sysUpTime on the most recent occasion at which the session came up. If no such up event exists this object contains a zero value.')
bfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastSessDownTime.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfLastSessDownTime.setDescription('The value of sysUpTime on the most recent occasion at which the last time communication was lost with the neighbor. If no such down event exist this object contains a zero value.')
bfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 5), BfdDiag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastCommLostDiag.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfLastCommLostDiag.setDescription('The BFD diag code for the last time communication was lost with the neighbor. If no such down event exists this object contains a zero value.')
bfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfSessUpCount.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfSessUpCount.setDescription('The number of times this session has gone into the Up state since the router last rebooted.')
bfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfDiscTime.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfDiscTime.setDescription('The value of sysUpTime on the most recent occasion at which any one or more of the session counters suffered a discontinuity. The relevant counters are the specific instances associated with this BFD session of any Counter32 object contained in the BfdSessPerfTable. If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this object contains a zero value.')
bfdSessPerfPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktInHC.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfPktInHC.setDescription('This value represents the total number of BFD messages received for this BFD session. It MUST be equal to the least significant 32 bits of bfdSessPerfPktIn if bfdSessPerfPktInHC is supported according to the rules spelled out in RFC2863.')
bfdSessPerfPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOutHC.setStatus('current')
if mibBuilder.loadTexts: bfdSessPerfPktOutHC.setDescription('This value represents the total number of total number of BFD messages transmitted for this BFD session. It MUST be equal to the least significant 32 bits of bfdSessPerfPktIn if bfdSessPerfPktOutHC is supported according to the rules spelled out in RFC2863.')
bfdSessMapTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4), )
if mibBuilder.loadTexts: bfdSessMapTable.setReference('BFD Version 0 (draft-katz-ward-bfd-02.txt)')
if mibBuilder.loadTexts: bfdSessMapTable.setStatus('current')
if mibBuilder.loadTexts: bfdSessMapTable.setDescription('The BFD Session Mapping Table maps the complex indexing of the BFD sessions to the flat BFDIndex used in the BfdSessionTable. Implementors need to be aware that if the value of the bfdSessAddr (an OID) has more that 111 sub-identifiers, then OIDs of column instances in this table will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3. ')
bfdSessMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4, 1), ).setIndexNames((0, "FOUNDRY-BFD-STD-MIB", "bfdSessApplicationId"), (0, "FOUNDRY-BFD-STD-MIB", "bfdSessDiscriminator"), (0, "FOUNDRY-BFD-STD-MIB", "bfdSessAddrType"), (0, "FOUNDRY-BFD-STD-MIB", "bfdSessAddr"))
if mibBuilder.loadTexts: bfdSessMapEntry.setStatus('current')
if mibBuilder.loadTexts: bfdSessMapEntry.setDescription('The BFD Session Entry describes BFD session that is mapped to this index. Implementors need to be aware that if the value of the mplsInSegmentMapLabelPtrIndex (an OID) has more that 111 sub-identifiers, then OIDs of column instances in this table will have more than 128 sub-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.')
bfdSessMapBfdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 4, 1, 1), BfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessMapBfdIndex.setStatus('current')
if mibBuilder.loadTexts: bfdSessMapBfdIndex.setDescription('This object specifies the BfdIndex referred to by the indexes of this row. In essence, a mapping is provided between these indexes and the BfdSessTable.')
bfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdSessNotificationsEnable.setReference('See also RFC3413 for explanation that notifications are under the ultimate control of the MIB modules in this document.')
if mibBuilder.loadTexts: bfdSessNotificationsEnable.setStatus('current')
if mibBuilder.loadTexts: bfdSessNotificationsEnable.setDescription('If this object is set to true(1), then it enables the emission of bfdSessUp and bfdSessDown notifications; otherwise these notifications are not emitted.')
bfdSessUp = NotificationType((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0, 1)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessUp.setStatus('current')
if mibBuilder.loadTexts: bfdSessUp.setDescription('This notification is generated when the bfdSessState object for one or more contiguous entries in bfdSessTable are about to enter the up(2) state from some other state. The included values of bfdSessDiag MUST both be set equal to this new state (i.e: up(1)). The two instances of bfdSessDiag in this notification indicate the range of indexes that are affected. Note that all the indexes of the two ends of the range can be derived from the instance identifiers of these two objects. For the cases where a contiguous range of sessions have transitioned into the up(1) state at roughly the same time, the device SHOULD issue a single notification for each range of contiguous indexes in an effort to minimize the emission of a large number of notifications. If a notification has to be issued for just a single bfdSessEntry, then the instance identifier (and values) of the two bfdSessDiag objects MUST be the identical.')
bfdSessDown = NotificationType((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 0, 2)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessDown.setStatus('current')
if mibBuilder.loadTexts: bfdSessDown.setDescription('This notification is generated when the bfdSessState object for one or more contiguous entries in bfdSessTable are about to enter the down(4) or adminDown(5) states from some other state. The included values of bfdSessDiag MUST both be set equal to this new state (i.e: down(4) or adminDown(5)). The two instances of bfdSessDiag in this notification indicate the range of indexes that are affected. Note that all the indexes of the two ends of the range can be derived from the instance identifiers of these two objects. For cases where a contiguous range of sessions have transitioned into the down(4) or adminDown(5) states at roughly the same time, the device SHOULD issue a single notification for each range of contiguous indexes in an effort to minimize the emission of a large number of notifications. If a notification has to be issued for just a single bfdSessEntry, then the instance identifier (and values) of the two bfdSessDiag objects MUST be the identical.')
bfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1))
bfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 2))
bfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 2, 1)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessionGroup"), ("FOUNDRY-BFD-STD-MIB", "bfdSessionPerfGroup"), ("FOUNDRY-BFD-STD-MIB", "bfdSessionPerfHCGroup"), ("FOUNDRY-BFD-STD-MIB", "bfdNotificationGroup"), ("FOUNDRY-BFD-STD-MIB", "bfdSessionPerfHCGroup"), ("FOUNDRY-BFD-STD-MIB", "bfdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdModuleFullCompliance = bfdModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: bfdModuleFullCompliance.setDescription('Compliance statement for agents that provide full support for BFD-MIB. Such devices can then be monitored and also be configured using this MIB module.')
bfdSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 1)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessNotificationsEnable"), ("FOUNDRY-BFD-STD-MIB", "bfdAdminStatus"), ("FOUNDRY-BFD-STD-MIB", "bfdVersionNumber"), ("FOUNDRY-BFD-STD-MIB", "bfdSessApplicationId"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDiscriminator"), ("FOUNDRY-BFD-STD-MIB", "bfdSessAddrType"), ("FOUNDRY-BFD-STD-MIB", "bfdSessAddr"), ("FOUNDRY-BFD-STD-MIB", "bfdSessRemoteDiscr"), ("FOUNDRY-BFD-STD-MIB", "bfdSessUdpPort"), ("FOUNDRY-BFD-STD-MIB", "bfdSessState"), ("FOUNDRY-BFD-STD-MIB", "bfdSessRemoteHeardFlag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDiag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessOperMode"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDemandModeDesiredFlag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessEchoFuncModeDesiredFlag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessControlPlanIndepFlag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDesiredMinTxInterval"), ("FOUNDRY-BFD-STD-MIB", "bfdSessReqMinRxInterval"), ("FOUNDRY-BFD-STD-MIB", "bfdSessReqMinEchoRxInterval"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDetectMult"), ("FOUNDRY-BFD-STD-MIB", "bfdSessStorType"), ("FOUNDRY-BFD-STD-MIB", "bfdSessRowStatus"), ("FOUNDRY-BFD-STD-MIB", "bfdSessMapBfdIndex"), ("FOUNDRY-BFD-STD-MIB", "bfdSessAuthPresFlag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessAuthenticationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionGroup = bfdSessionGroup.setStatus('current')
if mibBuilder.loadTexts: bfdSessionGroup.setDescription('Collection of objects needed for BFD sessions.')
bfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 2)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktIn"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktOut"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfUpTime"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfLastSessDownTime"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfLastCommLostDiag"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfSessUpCount"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfGroup = bfdSessionPerfGroup.setStatus('current')
if mibBuilder.loadTexts: bfdSessionPerfGroup.setDescription('Collection of objects needed to monitor the performance of BFD sessions.')
bfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 3)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktInHC"), ("FOUNDRY-BFD-STD-MIB", "bfdSessPerfPktOutHC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfHCGroup = bfdSessionPerfHCGroup.setStatus('current')
if mibBuilder.loadTexts: bfdSessionPerfHCGroup.setDescription('Collection of objects needed to monitor the performance of BFD sessions for which the values of bfdSessPerfPktIn, bfdSessPerfPktOut wrap around too quickly.')
bfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1991, 3, 3, 1, 3, 1, 4)).setObjects(("FOUNDRY-BFD-STD-MIB", "bfdSessUp"), ("FOUNDRY-BFD-STD-MIB", "bfdSessDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdNotificationGroup = bfdNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: bfdNotificationGroup.setDescription('Set of notifications implemented in this module.')
mibBuilder.exportSymbols("FOUNDRY-BFD-STD-MIB", bfdSessReqMinEchoRxInterval=bfdSessReqMinEchoRxInterval, bfdSessDesiredMinTxInterval=bfdSessDesiredMinTxInterval, bfdSessPerfPktIn=bfdSessPerfPktIn, bfdVersionNumber=bfdVersionNumber, bfdSessTable=bfdSessTable, bfdSessRemoteHeardFlag=bfdSessRemoteHeardFlag, bfdSessAddr=bfdSessAddr, bfdSessionPerfGroup=bfdSessionPerfGroup, bfdSessMapBfdIndex=bfdSessMapBfdIndex, bfdSessEntry=bfdSessEntry, bfdSessPerfLastSessDownTime=bfdSessPerfLastSessDownTime, bfdSessPerfLastCommLostDiag=bfdSessPerfLastCommLostDiag, bfdSessMapEntry=bfdSessMapEntry, bfdSessMapTable=bfdSessMapTable, bfdSessDetectMult=bfdSessDetectMult, bfdSessPerfEntry=bfdSessPerfEntry, bfdSessEchoFuncModeDesiredFlag=bfdSessEchoFuncModeDesiredFlag, bfdSessStorType=bfdSessStorType, bfdSessionPerfHCGroup=bfdSessionPerfHCGroup, bfdAdminStatus=bfdAdminStatus, bfdSessPerfUpTime=bfdSessPerfUpTime, bfdSessDown=bfdSessDown, bfdModuleFullCompliance=bfdModuleFullCompliance, bfdSessNotificationsEnable=bfdSessNotificationsEnable, bfdSessRowStatus=bfdSessRowStatus, bfdObjects=bfdObjects, bfdScalarObjects=bfdScalarObjects, bfdSessAuthPresFlag=bfdSessAuthPresFlag, bfdSessUp=bfdSessUp, BfdInterval=BfdInterval, bfdSessDiag=bfdSessDiag, bfdSessApplicationId=bfdSessApplicationId, bfdConformance=bfdConformance, bfdSessPerfPktOutHC=bfdSessPerfPktOutHC, bfdMIB=bfdMIB, bfdSessPerfDiscTime=bfdSessPerfDiscTime, BfdDiag=BfdDiag, bfdSessPerfTable=bfdSessPerfTable, bfdSessReqMinRxInterval=bfdSessReqMinRxInterval, bfdCompliances=bfdCompliances, bfdSessPerfSessUpCount=bfdSessPerfSessUpCount, BfdSessIndexTC=BfdSessIndexTC, bfdSessOperMode=bfdSessOperMode, bfdSessAuthenticationType=bfdSessAuthenticationType, bfdSessControlPlanIndepFlag=bfdSessControlPlanIndepFlag, bfdSessDemandModeDesiredFlag=bfdSessDemandModeDesiredFlag, bfdNotifications=bfdNotifications, bfdSessUdpPort=bfdSessUdpPort, bfdSessRemoteDiscr=bfdSessRemoteDiscr, bfdSessionGroup=bfdSessionGroup, bfdSessDiscriminator=bfdSessDiscriminator, bfdSessAddrType=bfdSessAddrType, bfdSessPerfPktOut=bfdSessPerfPktOut, bfdSessState=bfdSessState, bfdNotificationGroup=bfdNotificationGroup, bfdSessPerfPktInHC=bfdSessPerfPktInHC, PYSNMP_MODULE_ID=bfdMIB, bfdSessIndex=bfdSessIndex, bfdGroups=bfdGroups)
