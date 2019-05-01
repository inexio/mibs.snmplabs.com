#
# PySNMP MIB module CISCO-SAN-BASE-SVC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SAN-BASE-SVC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:11:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameId, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameId")
InterfaceIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifDescr")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, IpAddress, Gauge32, Counter32, MibIdentifier, Bits, Counter64, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Gauge32", "Counter32", "MibIdentifier", "Bits", "Counter64", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity")
TruthValue, RowStatus, TimeStamp, StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TimeStamp", "StorageType", "TextualConvention", "DisplayString")
ciscoSanBaseSvcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 702))
ciscoSanBaseSvcMIB.setRevisions(('2009-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSanBaseSvcMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: ciscoSanBaseSvcMIB.setLastUpdated('200906110000Z')
if mibBuilder.loadTexts: ciscoSanBaseSvcMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoSanBaseSvcMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoSanBaseSvcMIB.setDescription('Common MIB module to manage services in Storage Area Network (SAN). Service is deployed on service nodes on multiple switches forming a cluster. Nodes in the same cluster pick up the workload of a failed node to provide fault tolerance. An example of service that can be deployed is IO Acceleration (IOA) service. Glossary: The following terms are used in this MIB: pWWN: Port World Wide Name is a identifier assigned to a port in a Fibre Channel fabric. They perform a function equivalent to the MAC address in Ethernet protocol, as it is supposed to be unique identifier in the network. Nx_port: Nx_port is a storage port in Fibre Channel fabric that belongs to host or target.')
ciscoSanBaseSvcMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 0))
ciscoSanBaseSvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 1))
ciscoSanBaseSvcMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 2))
cSanBaseSvcConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1))
cSanBaseSvcInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2))
class CiscoSanBaseSvcInterfaceStatus(TextualConvention, Integer32):
    description = "Operational state of the service interface. 'unknown(1)' -- interface is in an unknown state 'initializing(2)' -- interface is being initialized 'offline(3)' -- interface is not active 'online(4)' -- interface is online and can be used"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("initializing", 2), ("offline", 3), ("online", 4))

class CiscoSanBaseSvcClusterStatus(TextualConvention, Integer32):
    description = "Operational state of the service cluster 'unknown(1)' -- cluster is in an unknown state 'inactive(2)' -- cluster is not active 'degraded(3)' -- cluster has lost some of its members 'recovery(4)' -- cluster is recovering from membership lost 'active(5)' -- cluster is active"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("inactive", 2), ("degraded", 3), ("recovery", 4), ("active", 5))

class CiscoSanBaseSvcClusterIndex(TextualConvention, OctetString):
    description = 'This denotes the globally unique index for a service cluster. The value of the CiscoSanBaseSvcClusterIndex is an eight-octet unsigned integer value encoded in a network-byte order.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

cSanBaseSvcClusterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1), )
if mibBuilder.loadTexts: cSanBaseSvcClusterTable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterTable.setDescription('This table lists all the service clusters that are configured on this device. It is important that any service is provided in a fault-tolerant manner. Base Service provides this by allowing service nodes to be grouped into cluster. Nodes in the same cluster immediately pick up the work of any failed node so user does not see service disruption.')
cSanBaseSvcClusterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"))
if mibBuilder.loadTexts: cSanBaseSvcClusterEntry.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterEntry.setDescription('A conceptual row in the cSanBaseSvcClusterTable. Each row represents a service cluster in the system and provides the runtime and configuration information of a cluster.')
cSanBaseSvcClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 1), CiscoSanBaseSvcClusterIndex())
if mibBuilder.loadTexts: cSanBaseSvcClusterId.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterId.setDescription('Globally unique index that identifies a service cluster. This index must be generated in such a way that the same value is never reused even after cluster has been deleted.')
cSanBaseSvcClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterName.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterName.setDescription('The name of the service cluster.')
cSanBaseSvcClusterState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 3), CiscoSanBaseSvcClusterStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterState.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterState.setDescription('The operational state of the service cluster.')
cSanBaseSvcClusterMasterInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterMasterInetAddrType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMasterInetAddrType.setDescription('The type of Internet address of the service cluster master. The Internet address of service cluster master is specified by the value of the corresponding instance of cSanBaseSvcClusterMasterInetAddr.')
cSanBaseSvcClusterMasterInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterMasterInetAddr.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMasterInetAddr.setDescription('The Internet address of the service cluster master device. The type of this Internet address is determined by the value of the corresponding instance of cSanBaseSvcClusterMasterInetAddrType.')
cSanBaseSvcClusterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterStorageType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterStorageType.setDescription('This object specifies the storage type for this conceptual row.')
cSanBaseSvcClusterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterRowStatus.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterRowStatus.setDescription('The status of this conceptual row. There is no restriction on the value of other columns before a newly created row can be made active.')
cSanBaseSvcClusterApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterApplication.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterApplication.setDescription('This object represents the name of the application that is enabled on this cluster.')
cSanBaseSvcClusterMembersTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2), )
if mibBuilder.loadTexts: cSanBaseSvcClusterMembersTable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMembersTable.setDescription('This table lists the information of devices, local or remote, which are members of a service cluster configured on a device.')
cSanBaseSvcClusterMembersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"), (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddrType"), (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddr"))
if mibBuilder.loadTexts: cSanBaseSvcClusterMembersEntry.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMembersEntry.setDescription('A conceptual row in the cSanBaseSvcClusterMembersTable. Each row represents a member device within a specified service Cluster.')
cSanBaseSvcClusterMemberInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberInetAddrType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberInetAddrType.setDescription('The type of Internet address of a cluster member within a specified service cluster. The Internet address of this device is specified by the value of the corresponding instance of cSanBaseSvcMemberInetAddr.')
cSanBaseSvcClusterMemberInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberInetAddr.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberInetAddr.setDescription('The Internet address of the cluster member device within a specified service cluster. The type of this Internet address is determined by the value of the corresponding instance of cSanBaseSvcClusterMemberInetAddrType.')
cSanBaseSvcClusterMemberFabric = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberFabric.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberFabric.setDescription('This object represents the name of the physical fibre channel fabric in the SAN. A typical SAN deployment consists of a dual fabric topology which corresponds to two physical fabrics. In such a deployment, a cluster is configured in both fabrics to allow multi-pathing and redundancy. The user specifies the physical fabric to which a device belongs to when the cluster is configured.')
cSanBaseSvcClusterMemberIsLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIsLocal.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIsLocal.setDescription("Identifies if the device is a local or remote member of this cluster. 'true' means this device is a local device. 'false' means this device is a remote device.")
cSanBaseSvcClusterMemberIsMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIsMaster.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIsMaster.setDescription("Indicates if this device is currently the master of the service cluster. The value 'true' means this device is the master. The value 'false' means this device is not the master. Devices in a cluster select one of the cluster member to be a master. The master is responsible for handling cluster membership.")
cSanBaseSvcClusterMemberStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberStorageType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberStorageType.setDescription('This object specifies the storage type for this conceptual row.')
cSanBaseSvcClusterMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberRowStatus.setDescription('The status of this conceptual row. There is no restriction on the value of other columns before a newly created row can be made active. When a cluster is deleted, all entries in this table should be purged automatically.')
cSanBaseSvcInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3), )
if mibBuilder.loadTexts: cSanBaseSvcInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceTable.setDescription('This table lists all service interfaces on the local device and its corresponding information.')
cSanBaseSvcInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceIndex"))
if mibBuilder.loadTexts: cSanBaseSvcInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceEntry.setDescription('A conceptual row in the cSanBaseSvcInterfaceTable. Each row represents a particular service interface on a local device.')
cSanBaseSvcInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cSanBaseSvcInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceIndex.setDescription('A unique Interface index for a service interface on this device. This is the same as ifIndex of the ifTable of RFC1213.')
cSanBaseSvcInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 2), CiscoSanBaseSvcInterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcInterfaceState.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceState.setDescription('Operational state of this service interface.')
cSanBaseSvcInterfaceClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 3), CiscoSanBaseSvcClusterIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcInterfaceClusterId.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceClusterId.setDescription('Identifies the cluster to which this service interface belongs.')
cSanBaseSvcInterfaceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcInterfaceStorageType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceStorageType.setDescription('This object specifies the storage type for this conceptual row.')
cSanBaseSvcInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcInterfaceRowStatus.setDescription('The status of this conceptual row. There is no restriction on the value of other columns before a newly created row can be made active. For example, cSanBaseSvcInterfaceClusterId column can be set independently later.')
cSanBaseSvcDevicePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4), )
if mibBuilder.loadTexts: cSanBaseSvcDevicePortTable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortTable.setDescription('This table lists the devices that are configured to receive storage service.')
cSanBaseSvcDevicePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortName"))
if mibBuilder.loadTexts: cSanBaseSvcDevicePortEntry.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortEntry.setDescription('A conceptual row in the cSanBaseSvcDevicePortTable. Each row represents a particular device configured to receive storage service in a particular cluster.')
cSanBaseSvcDevicePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 1), FcNameId())
if mibBuilder.loadTexts: cSanBaseSvcDevicePortName.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortName.setDescription('This object represents Fibre-channel Port name (pWWN) of the Device Nx_Port.')
cSanBaseSvcDevicePortClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 2), CiscoSanBaseSvcClusterIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcDevicePortClusterId.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortClusterId.setDescription('This object represents the cluster identifier of the cluster to which this port belongs.')
cSanBaseSvcDevicePortStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 3), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcDevicePortStorageType.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortStorageType.setDescription('This object specifies the storage type for this conceptual row.')
cSanBaseSvcDevicePortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cSanBaseSvcDevicePortRowStatus.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortRowStatus.setDescription('The status of this conceptual row. There is no restriction on the value of other columns before a newly created row can be made active.')
cSanBaseSvcConfigTableLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcConfigTableLastChanged.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcConfigTableLastChanged.setDescription('The value of sysUpTime when a change to any Base Service MIB table other than the cSanBaseSvcDevicePortTable last occurred.')
cSanBaseSvcDevicePortTableLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcDevicePortTableLastChanged.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcDevicePortTableLastChanged.setDescription('The value of sysUpTime when a change to cSanBaseSvcDevicePortTable last occurred.')
cSanBaseSvcNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cSanBaseSvcNotifyEnable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcNotifyEnable.setDescription("This object specifies if the service notifications should be generated or not. If the value of this object is 'true', then the notifications are generated. If the value of this object is 'false', then the notifications are not generated.")
cSanBaseSvcClusterMemberIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1), )
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIfTable.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIfTable.setDescription('This table lists the information of service interfaces on all devices, local or remote, which are members of a service cluster configured on a device.')
cSanBaseSvcClusterMemberIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterId"), (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddrType"), (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberInetAddr"), (0, "CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterInterfaceIndex"))
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIfEntry.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterMemberIfEntry.setDescription('A conceptual row in the cSanBaseSvcClusterMemberIfTable. Each row represents a participating interface on local/remote device member within the specified service cluster.')
cSanBaseSvcClusterInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: cSanBaseSvcClusterInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterInterfaceIndex.setDescription('A unique Interface index for a service interface on a device in this cluster. This is the same as ifIndex of the ifTable of RFC1213.')
cSanBaseSvcClusterInterfaceState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 702, 1, 2, 1, 1, 2), CiscoSanBaseSvcInterfaceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cSanBaseSvcClusterInterfaceState.setStatus('current')
if mibBuilder.loadTexts: cSanBaseSvcClusterInterfaceState.setDescription('The operational state of this service interface.')
ciscoSanBaseSvcInterfaceCreate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 1)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: ciscoSanBaseSvcInterfaceCreate.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcInterfaceCreate.setDescription('This notification is generated when a service interface associated with a local device is created. The generation of this notification is controlled by cSanBaseSvcNotifyEnable')
ciscoSanBaseSvcInterfaceDelete = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 2)).setObjects(("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: ciscoSanBaseSvcInterfaceDelete.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcInterfaceDelete.setDescription('This notification is generated when a service interface associated with a local device is deleted. The generation of this notification is controlled by cSanBaseSvcNotifyEnable')
ciscoSanBaseSvcClusterNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 702, 0, 3)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterName"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddrType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddr"))
if mibBuilder.loadTexts: ciscoSanBaseSvcClusterNewMaster.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcClusterNewMaster.setDescription('This notification is generated when the sending device who is participating in a service cluster has transitioned to be the master of the cluster. The generation of this notification is controlled by cSanBaseSvcNotifyEnable')
ciscoSanBaseSvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 1))
ciscoSanBaseSvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2))
ciscoSanBaseSvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 1, 1)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcConfigGroup"), ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcNotifControlGroup"), ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcNotifsGroup"), ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSanBaseSvcMIBCompliance = ciscoSanBaseSvcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcMIBCompliance.setDescription('The compliance statement for entities that implement this base service.')
ciscoSanBaseSvcConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 1)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterState"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddrType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMasterInetAddr"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberIsLocal"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceState"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceClusterId"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortClusterId"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcConfigTableLastChanged"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberFabric"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterName"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceRowStatus"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterRowStatus"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberIsMaster"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberRowStatus"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterStorageType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterMemberStorageType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcInterfaceStorageType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortStorageType"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortRowStatus"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterApplication"), ("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcDevicePortTableLastChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSanBaseSvcConfigGroup = ciscoSanBaseSvcConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcConfigGroup.setDescription('A collection of objects for storage service configuration.')
ciscoSanBaseSvcNotifControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 2)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSanBaseSvcNotifControlGroup = ciscoSanBaseSvcNotifControlGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcNotifControlGroup.setDescription('A collection of objects for controlling storage service notification.')
ciscoSanBaseSvcNotifsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 3)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcInterfaceCreate"), ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcInterfaceDelete"), ("CISCO-SAN-BASE-SVC-MIB", "ciscoSanBaseSvcClusterNewMaster"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSanBaseSvcNotifsGroup = ciscoSanBaseSvcNotifsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcNotifsGroup.setDescription('A collection of objects for notification of storage service events.')
ciscoSanBaseSvcInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 702, 2, 2, 4)).setObjects(("CISCO-SAN-BASE-SVC-MIB", "cSanBaseSvcClusterInterfaceState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSanBaseSvcInterfaceGroup = ciscoSanBaseSvcInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSanBaseSvcInterfaceGroup.setDescription('A collection of storage service interface.')
mibBuilder.exportSymbols("CISCO-SAN-BASE-SVC-MIB", cSanBaseSvcClusterMasterInetAddrType=cSanBaseSvcClusterMasterInetAddrType, cSanBaseSvcDevicePortClusterId=cSanBaseSvcDevicePortClusterId, cSanBaseSvcClusterEntry=cSanBaseSvcClusterEntry, ciscoSanBaseSvcMIBObjects=ciscoSanBaseSvcMIBObjects, ciscoSanBaseSvcNotifsGroup=ciscoSanBaseSvcNotifsGroup, cSanBaseSvcInterfaceRowStatus=cSanBaseSvcInterfaceRowStatus, cSanBaseSvcDevicePortStorageType=cSanBaseSvcDevicePortStorageType, cSanBaseSvcConfigTableLastChanged=cSanBaseSvcConfigTableLastChanged, cSanBaseSvcInterfaceState=cSanBaseSvcInterfaceState, cSanBaseSvcClusterTable=cSanBaseSvcClusterTable, cSanBaseSvcClusterMemberIsMaster=cSanBaseSvcClusterMemberIsMaster, cSanBaseSvcInterfaceStorageType=cSanBaseSvcInterfaceStorageType, cSanBaseSvcInterfaceIndex=cSanBaseSvcInterfaceIndex, ciscoSanBaseSvcMIBGroups=ciscoSanBaseSvcMIBGroups, ciscoSanBaseSvcMIBCompliance=ciscoSanBaseSvcMIBCompliance, cSanBaseSvcClusterMemberInetAddrType=cSanBaseSvcClusterMemberInetAddrType, CiscoSanBaseSvcClusterIndex=CiscoSanBaseSvcClusterIndex, cSanBaseSvcClusterState=cSanBaseSvcClusterState, cSanBaseSvcConfig=cSanBaseSvcConfig, cSanBaseSvcClusterInterfaceState=cSanBaseSvcClusterInterfaceState, ciscoSanBaseSvcClusterNewMaster=ciscoSanBaseSvcClusterNewMaster, cSanBaseSvcClusterName=cSanBaseSvcClusterName, cSanBaseSvcClusterRowStatus=cSanBaseSvcClusterRowStatus, cSanBaseSvcInterfaceEntry=cSanBaseSvcInterfaceEntry, ciscoSanBaseSvcMIBNotifs=ciscoSanBaseSvcMIBNotifs, cSanBaseSvcDevicePortTableLastChanged=cSanBaseSvcDevicePortTableLastChanged, cSanBaseSvcClusterMembersTable=cSanBaseSvcClusterMembersTable, cSanBaseSvcClusterMemberStorageType=cSanBaseSvcClusterMemberStorageType, cSanBaseSvcInterfaceClusterId=cSanBaseSvcInterfaceClusterId, cSanBaseSvcClusterMemberIsLocal=cSanBaseSvcClusterMemberIsLocal, cSanBaseSvcNotifyEnable=cSanBaseSvcNotifyEnable, ciscoSanBaseSvcInterfaceDelete=ciscoSanBaseSvcInterfaceDelete, ciscoSanBaseSvcNotifControlGroup=ciscoSanBaseSvcNotifControlGroup, cSanBaseSvcClusterMemberIfEntry=cSanBaseSvcClusterMemberIfEntry, ciscoSanBaseSvcInterfaceGroup=ciscoSanBaseSvcInterfaceGroup, ciscoSanBaseSvcConfigGroup=ciscoSanBaseSvcConfigGroup, cSanBaseSvcClusterMasterInetAddr=cSanBaseSvcClusterMasterInetAddr, ciscoSanBaseSvcMIB=ciscoSanBaseSvcMIB, cSanBaseSvcInterfaceTable=cSanBaseSvcInterfaceTable, cSanBaseSvcInterface=cSanBaseSvcInterface, ciscoSanBaseSvcInterfaceCreate=ciscoSanBaseSvcInterfaceCreate, ciscoSanBaseSvcMIBConform=ciscoSanBaseSvcMIBConform, cSanBaseSvcClusterStorageType=cSanBaseSvcClusterStorageType, CiscoSanBaseSvcInterfaceStatus=CiscoSanBaseSvcInterfaceStatus, PYSNMP_MODULE_ID=ciscoSanBaseSvcMIB, cSanBaseSvcClusterApplication=cSanBaseSvcClusterApplication, CiscoSanBaseSvcClusterStatus=CiscoSanBaseSvcClusterStatus, cSanBaseSvcClusterMemberFabric=cSanBaseSvcClusterMemberFabric, cSanBaseSvcClusterMemberIfTable=cSanBaseSvcClusterMemberIfTable, cSanBaseSvcClusterInterfaceIndex=cSanBaseSvcClusterInterfaceIndex, cSanBaseSvcClusterMembersEntry=cSanBaseSvcClusterMembersEntry, cSanBaseSvcDevicePortTable=cSanBaseSvcDevicePortTable, ciscoSanBaseSvcMIBCompliances=ciscoSanBaseSvcMIBCompliances, cSanBaseSvcClusterId=cSanBaseSvcClusterId, cSanBaseSvcClusterMemberInetAddr=cSanBaseSvcClusterMemberInetAddr, cSanBaseSvcDevicePortEntry=cSanBaseSvcDevicePortEntry, cSanBaseSvcClusterMemberRowStatus=cSanBaseSvcClusterMemberRowStatus, cSanBaseSvcDevicePortName=cSanBaseSvcDevicePortName, cSanBaseSvcDevicePortRowStatus=cSanBaseSvcDevicePortRowStatus)
