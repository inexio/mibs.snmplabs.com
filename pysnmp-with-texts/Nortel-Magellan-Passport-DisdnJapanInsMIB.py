#
# PySNMP MIB module Nortel-Magellan-Passport-DisdnJapanInsMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-DisdnJapanInsMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:26:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dataSigChanIndex, dataSigChan = mibBuilder.importSymbols("Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex", "dataSigChan")
Unsigned32, DisplayString, RowStatus, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "Unsigned32", "DisplayString", "RowStatus", "StorageType")
NonReplicated, Link = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "Link")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, MibIdentifier, Integer32, Unsigned32, Counter32, Counter64, ModuleIdentity, TimeTicks, iso, Bits, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "Unsigned32", "Counter32", "Counter64", "ModuleIdentity", "TimeTicks", "iso", "Bits", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
disdnJapanInsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118))
dataSigChanIns = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11))
dataSigChanInsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1), )
if mibBuilder.loadTexts: dataSigChanInsRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsRowStatusTable.setDescription('This entry controls the addition and deletion of dataSigChanIns components.')
dataSigChanInsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"))
if mibBuilder.loadTexts: dataSigChanInsRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsRowStatusEntry.setDescription('A single entry in the table represents a single dataSigChanIns component.')
dataSigChanInsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsRowStatus.setDescription('This variable is used as the basis for SNMP naming of dataSigChanIns components. These components can be added and deleted.')
dataSigChanInsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
dataSigChanInsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsStorageType.setDescription('This variable represents the storage type value for the dataSigChanIns tables.')
dataSigChanInsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dataSigChanInsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsIndex.setDescription('This variable represents the index for the dataSigChanIns tables.')
dataSigChanInsL2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11), )
if mibBuilder.loadTexts: dataSigChanInsL2Table.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsL2Table.setDescription('This group represents the provisionable Layer 2 attributes of the Q931 CCITT protocol.')
dataSigChanInsL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"))
if mibBuilder.loadTexts: dataSigChanInsL2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsL2Entry.setDescription('An entry in the dataSigChanInsL2Table.')
dataSigChanInsT23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsT23.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsT23.setDescription('This attribute specifies the layer2 enable request timer.')
dataSigChanInsT200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsT200.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsT200.setDescription('This attribute specifies the maximum time between a layer 2 frame and its acknowledgement')
dataSigChanInsN200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsN200.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsN200.setDescription('This attribute specifies the maximum number of re-transmissions of a layer2 frame.')
dataSigChanInsT203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsT203.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsT203.setDescription('This attribute specifies the maximum time that a no layer 2 traffic situation can last. Expiry triggers a check on whether the far end is a live.')
dataSigChanInsN201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsN201.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsN201.setDescription('This attribute specifies the maximum number of octets in an information field.')
dataSigChanInsCircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsCircuitSwitchedK.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsCircuitSwitchedK.setDescription('This attribute specifies the maximum number of frames for B channel use.')
dataSigChanInsProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13), )
if mibBuilder.loadTexts: dataSigChanInsProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsProvTable.setDescription('This group defines the general options of the d-channel signalling link.')
dataSigChanInsProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"))
if mibBuilder.loadTexts: dataSigChanInsProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsProvEntry.setDescription('An entry in the dataSigChanInsProvTable.')
dataSigChanInsSide = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsSide.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsSide.setDescription('This attribute specifies whether the layer 2 HDLC interface is the network or user side of the connection.')
dataSigChanInsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15), )
if mibBuilder.loadTexts: dataSigChanInsOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsOperTable.setDescription('This group provides the operational attributes for the signalling protocol.')
dataSigChanInsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"))
if mibBuilder.loadTexts: dataSigChanInsOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsOperEntry.setDescription('An entry in the dataSigChanInsOperTable.')
dataSigChanInsActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsActiveChannels.setDescription('This attribute indicates the number of currently active channels. This includes data and voice channels.')
dataSigChanInsPeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsPeakActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsPeakActiveChannels.setDescription('This attribute indicates the maximum number of channels that have been active on this signalling channel during the last polling period.')
dataSigChanInsDChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsDChanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsDChanStatus.setDescription('This attribute indicates the state of the D-channel. outOfService means that there is no layer 2 or layer 3 connectivity to the PBX. establishing means that the signalling channel is attempting to stage the layer 2. established means that the layer 2 is enabled. If the signalling channel stays in the established state, then it is waiting for a restart from the PBX. enabling means that the resources for processing calls are being initialized. If the signalling channel stays in the enabling state then it is waiting for a restart acknowledgement from the PBX. inService means that the resources for processing calls are available. restarting means that the resources for call processing are being rei- initialized.')
dataSigChanInsToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16), )
if mibBuilder.loadTexts: dataSigChanInsToolsTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsToolsTable.setDescription('This group contains a series of operational attributes which turn on and off several kinds of tracing.')
dataSigChanInsToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"))
if mibBuilder.loadTexts: dataSigChanInsToolsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsToolsEntry.setDescription('An entry in the dataSigChanInsToolsTable.')
dataSigChanInsTracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsTracing.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsTracing.setDescription('This attribute defines which types of tracing are active for this signalling channel. The tracing messages are sent to the debug stream. To see the messages the agentQueue attribute in Col/debug must be greater than 0 and a Telnet NMIS session must list the debug stream in in its data streams (ex. set nmis telnet session/1 dataStreams debug). Different types of tracing can be enabled simultaneously. Note that tracing consumes additional CPU resources and will slow down call processing on a heavily loaded card. If there is message block exhaustion tracing will be suspended for a period and then automatically reenabled. An alarm is generated on tracing suspension and resumption. This mechanism protects the function processor against excessive numbers of tracing messages. Types of tracing include: protocolErrors - get details of any protocol errors which are occuring. Protocol errors are also reported in summary form as alarms. q931Summary - Summary of the Q.931 messages on the signalling link, including certain call details (calling number, called number, release codes). q931Hex - Q.931 messages displayed in hex format. Useful to determine protocol compliance in case of errors reported on local or remote ends. q931Symbolic - Q.931 messages parsed to give maximum detail. Useful for understanding content of messages flowing on the link. portHex - Messages in hex format being sent and received on the link. Description of bits: protocolErrors(0) q931Summary(1) q931Hex(2) q931Symbolic(3) portHex(4)')
dataSigChanInsFramer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2))
dataSigChanInsFramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1), )
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatusTable.setDescription('This entry controls the addition and deletion of dataSigChanInsFramer components.')
dataSigChanInsFramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatusEntry.setDescription('A single entry in the table represents a single dataSigChanInsFramer component.')
dataSigChanInsFramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerRowStatus.setDescription('This variable is used as the basis for SNMP naming of dataSigChanInsFramer components. These components cannot be added nor deleted.')
dataSigChanInsFramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
dataSigChanInsFramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerStorageType.setDescription('This variable represents the storage type value for the dataSigChanInsFramer tables.')
dataSigChanInsFramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: dataSigChanInsFramerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerIndex.setDescription('This variable represents the index for the dataSigChanInsFramer tables.')
dataSigChanInsFramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10), )
if mibBuilder.loadTexts: dataSigChanInsFramerProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerProvTable.setDescription('This group contains the base provisioning data for the Framer component. Application or hardware interface specific provisioning data is contained in other provisionable Framer groups.')
dataSigChanInsFramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: dataSigChanInsFramerProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerProvEntry.setDescription('An entry in the dataSigChanInsFramerProvTable.')
dataSigChanInsFramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataSigChanInsFramerInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerInterfaceName.setDescription("This attribute contains a hardware component name. The attribute associates the application with a specific link. This defines the module processor on which Framer's parent component (as well as Framer itself) will run.")
dataSigChanInsFramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12), )
if mibBuilder.loadTexts: dataSigChanInsFramerStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
dataSigChanInsFramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: dataSigChanInsFramerStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerStateEntry.setDescription('An entry in the dataSigChanInsFramerStateTable.')
dataSigChanInsFramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
dataSigChanInsFramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
dataSigChanInsFramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
dataSigChanInsFramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13), )
if mibBuilder.loadTexts: dataSigChanInsFramerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerStatsTable.setDescription('This group contains the operational statistics data for a Framer component.')
dataSigChanInsFramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-DataIsdnMIB", "dataSigChanIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsIndex"), (0, "Nortel-Magellan-Passport-DisdnJapanInsMIB", "dataSigChanInsFramerIndex"))
if mibBuilder.loadTexts: dataSigChanInsFramerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerStatsEntry.setDescription('An entry in the dataSigChanInsFramerStatsTable.')
dataSigChanInsFramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerFrmToIf.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerFrmToIf.setDescription('This attribute counts the number of frames transmitted to the link interface by Framer. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerFrmFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerFrmFromIf.setDescription('This attribute counts the number of frames received from the link interface by Framer. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerOctetFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerOctetFromIf.setDescription('The number of bytes received from the link interface by Framer.')
dataSigChanInsFramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerAborts.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerAborts.setDescription('This attribute counts the total number of aborts received. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerCrcErrors.setDescription('This attribute counts the total number of frames with CRC errors. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerLrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerLrcErrors.setDescription('This attribute counts the total number of frames with LRC errors. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerNonOctetErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerNonOctetErrors.setDescription('This attribute counts the total number of frames that were non octet aligned. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerOverruns.setDescription('This attribute counts the total number of frames received from the link for which overruns occurred. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerUnderruns.setDescription('This attribute counts the total number of frames transmitted to the link for which underruns occurred. This count wraps to zero after reaching its maximum value.')
dataSigChanInsFramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 120, 11, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dataSigChanInsFramerLargeFrmErrors.setStatus('mandatory')
if mibBuilder.loadTexts: dataSigChanInsFramerLargeFrmErrors.setDescription('This attribute counts the total number of frames received which were too large. The frame was longer than 500 bytes. This count wraps to zero after reaching its maximum value.')
disdnJapanInsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1))
disdnJapanInsGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5))
disdnJapanInsGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5, 1))
disdnJapanInsGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 1, 5, 1, 2))
disdnJapanInsCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3))
disdnJapanInsCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5))
disdnJapanInsCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5, 1))
disdnJapanInsCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 118, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-DisdnJapanInsMIB", dataSigChanInsFramerStateTable=dataSigChanInsFramerStateTable, dataSigChanInsSide=dataSigChanInsSide, dataSigChanInsDChanStatus=dataSigChanInsDChanStatus, dataSigChanInsT200=dataSigChanInsT200, dataSigChanInsTracing=dataSigChanInsTracing, dataSigChanInsProvEntry=dataSigChanInsProvEntry, dataSigChanInsFramerRowStatusTable=dataSigChanInsFramerRowStatusTable, disdnJapanInsCapabilitiesBE00A=disdnJapanInsCapabilitiesBE00A, dataSigChanInsFramerProvEntry=dataSigChanInsFramerProvEntry, dataSigChanInsComponentName=dataSigChanInsComponentName, dataSigChanInsFramerLargeFrmErrors=dataSigChanInsFramerLargeFrmErrors, dataSigChanInsN200=dataSigChanInsN200, dataSigChanInsFramerRowStatus=dataSigChanInsFramerRowStatus, dataSigChanInsFramerOverruns=dataSigChanInsFramerOverruns, disdnJapanInsGroup=disdnJapanInsGroup, dataSigChanInsT203=dataSigChanInsT203, disdnJapanInsGroupBE=disdnJapanInsGroupBE, dataSigChanInsFramerComponentName=dataSigChanInsFramerComponentName, dataSigChanInsFramerProvTable=dataSigChanInsFramerProvTable, dataSigChanInsL2Table=dataSigChanInsL2Table, dataSigChanInsToolsTable=dataSigChanInsToolsTable, dataSigChanInsToolsEntry=dataSigChanInsToolsEntry, dataSigChanInsFramerUsageState=dataSigChanInsFramerUsageState, dataSigChanInsFramerLrcErrors=dataSigChanInsFramerLrcErrors, dataSigChanInsFramerAdminState=dataSigChanInsFramerAdminState, dataSigChanInsFramerOperationalState=dataSigChanInsFramerOperationalState, dataSigChanInsRowStatus=dataSigChanInsRowStatus, dataSigChanInsFramerFrmToIf=dataSigChanInsFramerFrmToIf, dataSigChanInsFramerOctetFromIf=dataSigChanInsFramerOctetFromIf, dataSigChanInsFramerFrmFromIf=dataSigChanInsFramerFrmFromIf, dataSigChanInsFramerAborts=dataSigChanInsFramerAborts, dataSigChanInsFramerNonOctetErrors=dataSigChanInsFramerNonOctetErrors, dataSigChanInsActiveChannels=dataSigChanInsActiveChannels, dataSigChanInsFramerIndex=dataSigChanInsFramerIndex, dataSigChanInsFramerInterfaceName=dataSigChanInsFramerInterfaceName, dataSigChanInsN201=dataSigChanInsN201, dataSigChanInsFramerUnderruns=dataSigChanInsFramerUnderruns, dataSigChanInsFramerStatsTable=dataSigChanInsFramerStatsTable, disdnJapanInsGroupBE00=disdnJapanInsGroupBE00, disdnJapanInsGroupBE00A=disdnJapanInsGroupBE00A, dataSigChanInsT23=dataSigChanInsT23, dataSigChanInsFramerCrcErrors=dataSigChanInsFramerCrcErrors, dataSigChanInsCircuitSwitchedK=dataSigChanInsCircuitSwitchedK, dataSigChanInsFramer=dataSigChanInsFramer, disdnJapanInsCapabilitiesBE=disdnJapanInsCapabilitiesBE, dataSigChanInsL2Entry=dataSigChanInsL2Entry, dataSigChanInsFramerStatsEntry=dataSigChanInsFramerStatsEntry, disdnJapanInsCapabilities=disdnJapanInsCapabilities, dataSigChanInsStorageType=dataSigChanInsStorageType, dataSigChanInsFramerStorageType=dataSigChanInsFramerStorageType, dataSigChanInsIndex=dataSigChanInsIndex, disdnJapanInsCapabilitiesBE00=disdnJapanInsCapabilitiesBE00, dataSigChanInsPeakActiveChannels=dataSigChanInsPeakActiveChannels, dataSigChanInsRowStatusEntry=dataSigChanInsRowStatusEntry, dataSigChanInsFramerRowStatusEntry=dataSigChanInsFramerRowStatusEntry, dataSigChanInsRowStatusTable=dataSigChanInsRowStatusTable, dataSigChanInsOperTable=dataSigChanInsOperTable, dataSigChanInsFramerStateEntry=dataSigChanInsFramerStateEntry, dataSigChanIns=dataSigChanIns, dataSigChanInsOperEntry=dataSigChanInsOperEntry, disdnJapanInsMIB=disdnJapanInsMIB, dataSigChanInsProvTable=dataSigChanInsProvTable)
