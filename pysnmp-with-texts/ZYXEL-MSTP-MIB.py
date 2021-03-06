#
# PySNMP MIB module ZYXEL-MSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MSTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dot1dBasePort, BridgeId, Timeout = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "BridgeId", "Timeout")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, ModuleIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, Counter64, IpAddress, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ModuleIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "Counter64", "IpAddress", "TimeTicks", "ObjectIdentity", "MibIdentifier")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMstp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53))
if mibBuilder.loadTexts: zyxelMstp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMstp.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelMstp.setContactInfo('')
if mibBuilder.loadTexts: zyxelMstp.setDescription('The subtree for Multiple Spanning Tree Protocol (MSTP)')
zyxelMstpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1))
zyxelMstpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2))
zyxelMstpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3))
class MstiOrCistInstanceIndex(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the MstiInstanceIndex convention. This extension permits the additional value of zero, which means Common and Internal Spanning Tree (CIST).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

zyxelMstpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1))
zyMstpGeneralState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralState.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralState.setDescription('Enable/Disable MSTP on the switch.')
zyMstpGeneralConfigIdName = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralConfigIdName.setReference('(12.12.3.4.2.b)')
if mibBuilder.loadTexts: zyMstpGeneralConfigIdName.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralConfigIdName.setDescription('The configuration name that identifies the MST region and is used as one of the inputs in the computation of the MST Configuration Identifier.')
zyMstpGeneralConfigIdRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralConfigIdRevisionLevel.setReference('(12.12.3.4.2.c)')
if mibBuilder.loadTexts: zyMstpGeneralConfigIdRevisionLevel.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralConfigIdRevisionLevel.setDescription('This object identifies the MST revision that identifies the MST region and is used as one of the inputs in the computation of the MST configuration Identifier.')
zyMstpGeneralHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 4), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralHelloTime.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralHelloTime.setDescription('The time interval in seconds between BPDU configuration message generations by the root switch. The allowed range is 1 to 10 seconds.')
zyMstpGeneralMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 5), Timeout().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralMaxAge.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralMaxAge.setDescription('This is the maximum time (in seconds) the switch can wait without receiving a BPDU before attempting to reconfigure')
zyMstpGeneralForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 6), Timeout().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralForwardDelay.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralForwardDelay.setDescription('This is the maximum time (in seconds) the switch will wait before changing states. This delay is required because every switch must receive information about topology changes before it starts to forward frames.')
zyMstpGeneralMaxHops = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpGeneralMaxHops.setStatus('current')
if mibBuilder.loadTexts: zyMstpGeneralMaxHops.setDescription('The number of hops (between 1 and 255) in an MSTP region before the BPDU is discarded and the port information is aged.')
zyMstpVlanMapMaxNumberOfInstances = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpVlanMapMaxNumberOfInstances.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapMaxNumberOfInstances.setDescription('The maximum number of MSTP VLAN instances that can be created.')
zyxelMstpVlanMapTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3), )
if mibBuilder.loadTexts: zyxelMstpVlanMapTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpVlanMapTable.setDescription('The table contains MSTP VLAN map configuration.')
zyxelMstpVlanMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpVlanMapInstance"))
if mibBuilder.loadTexts: zyxelMstpVlanMapEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpVlanMapEntry.setDescription('An entry contains MSTP VLAN map configuration. ')
zyMstpVlanMapInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 1), MstiOrCistInstanceIndex())
if mibBuilder.loadTexts: zyMstpVlanMapInstance.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapInstance.setDescription('Uniquely identifies an instance. The entry of this table with index 0 presents always, represents CIST. When SET operation ')
zyMstpVlanMapVlans1k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpVlanMapVlans1k.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapVlans1k.setDescription("A string of octets containing one bit per VLAN. The first octet corresponds to VLANs with VlanIndex values 1 through 8; the second octet to VLANs 9 through 16 etc. The most significant bit of each octet corresponds to the lowest VlanIndex value in that octet. For each VLAN that is mapped to this MSTP instance, the bit corresponding to that VLAN is set to '1'. Empty (zero) most significant octes are not mandatory.")
zyMstpVlanMapVlans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpVlanMapVlans2k.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapVlans2k.setDescription("A string of octets containing one bit per VLAN for VLANS with VlanIndex values 1024 through 2047. The first octet corresponds to VLANs with VlanIndex values 1024 through 1031; the second octet to VLANs 1032 through 1039 etc. The most significant bit of each octet corresponds to the lowest VlanIndex value in that octet. For each VLAN that is mapped to this MSTP instance, the bit corresponding to that VLAN is set to '1'. Empty (zero) most significant octes are not mandatory.")
zyMstpVlanMapVlans3k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpVlanMapVlans3k.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapVlans3k.setDescription("A string of octets containing one bit per VLAN for VLANS with VlanIndex values 2048 through 3071. The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063 etc. The most significant bit of each octet corresponds to the lowest VlanIndex value in that octet. For each VLAN that is mapped to this MSTP instance, the bit corresponding to that VLAN is set to '1'. Empty (zero) most significant octes are not mandatory.")
zyMstpVlanMapVlans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpVlanMapVlans4k.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapVlans4k.setDescription("A string of octets containing one bit per VLAN for VLANS with VlanIndex values 3072 through 4095. The first octet corresponds to VLANs with VlanIndex values 3072 through 3079; the second octet to VLANs 3080 through 3087 etc. The most significant bit of each octet corresponds to the lowest VlanIndex value in that octet. For each VLAN that is mapped to this MSTP instance, the bit corresponding to that VLAN is set to '1'. Empty (zero) most significant octes are not mandatory.")
zyMstpVlanMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyMstpVlanMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyMstpVlanMapRowStatus.setDescription('This object allow entries to be created and deleted from the MSTP VLAN map table.')
zyxelMstpPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4), )
if mibBuilder.loadTexts: zyxelMstpPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpPortTable.setDescription('The table contains MSTP port configuration.')
zyxelMstpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMstpPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpPortEntry.setDescription('An entry contains MSTP port configuration. ')
zyMstpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpPortAdminEdgePort.setStatus('current')
if mibBuilder.loadTexts: zyMstpPortAdminEdgePort.setDescription('The administrative value of the Edge Port parameter. A value of true(1) indicates that this port should be assumed as an edge-port, and a value of false(2) indicates that this port should be assumed as a non-edge-port. ')
zyxelMstpInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5), )
if mibBuilder.loadTexts: zyxelMstpInstanceTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInstanceTable.setDescription('The table contains MSTP instance configuration.')
zyxelMstpInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpInstanceId"))
if mibBuilder.loadTexts: zyxelMstpInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInstanceEntry.setDescription('An entry contains MSTP instance configuration. ')
zyMstpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1, 1), MstiOrCistInstanceIndex())
if mibBuilder.loadTexts: zyMstpInstanceId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstanceId.setDescription('The number you want to use to identify this MST instance on the switch. 0 means CIST.')
zyMstpInstanceBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440)).clone(32768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpInstanceBridgePriority.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstanceBridgePriority.setDescription('priority of the switch for the specific spanning tree instance. The lower the number , the more likely the switch will be chosen as the root bridge within the spanning tree instance. In steps of 4096.')
zyxelMstpInstancePortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6), )
if mibBuilder.loadTexts: zyxelMstpInstancePortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInstancePortTable.setDescription('The table contains MSTP instance port configuration.')
zyxelMstpInstancePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpInstancePortInstanceId"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMstpInstancePortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInstancePortEntry.setDescription('An entry contains MSTP instance port configuration. ')
zyMstpInstancePortInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 1), MstiOrCistInstanceIndex())
if mibBuilder.loadTexts: zyMstpInstancePortInstanceId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstancePortInstanceId.setDescription('The number you want to use to identify this MST instance on the switch. 0 means CIST.')
zyMstpInstancePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpInstancePortState.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstancePortState.setDescription('Enable/Disable this port to the MST instance.')
zyMstpInstancePortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpInstancePortPriority.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstancePortPriority.setDescription('Port priority. Priority decides which port should be disable when more than one port forms a loop in a switch. Ports with a higher priority numeric value are disabled first. In steps of 16.')
zyMstpInstancePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpInstancePortPathCost.setStatus('current')
if mibBuilder.loadTexts: zyMstpInstancePortPathCost.setDescription('The cost of transmitting a frame on to a LAN through that port.')
zyxelMstpInfoGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1))
zyMstpInfoGeneralConfigIdName = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdName.setReference('12.12.3.4.2.b)')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdName.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdName.setDescription('The configuration name that identifies the MST region and is used as one of the inputs in the computation of the MST Configuration Identifier.')
zyMstpInfoGeneralConfigIdRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdRevisionLevel.setReference('12.12.3.4.2.c)')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdRevisionLevel.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdRevisionLevel.setDescription('This object identifies the MST revision that identifies the MST region and is used as one of the inputs in the computation of the MST configuration Identifier.')
zyMstpInfoGeneralConfigIdConfigDigest = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdConfigDigest.setReference('12.12.3.3.3.a.4')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdConfigDigest.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralConfigIdConfigDigest.setDescription('A configuration digest is generated from the VLAN-MSTI mapping information. This field displays the 16-octet signature that is included in an MSTP BPDU. This field displays the digest when MSTP is activated on the system. ')
zyMstpInfoGeneralHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 4), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralHelloTime.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralHelloTime.setDescription('The time interval in seconds between BPDU configuration message generations by the root switch.')
zyMstpInfoGeneralMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 5), Timeout().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralMaxAge.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralMaxAge.setDescription('This is the maximum time (in seconds) the switch can wait without receiving a BPDU before attempting to reconfigure')
zyMstpInfoGeneralForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 6), Timeout().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMstpInfoGeneralForwardDelay.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralForwardDelay.setDescription('This is the maximum time (in seconds) the switch will wait before changing states. This delay is required because every switch must receive information about topology changes before it starts to forward frames.')
zyMstpInfoGeneralCistRootPathCost = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralCistRootPathCost.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralCistRootPathCost.setDescription('This is the path cost from the root port on this switch to the root switch.')
zyMstpInfoGeneralCistRootBridgeId = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoGeneralCistRootBridgeId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoGeneralCistRootBridgeId.setDescription('This is the path cost from the root port on this switch to the root switch.')
zyxelMstpInfoVlanMapTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2), )
if mibBuilder.loadTexts: zyxelMstpInfoVlanMapTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoVlanMapTable.setDescription('The table contains MSTP VLAN map information.')
zyxelMstpInfoVlanMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpInfoVlanMapVid"))
if mibBuilder.loadTexts: zyxelMstpInfoVlanMapEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoVlanMapEntry.setDescription('An entry contains MSTP VLAN map information.')
zyMstpInfoVlanMapVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyMstpInfoVlanMapVid.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoVlanMapVid.setDescription('The VLAN ID for which this entry contains the instance mapped.')
zyMstpInfoVlanMapInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1, 2), MstiOrCistInstanceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoVlanMapInstance.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoVlanMapInstance.setDescription('An integer with values ranging from 0 to 64 that identify a the CIST/MSTI instance to which this VLAN is mapped')
zyxelMstpInfoPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3), )
if mibBuilder.loadTexts: zyxelMstpInfoPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoPortTable.setDescription('The table contains MSTP VLAN map information.')
zyxelMstpInfoPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMstpInfoPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoPortEntry.setDescription('An entry contains MSTP VLAN map information.')
zyMstpInfoPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoPortOperEdgePort.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoPortOperEdgePort.setDescription('The operational value of the Edge Port parameter. The object is initialized to the value of the corresponding instance of zyxelMstpPortAdminEdgePort. When the corresponding instance of zyxelMstpPortAdminEdgePort is set, this object will be changed as well. This object will also be changed to false on reception of a BPDU.')
zyMstpInfoPortOperPointToPointMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoPortOperPointToPointMAC.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoPortOperPointToPointMAC.setDescription('The port is operationally connected to a point-to-point link.')
zyxelMstpInfoInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4), )
if mibBuilder.loadTexts: zyxelMstpInfoInstanceTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoInstanceTable.setDescription('The table contains MSTP instance information.')
zyxelMstpInfoInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpInfoInstanceId"))
if mibBuilder.loadTexts: zyxelMstpInfoInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoInstanceEntry.setDescription('An entry contains MSTP instance information.')
zyMstpInfoInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 1), MstiOrCistInstanceIndex())
if mibBuilder.loadTexts: zyMstpInfoInstanceId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceId.setDescription('the number you want to use to identify this MST instance on the switch. 0 means CIST.')
zyMstpInfoInstanceBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 2), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstanceBridgeId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceBridgeId.setDescription('this is the unique identifier for this bridge, consisting of bridge priority plus MAC address. This ID is the same for root and our bridge if the switch is the root switch.')
zyMstpInfoInstanceInternalRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstanceInternalRootCost.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceInternalRootCost.setDescription('This is the path cost from the root port in this MST instance to the regional root switch.')
zyMstpInfoInstanceRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstanceRootPort.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceRootPort.setDescription('This is the priority and number of the port on the switch through which this switch must communicate with the root of the MST instance.')
zyMstpInfoInstanceTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstanceTimeSinceTopologyChange.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceTimeSinceTopologyChange.setDescription('This is the time since the spanning tree was last reconfigured.')
zyMstpInfoInstanceTopologyChangesCount = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstanceTopologyChangesCount.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstanceTopologyChangesCount.setDescription('This is the number of times the spanning tree has been reconfigured.')
zyxelMstpInfoInstancePortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5), )
if mibBuilder.loadTexts: zyxelMstpInfoInstancePortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoInstancePortTable.setDescription('The table contains MSTP instance port information.')
zyxelMstpInfoInstancePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1), ).setIndexNames((0, "ZYXEL-MSTP-MIB", "zyMstpInfoInstancePortInstanceId"), (0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelMstpInfoInstancePortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMstpInfoInstancePortEntry.setDescription('An entry contains MSTP instance port information.')
zyMstpInfoInstancePortInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 1), MstiOrCistInstanceIndex())
if mibBuilder.loadTexts: zyMstpInfoInstancePortInstanceId.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortInstanceId.setDescription('The number you want to use to identify this MST instance on the switch. 0 means CIST.')
zyMstpInfoInstancePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortPathCost.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortPathCost.setDescription('The cost of transmitting a frame on to a LAN through that port.')
zyMstpInfoInstancePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 0), ("discarding", 1), ("learning", 2), ("forwarding", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortState.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortState.setDescription('STP assigns five port states to eliminate packet looping. A bridge port is not allowed to go directly from blocking state to forwarding state so as to eliminate transient loops.')
zyMstpInfoInstancePortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedRoot.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedRoot.setDescription('The unique Bridge Identifier of the Bridge recorded as the Root in the Configuration BPDUs transmitted by the Designated Bridge for the segment to which the port is attached.')
zyMstpInfoInstancePortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedCost.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedCost.setDescription('The path cost of the Designated Port is connected to this port. This value is compared to the Root Path Cost field in received bridge PDUs.')
zyMstpInfoInstancePortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedBridge.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedBridge.setDescription("The Bridge Identifier of the bridge that this port considers to be the Designated Bridge for this port's segment.")
zyMstpInfoInstancePortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedPort.setStatus('current')
if mibBuilder.loadTexts: zyMstpInfoInstancePortDesignatedPort.setDescription("The Port Identifier of the port on the Designated Bridge for this port's segment.")
zyMstpNewRoot = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3, 1)).setObjects(("ZYXEL-MSTP-MIB", "zyMstpInstanceId"))
if mibBuilder.loadTexts: zyMstpNewRoot.setStatus('current')
if mibBuilder.loadTexts: zyMstpNewRoot.setDescription('The newRoot trap indicates that the sending agent has become the new root of the Spanning Tree; the trap is sent by a bridge soon after its election as the new root, e.g., upon expiration of the Topology Change Timer, immediately subsequent to its election. Implementation of this trap is optional.')
zyMstpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3, 2)).setObjects(("ZYXEL-MSTP-MIB", "zyMstpInstanceId"))
if mibBuilder.loadTexts: zyMstpTopologyChange.setStatus('current')
if mibBuilder.loadTexts: zyMstpTopologyChange.setDescription('A topologyChange is sent if the topology changed of MSTP has detected.')
mibBuilder.exportSymbols("ZYXEL-MSTP-MIB", zyMstpVlanMapVlans1k=zyMstpVlanMapVlans1k, zyMstpInfoGeneralCistRootPathCost=zyMstpInfoGeneralCistRootPathCost, zyxelMstpGeneral=zyxelMstpGeneral, zyMstpGeneralConfigIdName=zyMstpGeneralConfigIdName, zyMstpInfoGeneralConfigIdConfigDigest=zyMstpInfoGeneralConfigIdConfigDigest, zyMstpInfoInstanceBridgeId=zyMstpInfoInstanceBridgeId, zyMstpInfoGeneralForwardDelay=zyMstpInfoGeneralForwardDelay, zyxelMstpInfoVlanMapEntry=zyxelMstpInfoVlanMapEntry, zyxelMstpStatus=zyxelMstpStatus, zyMstpInstancePortPathCost=zyMstpInstancePortPathCost, zyMstpInstanceBridgePriority=zyMstpInstanceBridgePriority, zyMstpInfoInstancePortDesignatedCost=zyMstpInfoInstancePortDesignatedCost, zyMstpGeneralForwardDelay=zyMstpGeneralForwardDelay, MstiOrCistInstanceIndex=MstiOrCistInstanceIndex, zyMstpInfoInstancePortPathCost=zyMstpInfoInstancePortPathCost, zyxelMstpSetup=zyxelMstpSetup, zyMstpNewRoot=zyMstpNewRoot, zyMstpVlanMapVlans2k=zyMstpVlanMapVlans2k, zyxelMstpPortEntry=zyxelMstpPortEntry, zyxelMstpInstancePortTable=zyxelMstpInstancePortTable, zyMstpInfoPortOperPointToPointMAC=zyMstpInfoPortOperPointToPointMAC, zyMstpInfoPortOperEdgePort=zyMstpInfoPortOperEdgePort, zyMstpInfoInstancePortState=zyMstpInfoInstancePortState, zyxelMstpInfoInstancePortTable=zyxelMstpInfoInstancePortTable, zyxelMstpVlanMapTable=zyxelMstpVlanMapTable, zyMstpVlanMapInstance=zyMstpVlanMapInstance, zyMstpInfoInstanceTopologyChangesCount=zyMstpInfoInstanceTopologyChangesCount, zyMstpInfoInstanceInternalRootCost=zyMstpInfoInstanceInternalRootCost, zyxelMstpPortTable=zyxelMstpPortTable, zyxelMstpInfoInstancePortEntry=zyxelMstpInfoInstancePortEntry, zyxelMstp=zyxelMstp, zyMstpInstancePortInstanceId=zyMstpInstancePortInstanceId, zyMstpInstancePortState=zyMstpInstancePortState, zyMstpInfoGeneralCistRootBridgeId=zyMstpInfoGeneralCistRootBridgeId, zyMstpInfoGeneralConfigIdRevisionLevel=zyMstpInfoGeneralConfigIdRevisionLevel, zyMstpInfoInstanceId=zyMstpInfoInstanceId, zyxelMstpInfoPortTable=zyxelMstpInfoPortTable, zyMstpVlanMapVlans3k=zyMstpVlanMapVlans3k, PYSNMP_MODULE_ID=zyxelMstp, zyxelMstpInstanceEntry=zyxelMstpInstanceEntry, zyxelMstpInfoInstanceTable=zyxelMstpInfoInstanceTable, zyMstpVlanMapRowStatus=zyMstpVlanMapRowStatus, zyMstpInfoInstanceTimeSinceTopologyChange=zyMstpInfoInstanceTimeSinceTopologyChange, zyMstpInfoInstancePortDesignatedPort=zyMstpInfoInstancePortDesignatedPort, zyMstpVlanMapMaxNumberOfInstances=zyMstpVlanMapMaxNumberOfInstances, zyxelMstpInfoInstanceEntry=zyxelMstpInfoInstanceEntry, zyMstpInstancePortPriority=zyMstpInstancePortPriority, zyMstpInfoInstancePortDesignatedBridge=zyMstpInfoInstancePortDesignatedBridge, zyxelMstpVlanMapEntry=zyxelMstpVlanMapEntry, zyMstpInstanceId=zyMstpInstanceId, zyxelMstpInstanceTable=zyxelMstpInstanceTable, zyMstpInfoGeneralHelloTime=zyMstpInfoGeneralHelloTime, zyMstpGeneralConfigIdRevisionLevel=zyMstpGeneralConfigIdRevisionLevel, zyMstpInfoGeneralMaxAge=zyMstpInfoGeneralMaxAge, zyxelMstpInfoVlanMapTable=zyxelMstpInfoVlanMapTable, zyMstpGeneralState=zyMstpGeneralState, zyMstpInfoVlanMapInstance=zyMstpInfoVlanMapInstance, zyMstpInfoInstancePortInstanceId=zyMstpInfoInstancePortInstanceId, zyMstpTopologyChange=zyMstpTopologyChange, zyMstpInfoInstancePortDesignatedRoot=zyMstpInfoInstancePortDesignatedRoot, zyxelMstpInfoGeneral=zyxelMstpInfoGeneral, zyMstpVlanMapVlans4k=zyMstpVlanMapVlans4k, zyMstpInfoGeneralConfigIdName=zyMstpInfoGeneralConfigIdName, zyxelMstpNotifications=zyxelMstpNotifications, zyMstpGeneralHelloTime=zyMstpGeneralHelloTime, zyMstpInfoVlanMapVid=zyMstpInfoVlanMapVid, zyMstpGeneralMaxAge=zyMstpGeneralMaxAge, zyxelMstpInfoPortEntry=zyxelMstpInfoPortEntry, zyMstpInfoInstanceRootPort=zyMstpInfoInstanceRootPort, zyxelMstpInstancePortEntry=zyxelMstpInstancePortEntry, zyMstpPortAdminEdgePort=zyMstpPortAdminEdgePort, zyMstpGeneralMaxHops=zyMstpGeneralMaxHops)
