#
# PySNMP MIB module CISCO-QUEUE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QUEUE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, ObjectIdentity, IpAddress, MibIdentifier, iso, Counter64, NotificationType, ModuleIdentity, Integer32, Counter32, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "Counter32", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoQueueMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 37))
ciscoQueueMIB.setRevisions(('1995-08-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQueueMIB.setRevisionsDescriptions(('Minor cleanups to pacify mib compiler.',))
if mibBuilder.loadTexts: ciscoQueueMIB.setLastUpdated('9505310000Z')
if mibBuilder.loadTexts: ciscoQueueMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQueueMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQueueMIB.setDescription('This is the MIB module for objects used to manage interface queuing in Cisco devices.')
ciscoQueueObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 1))
ciscoQueueTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 2))
ciscoQueueConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3))
class CQAlgorithm(TextualConvention, Integer32):
    description = 'The type of queuing algorithm used on the interface.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fifo", 1), ("priority", 2), ("custom", 3), ("weightedFair", 4))

cQIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1), )
if mibBuilder.loadTexts: cQIfTable.setStatus('current')
if mibBuilder.loadTexts: cQIfTable.setDescription("This table contains objects that describe the queues on a Cisco Interface. An interface queue is modeled as a collection of one or more secondary queues that feed into a device's hardware queue. The hardware queue has a maximum depth set by the MCI tx-queue-limit command or equivalent. The secondary queues (also known as the 'hold queue') have maximum depths set by the hold-queue command or equivalent. This table parallels the ifTable, and indicates the type of queuing in use on the interface, number of queues, and similar parameters.")
cQIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cQIfEntry.setStatus('current')
if mibBuilder.loadTexts: cQIfEntry.setDescription('A list of queue attributes for an interface.')
cQIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 1), CQAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfQType.setStatus('current')
if mibBuilder.loadTexts: cQIfQType.setDescription("The type of queuing used in the Hold Queue. First In First Out Queuing implies that the interface always transmits messages in the order that they are received. Priority Queuing sorts messages out by the use of access lists. Messages in a higher priority queue are always sent in preference to messages in a lower priority queue. Custom Queuing sorts messages out by the use of access lists. Sub-queues are selected in round robin order as either the sub-queue is drained or a given number of octets is moved from the sub-queue to the transmission queue. Weighted Fair Queuing sorts messages by 'conversation', which is source-destination pair of addresses and sockets or ports, as defined by the network layer protocol. Messages are removed from queues in a sequence that gives each conversation a proportion of the available bandwidth.")
cQIfTxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfTxLimit.setStatus('current')
if mibBuilder.loadTexts: cQIfTxLimit.setDescription('The maximum number of messages placed into the hardware transmission queue. This is a first come first serve queue, fed by the hold queue. If the hold queue contains information, this queue is presumably full.')
cQIfSubqueues = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQIfSubqueues.setStatus('current')
if mibBuilder.loadTexts: cQIfSubqueues.setDescription('The number of sub-queues of which the hold queue is built. This is a constant for each value of cQIfQType.')
cQStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2), )
if mibBuilder.loadTexts: cQStatsTable.setStatus('current')
if mibBuilder.loadTexts: cQStatsTable.setDescription('This table contains statistical objects that for the sub-queues of a Cisco Interface.')
cQStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQStatsEntry.setStatus('current')
if mibBuilder.loadTexts: cQStatsEntry.setDescription('A list of sub-queue attributes for an interface.')
cQStatsQNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cQStatsQNumber.setStatus('current')
if mibBuilder.loadTexts: cQStatsQNumber.setDescription('The number of the queue within the queue set. In FIFO queuing, this value is always 2. In Priority Queuing, it corresponds to the various priorities: high = 0 medium = 1 normal = 2 low = 3 In Custom Queuing, it is the queue number referenced in the access list. In Weighted Fair Queuing, it is the queue number associated with the traffic stream (conversation) identified.')
cQStatsDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDepth.setStatus('current')
if mibBuilder.loadTexts: cQStatsDepth.setDescription('The number of messages in the sub-queue.')
cQStatsMaxDepth = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsMaxDepth.setStatus('current')
if mibBuilder.loadTexts: cQStatsMaxDepth.setDescription('The maximum number of messages permitted in the sub-queue.')
cQStatsDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQStatsDiscards.setStatus('current')
if mibBuilder.loadTexts: cQStatsDiscards.setDescription('The number of messages discarded from this queue since restart by reason of enqueue at a time that cQStatsDepth >= cQStatsMaxDepth.')
cQRotationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3), )
if mibBuilder.loadTexts: cQRotationTable.setStatus('current')
if mibBuilder.loadTexts: cQRotationTable.setDescription('This table describes the rotation of Custom Queuing on an Interface.')
cQRotationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QUEUE-MIB", "cQStatsQNumber"))
if mibBuilder.loadTexts: cQRotationEntry.setStatus('current')
if mibBuilder.loadTexts: cQRotationEntry.setDescription('Custom Queuing sub-queue attributes for an interface.')
cQRotationOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 37, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cQRotationOctets.setStatus('current')
if mibBuilder.loadTexts: cQRotationOctets.setDescription('The number of octets which may be transmitted from a custom queuing sub-queue before it must yield to another queue.')
cQCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1))
cQGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2))
cQCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 1, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfGroup"), ("CISCO-QUEUE-MIB", "cQStatsGroup"), ("CISCO-QUEUE-MIB", "cQRotationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQCompliance = cQCompliance.setStatus('current')
if mibBuilder.loadTexts: cQCompliance.setDescription('The core compliance statement for all queued interfaces.')
cQIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 1)).setObjects(("CISCO-QUEUE-MIB", "cQIfQType"), ("CISCO-QUEUE-MIB", "cQIfTxLimit"), ("CISCO-QUEUE-MIB", "cQIfSubqueues"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQIfGroup = cQIfGroup.setStatus('current')
if mibBuilder.loadTexts: cQIfGroup.setDescription('The configuration of queuing on the interface. Interface Queuing statistics (ifOutQDepth and ifOutDiscards) are kept in the interface table.')
cQStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 2)).setObjects(("CISCO-QUEUE-MIB", "cQStatsDepth"), ("CISCO-QUEUE-MIB", "cQStatsMaxDepth"), ("CISCO-QUEUE-MIB", "cQStatsDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQStatsGroup = cQStatsGroup.setStatus('current')
if mibBuilder.loadTexts: cQStatsGroup.setDescription('The statistics for individual queues in the interface queuing system.')
cQRotationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 37, 3, 2, 3)).setObjects(("CISCO-QUEUE-MIB", "cQRotationOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cQRotationGroup = cQRotationGroup.setStatus('current')
if mibBuilder.loadTexts: cQRotationGroup.setDescription('The Custom Queuing queue rotation weights.')
mibBuilder.exportSymbols("CISCO-QUEUE-MIB", cQStatsDepth=cQStatsDepth, cQGroups=cQGroups, cQStatsDiscards=cQStatsDiscards, CQAlgorithm=CQAlgorithm, cQStatsTable=cQStatsTable, cQCompliances=cQCompliances, cQIfGroup=cQIfGroup, PYSNMP_MODULE_ID=ciscoQueueMIB, cQIfSubqueues=cQIfSubqueues, cQStatsGroup=cQStatsGroup, cQStatsQNumber=cQStatsQNumber, ciscoQueueMIB=ciscoQueueMIB, cQRotationEntry=cQRotationEntry, cQIfEntry=cQIfEntry, ciscoQueueConformance=ciscoQueueConformance, cQRotationGroup=cQRotationGroup, ciscoQueueTraps=ciscoQueueTraps, cQRotationOctets=cQRotationOctets, cQIfTxLimit=cQIfTxLimit, cQIfTable=cQIfTable, cQStatsMaxDepth=cQStatsMaxDepth, cQCompliance=cQCompliance, cQStatsEntry=cQStatsEntry, cQRotationTable=cQRotationTable, ciscoQueueObjects=ciscoQueueObjects, cQIfQType=cQIfQType)