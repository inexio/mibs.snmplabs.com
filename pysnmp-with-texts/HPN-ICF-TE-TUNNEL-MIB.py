#
# PySNMP MIB module HPN-ICF-TE-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-TE-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:41:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
MplsLabel, MplsTunnelInstanceIndex, MplsTunnelIndex, MplsExtendedTunnelId = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel", "MplsTunnelInstanceIndex", "MplsTunnelIndex", "MplsExtendedTunnelId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, Counter64, ObjectIdentity, Gauge32, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, ModuleIdentity, Counter32, MibIdentifier, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "ModuleIdentity", "Counter32", "MibIdentifier", "TimeTicks", "NotificationType")
RowPointer, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TextualConvention", "DisplayString")
hpnicfTeTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115))
if mibBuilder.loadTexts: hpnicfTeTunnel.setLastUpdated('201103240948Z')
if mibBuilder.loadTexts: hpnicfTeTunnel.setOrganization('')
if mibBuilder.loadTexts: hpnicfTeTunnel.setContactInfo('')
if mibBuilder.loadTexts: hpnicfTeTunnel.setDescription('This MIB contains managed object definitions for the Multiprotocol Label Switching (MPLS) Te Tunnel.')
hpnicfTeTunnelScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1))
hpnicfTeTunnelMaxTunnelIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 1, 1), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelMaxTunnelIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelMaxTunnelIndex.setDescription('The max value of tunnel id is permitted configure on the device.')
hpnicfTeTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2))
hpnicfTeTunnelStaticCrlspTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1), )
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspTable.setDescription('This table contains information for static-crlsp, and through this to get detail information about this static-crlsp. Only support transit LSR and egress LSR.')
hpnicfTeTunnelStaticCrlspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspInLabel"))
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspEntry.setDescription('The entry in this table describes static-crlsp information.')
hpnicfTeTunnelStaticCrlspInLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 1), MplsLabel())
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspInLabel.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspInLabel.setDescription('This is unique label value that manualy assigned. Uniquely identifies a static-crlsp. Managers should use this to obtain detail static-crlsp information.')
hpnicfTeTunnelStaticCrlspName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspName.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspName.setDescription('The unique name assigned to the static-crlsp.')
hpnicfTeTunnelStaticCrlspStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspStatus.setDescription('Indicates the actual status of this static-crlsp, The value must be up when the static-crlsp status is up and the value must be down when the static-crlsp status is down.')
hpnicfTeTunnelStaticCrlspRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transit", 1), ("tail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspRole.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspRole.setDescription('This value indicate the role of this static-crlsp. This value must be transit at transit point of the tunnel, and tail at terminating point of the tunnel.')
hpnicfTeTunnelStaticCrlspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 1, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspXCPointer.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspXCPointer.setDescription('This pointer unique identify a row of mplsXCTable. This value should be zeroDotZero when the static-crlsp is down. The mplsXCTable identifies the segments that compose this tunnel, their characteristics, and relationships to each other.')
hpnicfTeTunnelCoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2), )
if mibBuilder.loadTexts: hpnicfTeTunnelCoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoTable.setDescription('This table contains information for Co-routed reverse crlsp and infomation of Co-routed bidirectional Tunnel Interface. If hpnicfCorouteTunnelLspInstance is zero, to obtain infomation of Co-routed bidirectional Tunnel Interface, otherwise to obtain Co-routed reverse crlsp infomation.')
hpnicfTeTunnelCoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIndex"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoLspInstance"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoIngressLSRId"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoEgressLSRId"))
if mibBuilder.loadTexts: hpnicfTeTunnelCoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoEntry.setDescription('The entry in this table describes Co-routed infomation of bidirectional Tunnel Interface and reserver lsp information.')
hpnicfTeTunnelCoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelCoIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoIndex.setDescription('Uniquely identifies a set of tunnel instances between a pair of ingress and egress LSRs that specified at originating point. This value should be equal to the value signaled in the Tunnel Id of the Session object.')
hpnicfTeTunnelCoLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 2), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelCoLspInstance.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoLspInstance.setDescription('When obtain infomation of Co-routed bidirectional Tunnel Interface, this vlaue should be zero. And this value must be LspID to obtain reverse crlsp information. Values greater than 0, but less than or equal to 65535, should be useless.')
hpnicfTeTunnelCoIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelCoIngressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoIngressLSRId.setDescription('Identity the ingress LSR associated with this tunnel instance. This vlaue is equal to the LsrID of originating endpoint.')
hpnicfTeTunnelCoEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 4), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelCoEgressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoEgressLSRId.setDescription('Identity of the egress LSR associated with this tunnel instance. This vlaue is equal to the LsrID of terminating point.')
hpnicfTeTunnelCoBiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("coroutedActive", 1), ("coroutedPassive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoBiMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoBiMode.setDescription('This vlaue indicated the bidirection mode of tunnel interface. The valuemust be coroutedActive at the originating point of the tunnel and coroutedPassive at the terminating point.')
hpnicfTeTunnelCoReverseLspInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 6), MplsTunnelInstanceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspInstance.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspInstance.setDescription('This value indicated the reverse lsp instance, and should be equal to obverse lsp instance.')
hpnicfTeTunnelCoReverseLspXCPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspXCPointer.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCoReverseLspXCPointer.setDescription('This pointer unique index to mplsXCTable of the reverse lsp. The mplsXCTable identifies the segments that compose this tunnel, their characteristics, and relationships to each other. A value of zeroDotZero indicate that there is no crlsp assigned to this.')
hpnicfTeTunnelPsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3), )
if mibBuilder.loadTexts: hpnicfTeTunnelPsTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsTable.setDescription('This table defines some objects for managers to obtain TE tunnel Protection Switching group current status information.')
hpnicfTeTunnelPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1), ).setIndexNames((0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIndex"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsIngressLSRId"), (0, "HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsEgressLSRId"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsEntry.setDescription('The entry in this table describes TE tunnel Protection Switching group infromation.')
hpnicfTeTunnelPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: hpnicfTeTunnelPsIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsIndex.setDescription('Uniquely identifies a TE tunnel Protection Switching group instance. This value must be equal to the tunnel id of work tunnel instance.')
hpnicfTeTunnelPsIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 2), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelPsIngressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsIngressLSRId.setDescription('Identity the ingress LSR associated with work tunnel instance.')
hpnicfTeTunnelPsEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 3), MplsExtendedTunnelId())
if mibBuilder.loadTexts: hpnicfTeTunnelPsEgressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsEgressLSRId.setDescription('Identity of the egress LSR associated with work tunnel instance.')
hpnicfTeTunnelPsProtectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 4), MplsTunnelIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIndex.setDescription('Uniquely identifies a TE tunnel Protection Switching group instance. This value must be equal to the tunnel id of TE tunnel Protection Switching group instance.')
hpnicfTeTunnelPsProtectIngressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 5), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIngressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectIngressLSRId.setDescription('Identity the ingress LSR associated with TE tunnel Protection Switching group instance.')
hpnicfTeTunnelPsProtectEgressLSRId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 6), MplsExtendedTunnelId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectEgressLSRId.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectEgressLSRId.setDescription('Identity of the egress LSR associated with TE tunnel Protection Switching group instance.')
hpnicfTeTunnelPsProtectType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("oneToOne", 1), ("onePlusOne", 2))).clone('oneToOne')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectType.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectType.setDescription('This value indicated TE tunnel Protection Switching group type. The default value is oneToOne.')
hpnicfTeTunnelPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("revertive", 1), ("noRevertive", 2))).clone('revertive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsRevertiveMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsRevertiveMode.setDescription('This value indicated protect switch mode. The value must be revertive or nonRevertive, default value is revertive. ')
hpnicfTeTunnelPsWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(24)).setUnits('30 seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsWtrTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsWtrTime.setDescription('The cycle time that switch to protect tunnel.')
hpnicfTeTunnelPsHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setUnits('500ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsHoldOffTime.setDescription('This value is switchback delay time. When detected the work path fault, switch to protect path after this time.')
hpnicfTeTunnelPsSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uniDirectional", 1), ("biDirectional", 2))).clone('uniDirectional')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchMode.setDescription('This value indicated TE tunnel Protection Switching group switch mode.')
hpnicfTeTunnelPsWorkPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsWorkPathStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsWorkPathStatus.setDescription('This value indicates work path status. none, noDefect, inDefect will be used.')
hpnicfTeTunnelPsProtectPathStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("noDefect", 2), ("inDefect", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectPathStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsProtectPathStatus.setDescription('This value indicates protect path status. none, noDefect, inDefect(3) will be used.')
hpnicfTeTunnelPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("workPath", 1), ("protectPath", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchResult.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchResult.setDescription('This value indicated current using path is work path or protect path.')
hpnicfTeTunnelNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3))
hpnicfTeTunnelNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0))
hpnicfTeTunnelPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchWtoP.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchWtoP.setDescription('This notification is generated when protect workgroup switch from work tunnel to protect tunnel.')
hpnicfTeTunnelPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 3, 0, 2)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"))
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchPtoW.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsSwitchPtoW.setDescription('This notification is generated when protect workgroup switch from protect tunnel to work tunnel.')
hpnicfTeTunnelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4))
hpnicfTeTunnelCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1))
hpnicfTeTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 1, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelNotificationsGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelScalarsGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCorouteGroup"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelCompliance = hpnicfTeTunnelCompliance.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCompliance.setDescription('The compliance statement for SNMP.')
hpnicfTeTunnelGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2))
hpnicfTeTunnelNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 1)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchPtoW"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchWtoP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelNotificationsGroup = hpnicfTeTunnelNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelNotificationsGroup.setDescription('This group contains MPLS Te Tunnel traps.')
hpnicfTeTunnelScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 2)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelMaxTunnelIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelScalarsGroup = hpnicfTeTunnelScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelScalarsGroup.setDescription('Scalar object needed to implement MPLS te tunnels.')
hpnicfTeTunnelStaticCrlspGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 3)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspName"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspRole"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelStaticCrlspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelStaticCrlspGroup = hpnicfTeTunnelStaticCrlspGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelStaticCrlspGroup.setDescription('Objects for quering static-crlsp information.')
hpnicfTeTunnelCorouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 4)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoBiMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspInstance"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelCoReverseLspXCPointer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelCorouteGroup = hpnicfTeTunnelCorouteGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelCorouteGroup.setDescription('Objects for quering Co-routed reverse crlsp information.')
hpnicfTeTunnelPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115, 4, 2, 5)).setObjects(("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIndex"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectIngressLSRId"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectEgressLSRId"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectType"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsRevertiveMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWtrTime"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsHoldOffTime"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchMode"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsWorkPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsProtectPathStatus"), ("HPN-ICF-TE-TUNNEL-MIB", "hpnicfTeTunnelPsSwitchResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfTeTunnelPsGroup = hpnicfTeTunnelPsGroup.setStatus('current')
if mibBuilder.loadTexts: hpnicfTeTunnelPsGroup.setDescription('Objects for quering protect workgroup information.')
mibBuilder.exportSymbols("HPN-ICF-TE-TUNNEL-MIB", hpnicfTeTunnelCoIndex=hpnicfTeTunnelCoIndex, hpnicfTeTunnelNotificationsPrefix=hpnicfTeTunnelNotificationsPrefix, hpnicfTeTunnelCoIngressLSRId=hpnicfTeTunnelCoIngressLSRId, hpnicfTeTunnelPsWorkPathStatus=hpnicfTeTunnelPsWorkPathStatus, hpnicfTeTunnelConformance=hpnicfTeTunnelConformance, hpnicfTeTunnelPsProtectPathStatus=hpnicfTeTunnelPsProtectPathStatus, hpnicfTeTunnelStaticCrlspInLabel=hpnicfTeTunnelStaticCrlspInLabel, hpnicfTeTunnelCoEgressLSRId=hpnicfTeTunnelCoEgressLSRId, hpnicfTeTunnelObjects=hpnicfTeTunnelObjects, hpnicfTeTunnelCompliance=hpnicfTeTunnelCompliance, hpnicfTeTunnelCoLspInstance=hpnicfTeTunnelCoLspInstance, hpnicfTeTunnelStaticCrlspRole=hpnicfTeTunnelStaticCrlspRole, hpnicfTeTunnelPsIndex=hpnicfTeTunnelPsIndex, hpnicfTeTunnelPsRevertiveMode=hpnicfTeTunnelPsRevertiveMode, hpnicfTeTunnel=hpnicfTeTunnel, hpnicfTeTunnelPsSwitchResult=hpnicfTeTunnelPsSwitchResult, hpnicfTeTunnelNotifications=hpnicfTeTunnelNotifications, hpnicfTeTunnelPsEgressLSRId=hpnicfTeTunnelPsEgressLSRId, hpnicfTeTunnelPsWtrTime=hpnicfTeTunnelPsWtrTime, hpnicfTeTunnelPsSwitchPtoW=hpnicfTeTunnelPsSwitchPtoW, hpnicfTeTunnelGroups=hpnicfTeTunnelGroups, hpnicfTeTunnelPsTable=hpnicfTeTunnelPsTable, hpnicfTeTunnelPsSwitchMode=hpnicfTeTunnelPsSwitchMode, hpnicfTeTunnelNotificationsGroup=hpnicfTeTunnelNotificationsGroup, hpnicfTeTunnelMaxTunnelIndex=hpnicfTeTunnelMaxTunnelIndex, hpnicfTeTunnelScalars=hpnicfTeTunnelScalars, hpnicfTeTunnelCoEntry=hpnicfTeTunnelCoEntry, hpnicfTeTunnelPsEntry=hpnicfTeTunnelPsEntry, hpnicfTeTunnelPsIngressLSRId=hpnicfTeTunnelPsIngressLSRId, hpnicfTeTunnelPsProtectIndex=hpnicfTeTunnelPsProtectIndex, hpnicfTeTunnelStaticCrlspXCPointer=hpnicfTeTunnelStaticCrlspXCPointer, hpnicfTeTunnelPsSwitchWtoP=hpnicfTeTunnelPsSwitchWtoP, hpnicfTeTunnelScalarsGroup=hpnicfTeTunnelScalarsGroup, hpnicfTeTunnelPsProtectType=hpnicfTeTunnelPsProtectType, hpnicfTeTunnelCompliances=hpnicfTeTunnelCompliances, hpnicfTeTunnelPsProtectIngressLSRId=hpnicfTeTunnelPsProtectIngressLSRId, PYSNMP_MODULE_ID=hpnicfTeTunnel, hpnicfTeTunnelStaticCrlspName=hpnicfTeTunnelStaticCrlspName, hpnicfTeTunnelPsHoldOffTime=hpnicfTeTunnelPsHoldOffTime, hpnicfTeTunnelStaticCrlspStatus=hpnicfTeTunnelStaticCrlspStatus, hpnicfTeTunnelPsGroup=hpnicfTeTunnelPsGroup, hpnicfTeTunnelStaticCrlspTable=hpnicfTeTunnelStaticCrlspTable, hpnicfTeTunnelStaticCrlspEntry=hpnicfTeTunnelStaticCrlspEntry, hpnicfTeTunnelStaticCrlspGroup=hpnicfTeTunnelStaticCrlspGroup, hpnicfTeTunnelCoReverseLspXCPointer=hpnicfTeTunnelCoReverseLspXCPointer, hpnicfTeTunnelPsProtectEgressLSRId=hpnicfTeTunnelPsProtectEgressLSRId, hpnicfTeTunnelCorouteGroup=hpnicfTeTunnelCorouteGroup, hpnicfTeTunnelCoTable=hpnicfTeTunnelCoTable, hpnicfTeTunnelCoReverseLspInstance=hpnicfTeTunnelCoReverseLspInstance, hpnicfTeTunnelCoBiMode=hpnicfTeTunnelCoBiMode)
