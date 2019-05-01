#
# PySNMP MIB module AVIDIA-SUBTEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVIDIA-SUBTEND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, iso, ObjectIdentity, Bits, Counter64, NotificationType, Gauge32, IpAddress, Unsigned32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "iso", "ObjectIdentity", "Bits", "Counter64", "NotificationType", "Gauge32", "IpAddress", "Unsigned32", "Counter32", "MibIdentifier")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
avSubtendMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 14))
if mibBuilder.loadTexts: avSubtendMIB.setLastUpdated('0006210000Z')
if mibBuilder.loadTexts: avSubtendMIB.setOrganization('Pairgain Technologies Inc.')
if mibBuilder.loadTexts: avSubtendMIB.setContactInfo('Ashok Singh Pairgain Technologies Inc 14402 Franklin Avenue Tustin, CA 92780')
if mibBuilder.loadTexts: avSubtendMIB.setDescription('The module defines MIB for Avidia subtending')
avSubtendInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1))
avSubtendIfTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1), )
if mibBuilder.loadTexts: avSubtendIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfTable.setDescription('A table that contains subtended interface information in Avidia')
avSubtendIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1), ).setIndexNames((0, "AVIDIA-SUBTEND-MIB", "avSubtendIndex"))
if mibBuilder.loadTexts: avSubtendIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfEntry.setDescription('Entry in avSubtendIfTable that contains port database information for a subtended interface')
avSubtendIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avSubtendIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIndex.setDescription('This is the index for the avSubtendIfTable. The index is generated by the agent implementation and is available by querying avSubtendIndexNext')
avSubtendIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfRowStatus.setDescription('This specifies the status of a row in the avSubtendIfTable. This allows table entries to be created and deleted.')
avSubtendIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfIndex.setDescription('This specifies the IfIndex which is computed from Slot number and Port Number for the subtending entry')
avSubtendIfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfVpi.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfVpi.setDescription('This specifies the VPI for the subtending entry')
avSubtendIfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfVci.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfVci.setDescription('This specifies the VCI for the subtending entry')
avSubtendIfSourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfSourceIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfSourceIpAddress.setDescription('This specifies the source IP address for the subtending entry')
avSubtendIfDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfDestinationIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfDestinationIpAddress.setDescription('This specifies the destination IP address for the subtending entry')
avSubtendIfSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfSubnetMask.setDescription('This specifies the IP subnet mask for the subtending entry')
avSubtendIfParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 9), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfParentIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfParentIfIndex.setDescription('This specifies the IfIndex for the parent. This is calculated from the slot and port number of the parent')
avSubtendIfParentIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfParentIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfParentIpAddress.setDescription('This specifies the parent IP address for the subtending entry')
avSubtendIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: avSubtendIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfAdminStatus.setDescription('The desired state of the interface. The testing(3) state indicates that no operational packets can be passed. When a managed system initializes, all interfaces start with ifAdminStatus in the down(2) state. As a result of either explicit management action or per configuration information retained by the managed system, ifAdminStatus is then changed to either the up(1) or testing(3) states (or remains in the down(2) state).')
avSubtendIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avSubtendIfOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIfOperStatus.setDescription('The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed. If ifAdminStatus is down(2) then ifOperStatus should be down(2). If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic; it should change to dormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incomming connection); it should remain in the down(2) state if and only if there is a fault that prevents if from going to the up(1) state.')
avSubtendIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 9, 14, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: avSubtendIndexNext.setStatus('mandatory')
if mibBuilder.loadTexts: avSubtendIndexNext.setDescription('This object contains an appropriate value to be used for avSubtendIndex when creating entries in the avSubtendIfTable. The value 0 indicates that no unassigned entries are available. To obtain the avSubtendIndex value for a new entry, the manager issues a management protocol retrieval operation to obtain the current value of this object.')
mibBuilder.exportSymbols("AVIDIA-SUBTEND-MIB", avSubtendIfParentIfIndex=avSubtendIfParentIfIndex, avSubtendIfAdminStatus=avSubtendIfAdminStatus, avSubtendIndex=avSubtendIndex, avSubtendIfSubnetMask=avSubtendIfSubnetMask, avSubtendIfParentIpAddress=avSubtendIfParentIpAddress, avSubtendIfRowStatus=avSubtendIfRowStatus, avSubtendIndexNext=avSubtendIndexNext, avSubtendIfDestinationIpAddress=avSubtendIfDestinationIpAddress, avSubtendIfSourceIpAddress=avSubtendIfSourceIpAddress, avSubtendInterfaces=avSubtendInterfaces, avSubtendIfOperStatus=avSubtendIfOperStatus, avSubtendIfVpi=avSubtendIfVpi, PYSNMP_MODULE_ID=avSubtendMIB, avSubtendIfEntry=avSubtendIfEntry, avSubtendIfVci=avSubtendIfVci, avSubtendMIB=avSubtendMIB, avSubtendIfTable=avSubtendIfTable, avSubtendIfIndex=avSubtendIfIndex)
