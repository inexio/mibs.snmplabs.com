#
# PySNMP MIB module HH3C-LswMSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswMSTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
dot1dStpPort, dot1dStpPortEntry = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStpPort", "dot1dStpPortEntry")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, IpAddress, TimeTicks, ModuleIdentity, NotificationType, Gauge32, Counter32, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "Gauge32", "Counter32", "MibIdentifier", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cdot1sMstp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14))
hh3cdot1sMstp.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cdot1sMstp.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hh3cdot1sMstp.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cdot1sMstp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cdot1sMstp.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cdot1sMstp.setDescription('')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Hh3cdot1sFormatStatus(TextualConvention, Integer32):
    description = 'Legacy means that the BPDU format is legacy. Dot1s means that the BPDU format is IEEE 802.1s. Auto means that the format of BPDU sending on the port is determined by the BPDU format of its connective port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("legacy", 1), ("dot1s", 2), ("auto", 3))

hh3cdot1sStpStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 1), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sStpStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sStpStatus.setDescription('Whether the Bridge MSTP is enabled.')
hh3cdot1sStpForceVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("stp", 0), ("rstp", 2), ("mstp", 3))).clone('mstp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sStpForceVersion.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sStpForceVersion.setDescription(' The mode of this Bridge spanning-tree protocol.')
hh3cdot1sStpDiameter = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 7)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sStpDiameter.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sStpDiameter.setDescription('The diameter of Bridge.')
hh3cdot1sMstBridgeMaxHops = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 40)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstBridgeMaxHops.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstBridgeMaxHops.setDescription('The maximum value of the Bridge hops.')
hh3cdot1sMstMasterBridgeID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstMasterBridgeID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstMasterBridgeID.setDescription('The Bridge Identifier of the current Master Bridge.')
hh3cdot1sMstMasterPathCost = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstMasterPathCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstMasterPathCost.setDescription('The CIST path cost from the transmitting Bridge to the Master Bridge.')
hh3cdot1sMstBpduGuard = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 7), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstBpduGuard.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstBpduGuard.setDescription('Whether the Bridge BPDU Guard function is enabled. If the function is enabled, the port will shutdown when received BPDU and the port is configured as portfast.')
hh3cdot1sMstAdminFormatSelector = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstAdminFormatSelector.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstAdminFormatSelector.setDescription('The administrative Configuration Identifier Format Selector in use by the Bridge. This has a value of 0 indicate the format specified in the Standard of IEEE 802.1s.')
hh3cdot1sMstAdminRegionName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstAdminRegionName.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstAdminRegionName.setDescription('This MSTP administrative region name.')
hh3cdot1sMstAdminRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstAdminRevisionLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstAdminRevisionLevel.setDescription('This MSTP administrative revision level.')
hh3cdot1sMstOperFormatSelector = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstOperFormatSelector.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstOperFormatSelector.setDescription('The operative Configuration Identifier Format Selector in use by the Bridge. This has a value of 0 indicate the format specified in the Standard of IEEE 802.1s.')
hh3cdot1sMstOperRegionName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstOperRegionName.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstOperRegionName.setDescription('This MSTP operative region name.')
hh3cdot1sMstOperRevisionLevel = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstOperRevisionLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstOperRevisionLevel.setDescription('This MSTP operative revision level.')
hh3cdot1sMstOperConfigDigest = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstOperConfigDigest.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstOperConfigDigest.setDescription("This MSTP Region's Configuration Digest Signature Key.")
hh3cdot1sMstRegionConfActive = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstRegionConfActive.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstRegionConfActive.setDescription('Active the region configuration.')
hh3cdot1sMstDefaultVlanAllo = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("enable", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstDefaultVlanAllo.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstDefaultVlanAllo.setDescription('Set default configuration about VLAN allocation and all VLANs are mapped to CIST.')
hh3cdot1sMstDefaultRegionName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("enable", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstDefaultRegionName.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstDefaultRegionName.setDescription('Set default region name.')
hh3cdot1sVIDAllocationTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18), )
if mibBuilder.loadTexts: hh3cdot1sVIDAllocationTable.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sVIDAllocationTable.setDescription('')
hh3cdot1sVIDAllocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1), ).setIndexNames((0, "HH3C-LswMSTP-MIB", "hh3cdot1sMstVID"))
if mibBuilder.loadTexts: hh3cdot1sVIDAllocationEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sVIDAllocationEntry.setDescription('')
hh3cdot1sMstVID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstVID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstVID.setDescription('VLAN Identifier')
hh3cdot1sAdminMstID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sAdminMstID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sAdminMstID.setDescription('Administrative Multiple spanning-tree instance Identifier.')
hh3cdot1sOperMstID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sOperMstID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sOperMstID.setDescription('Operative Multiple spanning-tree instance Identifier.')
hh3cdot1sInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19), )
if mibBuilder.loadTexts: hh3cdot1sInstanceTable.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sInstanceTable.setDescription('')
hh3cdot1sInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1), ).setIndexNames((0, "HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"))
if mibBuilder.loadTexts: hh3cdot1sInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sInstanceEntry.setDescription('')
hh3cdot1sInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sInstanceID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sInstanceID.setDescription('Multiple spanning-tree instance Identifier')
hh3cdot1sMstiBridgeID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 2), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiBridgeID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiBridgeID.setDescription('The Bridge Identifier for the spanning tree instance identified by MSTID')
hh3cdot1sMstiBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440)).clone(32768)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiBridgePriority.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiBridgePriority.setDescription('The Bridge Priority for the spanning tree instance identified by MSTID. Step of 4096')
hh3cdot1sMstiDesignedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 4), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiDesignedRoot.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiDesignedRoot.setDescription('The Bridge Identifier of the Root Bridge for the spanning tree instance identified by MSTID')
hh3cdot1sMstiRootPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiRootPathCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiRootPathCost.setDescription('The path cost from the transmitting Bridge to the Root Bridge for the spanning tree instance identified by MSTID')
hh3cdot1sMstiRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiRootPort.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiRootPort.setDescription('The Root Port for the spanning tree instance identified by the MSTID')
hh3cdot1sMstiRootType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("normal", 0), ("secondary", 1), ("primary", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiRootType.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiRootType.setDescription('Config this Bridge as a primary root or seconary root and or cancel the root for this spanning tree instance identified by MSTID')
hh3cdot1sMstiRemainingHops = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiRemainingHops.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiRemainingHops.setDescription('The remaining hops of the spanning tree instance identified by MSTID')
hh3cdot1sMstiAdminMappedVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiAdminMappedVlanListLow.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiAdminMappedVlanListLow.setDescription(' The lower part of administrative Vlan list mapped to the spanning tree instance identified by MSTID')
hh3cdot1sMstiAdminMappedVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiAdminMappedVlanListHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiAdminMappedVlanListHigh.setDescription(' The higher part of administrative Vlan list mapped to the spanning tree instance identified by MSTID')
hh3cdot1sMstiOperMappedVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiOperMappedVlanListLow.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiOperMappedVlanListLow.setDescription(' The lower part of operative Vlan list mapped to the spanning tree instance identified by MSTID')
hh3cdot1sMstiOperMappedVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiOperMappedVlanListHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiOperMappedVlanListHigh.setDescription(' The higher part of operative Vlan list mapped to the spanning tree instance identified by MSTID')
hh3cdot1sPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20), )
if mibBuilder.loadTexts: hh3cdot1sPortTable.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sPortTable.setDescription('')
hh3cdot1sPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1), ).setIndexNames((0, "HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"), (0, "HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
if mibBuilder.loadTexts: hh3cdot1sPortEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sPortEntry.setDescription('')
hh3cdot1sMstiPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiPortIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiPortIndex.setDescription('The index of the Bridge Port')
hh3cdot1sMstiState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("discarding", 2), ("learning", 4), ("forwarding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiState.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiState.setDescription('The current state of the Port (i.e., Disabled, Discarding , Learning, Forwarding)')
hh3cdot1sMstiPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 240)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiPortPriority.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiPortPriority.setDescription('The value of the priority field which is contained in the first (in network byte order) four bits of the (2 octet long) Port ID. The other octet of the Port ID is given by the value of mstiPortIndex. And step of 16')
hh3cdot1sMstiPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiPathCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiPathCost.setDescription('The contribution of this port to the path cost of paths towards the spanning tree root which include this port. The range of path cost is 1..65535 for 802.1d standard, is 1..200000000 for 802.1t standard, and is 1..200000 for the legacy standard. ')
hh3cdot1sMstiDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedRoot.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedRoot.setDescription('The Bridge Identifier of the Root Bridge for the port of the Spanning Tree instance identified by the MSTID')
hh3cdot1sMstiDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedCost.setDescription('The path cost of the Designated Port of the segment connected to this port. This value is compared to the Root Path Cost field in received bridge PDUs.')
hh3cdot1sMstiDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 7), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedBridge.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedBridge.setDescription("The Bridge Identifier of the bridge which this port considers to be the Designated Bridge for this port's segment.")
hh3cdot1sMstiDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedPort.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiDesignatedPort.setDescription("The Port Identifier of the port on the Designated Bridge for this port's segment.")
hh3cdot1sMstiMasterBridgeID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 9), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiMasterBridgeID.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiMasterBridgeID.setDescription('The Bridge Idnetifier of the current Master Bridge. Effective in CIST.')
hh3cdot1sMstiMasterPortCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiMasterPortCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiMasterPortCost.setDescription('The CIST path cost from the transmitting Bridge to the Master Bridge. Effective in CIST.')
hh3cdot1sMstiStpPortEdgeport = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 11), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortEdgeport.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortEdgeport.setDescription(' Whether the port fast is enabled. Effective in CIST.')
hh3cdot1sMstiStpPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forceTrue", 1), ("forceFalse", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortPointToPoint.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortPointToPoint.setDescription(' Whether the port conects the point to point link. Effective in CIST.')
hh3cdot1sMstiStpMcheck = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("enable", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpMcheck.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpMcheck.setDescription(' Forcing the state machine to send MST BPDUs in this manner can be used to test whether all legacy Bridges on a given LAN have been removed. Effective in CIST.')
hh3cdot1sMstiStpTransLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpTransLimit.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpTransLimit.setDescription('The value used by the Port Transmit state machine to limit the maximum transmission rate. Effective in CIST.')
hh3cdot1sMstiStpRXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXStpBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXStpBPDU.setDescription('The number of received Config BPDU. Effective in CIST.')
hh3cdot1sMstiStpTXStpBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXStpBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXStpBPDU.setDescription('The number of transimitted Config BPDU. Effective in CIST.')
hh3cdot1sMstiStpRXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXTCNBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXTCNBPDU.setDescription('The number of received TCN BPDU. Effective in CIST.')
hh3cdot1sMstiStpTXTCNBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXTCNBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXTCNBPDU.setDescription('The number of transimitted TCN BPDU. Effective in CIST.')
hh3cdot1sMstiStpRXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXRSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXRSTPBPDU.setDescription('The number of received RST BPDU. Effective in CIST.')
hh3cdot1sMstiStpTXRSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXRSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXRSTPBPDU.setDescription('The number of transimitted RST BPDU. Effective in CIST.')
hh3cdot1sMstiStpRXMSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXMSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpRXMSTPBPDU.setDescription('The number of received MST BPDU. Effective in CIST.')
hh3cdot1sMstiStpTXMSTPBPDU = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXMSTPBPDU.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpTXMSTPBPDU.setDescription('The number of transimitted MST BPDU. Effective in CIST.')
hh3cdot1sMstiStpClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("clear", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpClearStatistics.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpClearStatistics.setDescription('Clear the spanning tree statistic. Effective in CIST.')
hh3cdot1sMstiStpDefaultPortCost = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 65535))).clone(namedValues=NamedValues(("enable", 1), ("unused", 65535)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpDefaultPortCost.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpDefaultPortCost.setDescription('Set default Port path cost. ')
hh3cdot1sMstiStpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 25), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpStatus.setDescription('Whether the spanning tree protocol is enabled on this port. Effective in CIST.')
hh3cdot1sMstiPortRootGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 26), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiPortRootGuard.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiPortRootGuard.setDescription('Whether the root guard is enabled. Effective in CIST.')
hh3cdot1sMstiPortLoopGuard = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 27), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiPortLoopGuard.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiPortLoopGuard.setDescription('Whether the loop protection is enabled. Effective in CIST.')
hh3cdot1sMstiStpPortSendingBPDUType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stp", 1), ("rstp", 2), ("mstp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortSendingBPDUType.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortSendingBPDUType.setDescription('Type of BPDU which the port is sending.')
hh3cdot1sMstiStpOperPortPointToPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpOperPortPointToPoint.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpOperPortPointToPoint.setDescription('This object indicates whether the port has connected to a point-to-point link or not. The value of the node is an operative value. The administrative value can be read from the node hh3cdot1sMstiStpPortPointToPoint. If the value of hh3cdot1sMstiStpPortPointToPoint is auto, the value of this node should be calculated by the network topology of this port. If the value of hh3cdot1sMstiStpPortPointToPoint is forceFalse, the value of this node is false. If the value of hh3cdot1sMstiStpPortPointToPoint is forceTrue, the value of this node is true.')
hh3cdot1sMstiStpPortAdminBPDUFmt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 30), Hh3cdot1sFormatStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortAdminBPDUFmt.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortAdminBPDUFmt.setDescription('The value of the node is an administrative value. Value legacy means that the MST BPDU format is forced to legacy. Value dot1s means that the MST BPDU format is forced to IEEE 802.1s. Value auto means that the format of MST BPDU sending on the port is determined by the MST BPDU that the port has received. Effective in CIST.')
hh3cdot1sMstiStpPortOperBPDUFmt = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 31), Hh3cdot1sFormatStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortOperBPDUFmt.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sMstiStpPortOperBPDUFmt.setDescription('The format of MST BPDU which the port is sending. Value legacy means that the format of MST BPDU sending on the port is legacy. Value dot1s means that the format of MST BPDU sending on the port is IEEE 802.1s. Effective in CIST.')
hh3cdot1sStpPathCostStandard = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("legacy", 0), ("dot1d-1998", 1), ("dot1t", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cdot1sStpPathCostStandard.setStatus('current')
if mibBuilder.loadTexts: hh3cdot1sStpPathCostStandard.setDescription('Path cost standard of the bridge. Value dot1d-1998 is IEEE 802.1d standard in 1998, value dot1t is IEEE 802.1t standard, and value legacy is a private legacy standard.')
hh3cMstpEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0))
if mibBuilder.loadTexts: hh3cMstpEventsV2.setStatus('current')
if mibBuilder.loadTexts: hh3cMstpEventsV2.setDescription('Definition point for Mstp notifications.')
hh3cPortMstiStateForwarding = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 1)).setObjects(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"), ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
if mibBuilder.loadTexts: hh3cPortMstiStateForwarding.setStatus('current')
if mibBuilder.loadTexts: hh3cPortMstiStateForwarding.setDescription('The SNMP trap that is generated when a port turns into forwarding state form other state.')
hh3cPortMstiStateDiscarding = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 2)).setObjects(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"), ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
if mibBuilder.loadTexts: hh3cPortMstiStateDiscarding.setStatus('current')
if mibBuilder.loadTexts: hh3cPortMstiStateDiscarding.setDescription('The SNMP trap that is generated when a port turns into discarding state form forwarding state.')
hh3cBridgeLostRootPrimary = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 3)).setObjects(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"))
if mibBuilder.loadTexts: hh3cBridgeLostRootPrimary.setStatus('current')
if mibBuilder.loadTexts: hh3cBridgeLostRootPrimary.setDescription('The SNMP trap that is generated when the bridge is no longer the root bridge of the instance. Another switch with higher priority has already been the root bridge of the instance.')
hh3cPortMstiRootGuarded = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 4)).setObjects(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"), ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
if mibBuilder.loadTexts: hh3cPortMstiRootGuarded.setStatus('current')
if mibBuilder.loadTexts: hh3cPortMstiRootGuarded.setDescription('The SNMP trap that is generated when a root-guard port receives a superior message on the relevant instance.')
hh3cPortMstiBpduGuarded = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 5)).setObjects(("BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts: hh3cPortMstiBpduGuarded.setStatus('current')
if mibBuilder.loadTexts: hh3cPortMstiBpduGuarded.setDescription('The SNMP trap that is generated when an edged port of the BPDU-guard switch recevies BPDU packets.')
hh3cPortMstiLoopGuarded = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 6)).setObjects(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"), ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
if mibBuilder.loadTexts: hh3cPortMstiLoopGuarded.setStatus('current')
if mibBuilder.loadTexts: hh3cPortMstiLoopGuarded.setDescription('The SNMP trap that is generated when an Alternate-Port or Root-Port is aged out.')
mibBuilder.exportSymbols("HH3C-LswMSTP-MIB", hh3cPortMstiStateForwarding=hh3cPortMstiStateForwarding, hh3cdot1sPortTable=hh3cdot1sPortTable, hh3cdot1sMstOperRevisionLevel=hh3cdot1sMstOperRevisionLevel, hh3cdot1sMstiRootPathCost=hh3cdot1sMstiRootPathCost, hh3cdot1sMstiOperMappedVlanListHigh=hh3cdot1sMstiOperMappedVlanListHigh, hh3cdot1sMstMasterPathCost=hh3cdot1sMstMasterPathCost, hh3cdot1sMstiPathCost=hh3cdot1sMstiPathCost, hh3cdot1sMstVID=hh3cdot1sMstVID, hh3cdot1sStpDiameter=hh3cdot1sStpDiameter, hh3cdot1sAdminMstID=hh3cdot1sAdminMstID, hh3cPortMstiStateDiscarding=hh3cPortMstiStateDiscarding, hh3cdot1sMstiAdminMappedVlanListHigh=hh3cdot1sMstiAdminMappedVlanListHigh, hh3cdot1sMstDefaultRegionName=hh3cdot1sMstDefaultRegionName, hh3cPortMstiBpduGuarded=hh3cPortMstiBpduGuarded, hh3cdot1sMstiStpTransLimit=hh3cdot1sMstiStpTransLimit, hh3cdot1sMstiStpRXTCNBPDU=hh3cdot1sMstiStpRXTCNBPDU, hh3cBridgeLostRootPrimary=hh3cBridgeLostRootPrimary, hh3cdot1sMstOperConfigDigest=hh3cdot1sMstOperConfigDigest, PYSNMP_MODULE_ID=hh3cdot1sMstp, hh3cdot1sMstiDesignedRoot=hh3cdot1sMstiDesignedRoot, hh3cdot1sMstiMasterPortCost=hh3cdot1sMstiMasterPortCost, hh3cdot1sMstiOperMappedVlanListLow=hh3cdot1sMstiOperMappedVlanListLow, hh3cdot1sMstiBridgeID=hh3cdot1sMstiBridgeID, hh3cdot1sMstOperFormatSelector=hh3cdot1sMstOperFormatSelector, hh3cdot1sMstiStpOperPortPointToPoint=hh3cdot1sMstiStpOperPortPointToPoint, hh3cdot1sMstiRootType=hh3cdot1sMstiRootType, hh3cdot1sMstOperRegionName=hh3cdot1sMstOperRegionName, hh3cdot1sMstBpduGuard=hh3cdot1sMstBpduGuard, hh3cdot1sMstiStpRXMSTPBPDU=hh3cdot1sMstiStpRXMSTPBPDU, hh3cdot1sMstiStpStatus=hh3cdot1sMstiStpStatus, hh3cdot1sMstiDesignatedBridge=hh3cdot1sMstiDesignatedBridge, hh3cdot1sMstiPortLoopGuard=hh3cdot1sMstiPortLoopGuard, hh3cdot1sMstiDesignatedPort=hh3cdot1sMstiDesignatedPort, hh3cdot1sMstiStpTXTCNBPDU=hh3cdot1sMstiStpTXTCNBPDU, hh3cdot1sInstanceID=hh3cdot1sInstanceID, hh3cdot1sMstiDesignatedCost=hh3cdot1sMstiDesignatedCost, hh3cdot1sMstiPortIndex=hh3cdot1sMstiPortIndex, hh3cdot1sMstiRootPort=hh3cdot1sMstiRootPort, hh3cdot1sMstiStpDefaultPortCost=hh3cdot1sMstiStpDefaultPortCost, hh3cdot1sMstiStpPortPointToPoint=hh3cdot1sMstiStpPortPointToPoint, hh3cdot1sVIDAllocationEntry=hh3cdot1sVIDAllocationEntry, hh3cdot1sMstiStpPortSendingBPDUType=hh3cdot1sMstiStpPortSendingBPDUType, hh3cPortMstiLoopGuarded=hh3cPortMstiLoopGuarded, hh3cdot1sMstiStpPortAdminBPDUFmt=hh3cdot1sMstiStpPortAdminBPDUFmt, hh3cdot1sMstp=hh3cdot1sMstp, hh3cdot1sMstAdminRevisionLevel=hh3cdot1sMstAdminRevisionLevel, Hh3cdot1sFormatStatus=Hh3cdot1sFormatStatus, hh3cdot1sMstiStpTXMSTPBPDU=hh3cdot1sMstiStpTXMSTPBPDU, hh3cdot1sMstiStpTXRSTPBPDU=hh3cdot1sMstiStpTXRSTPBPDU, hh3cdot1sInstanceEntry=hh3cdot1sInstanceEntry, hh3cdot1sMstiDesignatedRoot=hh3cdot1sMstiDesignatedRoot, hh3cdot1sMstiStpPortEdgeport=hh3cdot1sMstiStpPortEdgeport, hh3cdot1sStpForceVersion=hh3cdot1sStpForceVersion, hh3cdot1sMstiAdminMappedVlanListLow=hh3cdot1sMstiAdminMappedVlanListLow, hh3cdot1sMstiStpTXStpBPDU=hh3cdot1sMstiStpTXStpBPDU, hh3cdot1sMstiStpMcheck=hh3cdot1sMstiStpMcheck, hh3cdot1sMstiStpRXRSTPBPDU=hh3cdot1sMstiStpRXRSTPBPDU, hh3cdot1sMstAdminFormatSelector=hh3cdot1sMstAdminFormatSelector, hh3cdot1sVIDAllocationTable=hh3cdot1sVIDAllocationTable, hh3cdot1sOperMstID=hh3cdot1sOperMstID, hh3cdot1sMstiStpRXStpBPDU=hh3cdot1sMstiStpRXStpBPDU, hh3cdot1sMstDefaultVlanAllo=hh3cdot1sMstDefaultVlanAllo, hh3cMstpEventsV2=hh3cMstpEventsV2, hh3cdot1sMstiState=hh3cdot1sMstiState, hh3cdot1sStpStatus=hh3cdot1sStpStatus, hh3cdot1sMstAdminRegionName=hh3cdot1sMstAdminRegionName, hh3cdot1sStpPathCostStandard=hh3cdot1sStpPathCostStandard, hh3cdot1sMstiRemainingHops=hh3cdot1sMstiRemainingHops, hh3cdot1sMstiStpClearStatistics=hh3cdot1sMstiStpClearStatistics, hh3cdot1sMstiPortRootGuard=hh3cdot1sMstiPortRootGuard, hh3cdot1sMstBridgeMaxHops=hh3cdot1sMstBridgeMaxHops, hh3cdot1sMstiBridgePriority=hh3cdot1sMstiBridgePriority, EnabledStatus=EnabledStatus, hh3cdot1sMstMasterBridgeID=hh3cdot1sMstMasterBridgeID, hh3cdot1sMstRegionConfActive=hh3cdot1sMstRegionConfActive, hh3cdot1sMstiMasterBridgeID=hh3cdot1sMstiMasterBridgeID, hh3cdot1sPortEntry=hh3cdot1sPortEntry, hh3cdot1sMstiPortPriority=hh3cdot1sMstiPortPriority, hh3cdot1sMstiStpPortOperBPDUFmt=hh3cdot1sMstiStpPortOperBPDUFmt, hh3cPortMstiRootGuarded=hh3cPortMstiRootGuarded, hh3cdot1sInstanceTable=hh3cdot1sInstanceTable, BridgeId=BridgeId)
