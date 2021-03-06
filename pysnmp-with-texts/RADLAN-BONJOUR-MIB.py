#
# PySNMP MIB module RADLAN-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-BONJOUR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:45:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter32, IpAddress, NotificationType, iso, ObjectIdentity, Gauge32, Counter64, MibIdentifier, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter32", "IpAddress", "NotificationType", "iso", "ObjectIdentity", "Gauge32", "Counter64", "MibIdentifier", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 114))
rlBonjour.setRevisions(('2009-04-23 00:00', '2015-05-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlBonjour.setRevisionsDescriptions(('Initial revision.', 'Added fields rlBonjourStateIPv6OperationMode, rlBonjourStateIPv6OperationReason to rlBonjourStateEntry.',))
if mibBuilder.loadTexts: rlBonjour.setLastUpdated('201505120000Z')
if mibBuilder.loadTexts: rlBonjour.setOrganization('Marvell Computer Communications Ltd.')
if mibBuilder.loadTexts: rlBonjour.setContactInfo('marvell.com')
if mibBuilder.loadTexts: rlBonjour.setDescription('The private MIB module definition for Bonjour protocol.')
rlBonjourPublish = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourPublish.setStatus('current')
if mibBuilder.loadTexts: rlBonjourPublish.setDescription('Enables or disables Bonjour publishing.')
class RlBonjourServiceState(TextualConvention, Integer32):
    description = 'Bonjour service status - (per IP interface).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlBonjourNotPublished", 0), ("rlBonjourInactive", 1), ("rlBonjourRegistering", 2), ("rlBonjourRunning", 3))

class RlBonjourOperationState(TextualConvention, Integer32):
    description = 'Bonjour service an L2 interface operation state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class RlBonjourOperationReason(TextualConvention, Integer32):
    description = 'Bonjour service an L2 interface operation state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notExclude", 0), ("include", 1), ("notInclude", 2), ("exclude", 3), ("bonjourDisabled", 4), ("serviceDisabled", 5), ("noIPaddress", 6), ("l2InterfaceDown", 7), ("notPresent", 8), ("unknown", 9))

rlBonjourStatusTable = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 2), )
if mibBuilder.loadTexts: rlBonjourStatusTable.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusTable.setDescription('The table listing the service bonjour status per service and IP interface. In order to keep the table sorted according to the customary lexicographical order of the rlBonjourStatusServiceName strings, rlBonjourStatusServiceName will be padded with blanks. Bonjour will truncate the padded blanks when advertising this service name. Using this MIB user can monitor actual state of a service on an IP interface')
rlBonjourStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 2, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusServiceName"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusIPInterfaceType"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStatusIPInterfaceAddr"))
if mibBuilder.loadTexts: rlBonjourStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusEntry.setDescription(' An entry in the rlBonjourStatusEntry.')
rlBonjourStatusServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setDescription('This variable identifies the service name.')
rlBonjourStatusIPInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setDescription('This variable indicates the type of the IP interface on which the Bonjour service should be published.')
rlBonjourStatusIPInterfaceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setDescription('This variable indicates the address of the IP interface on which the Bonjour service should be published.')
rlBonjourStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 2, 1, 4), RlBonjourServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStatusState.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusState.setDescription('This variable identifies the service state on IP interface of the device.')
rlBonjourStateTable = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 3), )
if mibBuilder.loadTexts: rlBonjourStateTable.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateTable.setDescription("The table listing the service bonjour state per service and L2 interface. The services that are displayed here are only those who are supported per project. The L2 interfaces that are displayed here are either: L2 interfaces with an IP on it OR L2 interfaces listed in the table below Per each pair (service and L2 interface) table displays: state : UP - Bonjour published the service on this L2 interface Not-exclude - the L2 interface has IP address (L2 interface is in UP state) AND rlBonjourL2Table is empty AND rlBonjourL2Mode is disable include - the L2 interfaces are listed in the table rlBonjourL2Table AND rlBonjourL2Mode is enabled Down - Bonjour sent goodbye packets regarding this service on this L2 interface exclude - the L2 interface is a member of the rlBonjourL2Table AND rlBonjourL2Mode is disable Not-Include - rlBonjourL2Table is empty AND rlBonjourL2Mode is enable service disabled - service was removed due to specific request from L1 manager No IP address - the L2 interfaces is listed in the table rlBonjourL2EnableTable BUT don't have an IP on it Not-present - the L2 interfaces is listed in the table rlBonjourL2EnableTable BUT not yet defined (like vlan not created or port in an unconnected slave) Bonjour disabled - rlBonjourPublish scalar is off Using this MIB user can monitor actual state of a service on an L2 interface")
rlBonjourStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 3, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourStateServiceName"), (0, "RADLAN-BONJOUR-MIB", "rlBonjourStateL2Interface"))
if mibBuilder.loadTexts: rlBonjourStateEntry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateEntry.setDescription(' An entry in the rlBonjourStatusEntry.')
rlBonjourStateServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStateServiceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateServiceName.setDescription('This variable identifies the service name.')
rlBonjourStateL2Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setDescription('This variable indicates the L2 interface on which the Bonjour service should be published.')
rlBonjourStateOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 3), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setDescription('This variable indicates whether Bonjour over IPv4 is operational on the pair (service + L2 interface).')
rlBonjourStateOperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 4), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setDescription('This variable specifies the reason for the value of rlBonjourStateOperationMode.')
rlBonjourStateIPv6OperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 5), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationMode.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationMode.setDescription('This variable indicates whether Bonjour over IPv4 is operational on the pair (service + L2 interface).')
rlBonjourStateIPv6OperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 3, 1, 6), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationReason.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateIPv6OperationReason.setDescription('This variable specifies the reason for the value of rlBonjourStateIPv6OperationMode')
rlBonjourL2Table = MibTable((1, 3, 6, 1, 4, 1, 89, 114, 4), )
if mibBuilder.loadTexts: rlBonjourL2Table.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Table.setDescription("The table listing the L2 interfaces on which the user wishes to enable OR disable Bonjour with respect to rlBonjourL2Mode. If rlBonjourL2Mode is set to include AND L2 interface is in this table it does not ensure Bonjour WILL publish services on it. Publication is also dependent on these fundemental conditions: rlBonjourPublish must be on at least one service should be enabled L2 must be present and UP have at least one IP on it If this table is empty AND rlBonjourL2Mode is set to include Bonjour won't operate at all. If rlBonjourL2Mode is set to exclude, and rlBonjourL2Table is empty Bonjour will be published on ALL L2 interfaces answering to the fundemental conditions specified above. If rlBonjourL2Table is NOT empty then Bonjour will operate on ALL L2 interfaces answering to the fundemental conditions specified above BUT NOT members of this list. ")
rlBonjourL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 114, 4, 1), ).setIndexNames((0, "RADLAN-BONJOUR-MIB", "rlBonjourL2Ifindex"))
if mibBuilder.loadTexts: rlBonjourL2Entry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Entry.setDescription(' An entry in the rlBonjourL2Entry.')
rlBonjourL2Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setDescription('This variable identifies the L2 interface.')
rlBonjourL2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 114, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setDescription('This variable identifies the L2 interface status manager.')
rlBonjourL2Mode = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2Mode.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Mode.setDescription('specify whether the L2 interfaces listed in rlBonjourL2Table means include bonjour on these L2 interfaces once they: rlBonjourPublish must be on at least one service should be enabled L2 must be present and UP have at least one IP on it OR exclude bonjour on these L2 interfaces even if they answer to all the conditions above.')
rlBonjourInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourInstanceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourInstanceName.setDescription('Instance Name is given to Bonjour driver by the project part (L1Manager) When a conflict occurs: found another station with the same instance name. Bonjour driver is required to append _m to the given name while m is an incremental integer, increasing on each conflict')
rlBonjourHostName = MibScalar((1, 3, 6, 1, 4, 1, 89, 114, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourHostName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourHostName.setDescription('Host Name is given to Bonjour driver by the project part (L1Manager) When a conflict occurs: found another station with the same host name. Bonjour driver is required to append _m to the given name while m is an incremental integer, increasing on each conflict')
mibBuilder.exportSymbols("RADLAN-BONJOUR-MIB", rlBonjourStatusIPInterfaceType=rlBonjourStatusIPInterfaceType, rlBonjourL2Ifindex=rlBonjourL2Ifindex, rlBonjourL2Mode=rlBonjourL2Mode, RlBonjourOperationReason=RlBonjourOperationReason, rlBonjourStatusEntry=rlBonjourStatusEntry, rlBonjourHostName=rlBonjourHostName, rlBonjourStatusTable=rlBonjourStatusTable, rlBonjourStateTable=rlBonjourStateTable, rlBonjourL2Table=rlBonjourL2Table, rlBonjourPublish=rlBonjourPublish, rlBonjourL2RowStatus=rlBonjourL2RowStatus, rlBonjourStatusServiceName=rlBonjourStatusServiceName, rlBonjourInstanceName=rlBonjourInstanceName, rlBonjourStateEntry=rlBonjourStateEntry, rlBonjour=rlBonjour, rlBonjourStateIPv6OperationReason=rlBonjourStateIPv6OperationReason, rlBonjourStateOperationReason=rlBonjourStateOperationReason, rlBonjourStatusIPInterfaceAddr=rlBonjourStatusIPInterfaceAddr, rlBonjourStateL2Interface=rlBonjourStateL2Interface, PYSNMP_MODULE_ID=rlBonjour, rlBonjourStatusState=rlBonjourStatusState, rlBonjourStateOperationMode=rlBonjourStateOperationMode, RlBonjourServiceState=RlBonjourServiceState, RlBonjourOperationState=RlBonjourOperationState, rlBonjourStateIPv6OperationMode=rlBonjourStateIPv6OperationMode, rlBonjourL2Entry=rlBonjourL2Entry, rlBonjourStateServiceName=rlBonjourStateServiceName)
