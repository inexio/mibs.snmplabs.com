#
# PySNMP MIB module CISCO-OBMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-OBMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Gauge32, Unsigned32, ModuleIdentity, ObjectIdentity, NotificationType, TimeTicks, Counter64, IpAddress, iso, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "iso", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoObmiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 698))
ciscoObmiMIB.setRevisions(('2009-05-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoObmiMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoObmiMIB.setLastUpdated('200905280000Z')
if mibBuilder.loadTexts: ciscoObmiMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoObmiMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-obmi@cisco.com')
if mibBuilder.loadTexts: ciscoObmiMIB.setDescription("The On-Board Management Interface (OBMI) provides an out-of-band communications channel (in Cisco terms: a console port), that is capable of running on various low-speed to high-speed satellite telemetry busses, such as the m500 bus. OBMI is similar to SNMP in principle and function, in that it allows 'getting' data from or 'setting' configurations in a device, however, OBMI is functional regardless of the software state of the device. It must be so, because OBMI is the primary control mechanism for a device operating in the harsh environment of space. OBMI transports command messages that originate from the ground to a device in space and transports telemetry messages that originate from that device in space to the ground. The OBMI application is divided into three conceptual layers: 1. The OBMI application layer which concerns operating system subsystems and their associated command and telemetry messages. 2. A FRAMING layer which formats the OBMI messages into frames that are suitable for transport over a specific spacecraft bus. 3. The PHY (physical) layer which handles sending and receiving the frames over the physical media. Counts associated with the success or failure of these various transport layers are reported by this MIB. GLOSSARY command : data that goes from the ground to the device in space frame : OBMI messages are broken into frames to be sent by the physical bus or reassembled from the bus to be sent to the OBMI subsystem m500 : A particular space command/telemetry bus message : fully assembled set of frames that make up commands or telemetry. The topmost OBMI layer of the OBMI subsystem operates with messages OBMI : On-board Management Interface telemetry : data that goes from the device in space to the ground word : a collection of bits, sized for the particular bus ")
ciscoObmiMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 0))
ciscoObmiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 1))
ciscoObmiMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2))
cObmiTransportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2), )
if mibBuilder.loadTexts: cObmiTransportTable.setStatus('current')
if mibBuilder.loadTexts: cObmiTransportTable.setDescription('This table provides the statistics, in the form of counters associated with the transport of OBMI over one or more busses. At startup, all entries in this table are set up by the OBMI subsystem.')
cObmiTransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiTransportEntry.setStatus('current')
if mibBuilder.loadTexts: cObmiTransportEntry.setDescription('Each entry represents a row in cObmiTransportTable and corresponds to the statistics for a particular transport bus.')
cObmiBusID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: cObmiBusID.setStatus('current')
if mibBuilder.loadTexts: cObmiBusID.setDescription('This object uniquely indentifies a particular OBMI transport bus.')
cObmiBusName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiBusName.setStatus('current')
if mibBuilder.loadTexts: cObmiBusName.setDescription('This object indicates the name of the OBMI transport bus.')
cObmiCommandRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 3), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandRx.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandRx.setDescription('This object indicates the total number of commands received by the OBMI subsystem.')
cObmiCommandProcessedTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 4), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandProcessedTotal.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandProcessedTotal.setDescription('This object indicates the total number of commands successfully processed by the OBMI subsystem.')
cObmiCommandGets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 5), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandGets.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandGets.setDescription("This object indicates the total number of 'get' commands processed by the OBMI subsystem. A 'get' command requests information from the device that the OBMI subsystem resides on and is different from an SNMP 'get'.")
cObmiCommandSets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 6), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandSets.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandSets.setDescription("This object indicates the total number of 'set' commands processed by the OBMI subsystem. A 'set' command changes information ON the device that the OBMI subsystem resides on and is different from and SNMP 'set'.")
cObmiCommandProcessedInvalid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 7), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandProcessedInvalid.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandProcessedInvalid.setDescription('This object indicates the total number of commands that the OBMI subsystem interpreted as not fully conforming to the formatting requirements and therefore considered invalid.')
cObmiCommandPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 8), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandPending.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandPending.setDescription('This object indicates the total number of commands that are awaiting processing by the OBMI subsystem.')
cObmiCommandDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 9), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiCommandDropped.setStatus('current')
if mibBuilder.loadTexts: cObmiCommandDropped.setDescription('This object indicates the total number of commands that the OBMI subsystem did not recognize and therefore dropped.')
cObmiTelemetrySent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 10), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetrySent.setStatus('current')
if mibBuilder.loadTexts: cObmiTelemetrySent.setDescription('This object indicates the total count of telemetry messages that were sent by the OBMI subsystem.')
cObmiTelemetryDemandSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 11), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetryDemandSent.setStatus('current')
if mibBuilder.loadTexts: cObmiTelemetryDemandSent.setDescription("This object indicates the total count of telemetry messages that were sent by the OBMI subsystem, but only upon commanded 'gets' to the OBMI subsystem. This number excludes telemetry messages that were automatically sent by heartbeats.")
cObmiTelemetryPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 2, 1, 12), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiTelemetryPending.setStatus('current')
if mibBuilder.loadTexts: cObmiTelemetryPending.setDescription('This object indicates the total number of of telemetry messages waiting to be sent to the ground from the OBMI subsystem.')
cObmiTransportHeartBeatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3), )
if mibBuilder.loadTexts: cObmiTransportHeartBeatTable.setStatus('current')
if mibBuilder.loadTexts: cObmiTransportHeartBeatTable.setDescription('This table lists the number of heartbeats sent and the number pending by the OBMI subsystem by port number for a particular bus. At startup, all entries in this table are set up by the OBMI subsystem.')
cObmiTransportHeartBeatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"), (0, "CISCO-OBMI-MIB", "cObmiHeartBeatPort"))
if mibBuilder.loadTexts: cObmiTransportHeartBeatEntry.setStatus('current')
if mibBuilder.loadTexts: cObmiTransportHeartBeatEntry.setDescription('Each entry represents a row in cObmiTransportHearBeatTable and identifies heartbeat- related statistics.')
cObmiHeartBeatPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)))
if mibBuilder.loadTexts: cObmiHeartBeatPort.setStatus('current')
if mibBuilder.loadTexts: cObmiHeartBeatPort.setDescription('This object, along with cObmiBusID uniquely identifies heartbeat-related statistics.')
cObmiHeartBeatSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 2), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiHeartBeatSent.setStatus('current')
if mibBuilder.loadTexts: cObmiHeartBeatSent.setDescription('This object indicates the total number of hearbeats sent.')
cObmiHeartBeatPending = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 3, 1, 3), Gauge32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiHeartBeatPending.setStatus('current')
if mibBuilder.loadTexts: cObmiHeartBeatPending.setDescription('This object indicates the total number of heartbeats waiting in the queue ready to be sent.')
cObmiM500FramingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4), )
if mibBuilder.loadTexts: cObmiM500FramingTable.setStatus('current')
if mibBuilder.loadTexts: cObmiM500FramingTable.setDescription("This table lists the statistics associated with the 'framing-layer' of logical organization for the m500 bus used to transport OBMI. The frame size for m500 is 32 bits. At startup, all entries in this table are set up by the OBMI subsystem.")
cObmiM500FramingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiM500FramingEntry.setStatus('current')
if mibBuilder.loadTexts: cObmiM500FramingEntry.setDescription("Each entry represents an entry in the cObmiM500FramingTable and corresponds to the statistics associated with the framing for an 'm500' bus used to transport OBMI.")
cObmiM500RxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 1), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxFrames.setDescription('This object indicates the total number of m500 frames received.')
cObmiM500RxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 2), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxBytes.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxBytes.setDescription('This object indicates the total number of m500 bytes received.')
cObmiM500RxAbortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 3), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxAbortFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxAbortFrames.setDescription('This object indicates the total number of received m500 frames aborted.')
cObmiM500RxEchoFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 4), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxEchoFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxEchoFrames.setDescription('This object indicates the total number of m500 echo frames received.')
cObmiM500RxResetFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 5), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxResetFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxResetFrames.setDescription('This object indicates the total number of m500 reset frames received.')
cObmiM500RxTransportErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 6), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxTransportErrFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxTransportErrFrames.setDescription('This object indicates the total number of errored m500 transport frames received.')
cObmiM500RxUnknownOpFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 7), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxUnknownOpFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxUnknownOpFrames.setDescription('This object indicates the total number of m500 frames with unknown operation codes received.')
cObmiM500TxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 8), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxFrames.setDescription('This object indicates the total number of m500 frames transmitted.')
cObmiM500TxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 9), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxBytes.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxBytes.setDescription('This object indicates the total number of m500 bytes transmitted.')
cObmiM500TxAbortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 10), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxAbortFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxAbortFrames.setDescription('This object indicates the total number of aborted m500 frames transmitted.')
cObmiM500TxEchoFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 11), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxEchoFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxEchoFrames.setDescription('This object indicates the total number of m500 echo frames transmitted.')
cObmiM500TxTransportErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 12), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxTransportErrFrames.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxTransportErrFrames.setDescription('This object indicates the total number of m500 transport frames transmitted with error.')
cObmiM500RxQOverRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 13), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500RxQOverRun.setStatus('current')
if mibBuilder.loadTexts: cObmiM500RxQOverRun.setDescription('This object indicates the total number of control queue overruns transmitted.')
cObmiM500TxQ0UnderRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 14), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxQ0UnderRun.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxQ0UnderRun.setDescription('This object indicates the total number of underruns transmitted from queue number 0.')
cObmiM500TxQ1UnderRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 15), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxQ1UnderRun.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxQ1UnderRun.setDescription('This object indicates the total number of underruns transmitted from queue number 1.')
cObmiM500TxCtlQOverRun = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 4, 1, 16), Counter32()).setUnits('Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TxCtlQOverRun.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TxCtlQOverRun.setDescription('This object indicates the total number of transmit control queue overruns.')
cObmiM500PhyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5), )
if mibBuilder.loadTexts: cObmiM500PhyTable.setStatus('current')
if mibBuilder.loadTexts: cObmiM500PhyTable.setDescription("This table lists the statistics associated with the 'physical-layer' of logical organization for the m500 bus used to transport OBMI. At startup, all entries in this table are set up by the OBMI subsystem.")
cObmiM500PhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1), ).setIndexNames((0, "CISCO-OBMI-MIB", "cObmiBusID"))
if mibBuilder.loadTexts: cObmiM500PhyEntry.setStatus('current')
if mibBuilder.loadTexts: cObmiM500PhyEntry.setDescription("Each entry represents an entry in the cObmiM500PhyTable and corresponds to the statistics associated with the physical layer for an 'm500' bus used to transport OBMI. The size of a 'Word' for the m500 bus is 32-bits.")
cObmiM500BusALOS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500BusALOS.setStatus('current')
if mibBuilder.loadTexts: cObmiM500BusALOS.setDescription('This object indicates whether or not there is a loss of signal on m500 bus A. True : Loss of Signal on m500 bus A. False : No Loss of Signal on m500 bus A.')
cObmiM500BusBLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500BusBLOS.setStatus('current')
if mibBuilder.loadTexts: cObmiM500BusBLOS.setDescription('This object indicates whether or not there is a loss of signal on m500 bus B. True : Loss of Signal on m500 bus B. False : No Loss of Signal on m500 bus B.')
cObmiM500LastActiveBus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 3), Bits().clone(namedValues=NamedValues(("a", 0), ("b", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500LastActiveBus.setStatus('current')
if mibBuilder.loadTexts: cObmiM500LastActiveBus.setDescription('This object indicates which bus was last active: a : m500 bus A was last active b : m500 bus B was last active')
cObmiM500CommandsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 4), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandsRcvd.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandsRcvd.setDescription('This object indicates the total number of m500 command words received.')
cObmiM500TelemetrySent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 5), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetrySent.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TelemetrySent.setDescription('This object indicates the total number of m500 telemetry words sent.')
cObmiM500TelemetryErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 6), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetryErrs.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TelemetryErrs.setDescription('This object indicates the total number of m500 telemetry words with errors.')
cObmiM500CommandErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 7), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandErrs.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandErrs.setDescription('This object indicates the total number of m500 command words with errors.')
cObmiM500CommandOverWrts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 8), Counter32()).setUnits('Words').setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandOverWrts.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandOverWrts.setDescription('This object indicates the total number of m500 command words that were overwritten.')
cObmiM500HWParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500HWParityErr.setStatus('current')
if mibBuilder.loadTexts: cObmiM500HWParityErr.setDescription('This object indicates whether or not there was a hardwired parity error in the LAST command word received. True : Parity error occurred. False : No parity error occurred.')
cObmiM500TelemetryReqParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500TelemetryReqParityErr.setStatus('current')
if mibBuilder.loadTexts: cObmiM500TelemetryReqParityErr.setDescription('This object indicates whether or not there was a parity error in the LAST telemetry request word received. True : Parity error occurred. False : No parity error occurred.')
cObmiM500CommandParityErr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandParityErr.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandParityErr.setDescription('This object indicates whether or not there was a parity error in the LAST command word received. True : Parity error occurred. False : No parity error occurred.')
cObmiM500CommandTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandTimeout.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandTimeout.setDescription('This object indicates whether or not there was a timeout in receiving the LAST command word: True : Timeout occurred. False : Timeout did NOT occur.')
cObmiM500CommandOverWrt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 698, 1, 5, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cObmiM500CommandOverWrt.setStatus('current')
if mibBuilder.loadTexts: cObmiM500CommandOverWrt.setDescription('This object indicates whether or not the last command received was overwritten: True : Command received was overwritten. False : Command received was NOT overwritten.')
ciscoObmiMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1))
ciscoObmiMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2))
ciscoObmiMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 1, 1)).setObjects(("CISCO-OBMI-MIB", "ciscoObmiMIBMainObjectGroup"), ("CISCO-OBMI-MIB", "ciscoObmiMIBM500ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBCompliance = ciscoObmiMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoObmiMIBCompliance.setDescription('This is a default module-compliance containing default object groups.')
ciscoObmiMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 1)).setObjects(("CISCO-OBMI-MIB", "cObmiBusName"), ("CISCO-OBMI-MIB", "cObmiCommandRx"), ("CISCO-OBMI-MIB", "cObmiCommandProcessedTotal"), ("CISCO-OBMI-MIB", "cObmiCommandGets"), ("CISCO-OBMI-MIB", "cObmiCommandSets"), ("CISCO-OBMI-MIB", "cObmiCommandProcessedInvalid"), ("CISCO-OBMI-MIB", "cObmiCommandPending"), ("CISCO-OBMI-MIB", "cObmiCommandDropped"), ("CISCO-OBMI-MIB", "cObmiTelemetrySent"), ("CISCO-OBMI-MIB", "cObmiTelemetryDemandSent"), ("CISCO-OBMI-MIB", "cObmiTelemetryPending"), ("CISCO-OBMI-MIB", "cObmiHeartBeatSent"), ("CISCO-OBMI-MIB", "cObmiHeartBeatPending"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBMainObjectGroup = ciscoObmiMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoObmiMIBMainObjectGroup.setDescription('This is the list of objects required for OBMI.')
ciscoObmiMIBM500ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 698, 2, 2, 2)).setObjects(("CISCO-OBMI-MIB", "cObmiM500RxFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxBytes"), ("CISCO-OBMI-MIB", "cObmiM500RxAbortFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxEchoFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxResetFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxTransportErrFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxUnknownOpFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxBytes"), ("CISCO-OBMI-MIB", "cObmiM500TxAbortFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxEchoFrames"), ("CISCO-OBMI-MIB", "cObmiM500TxTransportErrFrames"), ("CISCO-OBMI-MIB", "cObmiM500RxQOverRun"), ("CISCO-OBMI-MIB", "cObmiM500TxQ0UnderRun"), ("CISCO-OBMI-MIB", "cObmiM500TxQ1UnderRun"), ("CISCO-OBMI-MIB", "cObmiM500TxCtlQOverRun"), ("CISCO-OBMI-MIB", "cObmiM500BusALOS"), ("CISCO-OBMI-MIB", "cObmiM500BusBLOS"), ("CISCO-OBMI-MIB", "cObmiM500LastActiveBus"), ("CISCO-OBMI-MIB", "cObmiM500CommandsRcvd"), ("CISCO-OBMI-MIB", "cObmiM500TelemetrySent"), ("CISCO-OBMI-MIB", "cObmiM500TelemetryErrs"), ("CISCO-OBMI-MIB", "cObmiM500CommandErrs"), ("CISCO-OBMI-MIB", "cObmiM500HWParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrts"), ("CISCO-OBMI-MIB", "cObmiM500TelemetryReqParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandParityErr"), ("CISCO-OBMI-MIB", "cObmiM500CommandTimeout"), ("CISCO-OBMI-MIB", "cObmiM500CommandOverWrt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoObmiMIBM500ObjectGroup = ciscoObmiMIBM500ObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoObmiMIBM500ObjectGroup.setDescription('This is the list of objects required for m500.')
mibBuilder.exportSymbols("CISCO-OBMI-MIB", cObmiHeartBeatPort=cObmiHeartBeatPort, cObmiM500TelemetrySent=cObmiM500TelemetrySent, ciscoObmiMIBGroups=ciscoObmiMIBGroups, cObmiM500CommandsRcvd=cObmiM500CommandsRcvd, cObmiM500TxAbortFrames=cObmiM500TxAbortFrames, cObmiCommandProcessedTotal=cObmiCommandProcessedTotal, cObmiM500TxEchoFrames=cObmiM500TxEchoFrames, cObmiM500TxQ0UnderRun=cObmiM500TxQ0UnderRun, ciscoObmiMIBMainObjectGroup=ciscoObmiMIBMainObjectGroup, cObmiM500FramingTable=cObmiM500FramingTable, cObmiTransportEntry=cObmiTransportEntry, cObmiM500RxAbortFrames=cObmiM500RxAbortFrames, cObmiM500TxFrames=cObmiM500TxFrames, cObmiM500TxBytes=cObmiM500TxBytes, ciscoObmiMIBConform=ciscoObmiMIBConform, cObmiM500CommandParityErr=cObmiM500CommandParityErr, cObmiM500TxCtlQOverRun=cObmiM500TxCtlQOverRun, cObmiHeartBeatSent=cObmiHeartBeatSent, cObmiTelemetryPending=cObmiTelemetryPending, cObmiCommandPending=cObmiCommandPending, cObmiCommandDropped=cObmiCommandDropped, PYSNMP_MODULE_ID=ciscoObmiMIB, cObmiTelemetrySent=cObmiTelemetrySent, cObmiM500RxFrames=cObmiM500RxFrames, cObmiBusID=cObmiBusID, cObmiM500CommandTimeout=cObmiM500CommandTimeout, ciscoObmiMIBCompliance=ciscoObmiMIBCompliance, cObmiCommandSets=cObmiCommandSets, cObmiM500LastActiveBus=cObmiM500LastActiveBus, cObmiCommandProcessedInvalid=cObmiCommandProcessedInvalid, cObmiTransportHeartBeatEntry=cObmiTransportHeartBeatEntry, ciscoObmiMIB=ciscoObmiMIB, cObmiTransportTable=cObmiTransportTable, cObmiM500RxUnknownOpFrames=cObmiM500RxUnknownOpFrames, cObmiM500TxTransportErrFrames=cObmiM500TxTransportErrFrames, cObmiM500TxQ1UnderRun=cObmiM500TxQ1UnderRun, cObmiTransportHeartBeatTable=cObmiTransportHeartBeatTable, cObmiM500RxTransportErrFrames=cObmiM500RxTransportErrFrames, cObmiM500CommandErrs=cObmiM500CommandErrs, cObmiM500TelemetryReqParityErr=cObmiM500TelemetryReqParityErr, cObmiTelemetryDemandSent=cObmiTelemetryDemandSent, cObmiCommandGets=cObmiCommandGets, cObmiM500HWParityErr=cObmiM500HWParityErr, cObmiM500BusBLOS=cObmiM500BusBLOS, cObmiM500PhyEntry=cObmiM500PhyEntry, cObmiCommandRx=cObmiCommandRx, cObmiM500PhyTable=cObmiM500PhyTable, cObmiBusName=cObmiBusName, ciscoObmiMIBCompliances=ciscoObmiMIBCompliances, cObmiM500RxResetFrames=cObmiM500RxResetFrames, cObmiM500RxBytes=cObmiM500RxBytes, cObmiM500FramingEntry=cObmiM500FramingEntry, ciscoObmiMIBNotifs=ciscoObmiMIBNotifs, cObmiM500CommandOverWrt=cObmiM500CommandOverWrt, cObmiM500TelemetryErrs=cObmiM500TelemetryErrs, ciscoObmiMIBM500ObjectGroup=ciscoObmiMIBM500ObjectGroup, cObmiHeartBeatPending=cObmiHeartBeatPending, cObmiM500CommandOverWrts=cObmiM500CommandOverWrts, ciscoObmiMIBObjects=ciscoObmiMIBObjects, cObmiM500RxQOverRun=cObmiM500RxQOverRun, cObmiM500BusALOS=cObmiM500BusALOS, cObmiM500RxEchoFrames=cObmiM500RxEchoFrames)
