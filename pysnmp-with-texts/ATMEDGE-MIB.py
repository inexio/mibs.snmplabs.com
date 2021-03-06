#
# PySNMP MIB module ATMEDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATMEDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lannet, = mibBuilder.importSymbols("GEN-MIB", "lannet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, ModuleIdentity, iso, Counter32, Counter64, ObjectIdentity, Gauge32, MibIdentifier, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "ModuleIdentity", "iso", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmEdge = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 26))
cti = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 29))
atmEdgePort = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 26, 1))
atmEdgePortTable = MibTable((1, 3, 6, 1, 4, 1, 81, 26, 1, 1), )
if mibBuilder.loadTexts: atmEdgePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortTable.setDescription('')
atmEdgePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1), ).setIndexNames((0, "ATMEDGE-MIB", "atmEdgePortGroupId"), (0, "ATMEDGE-MIB", "atmEdgePortId"))
if mibBuilder.loadTexts: atmEdgePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortEntry.setDescription('')
atmEdgePortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortGroupId.setDescription('Id of the slot to which the atm port belongs.')
atmEdgePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortId.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortId.setDescription('Id of the port.')
atmEdgePortHealthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("ok", 1), ("atmError", 2), ("sonetLinkError", 3), ("sonetRemoteLinkError", 4), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortHealthStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortHealthStatus.setDescription('Indicates the health state of the port. When this field indicates carrierFailure, it means that there is no carrier: the agent should send a trap of type fault.')
atmEdgePortMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortMACAddr.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortMACAddr.setDescription('MAC address of the ATM port. If the port has no MAC address, this value should be zero length octet string.')
atmEdgePortATMAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortATMAddr.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortATMAddr.setDescription('ATM address of the ATM port. If the port has no ATM address, this value should be zero length octet string.')
atmEdgePortLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ethernet", 1), ("token-ring", 2), ("notSupported", 255))).clone('ethernet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortLanType.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortLanType.setDescription("The type of the up link port. This is used do find whether the port wants to receive the association table and from what kind. ethernet - an Ethernet Edge device. token-ring - a Token Ring Edge device. notSupported means that currently the device doesn't currently act as an Edge Devices")
atmEdgePortILMIStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notsupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortILMIStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortILMIStatus.setDescription('The current state of the ILMI signalling of this port.')
atmEdgePortSignalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notsupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortSignalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortSignalStatus.setDescription('The current state of the ATM signalling for this port.')
atmEdgePortActualUNIVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("unknown", 1), ("uni-30", 2), ("uni-31", 3), ("uni-40", 4), ("notsupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortActualUNIVersion.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortActualUNIVersion.setDescription('The type of signalling that is currently being used on this port. ')
atmEdgePortNetworkPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(13, 13)).setFixedLength(13)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmEdgePortNetworkPrefix.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortNetworkPrefix.setDescription('The prefix of the ATM switch connected to this ATM port.')
atmEdgePortDormantHealthStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("ok", 1), ("atmError", 2), ("sonetLinkError", 3), ("sonetRemoteLinkError", 4), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortDormantHealthStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortDormantHealthStatus.setDescription('Indicates the health state of the Dormant port. When this field indicates carrierFailure, it means that there is no carrier: the agent should send a trap of type fault.')
atmEdgePortRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("masterNicActive", 1), ("secondaryNicActive", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgePortRedundancyStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgePortRedundancyStatus.setDescription('This item is relevant for ports which includes redundant links. This item indicates which of the links is active. Default value=masterNicActive(1). ')
atmEdgeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 26, 2))
atmEdgeGroupTable = MibTable((1, 3, 6, 1, 4, 1, 81, 26, 2, 1), )
if mibBuilder.loadTexts: atmEdgeGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgeGroupTable.setDescription('')
atmEdgeGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1), ).setIndexNames((0, "ATMEDGE-MIB", "atmEdgeGroupGroupId"))
if mibBuilder.loadTexts: atmEdgeGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgeGroupEntry.setDescription('')
atmEdgeGroupGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgeGroupGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgeGroupGroupId.setDescription('Slot number in which the module is located.')
atmEdgeGroupWorkState = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("run", 1), ("boot", 2), ("runAndBoot", 3), ("none", 4), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgeGroupWorkState.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgeGroupWorkState.setDescription('One of the possible states of the module: this item indicates if the module is runing or booting. The value runAndBoot(3) indicates a serious software problem.')
atmEdgeGroupBITResult = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("faulty", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmEdgeGroupBITResult.setStatus('mandatory')
if mibBuilder.loadTexts: atmEdgeGroupBITResult.setDescription('The Bit Indication Test in state faulty indicates a problem. The agent should send a fault trap in this case.')
atmEdgeAssociation = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 26, 3))
associationTable = MibTable((1, 3, 6, 1, 4, 1, 81, 26, 3, 1), )
if mibBuilder.loadTexts: associationTable.setStatus('mandatory')
if mibBuilder.loadTexts: associationTable.setDescription('This table contains all the information concerning the association between VLAN and ELAN names.')
associationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1), ).setIndexNames((0, "ATMEDGE-MIB", "associationSlotIndex"), (0, "ATMEDGE-MIB", "associationPortIndex"), (0, "ATMEDGE-MIB", "associationIndex"))
if mibBuilder.loadTexts: associationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: associationEntry.setDescription('An entry in the table, contains information about a VLAN associated to an ELAN on a particular up link port.')
associationSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: associationSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: associationSlotIndex.setDescription('Index which identifies the Slot inside the chassis.')
associationPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: associationPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: associationPortIndex.setDescription('Index which identifies the Port inside the Slot.')
associationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: associationIndex.setStatus('mandatory')
if mibBuilder.loadTexts: associationIndex.setDescription('An arbitrary integer which uniquely identifies an association number.')
associationVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: associationVlan.setStatus('mandatory')
if mibBuilder.loadTexts: associationVlan.setDescription('The VLAN number.')
associationElan = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: associationElan.setStatus('mandatory')
if mibBuilder.loadTexts: associationElan.setDescription('The ELAN name. For Ethernet devices the default is default. For Token Ring devices the default is defaultTrn')
associationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))).clone('active')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: associationRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: associationRowStatus.setDescription("The status of the entry, not a standard RowStatus. To create an entry, the console finds the next available entry. It changes the entry to 'notReady', it fills the VLAN number and the ELAN name, and it changes the entry to 'createAndGo'. The device creates the interface and the LEC, when it finishes, it changes the entry to 'active'. To delete an entry, the console changes the entry to 'destroy'. To disable an entry, the console changes the entry to 'notInService'.")
associationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 26, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: associationIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: associationIfIndex.setDescription('Creating a row in this table causes the agent to add one row in the interface table. Before setting the row status to active, the agent fills this field with the value of the ifIndex of the new created row.')
genCTIGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 29, 1))
genCTIGroupTable = MibTable((1, 3, 6, 1, 4, 1, 81, 29, 1, 1), )
if mibBuilder.loadTexts: genCTIGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupTable.setDescription('Attributes pertaining to the CTI module.')
genCTIGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1), ).setIndexNames((0, "ATMEDGE-MIB", "genCTIGroupId"))
if mibBuilder.loadTexts: genCTIGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupEntry.setDescription('An entry in the table.')
genCTIGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupId.setDescription('Slot number in which the module is located.')
genCTIGroupCellLossAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("cellLossAlarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIGroupCellLossAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupCellLossAlarm.setDescription('Indicates a condition of significant cell loss which results in performance degradation')
genCTIGroupRedunAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noRedun", 1), ("redunAvailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIGroupRedunAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupRedunAvailable.setDescription('Indication on the availability of external redundancy unit')
genCTIGroupRedunFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noFlip", 1), ("flipFiber", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genCTIGroupRedunFlip.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupRedunFlip.setDescription('In regular conditions this item is in the noFlip state. Changing the item value to flipFiber will result in flipping to the other link. After this flip is completed the value will return back to the noFlip sate. this item is relevant only when a redundant link is available')
genCTIGroupFiberActive = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fiberActiveA", 1), ("fiberActiveB", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIGroupFiberActive.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupFiberActive.setDescription('When there is an external fiber redundancy this item shows which of the links is active')
genCTIGroupVmuxMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localMaster", 1), ("localSlave", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIGroupVmuxMaster.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIGroupVmuxMaster.setDescription('On the poit to point voice connection via the FIM port one side is a master and the other side is a slave. This item shows whether the local module is master or slave')
genCTIPortTable = MibTable((1, 3, 6, 1, 4, 1, 81, 29, 1, 2), )
if mibBuilder.loadTexts: genCTIPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortTable.setDescription('Table of ports in a CTI module.')
genCTIPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1), ).setIndexNames((0, "ATMEDGE-MIB", "genCTIPortGroupId"), (0, "ATMEDGE-MIB", "genCTIPortId"))
if mibBuilder.loadTexts: genCTIPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortEntry.setDescription('Entry in the table.')
genCTIPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIPortGroupId.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortGroupId.setDescription('Slot number in which the module is located.')
genCTIPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIPortId.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortId.setDescription('The port index. The numbering scheme for the CTI ports follows: 1 - FIM Voice port 2 - UTP ATM Port 3 - SONET port')
genCTIPortSync = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("noSync", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIPortSync.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortSync.setDescription('Sync status for the port.')
genCTIPortRxAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("rxAlarm", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIPortRxAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortRxAlarm.setDescription('Rx Alarm status for the port')
genCTIPortTxAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 29, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("txAlarm", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genCTIPortTxAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: genCTIPortTxAlarm.setDescription(' Tx Alarm status for the port ')
mibBuilder.exportSymbols("ATMEDGE-MIB", atmEdgeGroupEntry=atmEdgeGroupEntry, atmEdgeGroupBITResult=atmEdgeGroupBITResult, associationVlan=associationVlan, genCTIPortTable=genCTIPortTable, associationSlotIndex=associationSlotIndex, atmEdgeGroup=atmEdgeGroup, associationIndex=associationIndex, genCTIGroupEntry=genCTIGroupEntry, genCTIPortId=genCTIPortId, atmEdgePort=atmEdgePort, atmEdgePortTable=atmEdgePortTable, atmEdgeGroupWorkState=atmEdgeGroupWorkState, atmEdgePortRedundancyStatus=atmEdgePortRedundancyStatus, atmEdgePortILMIStatus=atmEdgePortILMIStatus, atmEdgeGroupGroupId=atmEdgeGroupGroupId, associationEntry=associationEntry, genCTIPortRxAlarm=genCTIPortRxAlarm, associationTable=associationTable, genCTIGroupRedunAvailable=genCTIGroupRedunAvailable, atmEdgePortEntry=atmEdgePortEntry, associationIfIndex=associationIfIndex, genCTIGroupId=genCTIGroupId, genCTIPortSync=genCTIPortSync, genCTIPortEntry=genCTIPortEntry, atmEdgeGroupTable=atmEdgeGroupTable, genCTIGroupTable=genCTIGroupTable, genCTIGroupCellLossAlarm=genCTIGroupCellLossAlarm, atmEdgePortActualUNIVersion=atmEdgePortActualUNIVersion, atmEdgePortMACAddr=atmEdgePortMACAddr, associationPortIndex=associationPortIndex, atmEdgePortGroupId=atmEdgePortGroupId, cti=cti, genCTIGroup=genCTIGroup, atmEdgePortNetworkPrefix=atmEdgePortNetworkPrefix, atmEdgePortATMAddr=atmEdgePortATMAddr, genCTIGroupRedunFlip=genCTIGroupRedunFlip, genCTIGroupFiberActive=genCTIGroupFiberActive, atmEdge=atmEdge, atmEdgeAssociation=atmEdgeAssociation, atmEdgePortId=atmEdgePortId, genCTIPortTxAlarm=genCTIPortTxAlarm, atmEdgePortHealthStatus=atmEdgePortHealthStatus, atmEdgePortLanType=atmEdgePortLanType, genCTIPortGroupId=genCTIPortGroupId, associationElan=associationElan, genCTIGroupVmuxMaster=genCTIGroupVmuxMaster, associationRowStatus=associationRowStatus, atmEdgePortDormantHealthStatus=atmEdgePortDormantHealthStatus, atmEdgePortSignalStatus=atmEdgePortSignalStatus)
