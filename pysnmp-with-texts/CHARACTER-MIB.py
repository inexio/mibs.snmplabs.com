#
# PySNMP MIB module CHARACTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHARACTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
mib_2, ModuleIdentity, MibIdentifier, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, transmission, Counter64, NotificationType, Bits, ObjectIdentity, TimeTicks, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ModuleIdentity", "MibIdentifier", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "transmission", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "IpAddress")
DisplayString, TextualConvention, InstancePointer, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "InstancePointer", "AutonomousType")
char = ModuleIdentity((1, 3, 6, 1, 2, 1, 19))
if mibBuilder.loadTexts: char.setLastUpdated('9405261700Z')
if mibBuilder.loadTexts: char.setOrganization('IETF Character MIB Working Group')
if mibBuilder.loadTexts: char.setContactInfo(' Bob Stewart Postal: Xyplex, Inc. 295 Foster Street Littleton, MA 01460 Tel: 508-952-4816 Fax: 508-952-4887 E-mail: rlstewart@eng.xyplex.com')
if mibBuilder.loadTexts: char.setDescription('The MIB module for character stream devices.')
class PortIndex(TextualConvention, Integer32):
    description = "A unique value, greater than zero, for each character port in the managed system. It is recommended that values are assigned contiguously starting from 1. The value for each interface sub- layer must remain constant at least from one re- initialization of the entity's network management system to the next re-initialization. In a system where the character ports are attached to hardware represented by an ifIndex, it is conventional, but not required, to make the character port index equal to the corresponding ifIndex."
    status = 'current'
    displayHint = 'd'

