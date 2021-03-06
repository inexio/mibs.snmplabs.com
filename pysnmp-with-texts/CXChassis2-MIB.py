#
# PySNMP MIB module CXChassis2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXChassis2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cxChassis2, = mibBuilder.importSymbols("CXProduct-SMI", "cxChassis2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Gauge32, Unsigned32, Integer32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Bits, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxChassIfAdmGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5))
ifMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6))
ifMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("invalid", 1), ("valid", 2))

cxChassLogIfAdmTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2), )
if mibBuilder.loadTexts: cxChassLogIfAdmTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmTable.setDescription('A table containing mappings from ifIndex to CPU, type and logical channel.')
cxChassLogIfAdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1), ).setIndexNames((0, "CXChassis2-MIB", "cxChassLogIfAdmCpuIndex"), (0, "CXChassis2-MIB", "cxChassLogIfAdmIfType"), (0, "CXChassis2-MIB", "cxChassLogIfAdmChannelIndex"))
if mibBuilder.loadTexts: cxChassLogIfAdmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmEntry.setDescription('Row representing a mapping entry of ifIndex to CPU, type and logical channel.')
cxChassLogIfAdmCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChassLogIfAdmCpuIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmCpuIndex.setDescription("The CPU number which corresponds to the slot number in the chassis. For example, a row for CPU in slot 2 will use value '2'. For single CPU chassis, the value to be used is '1'.")
cxChassLogIfAdmIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxChassLogIfAdmIfType.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmIfType.setDescription('The type of interface to be created.')
cxChassLogIfAdmChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChassLogIfAdmChannelIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmChannelIndex.setDescription("The channel number belonging to a port in the IO card in a CPU. If the port is not channelized, then it will have only one entry in the table with this object set to value '1'. Within our system, a channel will be associated with its own service access point, thus requiring the use of a service access point control block. This object therefore takes on the sap control block identification. Due to the internal sap control block numbering limitation, this object will be restricted in range from 1 to 255, but may be expanded when the internal limitations are lifted.")
cxChassLogIfAdmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxChassLogIfAdmIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmIfIndex.setDescription('The Interface index which corressponds to the ifIndex in the ifTable. If this value is specified, then it is the registered ifIndex used for the interface, otherwise the ifIndex will be obtained from the ifTable.')
cxChassLogIfAdmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 5, 2, 1, 5), RowStatus().clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxChassLogIfAdmRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cxChassLogIfAdmRowStatus.setDescription('Used to create and deleted rows in this table.')
ifStackTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2), )
if mibBuilder.loadTexts: ifStackTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifStackTable.setDescription("The table containing information on the relationships between the multiple sub-layers of network interfaces. In particular, it contains information on which sub-layers run 'on top of' which other sub-layers. Each sub-layer corresponds to a conceptual row in the ifTable.")
ifStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1), ).setIndexNames((0, "CXChassis2-MIB", "ifStackHigherLayer"), (0, "CXChassis2-MIB", "ifStackLowerLayer"))
if mibBuilder.loadTexts: ifStackEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifStackEntry.setDescription("Information on a particular relationship between two sub-layers, specifying that one sub-layer runs on 'top' of the other sub-layer. Each sub-layer corresponds to a conceptual row in the ifTable.")
ifStackHigherLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifStackHigherLayer.setStatus('mandatory')
if mibBuilder.loadTexts: ifStackHigherLayer.setDescription("The value of ifIndex corresponding to the higher sub-layer of the relationship, i.e., the sub-layer which runs on 'top' of the sub-layer identified by the corresponding instance of ifStackLowerLayer. If there is no higher sub-layer (below the internetwork layer), then this object has the value 0.")
ifStackLowerLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifStackLowerLayer.setStatus('mandatory')
if mibBuilder.loadTexts: ifStackLowerLayer.setDescription("The value of ifIndex corresponding to the lower sub-layer of the relationship, i.e., the sub-layer which runs 'below' the sub-layer identified by the corresponding instance of ifStackHigherLayer. If there is no lower sub-layer, then this object has the value 0.")
ifStackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 9, 6, 1, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifStackStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ifStackStatus.setDescription("The status of the relationship between two sub-layers. Changing the value of this object from 'active' to 'notInService' or 'destroy' will likely have consequences up and down the interface stack. Thus, write access to this object is likely to be inappropriate for some types of interfaces, and many implementations will choose not to support write-access for any type of interface.")
mibBuilder.exportSymbols("CXChassis2-MIB", ifStackEntry=ifStackEntry, ifMIBObjects=ifMIBObjects, ifStackTable=ifStackTable, cxChassLogIfAdmTable=cxChassLogIfAdmTable, ifStackStatus=ifStackStatus, cxChassLogIfAdmEntry=cxChassLogIfAdmEntry, ifStackLowerLayer=ifStackLowerLayer, cxChassLogIfAdmRowStatus=cxChassLogIfAdmRowStatus, cxChassIfAdmGroup=cxChassIfAdmGroup, ifStackHigherLayer=ifStackHigherLayer, cxChassLogIfAdmChannelIndex=cxChassLogIfAdmChannelIndex, cxChassLogIfAdmIfIndex=cxChassLogIfAdmIfIndex, RowStatus=RowStatus, ifMIB=ifMIB, cxChassLogIfAdmCpuIndex=cxChassLogIfAdmCpuIndex, cxChassLogIfAdmIfType=cxChassLogIfAdmIfType)