charNumber = MibScalar((1, 3, 6, 1, 2, 1, 19, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charNumber.setStatus('current')
if mibBuilder.loadTexts: charNumber.setDescription('The number of entries in charPortTable, regardless of their current state.')
charPortTable = MibTable((1, 3, 6, 1, 2, 1, 19, 2), )
if mibBuilder.loadTexts: charPortTable.setStatus('current')
if mibBuilder.loadTexts: charPortTable.setDescription('A list of port entries. The number of entries is given by the value of charNumber.')
charPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 2, 1), ).setIndexNames((0, "CHARACTER-MIB", "charPortIndex"))
if mibBuilder.loadTexts: charPortEntry.setStatus('current')
if mibBuilder.loadTexts: charPortEntry.setDescription('Status and parameter values for a character port.')
charPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortIndex.setStatus('current')
if mibBuilder.loadTexts: charPortIndex.setDescription('A unique value for each character port, perhaps corresponding to the same value of ifIndex when the character port is associated with a hardware port represented by an ifIndex.')
charPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortName.setStatus('current')
if mibBuilder.loadTexts: charPortName.setDescription('An administratively assigned name for the port, typically with some local significance.')
charPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("physical", 1), ("virtual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortType.setStatus('current')
if mibBuilder.loadTexts: charPortType.setDescription("The port's type, 'physical' if the port represents an external hardware connector, 'virtual' if it does not.")
charPortHardware = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 4), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortHardware.setStatus('current')
if mibBuilder.loadTexts: charPortHardware.setDescription("A reference to hardware MIB definitions specific to a physical port's external connector. For example, if the connector is RS-232, then the value of this object refers to a MIB sub-tree defining objects specific to RS-232. If an agent is not configured to have such values, the agent returns the object identifier: nullHardware OBJECT IDENTIFIER ::= { 0 0 } ")
charPortReset = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortReset.setStatus('current')
if mibBuilder.loadTexts: charPortReset.setDescription("A control to force the port into a clean, initial state, both hardware and software, disconnecting all the port's existing sessions. In response to a get-request or get-next-request, the agent always returns 'ready' as the value. Setting the value to 'execute' causes a reset.")
charPortAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("off", 3), ("maintenance", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortAdminStatus.setStatus('current')
if mibBuilder.loadTexts: charPortAdminStatus.setDescription("The port's desired state, independent of flow control. 'enabled' indicates that the port is allowed to pass characters and form new sessions. 'disabled' indicates that the port is allowed to pass characters but not form new sessions. 'off' indicates that the port is not allowed to pass characters or have any sessions. 'maintenance' indicates a maintenance mode, exclusive of normal operation, such as running a test. 'enabled' corresponds to ifAdminStatus 'up'. 'disabled' and 'off' correspond to ifAdminStatus 'down'. 'maintenance' corresponds to ifAdminStatus 'test'.")
charPortOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("maintenance", 3), ("absent", 4), ("active", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOperStatus.setStatus('current')
if mibBuilder.loadTexts: charPortOperStatus.setDescription("The port's actual, operational state, independent of flow control. 'up' indicates able to function normally. 'down' indicates inability to function for administrative or operational reasons. 'maintenance' indicates a maintenance mode, exclusive of normal operation, such as running a test. 'absent' indicates that port hardware is not present. 'active' indicates up with a user present (e.g. logged in). 'up' and 'active' correspond to ifOperStatus 'up'. 'down' and 'absent' correspond to ifOperStatus 'down'. 'maintenance' corresponds to ifOperStatus 'test'.")
charPortLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortLastChange.setStatus('current')
if mibBuilder.loadTexts: charPortLastChange.setDescription('The value of sysUpTime at the time the port entered its current operational state. If the current state was entered prior to the last reinitialization of the local network management subsystem, then this object contains a zero value.')
charPortInFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortInFlowType.setStatus('deprecated')
if mibBuilder.loadTexts: charPortInFlowType.setDescription("The port's type of input flow control. 'none' indicates no flow control at this level or below. 'xonXoff' indicates software flow control by recognizing XON and XOFF characters. 'hardware' indicates flow control delegated to the lower level, for example a parallel port. 'ctsRts' and 'dsrDtr' are specific to RS-232-like ports. Although not architecturally pure, they are included here for simplicity's sake.")
charPortOutFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("xonXoff", 2), ("hardware", 3), ("ctsRts", 4), ("dsrDtr", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortOutFlowType.setStatus('deprecated')
if mibBuilder.loadTexts: charPortOutFlowType.setDescription("The port's type of output flow control. 'none' indicates no flow control at this level or below. 'xonXoff' indicates software flow control by recognizing XON and XOFF characters. 'hardware' indicates flow control delegated to the lower level, for example a parallel port. 'ctsRts' and 'dsrDtr' are specific to RS-232-like ports. Although not architecturally pure, they are included here for simplicy's sake.")
charPortInFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortInFlowState.setStatus('current')
if mibBuilder.loadTexts: charPortInFlowState.setDescription("The current operational state of input flow control on the port. 'none' indicates not applicable. 'unknown' indicates this level does not know. 'stop' indicates flow not allowed. 'go' indicates flow allowed.")
charPortOutFlowState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("unknown", 2), ("stop", 3), ("go", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOutFlowState.setStatus('current')
if mibBuilder.loadTexts: charPortOutFlowState.setDescription("The current operational state of output flow control on the port. 'none' indicates not applicable. 'unknown' indicates this level does not know. 'stop' indicates flow not allowed. 'go' indicates flow allowed.")
charPortInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortInCharacters.setStatus('current')
if mibBuilder.loadTexts: charPortInCharacters.setDescription("Total number of characters detected as input from the port since system re-initialization and while the port operational state was 'up', 'active', or 'maintenance', including, for example, framing, flow control (i.e. XON and XOFF), each occurrence of a BREAK condition, locally-processed input, and input sent to all sessions.")
charPortOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortOutCharacters.setStatus('current')
if mibBuilder.loadTexts: charPortOutCharacters.setDescription("Total number of characters detected as output to the port since system re-initialization and while the port operational state was 'up', 'active', or 'maintenance', including, for example, framing, flow control (i.e. XON and XOFF), each occurrence of a BREAK condition, locally-created output, and output received from all sessions.")
charPortAdminOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dynamic", 1), ("network", 2), ("local", 3), ("none", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortAdminOrigin.setStatus('current')
if mibBuilder.loadTexts: charPortAdminOrigin.setDescription("The administratively allowed origin for establishing session on the port. 'dynamic' allows 'network' or 'local' session establishment. 'none' disallows session establishment.")
charPortSessionMaximum = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortSessionMaximum.setStatus('current')
if mibBuilder.loadTexts: charPortSessionMaximum.setDescription('The maximum number of concurrent sessions allowed on the port. A value of -1 indicates no maximum. Setting the maximum to less than the current number of sessions has unspecified results.')
charPortSessionNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 17), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortSessionNumber.setStatus('current')
if mibBuilder.loadTexts: charPortSessionNumber.setDescription('The number of open sessions on the port that are in the connecting, connected, or disconnecting state.')
charPortSessionIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortSessionIndex.setStatus('current')
if mibBuilder.loadTexts: charPortSessionIndex.setDescription("The value of charSessIndex for the port's first or only active session. If the port has no active session, the agent returns the value zero.")
charPortInFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortInFlowTypes.setStatus('current')
if mibBuilder.loadTexts: charPortInFlowTypes.setDescription("The port's types of input flow control at the software level. Hardware-level flow control is independently controlled by the appropriate hardware-level MIB. A value of zero indicates no flow control. Depending on the specific implementation, any or all combinations of flow control may be chosen by adding the values: 128 xonXoff, recognizing XON and XOFF characters 64 enqHost, ENQ/ACK to allow input to host 32 enqTerm, ACK to allow output to port ")
charPortOutFlowTypes = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charPortOutFlowTypes.setStatus('current')
if mibBuilder.loadTexts: charPortOutFlowTypes.setDescription("The port's types of output flow control at the software level. Hardware-level flow control is independently controlled by the appropriate hardware-level MIB. A value of zero indicates no flow control. Depending on the specific implementation, any or all combinations of flow control may be chosen by adding the values: 128 xonXoff, recognizing XON and XOFF characters 64 enqHost, ENQ/ACK to allow input to host 32 enqTerm, ACK to allow output to port ")
charPortLowerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 2, 1, 21), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charPortLowerIfIndex.setStatus('current')
if mibBuilder.loadTexts: charPortLowerIfIndex.setDescription('The ifIndex value of the lower level hardware supporting this character port, zero if none.')
charSessTable = MibTable((1, 3, 6, 1, 2, 1, 19, 3), )
if mibBuilder.loadTexts: charSessTable.setStatus('current')
if mibBuilder.loadTexts: charSessTable.setDescription('A list of port session entries.')
charSessEntry = MibTableRow((1, 3, 6, 1, 2, 1, 19, 3, 1), ).setIndexNames((0, "CHARACTER-MIB", "charSessPortIndex"), (0, "CHARACTER-MIB", "charSessIndex"))
if mibBuilder.loadTexts: charSessEntry.setStatus('current')
if mibBuilder.loadTexts: charSessEntry.setDescription('Status and parameter values for a character port session.')
charSessPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessPortIndex.setStatus('current')
if mibBuilder.loadTexts: charSessPortIndex.setDescription('The value of charPortIndex for the port to which this session belongs.')
charSessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessIndex.setStatus('current')
if mibBuilder.loadTexts: charSessIndex.setDescription('The session index in the context of the port, a non-zero positive integer. Session indexes within a port need not be sequential. Session indexes may be reused for different ports. For example, port 1 and port 3 may both have a session 2 at the same time. Session indexes may have any valid integer value, with any meaning convenient to the agent implementation.')
charSessKill = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: charSessKill.setStatus('current')
if mibBuilder.loadTexts: charSessKill.setDescription("A control to terminate the session. In response to a get-request or get-next-request, the agent always returns 'ready' as the value. Setting the value to 'execute' causes termination.")
charSessState = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connecting", 1), ("connected", 2), ("disconnecting", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessState.setStatus('current')
if mibBuilder.loadTexts: charSessState.setDescription("The current operational state of the session, disregarding flow control. 'connected' indicates that character data could flow on the network side of session. 'connecting' indicates moving from nonexistent toward 'connected'. 'disconnecting' indicates moving from 'connected' or 'connecting' to nonexistent.")
charSessProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 5), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessProtocol.setStatus('current')
if mibBuilder.loadTexts: charSessProtocol.setDescription('The network protocol over which the session is running. Other OBJECT IDENTIFIER values may be defined elsewhere, in association with specific protocols. However, this document assigns those of known interest as of this writing.')
wellKnownProtocols = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4))
protocolOther = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 1))
protocolTelnet = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 2))
protocolRlogin = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 3))
protocolLat = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 4))
protocolX29 = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 5))
protocolVtp = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 4, 6))
charSessOperOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("network", 2), ("local", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessOperOrigin.setStatus('current')
if mibBuilder.loadTexts: charSessOperOrigin.setDescription("The session's source of establishment.")
charSessInCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessInCharacters.setStatus('current')
if mibBuilder.loadTexts: charSessInCharacters.setDescription("This session's subset of charPortInCharacters.")
charSessOutCharacters = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessOutCharacters.setStatus('current')
if mibBuilder.loadTexts: charSessOutCharacters.setDescription("This session's subset of charPortOutCharacters.")
charSessConnectionId = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 9), InstancePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessConnectionId.setStatus('current')
if mibBuilder.loadTexts: charSessConnectionId.setDescription('A reference to additional local MIB information. This should be the highest available related MIB, corresponding to charSessProtocol, such as Telnet. For example, the value for a TCP connection (in the absence of a Telnet MIB) is the object identifier of tcpConnState. If an agent is not configured to have such values, the agent returns the object identifier: nullConnectionId OBJECT IDENTIFIER ::= { 0 0 } ')
charSessStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 19, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: charSessStartTime.setStatus('current')
if mibBuilder.loadTexts: charSessStartTime.setDescription('The value of sysUpTime in MIB-2 when the session entered connecting state.')
charConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5))
charGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 1))
charCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 19, 5, 2))
charCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 19, 5, 2, 1)).setObjects(("CHARACTER-MIB", "charGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    charCompliance = charCompliance.setStatus('current')
if mibBuilder.loadTexts: charCompliance.setDescription('The compliance statement for SNMPv2 entities which have Character hardware interfaces.')
charGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 19, 5, 1, 1)).setObjects(("CHARACTER-MIB", "charNumber"), ("CHARACTER-MIB", "charPortIndex"), ("CHARACTER-MIB", "charPortName"), ("CHARACTER-MIB", "charPortType"), ("CHARACTER-MIB", "charPortHardware"), ("CHARACTER-MIB", "charPortReset"), ("CHARACTER-MIB", "charPortAdminStatus"), ("CHARACTER-MIB", "charPortOperStatus"), ("CHARACTER-MIB", "charPortLastChange"), ("CHARACTER-MIB", "charPortInFlowState"), ("CHARACTER-MIB", "charPortOutFlowState"), ("CHARACTER-MIB", "charPortAdminOrigin"), ("CHARACTER-MIB", "charPortSessionMaximum"), ("CHARACTER-MIB", "charPortInFlowTypes"), ("CHARACTER-MIB", "charPortOutFlowTypes"), ("CHARACTER-MIB", "charPortInCharacters"), ("CHARACTER-MIB", "charPortOutCharacters"), ("CHARACTER-MIB", "charPortSessionNumber"), ("CHARACTER-MIB", "charPortSessionIndex"), ("CHARACTER-MIB", "charPortLowerIfIndex"), ("CHARACTER-MIB", "charSessPortIndex"), ("CHARACTER-MIB", "charSessIndex"), ("CHARACTER-MIB", "charSessKill"), ("CHARACTER-MIB", "charSessState"), ("CHARACTER-MIB", "charSessProtocol"), ("CHARACTER-MIB", "charSessOperOrigin"), ("CHARACTER-MIB", "charSessInCharacters"), ("CHARACTER-MIB", "charSessOutCharacters"), ("CHARACTER-MIB", "charSessConnectionId"), ("CHARACTER-MIB", "charSessStartTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    charGroup = charGroup.setStatus('current')
if mibBuilder.loadTexts: charGroup.setDescription('A collection of objects providing information applicable to all Character interfaces.')
mibBuilder.exportSymbols("CHARACTER-MIB", protocolRlogin=protocolRlogin, charPortInFlowType=charPortInFlowType, charNumber=charNumber, charSessTable=charSessTable, char=char, PYSNMP_MODULE_ID=char, charPortOutCharacters=charPortOutCharacters, charGroups=charGroups, charPortAdminStatus=charPortAdminStatus, protocolLat=protocolLat, charPortOperStatus=charPortOperStatus, wellKnownProtocols=wellKnownProtocols, charPortInFlowTypes=charPortInFlowTypes, charSessPortIndex=charSessPortIndex, charSessConnectionId=charSessConnectionId, charPortType=charPortType, charPortLowerIfIndex=charPortLowerIfIndex, protocolX29=protocolX29, charPortOutFlowTypes=charPortOutFlowTypes, charCompliances=charCompliances, charPortInCharacters=charPortInCharacters, charPortTable=charPortTable, charPortSessionMaximum=charPortSessionMaximum, charPortLastChange=charPortLastChange, charSessInCharacters=charSessInCharacters, charSessState=charSessState, protocolTelnet=protocolTelnet, charPortReset=charPortReset, charSessOperOrigin=charSessOperOrigin, charSessStartTime=charSessStartTime, charPortInFlowState=charPortInFlowState, charSessIndex=charSessIndex, charSessEntry=charSessEntry, charPortOutFlowState=charPortOutFlowState, charSessKill=charSessKill, charSessProtocol=charSessProtocol, charSessOutCharacters=charSessOutCharacters, charPortAdminOrigin=charPortAdminOrigin, charConformance=charConformance, charPortSessionNumber=charPortSessionNumber, charGroup=charGroup, protocolVtp=protocolVtp, charPortEntry=charPortEntry, charPortSessionIndex=charPortSessionIndex, charPortOutFlowType=charPortOutFlowType, charCompliance=charCompliance, charPortName=charPortName, charPortHardware=charPortHardware, protocolOther=protocolOther, PortIndex=PortIndex, charPortIndex=charPortIndex)
